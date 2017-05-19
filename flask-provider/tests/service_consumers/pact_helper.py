import os
import subprocess
import urllib.request
from provider.controllers.application_controller import app


def set_up():
    print('STARTING PROVIDER...')
    start_script = os.path.join(os.getcwd(), 'bin', 'start')
    port = '1234'
    subprocess.call([start_script, port])


def tear_down():
    print('STOPPING PROVIDER...')
    with open(os.path.join(os.getcwd(), 'flask.pid')) as f:
        pid = f.read()
    print('PID: ' + pid)
    stop_script = os.path.join(os.getcwd(), 'bin', 'stop')
    subprocess.call([stop_script, pid])


def test_set_up():
    set_up()
    with urllib.request.urlopen('http://localhost:1234/books/42/') as r:
        json = r.read().decode('utf-8')
    print(json)
    tear_down()
