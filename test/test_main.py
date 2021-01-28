import pytest
from src.main import is_exist, get_args, get_files

files = [
    "",
    "\n",
    "    ",
    "tmp/test/test2s31.py",
    "asdfgdsiufgysauifsedgifyws/aqsdgahsyu",
    "tmp/test/main.c",
    "tmp/test/main.p",
]

correct = [
    "tmp/test/test_file.py",
    "tmp/test/test2.py",
]

files.extend(correct)


@pytest.mark.parametrize("paths", files)
def test_get_args(paths: str):
    if paths not in correct:
        try:
            get_args(paths)
        except IOError:
            assert True
            return

    args = get_args(paths)

    assert args[0] == "python"
    assert args[1] == paths
    assert args[2:] == ["test"]


@pytest.mark.parametrize("paths", files)
def test_get_files(paths: str):
    directory = paths.replace(f'/{paths.split("/")[-1]}', "")

    if paths in correct:
        files = get_files(directory)

        assert files is not None
    else:
        try:
            get_files(directory)
            assert False
        except Exception:
            assert True


@pytest.mark.parametrize("paths", files)
def test_is_exist(paths: str):
    if paths in correct:
        assert is_exist(paths) is True
    else:
        assert is_exist(paths) is False
