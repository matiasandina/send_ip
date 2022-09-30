import uuid
import re
import os
import posixpath
import yaml
import paramiko
from scp import SCPClient
import datetime
import socket
from py_console import console
import sys 

# In Ubuntu, you can setup this using crontabs
# In windows, there's no crontab
# check how to configure scheduler here
# https://www.askpython.com/python/examples/execute-python-windows-task-scheduler

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def get_mac():
    parsed_mac = re.findall('..', '%012x' % uuid.getnode())
    return(':'.join(parsed_mac))


def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

def create_info():
    # Write the info to file
    computer_name = socket.gethostname().upper()
    mac = get_mac()
    info  = {'computer_name': computer_name, 
             'mac': mac,
             'ip': get_ip(),
             'time': datetime.datetime.now().isoformat()}

    # do filename + _ + last 4 of mac address . yaml
    info_file = f"{computer_name}_{mac.replace(':', '')[:4]}.yaml"
    with open(info_file, 'w') as outputfile:
        outputfile.write(yaml.dump(info))
    if hasattr(sys, 'ps1'):
        console.success(f"{info_file} written")
    return info_file

def send_info(info_file):
    # Now connect and send the info
    with open("config.yaml", "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    ssh = createSSHClient(config["ip"], config["port"], config["user"], config["pass"])
    remote_path = posixpath.join('/home', config['user'], config['remote-path'])
    ssh.exec_command(f'mkdir -p {remote_path}')
    scp = SCPClient(ssh.get_transport())
    scp.put(info_file, remote_path=remote_path)

    # Check transfer was correct
    scp.get(posixpath.join(remote_path, info_file), "temp.yaml")

    with open("temp.yaml", "r") as temp:
        temp = yaml.load(temp, Loader=yaml.FullLoader)

    if temp['ip'] == info['ip']:
        os.remove("temp.yaml")
        if hasattr(sys, 'ps1'):
            console.success("Transfer was successful", severe=T)
    else: 
        os.remove("temp.yaml")
        if hasattr(sys, 'ps1'):
            console.error("Transfer was not successful", severe=T)


    # TODO: add logging ?