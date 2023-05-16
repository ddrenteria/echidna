import numpy as np
import subprocess
import pandas as pd
import matplotlib.pyplot as plt

# Mazes to run
mazes = [0]
# Test limits to use 
test_limits = [700000]
# Timeout limits to use
timeout_limits = [60]
# Sequence lengths to use
# seqLens = [1, 10, 100]
seqLens = [10, 100]

# For each combination run echidna
    # Save time, #tests results in file
    # Save (timestamp,#test) in another file
# Run for test limits

# Run for timeouts

OURS_ECHIDNA_PATH = "./"
OG_ECHIDNA_PATH = "~/Desktop/tesis/og/echidna"

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


def create_plot_coverage_points(df_ours, df_og, path, seqLen):
    df_ours = df_ours[df_ours["coverage_points"]>0]
    df_og = df_og[df_og["coverage_points"]>0]
    plt.plot(np.array(df_ours["time"]), np.array(df_ours["coverage_points"]))
    plt.plot(np.array(df_og["time"]), np.array(df_og["coverage_points"]))
    plt.xlabel("time (s)")
    plt.ylabel("coverage points")
    plt.legend(['ours', 'original'])
    plt.title('Coverage points through time\nSequence length: ' + str(seqLen))
    plt.savefig(path + "/average_comparison_coverage_points_zoom.jpg")
    plt.clf()

def get_df(path):
    return pd.read_csv(path)

# Main  ---------------------------------------------------

for test_limit in test_limits:
    for seqLen in seqLens:
        for maze in mazes:
            iterations_results_ours = []
            iterations_results_og = []

            # create_average() 
            df_ours = get_df(get_test_path(test_limit, MAX_TIMEOUT, seqLen, maze, "ours") + "/results_average.csv")
            df_og = get_df(get_test_path(test_limit, MAX_TIMEOUT, seqLen, maze, "og") + "/results_average.csv")  
            create_plot_coverage_points(df_ours, df_og, get_test_path_base(test_limit, MAX_TIMEOUT, seqLen, maze), seqLen)

for timeout in timeout_limits:
    for seqLen in seqLens:
        for maze in mazes:

            # create_average() 
            df_ours = get_df(get_test_path(MAX_TESTLIMIT, timeout, seqLen, maze, "ours") + "/results_average.csv")
            df_og = get_df(get_test_path(MAX_TESTLIMIT, timeout, seqLen, maze, "og") + "/results_average.csv")  
            create_plot_coverage_points(df_ours, df_og, get_test_path_base(MAX_TESTLIMIT, timeout, seqLen, maze), seqLen)

