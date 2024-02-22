# encoding: utf-8

import os

port = 8017
name = 'odoo17ce'
dblink = 'db5017'
localpath = os.path.abspath(".")

print("STOP DOCKER CONTAINER")
os.system("docker stop %s" % (name))

print("REMOVE DOCKER CONTAINER")
os.system("docker rm %s" % (name))

cmd  = "docker run "
cmd += '--name %s ' %(name)
cmd += '-v %s/odoo17ce.conf:/etc/odoo/odoo.conf ' %(localpath)
cmd += '-v %s/extra-addons:/mnt/extra-addons ' %(localpath)
cmd += '-v %s/var_lib_odoo:/var/lib/odoo ' %(localpath)

cmd += '-p %s:8069 ' %(port)
cmd += '--link %s:db ' %(dblink)
# cmd += '--network host '
# cmd += '-d '
cmd += '-t odoo:17.0 '

vcmd = cmd
vcmd = vcmd.replace("-v ", "\n-v ")
vcmd = vcmd.replace("-p ", "\n-p ")
print(vcmd)
os.system(cmd)
