import glob
import os
import sys

from watchdog.observers import Observer

if __name__ == "__main__":
    from handler.handler import FileHandler
else:
    from .handler.handler import FileHandler


def main() -> None:
    path = get_path()
    directory = path.replace(f'/{path.split("/")[-1]}', "")

    handler = FileHandler(get_args(), get_files(directory))
    handler.path = path

    observer = Observer()
    observer.schedule(handler, directory)
    observer.start()

    print(f"Start live reload file on {path}")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Stopping live reloading")
        observer.stop()
    observer.join()


def get_args(path="") -> list:
    """
    Create dict for subprocess.Popen() function

    Parameters:
    path (str): Path to main file
    """
    path = get_path(path)

    cmd = ["python", path]
    for arg in sys.argv[2:]:
        cmd.append(arg)

    return cmd


def get_path(path="") -> str:
    if path == "":
        path = sys.argv[1]

    if is_exist(path) and path.endswith(".py"):
        return path
    elif not is_exist(path):
        raise IOError(f"File {path} not found")
    else:
        raise IOError("Expect python file")


def is_exist(path: str) -> bool:
    return os.path.isdir(path) or os.path.isfile(path)


def get_files(path: str) -> dict:
    """
    Create files dict, which will be observed by live-reloading program

    Parameters:
    path (str): Directory, which is observed
    """

    return glob.glob(path + "/**/*.py", recursive=True) if is_exist(path) else None


if __name__ == "__main__":
    main()
