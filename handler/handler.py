import re
import subprocess

from watchdog.events import FileSystemEvent, FileSystemEventHandler


class FileHandler(FileSystemEventHandler):
    _path = ""

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, val: str):
        if len(val) == 0:
            raise ValueError("Path must not be empty or none")
        elif re.search("py$", val) is None:
            raise ValueError(f"{val} is wrong path. Path must be keept to python file")

        self._path = val

    def on_any_event(self, event: FileSystemEvent):
        if event.event_type == "modified" and not event.is_directory:
            self.run(["python", self._path])

    def run(self, cmd: dict):
        """
        Parameters:
        cmd (dict): Command with args, which will be run
        """
        subprocess.run(cmd)
