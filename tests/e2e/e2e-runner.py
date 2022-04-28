#!/usr/bin/python3

import sys
from framework import *

def run_all_tests():
    executable = sys.argv[1]
    test([executable], "Hello World\n")

e2e_framework_run(run_all_tests)
