import json
import subprocess

subprocess.run('sudo ./terraform-install.sh', shell=True)

with open('vars.json', 'r') as f:
  data = json.load(f)

  print(data)


# the result is a Python dictionary:
#print(data["age"])

if data["name"] == 'docker':
  subprocess.run('sudo ./terraform-docker.sh', shell=True)
