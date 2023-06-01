import numpy as np
import subprocess
import pandas as pd
import matplotlib.pyplot as plt


# Amount of times to run
run_amount = 1
# Contracts to run
contracts = ["Auction"]
# Test limits to use 
test_limits = [20000]
# Timeout limits to use
timeout_limits = []
# Sequence lengths to use
seqLens = [10, 100, 200]

# For each combination run echidna
    # Save time, #tests results in file
    # Save (timestamp,#test) in another file
# Run for test limits

# Run for timeouts

OURS_ECHIDNA_PATH = "./"
OG_ECHIDNA_PATH = "~/Desktop/tesis/og/echidna"
RANDOM_ECHIDNA_PATH = "~/Desktop/tesis/random/echidna"

MAX_TIMEOUT = 10 * 60 * 60 # 10 hours
MAX_TESTLIMIT = 2000000000


def save_results(results_data, path):
    df = pd.DataFrame(results_data)
    df.to_csv(f"{path}/results.csv")

def get_test_path_iteration(testLimit, timeout_minutes, seqLen, contractName, iteration, mode):
    return get_test_path(testLimit, timeout_minutes, seqLen, contractName, mode) + f"/it_{iteration}"

def get_test_path(testLimit, timeout_minutes, seqLen, contractName, mode):
    return get_test_path_base(testLimit, timeout_minutes, seqLen, contractName) + f"/{mode}"

def get_test_path_base(testLimit, timeout_minutes, seqLen, contractName):
    return f"echidna-test/seqLen_{seqLen}_timeout_{timeout_minutes}_testLim_{testLimit}/{contractName}"


def run_echidnas(testLimit, timeout_minutes, seqLen, contract_name, iteration):
    timeout = timeout_minutes * 60
    coverage = "true"
    testMode = "exploration"
    format = "text"
    shrinkLimit = 1
    config = f"shrinkLimit: {shrinkLimit}\ntestLimit: {testLimit}\ncoverage: {coverage}\nseqLen: {seqLen}\ntestMode: \"{testMode}\"\ntimeout: {timeout}\nformat: {format}"

    path_ours = get_test_path_iteration(testLimit, timeout_minutes, seqLen, contract_name, iteration, "ours")
    our_corpus_dir = f"\ncorpusDir: {path_ours}"

    path_og = get_test_path_iteration(testLimit, timeout_minutes, seqLen, contract_name, iteration, "og")
    og_corpus_dir = f"\ncorpusDir: {path_og}"

    path_random = get_test_path_iteration(testLimit, timeout_minutes, seqLen, contract_name, iteration, "random")
    random_corpus_dir = f"\ncorpusDir: {path_random}"

    contract_dir = "smart-pulse/" + contract_name + ".sol"

    our_compile_command = f"cd {OURS_ECHIDNA_PATH} && stack install --extra-include-dirs=/home/zhaeres/.local/include/ --extra-lib-dirs=libff/build/libff/ --flag echidna:-static > trash.txt"
    og_compile_command = f"cd {OG_ECHIDNA_PATH} && stack install --extra-include-dirs=/home/zhaeres/.local/include/ --extra-lib-dirs=libff/build/libff/ --flag echidna:-static > trash.txt"
    random_compile_command = f"cd {RANDOM_ECHIDNA_PATH} && stack install --extra-include-dirs=/home/zhaeres/.local/include/ --extra-lib-dirs=libff/build/libff/ --flag echidna:-static > trash.txt"
    our_run_command = f"echidna {contract_dir} --config config.yaml > {path_ours}/script_output.txt"
    og_run_command = f"echidna {contract_dir} --config config_og.yaml > {path_og}/script_output.txt"
    random_run_command = f"echidna {contract_dir} --config config_random.yaml > {path_random}/script_output.txt"

    # Create dirs
    subprocess.run(f"mkdir -p " + get_test_path_base(testLimit, timeout_minutes, seqLen, contract_name), shell=True)
    subprocess.run(f"mkdir -p " + get_test_path(testLimit, timeout_minutes, seqLen, contract_name, "ours"), shell=True)
    subprocess.run(f"mkdir -p " + get_test_path(testLimit, timeout_minutes, seqLen, contract_name, "og"), shell=True)
    subprocess.run(f"mkdir -p " + get_test_path(testLimit, timeout_minutes, seqLen, contract_name, "random"), shell=True)
    subprocess.run(f"mkdir " + get_test_path_iteration(testLimit, timeout_minutes, seqLen, contract_name, iteration, "ours"), shell=True)
    subprocess.run(f"mkdir " + get_test_path_iteration(testLimit, timeout_minutes, seqLen, contract_name, iteration, "og"), shell=True)
    subprocess.run(f"mkdir " + get_test_path_iteration(testLimit, timeout_minutes, seqLen, contract_name, iteration, "random"), shell=True)

    # Create configs
    subprocess.run(f"echo \"{config + our_corpus_dir}\" > config.yaml", shell=True)
    subprocess.run(f"echo \"{config + og_corpus_dir}\" > config_og.yaml", shell=True)
    subprocess.run(f"echo \"{config + random_corpus_dir}\" > config_random.yaml", shell=True)

    # Compile ours
    subprocess.run(our_compile_command, shell=True)
    subprocess.run(our_run_command, shell=True)

    # Compile og
    subprocess.run(og_compile_command, shell=True)
    subprocess.run(og_run_command, shell=True)

     # Compile random
    subprocess.run(random_compile_command, shell=True)
    subprocess.run(random_run_command, shell=True)

    # Clean folders
    for mode in ["ours", "og", "random"]:
        path = get_test_path_iteration(testLimit, timeout_minutes, seqLen, contract_name, iteration, mode)
        subprocess.run(f"rm -rf {path}/cache", shell=True)
        subprocess.run(f"rm -rf {path}/coverage", shell=True)
        subprocess.run(f"rm -rf {path}/reproducers", shell=True)


