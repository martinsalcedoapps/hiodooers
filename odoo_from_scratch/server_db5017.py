#encoding: utf-8
import os

port = 5017
db_user = 'odoo17'
db_pass = 'odoo17'
name = "db%s" %(port)
localpath = os.path.abspath(".")

print("STOP DOCKER CONTAINER")
os.system("docker stop %s" %(name))

print("REMOVE DOCKER CONTAINER")
os.system("docker rm %s" %(name))

print("PREPARING DOCKER DB SERVER")
print("PORT: ", port)

cmd  = "docker run --name db%s " %(port)
cmd += "-e POSTGRES_USER=%s " %(db_user)
cmd += "-e POSTGRES_PASSWORD=%s " %(db_pass)
cmd += "-e POSTGRES_DB=postgres "
cmd += "-e PGDATA=/mnt/postgres "
cmd += "-v %s/%s/:/mnt/postgres/ " %(localpath, name)
cmd += "-v %s/backups/:/mnt/backups/ " %(localpath)
cmd += "-p %s:5432 " %(port)
cmd += "--restart=always "
cmd += "--shm-size=256m "
cmd += "-d "
cmd += "postgres:15 "

print(cmd)
os.system(cmd)
