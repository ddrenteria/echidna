import numpy as np
import subprocess
import pandas as pd
import matplotlib.pyplot as plt

# Mazes to run
mazes = [0, 1, 2, 3, 4]
# Test limits to use 
test_limits = [2000000]
# Timeout limits to use
timeout_limits = []
# Sequence lengths to use
seqLens = [10, 100, 200]

OURS_ECHIDNA_PATH = "./"
OG_ECHIDNA_PATH = "~/Desktop/tesis/og/echidna"
RANDOM_ECHIDNA_PATH = "~/Desktop/tesis/random/echidna"

MAX_TIMEOUT = 10 * 60 * 60 # 10 hours
MAX_TESTLIMIT = 2000000000

def get_test_path(testLimit, timeout_minutes, seqLen, mazeNumber, mode):
    return get_test_path_base(testLimit, timeout_minutes, seqLen, mazeNumber) + f"/{mode}"

def get_test_path_base(testLimit, timeout_minutes, seqLen, mazeNumber):
    return f"echidna-test/seqLen_{seqLen}_timeout_{timeout_minutes}_testLim_{testLimit}_maze_{mazeNumber}"

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
    plt.title('Amount of tests discovered through time\nSequence length: ' + str(seqLen)')
    plt.savefig(path + "/average_comparison.jpg")
    plt.clf()


def get_df(path):
    return pd.read_csv(path)

# Main  ---------------------------------------------------

for test_limit in test_limits:
    for seqLen in seqLens:
        for maze in mazes:
            df_ours = get_df(get_test_path(test_limit, MAX_TIMEOUT, seqLen, maze, "ours") + "/results_average.csv")
            df_og = get_df(get_test_path(test_limit, MAX_TIMEOUT, seqLen, maze, "og") + "/results_average.csv")
            df_random = get_df(get_test_path(test_limit, MAX_TIMEOUT, seqLen, maze, "random") + "/results_average.csv")
            create_plot_coverage_points(df_ours, df_og, df_random, get_test_path_base(test_limit, MAX_TIMEOUT, seqLen, maze), seqLen)
            create_plot_coverage_points_seq_number(df_ours, df_og, df_random, get_test_path_base(test_limit, MAX_TIMEOUT, seqLen, maze), seqLen)
            create_plot_average(df_ours, df_og, df_random, get_test_path_base(test_limit, MAX_TIMEOUT, seqLen, maze), seqLen)

for timeout in timeout_limits:
    for seqLen in seqLens:
        for maze in mazes:
            df_ours = get_df(get_test_path(MAX_TESTLIMIT, timeout, seqLen, maze, "ours") + "/results_average.csv")
            df_og = get_df(get_test_path(MAX_TESTLIMIT, timeout, seqLen, maze, "og") + "/results_average.csv")
            df_og = get_df(get_test_path(MAX_TESTLIMIT, timeout, seqLen, maze, "random") + "/results_average.csv")
            create_plot_coverage_points(df_ours, df_og, df_random, get_test_path_base(MAX_TESTLIMIT, timeout, seqLen, maze), seqLen)
            create_plot_coverage_points_seq_number(df_ours, df_og, df_random, get_test_path_base(MAX_TESTLIMIT, timeout, seqLen, maze), seqLen)
            create_plot_average(df_ours, df_og, df_random, get_test_path_base(MAX_TESTLIMIT, timeout, seqLen, maze), seqLen)