def extract_results(testLimit, timeout_minutes, seqLen, contract_name, iteration):
    path_ours = get_test_path_iteration(testLimit, timeout_minutes, seqLen, contract_name, iteration, "ours")
    path_og = get_test_path_iteration(testLimit, timeout_minutes, seqLen, contract_name, iteration, "og")
    path_random = get_test_path_iteration(testLimit, timeout_minutes, seqLen, contract_name, iteration, "random")

    ours_result = extract_results_for_file(f"{path_ours}/script_output.txt")
    og_result = extract_results_for_file(f"{path_og}/script_output.txt")
    random_result = extract_results_for_file(f"{path_random}/script_output.txt")

    return ours_result, og_result, random_result

def extract_results_for_file(filename):
    results = [{"time": 0, 
                "tests_discovered": 0, 
                "coverage_points": 0,
                "sequence_number": 0,
                "corpus_size": 0
                }]
    time = 0
    with open (filename, "r") as output_file:
        for line in output_file.readlines():
            # Select lines with info
            if "] [status] tests: " in line:
                time += 3
                words = line.split()
                # Extract test number
                tests_number = words[words.index("tests:")+1].split("/")[0]
                
                # Extract coverage points
                coverage_points = words[words.index("cov:")+1].replace(",", "")

                # Extract sequence number
                sequence_number = words[words.index("fuzzing:")+1].split("/")[0]

                # Extract corpus size
                corpus_size = words[words.index("corpus:")+1]
                results.append({"time": time, 
                                "tests_discovered": int(tests_number), 
                                "coverage_points": int(coverage_points),
                                "sequence_number": int(sequence_number),
                                "corpus_size": int(corpus_size)
                                })

    return results


def create_average(iterations_results, path):
    df_result = pd.DataFrame()

    # complete_missing_values()
    max_size = np.max(list(map(len, iterations_results)))
    for iteration in iterations_results:
        while (len(iteration) < max_size):
            last = iteration[-1]
            last["time"] = last["time"] + 3
            iteration.append(last)

        df_it = pd.DataFrame(iteration)
        if df_result.empty:
            df_result = df_it
        else:
            df_result = df_result.add(df_it)
    
    # average_times()
    df_result["time"] = df_result["time"] / len(iterations_results)
    df_result["tests_discovered"] = df_result["tests_discovered"] / len(iterations_results)
    df_result["coverage_points"] = df_result["coverage_points"] / len(iterations_results)
    df_result["sequence_number"] = df_result["sequence_number"] / len(iterations_results)
    df_result["corpus_size"] = df_result["corpus_size"] / len(iterations_results)

    # write_averages_in_csv
    df_result.to_csv(f"{path}/results_average.csv")

    # return as df
    return df_result

