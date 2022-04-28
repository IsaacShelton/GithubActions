import os
import sys
import subprocess

if sys.version_info.major != 3:
    print("e2e-runner.py expects to be run with Python 3")
    sys.exit(1)

if len(sys.argv) != 2:
    print("e2e-runner.py requires executable location to be passed as argument")
    sys.exit(1)
    

exe = sys.argv[1]

try:
    subprocess.run([exe], capture_output=True).check_returncode()
except subprocess.CalledProcessError as e:
    print("e2e Testing Failed...")
    print("Cmd: " + str(e.cmd))
    print("Out ---------------------------")
    print(e.output.decode('ascii'))
    sys.exit(1)
