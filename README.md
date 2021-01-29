# Live
Simple live-reloading for Python projects

# Prerequiments
Live require [watchdog](https://github.com/gorakhargosh/watchdog) package. You can install with pip manager or you can use pipenv, but if you choose second options, you'll have to run by pipenv command:
```bash
bash test.sh
pipenv run dev
```
If you can't run bash script(test.sh), you'll change path in Pipfile or create python file about the following path: <path_to_your_dir>/tmp/test/test.py

# Run program
```bash
python src/main.py <path_to_your_script> <optional_args>
```

# Run test
```bash
bash test.sh
pipenv run test
```
