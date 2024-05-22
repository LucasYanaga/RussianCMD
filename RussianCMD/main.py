import GameManager as gm
import sys
import subprocess


if __name__ == '__main__':
    subprocess.check_call([sys.executable, "-m", "pip", "install", "keyboard"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
    gm.run()


