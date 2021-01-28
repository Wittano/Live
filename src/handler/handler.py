import subprocess

from watchdog.events import FileSystemEvent, FileSystemEventHandler, DirModifiedEvent


class FileHandler(FileSystemEventHandler):
    _subprocess = None

    def __init__(self, cmd: list, files: list):
        self._cmd = cmd
        self._files = files

    def on_modified(self, event: DirModifiedEvent):
        if event.src_path in self._files:
            if self._subprocess is not None:
                print("\nTerminate the last process!\n")
                self._subprocess.terminate()

            self._subprocess = subprocess.Popen(self._cmd)
