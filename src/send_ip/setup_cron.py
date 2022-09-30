from crontab import CronTab
import yaml
import getpass

def setup_cron():
    # Read info
    with open("config.yaml", "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    # this is what we want to run
    #cmd_command = "bash ~/homecage_quantification/send_ip.sh"
    # TODO: it should run python3 send_ip.py

    job_comment = f"send ip to {config['user']}"

    # Get cron object
    cron = CronTab(user=getpass.getuser())
    # don't create a new job if it is already there
    # first check if it's already there

    job_exists = any(list(map(lambda x: x.comment == job_comment, cron)))

    if job_exists:
        for job in cron:
            if job.comment == job_comment:
                print("job named: " + job_comment + " already exists, scheduling 1 minute")
                job.minute.every(1)
                # write the program
                cron.write()
    else:
        # only here, create it
        # create a new job
        job = cron.new(command = cmd_command, comment=job_comment)
        # schedule it every minute
        job.minute.every(1)
        # write the program
        cron.write()

    print("Current cron tab (same as $ crontab -l)")
    print("--------------------------------------")
    print(cron)

if __name__ == '__main__':
    setup_cron()