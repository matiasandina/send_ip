from crontab import CronTab
import yaml
import getpass
import os

def setup_cron(script_path, minutes=None):
    assert os.path.exists(script_path), f"File does not exist. {script_path} was provided"
    assert script_path.endswith("py"), f"File does not seem to be a python script. {script_path}"
    # Read info
    with open("config.yaml", "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    
    if minutes is None:
        minutes = config.get('refresh-freq')
        if minutes is None:
            print("Error: 'refresh-freq' not specified in config.yaml.")
            return
    
    # Ensure minutes is a positive integer
    try:
        minutes = int(minutes)
        if minutes <= 0:
            raise ValueError
    except ValueError:
        print(f"Error: 'minutes' must be a positive integer. {minutes} was provided.")
        return

    # Extract the Python path from config, fallback to 'python3' if not specified
    python_path = config.get('python_path', 'python3')

    # Warn if using the default python path
    if python_path == 'python3':
        print("Warning: Using default 'python3' path. Ensure this is intended.")

    # Check if the specified python path exists
    if not os.path.exists(python_path):
        print(f"Error: The specified python path does not exist: {python_path}")
        return
    
    # Build the command to run, incorporating the specified Python interpreter
    cmd_command = f"cd {os.path.dirname(script_path)} && {python_path} {script_path}"

    job_comment = f"send ip to {config['user']}"

    # Get cron object
    cron = CronTab(user=getpass.getuser())
    # don't create a new job if it is already there
    # first check if it's already there

    job_exists = any(list(map(lambda x: x.comment == job_comment, cron)))

    if job_exists:
        for job in cron:
            if job.comment == job_comment:
                print(f"job named: {job_comment} already exists, scheduling every {minutes} minute")
                job.minute.every(minutes)
                # write the program
                cron.write()
    else:
        # only here, create it
        # create a new job
        job = cron.new(command = cmd_command, comment=job_comment)
        # schedule it every minute
        job.minute.every(minutes)
        # write the program
        cron.write()

    print("Current cron tab (same as $ crontab -l)")
    print("--------------------------------------")
    print(cron)

if __name__ == '__main__':
    print("Calling from command line is not supported yet")
    pass