import numpy as np
import subprocess
import pandas as pd
import matplotlib.pyplot as plt

# Mazes to run
mazes = [1,2,3,4]
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
    plt.title('Amount of tests discovered through time\nSequence length: ' + str(seqLen))
    plt.savefig(path + "/average_comparison.jpg")
    plt.clf()

def create_data(df_ours, df_og, df_random, ar_our, ar_og, ar_random):
    ar_og.append([float(i) for i in df_og["coverage_points"]][-1])
    ar_our.append([float(i) for i in df_ours["coverage_points"]][-1])
    ar_random.append([float(i) for i in df_random["coverage_points"]][-1])
    return ar_our, ar_og, ar_random

def plot_data_all(ar_our, ar_og, ar_random, labels):
    x = np.arange(len(labels))  # the label locations
    width = 0.2  # the width of the bars

    fig, ax = plt.subplots(figsize=(18,5))
    rects1 = ax.bar(x - width, ar_our, width-0.02, label='EchidnaAfl', color="cadetblue")
    rects2 = ax.bar(x, ar_og, width-0.02, label='Original', color="forestgreen")
    rects3 = ax.bar(x + width, ar_random, width-0.02, label='Random', color="mediumpurple")

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Coverage points')
    ax.set_xlabel('')
    ax.set_title('Coverage points by contract, grouped by Maze')
    ax.legend(title='Version')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylim([4750, 6500])

    fig.tight_layout()
    # rcParams['figure.figsize'] = 15, 5
    plt.savefig("comparison_maze.jpg")
    plt.clf()
    # plt.show()

def plot_data_afl_og(ar_our, ar_og, ar_random, labels):
    x = np.arange(len(labels))  # the label locations
    width = 0.3  # the width of the bars

    fig, ax = plt.subplots(figsize=(18,5))
    rects1 = ax.bar(x - (width/2), ar_our, width-0.02, label='EchidnaAfl', color="cadetblue")
    rects3 = ax.bar(x + (width/2), ar_og, width-0.02, label='Original', color="forestgreen")

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Coverage points')
    ax.set_xlabel('')
    ax.set_title('Coverage points by contract, grouped by Maze')
    ax.legend(title='Version')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylim([4750, 6500])

    fig.tight_layout()
    # rcParams['figure.figsize'] = 15, 5
    plt.savefig("comparison_afl_maze.jpg")
    plt.clf()
    # plt.show()



def get_df(path):
    return pd.read_csv(path)

# Main  ---------------------------------------------------
ar_og = []
ar_ours = []
ar_random = []
labels = []

for test_limit in test_limits:
    for maze in mazes:
        for seqLen in seqLens:
            df_ours = get_df(get_test_path(test_limit, MAX_TIMEOUT, seqLen, maze, "ours") + "/results_average.csv")
            df_og = get_df(get_test_path(test_limit, MAX_TIMEOUT, seqLen, maze, "og") + "/results_average.csv")
            df_random = get_df(get_test_path(test_limit, MAX_TIMEOUT, seqLen, maze, "random") + "/results_average.csv")

            labels.append("SeqLen " + str(seqLen))    
            create_data(df_ours, df_og, df_random, ar_ours, ar_og, ar_random)
        
        labels.append("Maze " + str(maze))
        ar_og.append(0)
        ar_ours.append(0)
        ar_random.append(0)
        

plot_data_all(ar_ours, ar_og, ar_random, labels)
plot_data_afl_og(ar_ours, ar_og, ar_random, labels)
            
            