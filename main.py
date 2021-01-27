import glob
import sys

from watchdog.observers import Observer

from handler.handler import FileHandler


def main() -> None:
    if sys.argv[1].endswith(".py"):
        path = sys.argv[1]
    else:
        raise IOError("Expect python file")

    directory = path.replace(f'/{path.split("/")[-1]}', "")

    handler = FileHandler(get_args(path), get_files(directory))
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


def get_args(path: str) -> list:
    """
    Create dict for subprocess.Popen() function
    """
    cmd = ["python", path]
    for arg in sys.argv[2:]:
        cmd.append(arg)

    return cmd


def get_files(path: str) -> dict:
    """
    Create files dict, which will be observed by live-reloading program

    Parameters:
    path (str): Directory, which is observed
    """
    return glob.glob(path + "/**/*.py", recursive=True)


if __name__ == "__main__":
    main()
