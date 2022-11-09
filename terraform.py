import json
import subprocess

subprocess.run('sudo ./scripts/terraform-install.sh', shell=True)

with open('vars.json', 'r') as f:
  data = json.load(f)

  print(data)


# the result is a Python dictionary:
#print(data["age"])

if data["name"] == 'docker':
  subprocess.run('sudo ./scripts/terraform-docker.sh', shell=True)
if data["name"] == 'hadoop':
  subprocess.run('sudo ./scripts/terraform-hadoop.sh', shell=True)
if data["name"] == 'kubernetes':
  subprocess.run('sudo ./scripts/terraform-kubernetes.sh', shell=True)
