#!/usr/bin/python3

import os
import sys
import subprocess

# Tests ---------------------------------------------------

def run_tests():
    executable = sys.argv[1]
    test([executable], "Hello World\n")

# Implementation ---------------------------------------------------

RED = "\x1B[31m"
NORMAL = "\x1B[0m"
GREEN = "\x1B[32m"

all_good = True

if sys.version_info.major != 3:
    print(RED + "ERROR: e2e-runner.py expects to be run with Python 3" + NORMAL)
    sys.exit(1)

if len(sys.argv) != 2:
    print(RED + "ERROR: e2e-runner.py requires executable location!" + NORMAL)
    print(RED + "  e2e-runner.py <executable>" + NORMAL)
    sys.exit(1)

def main():
    global all_good

    try:
        run_tests()
    except subprocess.CalledProcessError as e:
        print(RED + "ERROR: A testing command exited with non-zero status" + NORMAL)
        print(RED + "Cmd: " + str(e.cmd) + NORMAL)
        print(RED + "Out ---------------------------" + NORMAL)
        print(e.output.decode('ascii'))
        all_good = False

    if not all_good:
        print(RED + "Exiting with status of 1..." + NORMAL)
        sys.exit(1)
    else:
        print(GREEN + "All tests passed..." + NORMAL)
        sys.exit(0)

def test(args, expected_output):
    global all_good
    res = subprocess.run(args, capture_output=True)
    res.check_returncode()

    actual_output = res.stdout.decode('ascii')

    if actual_output != expected_output:
        print(RED + "TEST FAILED: Command " + str(args) + " does not match expected output." + NORMAL)
        print(RED + "Expected...\n" + NORMAL + expected_output)
        print(RED + "Actual...\n" + NORMAL + actual_output)
        all_good = False

main()
