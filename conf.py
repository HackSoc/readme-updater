#!/usr/bin/env python3

import platform, os

template = open("hostname.hacksoc.org.conf").readlines()
hostname = platform.node().split(".")[0]
outfile = "/etc/nginx/sites-available/{}.hacksoc.org.conf".format(hostname);

if os.path.isfile(outfile):
    print("Moving {0} to {0}.old".format(outfile))
    os.rename(outfile, outfile + ".old")

with open(outfile, 'w') as fd:
    fd.write(hostname.replace("$hostname",hostname))
print("Written {}".format(outfile))
template.close()