def create_plot_coverage_points(df_ours, df_og, df_random, path, seqLen):
    df_ours = df_ours[df_ours["coverage_points"]>0]
    df_og = df_og[df_og["coverage_points"]>0]
    df_random = df_random[df_random["coverage_points"]>0]
    plt.plot(np.array(df_ours["time"]), np.array(df_ours["coverage_points"]))
    plt.plot(np.array(df_og["time"]), np.array(df_og["coverage_points"]))
    plt.plot(np.array(df_random["time"]), np.array(df_random["coverage_points"]))
    plt.xlabel("time (s)")
    plt.ylabel("coverage points")
    plt.legend(['ours', 'original', 'random'])
    plt.title('Coverage points through time\nSequence length: ' + str(seqLen))
    plt.savefig(path + "/average_comparison_coverage_points.jpg")
    plt.clf()

def create_plot_coverage_points_seq_number(df_ours, df_og, df_random, path, seqLen):
    df_ours = df_ours[df_ours["coverage_points"]>0]
    df_og = df_og[df_og["coverage_points"]>0]
    df_random = df_random[df_random["coverage_points"]>0]
    plt.plot(np.array(df_ours["sequence_number"]), np.array(df_ours["coverage_points"]))
    plt.plot(np.array(df_og["sequence_number"]), np.array(df_og["coverage_points"]))
    plt.plot(np.array(df_random["sequence_number"]), np.array(df_random["coverage_points"]))
    plt.xlabel("# sequence")
    plt.ylabel("coverage points")
    plt.legend(['ours', 'original', 'random'])
    plt.title('Coverage points through # of sequences\nSequence length: ' + str(seqLen))
    plt.savefig(path + "/average_comparison_coverage_points_seq_number.jpg")
    plt.clf()

def create_plot_average(df_ours, df_og, df_random, path, seqLen):
    plt.plot(np.array(df_ours["time"]), np.array(df_ours["tests_discovered"]))
    plt.plot(np.array(df_og["time"]), np.array(df_og["tests_discovered"]))
    plt.plot(np.array(df_random["time"]), np.array(df_random["tests_discovered"]))
    plt.xlabel("time (s)")
    plt.ylabel("# tests")
    plt.legend(['ours', 'original', 'random'])
    plt.title('Amount of tests discovered through time\nSequence length: ' + str(seqLen))
    plt.savefig(path + "/average_comparison.jpg")
    plt.clf()


# Main  ---------------------------------------------------

for test_limit in test_limits:
    for seqLen in seqLens:
        for contract_name in contracts:
            iterations_results_ours = []
            iterations_results_og = []
            iterations_results_random = []

            for iteration in range(0, run_amount):
                print("TestLimit: " + str(test_limit) + " SeqLen: " + str(seqLen) + " Contract: " + contract_name + " iteration: " + str(iteration))
                run_echidnas(test_limit, MAX_TIMEOUT, seqLen, contract_name, iteration)
                array_ours, array_og, array_random = extract_results(test_limit, MAX_TIMEOUT, seqLen, contract_name, iteration)
                iterations_results_ours.append(array_ours)
                iterations_results_og.append(array_og)
                iterations_results_random.append(array_random)

                # Save results
                save_results(array_ours, get_test_path_iteration(test_limit, MAX_TIMEOUT, seqLen, contract_name, iteration, "ours"))
                save_results(array_og, get_test_path_iteration(test_limit, MAX_TIMEOUT, seqLen, contract_name, iteration, "og"))
                save_results(array_random, get_test_path_iteration(test_limit, MAX_TIMEOUT, seqLen, contract_name, iteration, "random"))
            # create_average() 
            df_ours = create_average(iterations_results_ours, get_test_path(test_limit, MAX_TIMEOUT, seqLen, contract_name, "ours"))
            df_og = create_average(iterations_results_og, get_test_path(test_limit, MAX_TIMEOUT, seqLen, contract_name, "og"))
            df_random = create_average(iterations_results_random, get_test_path(test_limit, MAX_TIMEOUT, seqLen, contract_name, "random"))

            create_plot_coverage_points(df_ours, df_og, df_random, get_test_path_base(test_limit, MAX_TIMEOUT, seqLen, contract_name), seqLen)
            create_plot_coverage_points_seq_number(df_ours, df_og, df_random, get_test_path_base(test_limit, MAX_TIMEOUT, seqLen, contract_name), seqLen)
            create_plot_average(df_ours, df_og, df_random, get_test_path_base(test_limit, MAX_TIMEOUT, seqLen, contract_name), seqLen)
