import subprocess


class PythonRunner:
    """
    Script runner for python script or programs
    """

    def __init__(self):
        self.file_target = ""

    def run(self):
        """
        Execute python prorgam without any args
        """
        subprocess.run(["python", self.file_target])
