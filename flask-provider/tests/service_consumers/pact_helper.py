import os
import subprocess
from pact_test import PactHelper


class MyPactHelper(PactHelper):
    def setup(self):
        print('STARTING PROVIDER...')
        start_script = os.path.join(os.getcwd(), 'bin', 'start')
        print(start_script)
        port = '1234'
        subprocess.call([start_script, port])

    def tear_down(self):
        print('STOPPING PROVIDER...')
        with open(os.path.join(os.getcwd(), 'flask.pid')) as f:
            pid = f.read()
        print('PID: ' + pid)
        stop_script = os.path.join(os.getcwd(), 'bin', 'stop')
        print(stop_script)
        subprocess.call([stop_script, pid])
