# Send IP

Python software to configure machines for sending their IP through ssh.

## Installation

Run the following to install:

```python
pip3 install send_ip
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
2. Use the pacakge functions, for example:

```
from send_ip.send_ip import *

info_file = create_info()
send_info(info_file)
```

You can save this into a `send_ip_script.py` and schedule this task to run automatically (see below)

## Schedule task

### Chron


### Windows machines

Please refer to [this example](https://stackoverflow.com/a/59079452/3215940) and file issues if having trouble.

## For developers of `send_ip`

To install `send_ip` and tools needed for tests, you can install into a virtualenvironment like so:

```bash
pip install -e .[dev]
```
## Known issues

For a Raspberry pi installation, you might face this issue:

```
          =============================DEBUG ASSISTANCE=============================
          If you are seeing a compilation error please try the following steps to
          successfully install bcrypt:
          1) Upgrade to the latest pip and try again. This will fix errors for most
             users. See: https://pip.pypa.io/en/stable/installing/#upgrading-pip
          2) Ensure you have a recent Rust toolchain installed. bcrypt requires
             rustc >= 1.56.0.
      
          Python: 3.9.2
          platform: Linux-5.15.56-v7l+-armv7l-with-glibc2.31
          pip: n/a
          setuptools: 65.5.0
          setuptools_rust: 1.5.2
          rustc: n/a
          =============================DEBUG ASSISTANCE=============================
      

```

You might need:

```
sudo apt-get install build-essential cargo
```

You can also refer to this info in [bcrypt](https://pypi.org/project/bcrypt/).

You might also need to install or upgrade `rustc`

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```