#!/usr/bin/env python3

from bottle import post, run
import platform, subprocess, os

env = os.environ


def cmd(cmd, stdout=subprocess.DEVNULL):
    return subprocess.Popen(cmd, shell=True, env=env, stdout=stdout)

url = "https://www.hacksoc.org/servers/"
hostname = platform.node().split(".")[0]
outfile = "index.html"

@post('/update')
def update():
    cmd('wget "{0}{1}.html" -O {2}'.format(url,hostname,outfile), stdout=subprocess.STDOUT).wait()

run(host="0.0.0.0", port=4000)