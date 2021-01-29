$testDir=tmp/test

if [ ! -d  $testDir ]; then
    mkdir $testDir

    touch $testDir/__init__.py
    echo "print('Hello World!')" >> $testDir/test.py
fi
