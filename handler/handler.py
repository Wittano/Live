import subprocess

from watchdog.events import FileSystemEvent, FileSystemEventHandler


class FileHandler(FileSystemEventHandler):
    _subprocess = None

    def __init__(self, cmd: list, files: list):
        self._cmd = cmd
        self._files = files

    def on_any_event(self, event: FileSystemEvent):

        if event.event_type == "modified" and event.src_path in self._files:
            if self._subprocess is not None:
                print("\nTerminate the last process!\n")
                self._subprocess.terminate()

            self._subprocess = subprocess.Popen(self._cmd)
