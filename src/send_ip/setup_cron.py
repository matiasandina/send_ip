from crontab import CronTab
import yaml
import getpass
import os

def setup_cron(script_path, minutes):
    assert isinstance(minutes, int), f"Provide minutes as an integer. {minutes} was provided"
    assert os.path.exists(script_path), f"File does not exist. {script_path} was provided"
    assert script_path.endswith("py"), f"File does not seem to be a python script. {script_path}"
    # Read info
    with open("config.yaml", "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    # This is what we want to run
    cmd_command = f"cd {os.path.dirname(script_path)} && python3 {script_path}"

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
    setup_cron()