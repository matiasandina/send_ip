# Send IP

Python software to configure machines for sending their IP through ssh.

## Installation

You are advised to create a virtual environment for this program:

```
conda create -n "send_ip_env" python=3.10 pip=23.0.1
conda activate send_ip_env
```

Run the following to install:

```python
pip3 install send_ip
```

Running from a virtual environment will affect the python path that you supply to `config.yaml`. See information in [Usage](#usage) section.

## Usage

1. Make a `/send_ip` folder in your home directory and create a `config.yaml`

```
mkdir send_ip
cd send_ip
touch config.yaml # also nano config.yaml if you are familiar
```

2. Edit the `config.yaml` file to match your destination. These fields will be used to `scp` into the target machine (`user@ip:port` using password `pass` to login).


```yaml
user: target-user
ip: ip-address
pass: target-password
port: target-port #default port is usually 22 
remote-path: target-folder # this folder will be created under /home/user might create errors for not linux users
refresh-freq: 15 # minutes for cron-job
python_path: /path/to/virtualenv/bin/python3 # the python path you supply here will affect where the code runs (e.g., /usr/bin/python3), see docs! 
```

> [!TIP]
> If you are unsure about your python path. Activate your virtual environment and `which python`.


3. You can use this 'natively' in python. To use the pacakge functions, for example:

```
from send_ip.send_ip import *

info_file = create_info()
send_info(info_file)
```

You can save this into a `send_ip_script.py` and schedule this task to run automatically (see below)

## Schedule task

### Cron

You can setup `send_ip_script.py` to run on a schedule (e.g., every 60 minutes). For example, this is the configuration for a raspberry pi (`pi`) sending its IP to another machine (`matias`) using `config.yaml`.

```
from send_ip.setup_cron import setup_cron
setup_cron("/home/pi/send_ip/send_ip_script.py",60)
Current cron tab (same as $ crontab -l)
--------------------------------------

*/60 * * * * cd python3 /home/pi/send_ip/ && /home/pi/send_ip/send_ip_script.py # send ip to matias

```


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

**Don't forget to restart your shell after installation of rust!!**