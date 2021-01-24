import fire
import subprocess

def init():
    bashCommand = "git init"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    return

def stage():
    bashCommand = 'git add .'
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    return

def commit(message: str):
    bashCommand = 'git commit -m "%s"' % (message)
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    return

if __name__ == "__main__":
    fire.Fire({
        "init": init,
        "stage": stage,
        "commit": commit
    })
