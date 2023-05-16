import numpy as np
import subprocess
import pandas as pd
import matplotlib.pyplot as plt


# Amount of times to run
run_amount = 10
# Mazes to run
mazes = [1, 2, 3, 4]
# Test limits to use 
test_limits = [2000000]
# Timeout limits to use
timeout_limits = []
# Sequence lengths to use
# seqLens = [1, 10, 100]
seqLens = [10, 100, 200]

# For each combination run echidna
    # Save time, #tests results in file
    # Save (timestamp,#test) in another file
# Run for test limits

# Run for timeouts

RANDOM_ECHIDNA_PATH = "~/Desktop/tesis/random/echidna"

MAX_TIMEOUT = 10 * 60 * 60 # 10 hours
MAX_TESTLIMIT = 2000000000


def save_results(results_data, path):
    df = pd.DataFrame(results_data)
    df.to_csv(f"{path}/results.csv")
                
def get_test_path_iteration(testLimit, timeout_minutes, seqLen, mazeNumber, iteration, mode):
    return get_test_path(testLimit, timeout_minutes, seqLen, mazeNumber, mode) + f"/it_{iteration}"

def get_test_path(testLimit, timeout_minutes, seqLen, mazeNumber, mode):
    return get_test_path_base(testLimit, timeout_minutes, seqLen, mazeNumber) + f"/{mode}"

def get_test_path_base(testLimit, timeout_minutes, seqLen, mazeNumber):
    return f"echidna-test/seqLen_{seqLen}_timeout_{timeout_minutes}_testLim_{testLimit}_maze_{mazeNumber}"


def run_echidna(testLimit, timeout_minutes, seqLen, mazeNumber, iteration):
   
    timeout = timeout_minutes * 60
    coverage = "true"
    testMode = "property"
    format = "text"
    shrinkLimit = 1
    config = f"shrinkLimit: {shrinkLimit}\ntestLimit: {testLimit}\ncoverage: {coverage}\nseqLen: {seqLen}\ntestMode: \"{testMode}\"\ntimeout: {timeout}\nformat: {format}"
    
    path_ours = get_test_path_iteration(testLimit, timeout_minutes, seqLen, mazeNumber, iteration, "random")
    our_corpus_dir = f"\ncorpusDir: {path_ours}"

    contract_dir = f"generated-mazes/maze-{mazeNumber}.sol"
    # contract_dir = "/home/zhaeres/Desktop/Tesis/echidna/tests/solidity/thesis-investigation/contract-craft-v2-assert.sol"

    our_compile_command = f"cd {RANDOM_ECHIDNA_PATH} && stack install --extra-include-dirs=/home/zhaeres/.local/include/ --extra-lib-dirs=libff/build/libff/ --flag echidna:-static > trash.txt"
    our_run_command = f"echidna {contract_dir} --config config.yaml > {path_ours}/script_output.txt"

    # Create dirs
    subprocess.run(f"mkdir -p " + get_test_path_base(testLimit, timeout_minutes, seqLen, mazeNumber), shell=True)
    subprocess.run(f"mkdir -p " + get_test_path(testLimit, timeout_minutes, seqLen, mazeNumber, "random"), shell=True)
    subprocess.run(f"mkdir " + get_test_path_iteration(testLimit, timeout_minutes, seqLen, mazeNumber, iteration, "random"), shell=True)

    # Create configs
    subprocess.run(f"echo \"{config + our_corpus_dir}\" > config_random.yaml", shell=True)

    # Compile ours
    subprocess.run(our_compile_command, shell=True)
    subprocess.run(our_run_command, shell=True)

    # Clean folders
    for mode in ["random"]:
        path = get_test_path_iteration(testLimit, timeout_minutes, seqLen, mazeNumber, iteration, mode)
        subprocess.run(f"rm -rf {path}/cache", shell=True)
        subprocess.run(f"rm -rf {path}/coverage", shell=True)
        subprocess.run(f"rm -rf {path}/reproducers", shell=True)


def extract_results(testLimit, timeout_minutes, seqLen, mazeNumber, iteration):
    path_ours = get_test_path_iteration(testLimit, timeout_minutes, seqLen, mazeNumber, iteration, "random")

    ours_result = extract_results_for_file(f"{path_ours}/script_output.txt")

    return ours_result

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


# Main  ---------------------------------------------------

for test_limit in test_limits:
    for seqLen in seqLens:
        for maze in mazes:
            iterations_results_ours = []

            for iteration in range(0, run_amount):
                print("TestLimit: " + str(test_limit) + " SeqLen: " + str(seqLen) + " Maze: " + str(maze) + " iteration: " + str(iteration))
                run_echidna(test_limit, MAX_TIMEOUT, seqLen, maze, iteration)
                array_ours = extract_results(test_limit, MAX_TIMEOUT, seqLen, maze, iteration)
                iterations_results_ours.append(array_ours)

                # Save results
                save_results(array_ours, get_test_path_iteration(test_limit, MAX_TIMEOUT, seqLen, maze, iteration, "random"))
            # create_average() 
            df_ours = create_average(iterations_results_ours, get_test_path(test_limit, MAX_TIMEOUT, seqLen, maze, "random"))

for timeout in timeout_limits:
    for seqLen in seqLens:
        for maze in mazes:
            iterations_results_ours = []

            for iteration in range(0, run_amount):
                print("Timeout: " + str(timeout) + " SeqLen: " + str(seqLen) + " Maze: " + str(maze) + " iteration: " + str(iteration))
                run_echidna(MAX_TESTLIMIT, timeout, seqLen, maze, iteration)
                array_ours = extract_results(MAX_TESTLIMIT, timeout, seqLen, maze, iteration)
                iterations_results_ours.append(array_ours)

                # Save results
                save_results(array_ours, get_test_path_iteration(MAX_TESTLIMIT, timeout, seqLen, maze, iteration, "random"))
            # create_average() 
            df_ours = create_average(iterations_results_ours, get_test_path(MAX_TESTLIMIT, timeout, seqLen, maze, "random"))

