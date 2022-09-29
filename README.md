# Send IP

Python software to configure machines for sending their IP through ssh.

## Installation

Run the following to instal:

```python
pip install send_ip
```

## Usage

1. Edit the `config.yaml` file to match your destination. These fields will be used to `scp` into the target machine (`user@ip:port` using password `pass` to login).

```yaml
user: target-user
ip: ip-address
pass: target-password
port: target-port #default port is usually 22 
remote-path: target-folder # this folder will be created under /home/user might create errors for not linux users
refresh-freq: 15 # minutes for cron-job
```
2. Run the main script from command line (`python3 send_ip.py`).

You can schedule this task to run automatically (see below)

## Schedule task

### Chron


### Windows machines

Please refer to [this example](https://stackoverflow.com/a/59079452/3215940) and file issues if having trouble.

## For developers of `send_ip`

To install `send_ip` and tools needed for tests, you can install into a virtualenvironment like so:

```bash
pip install -e .[dev]
```
