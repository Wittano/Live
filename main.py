import sys

from watchdog.observers import Observer

from handler.handler import FileHandler


def main():
    if sys.argv[1].endswith(".py"):
        path = sys.argv[1]
    else:
        raise IOError("Expect python file")

    observer = Observer()
    handler = FileHandler()
    handler.path = path
    observer.schedule(handler, path)
    observer.start()

    print(f"Start live reload file on {path}")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Stopping live reloading")
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()
