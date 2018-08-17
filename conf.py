#!/usr/bin/env python3

import platform, os


print("""HackSoc README wizard
====================

This will set up a server to have a README served by nginx and automatically update from the HackSoc.org website.
Some things you need first:
1. To be running this as *root*
2. To have a user called `website`
3. To have nginx installed
4. To have Python 3 and bottle installed
5. To have a directory /srv/http/$hostname.hacksoc.org (which this is cloned into)

The tool will now copy nginx and service files to the correct locations
""")


hostname = platform.node().split(".")[0]
pwd = os.path.dirname(os.path.realpath(__file__))

conf_template = "\n".join(open("hostname.hacksoc.org.conf").readlines())
unit_template = "\n".join(open("readmehook.service").readlines())
conf_filename = "/etc/nginx/sites-available/{}.hacksoc.org.conf".format(hostname);
unit_filename = "/etc/systemd/system/readmehook.service"

if os.path.isfile(conf_filename):
    print("Moving {0} to {0}.old".format(conf_filename))
    os.rename(conf_filename, conf_filename + ".old")

with open(unit_filename, 'w+') as fd:
    fd.write(unit_template.replace("$hostname",hostname))
print("Written {} - don't forget to `systemctl enable`!".format(unit_filename))

with open(conf_filename, 'w+') as fd:
    fd.write(conf_template.replace("$hostname",hostname))
print("Written {}".format(conf_filename))

print("""
The files have now been copied, you need to:
 - ln -s {0} /etc/nginx/sites-enabled/{1}.hacksoc.org.conf  # enable the new config
 - systemctl reload nginx                                   # to update to the new config
 - systemctl daemon-reload                                  # scan for the new service file
 - systemctl enable readmehook.service                      # and enable it
""".format(conf_filename,hostname))