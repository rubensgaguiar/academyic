from subprocess import Popen, CalledProcessError
import subprocess
import time
import signal
import os
from sacademy.applications import Application


class LauncherException(Exception):
    """ Exception class to handle unsuccessfull launching."""

    def __init__(self, launchedcmd: str, return_code: int) -> None:
        super(Exception, self).__init__(f"Execution of {launchedcmd} failed. Exited with status code {return_code}.")
        self.launchedcmd = launchedcmd
        self.return_code = return_code


class Launcher:
    """ Class responsible for launching a given task in a separate process through the OS."""

    def __init__(self, app: Application) -> None:
        self.binpath = app.bin
        self.options = app.options
        self.process = None
        self.launched = False

    def launch(self) -> None:
        """ Launches the binary path set with the option list set"""
        if self.binpath is None:
            raise RuntimeError("No launching command set.")
        if self.launched:
            return

        cmdline_options = self.options.serialize() if self.options is not None else ""
        cmd = f"{self.binpath} {cmdline_options}"
        try:
            self.process = subprocess.Popen(cmd, shell=True, preexec_fn=os.setsid)
            time.sleep(1)
            self.launched = True
        except CalledProcessError as error:
            cmd = error.cmd
            returncode = error.returncode
            if returncode != 0:
                raise LauncherException(cmd, returncode)

    def kill(self) -> None:
        if self.process is not None and self.process.poll() is None:
            os.kill(self.process.pid, signal.SIGKILL)
            os.killpg(os.getpgid(self.process.pid), signal.SIGTERM)
            self.process.kill()
