import numpy
import subprocess
import time


shrinkLimit = 1
seqLen = 100
timeout_minutes = 4 * 60
timeout = timeout_minutes * 60

test_name = f"seqLen_{seqLen}_timeout_{timeout_minutes}_minutes_maze_1"

testMode = "exploration"
format = "text"
testLimit = 2000000000
coverage = "true"

config = f"shrinkLimit: {shrinkLimit}\ntestLimit: {testLimit}\ncoverage: {coverage}\nseqLen: {seqLen}\ntestMode: \"{testMode}\"\ntimeout: {timeout}\nformat: {format}"
our_corpus_dir = f"\ncorpusDir: echidna-test/{test_name}/ours"
og_corpus_dir = f"\ncorpusDir: echidna-test/{test_name}/og"

contract_dir = "/home/zhaeres/Desktop/Tesis/daedaluzz/generated-mazes/maze-1.sol"
# contract_dir = "/home/zhaeres/Desktop/Tesis/echidna/tests/solidity/thesis-investigation/contract-craft-v2-assert.sol"

our_compile_command = "cd ~/Desktop/Tesis/echidna-last-version/echidna && stack install --extra-include-dirs=/home/zhaeres/.local/include/ --extra-lib-dirs=libff/build/libff/ --flag echidna:-static > trash.txt"
og_compile_command = "cd ~/Desktop/Tesis/echidna-last-version-og/echidna && stack install --extra-include-dirs=/home/zhaeres/.local/include/ --extra-lib-dirs=libff/build/libff/ --flag echidna:-static > trash.txt"
our_run_command = f"echidna {contract_dir} --config config.yaml > script_output.txt"
og_run_command = f"echidna {contract_dir} --config config_og.yaml > script_output.txt"

# Create dirs
subprocess.run(f"mkdir echidna-test/{test_name}", shell=True)
subprocess.run(f"mkdir echidna-test/{test_name}/ours", shell=True)
subprocess.run(f"mkdir echidna-test/{test_name}/og", shell=True)

# Create configs
subprocess.run(f"echo \"{config + our_corpus_dir}\" > config.yaml", shell=True)
subprocess.run(f"echo \"{config + og_corpus_dir}\" > config_og.yaml", shell=True)

# Compile ours
subprocess.run(our_compile_command, shell=True)
subprocess.run(our_run_command, shell=True)
subprocess.run(f"grep \"[*roe]\s*|\s*emit AssertionFailed\" echidna-test/{test_name}/ours/covered.*.txt > echidna-test/{test_name}/ours/grep-test.txt", shell=True)

# Compile og
subprocess.run(og_compile_command, shell=True)
subprocess.run(og_run_command, shell=True)
subprocess.run(f"grep \"[*roe]\s*|\s*emit AssertionFailed\" echidna-test/{test_name}/og/covered.*.txt > echidna-test/{test_name}/og/grep-test.txt", shell=True)