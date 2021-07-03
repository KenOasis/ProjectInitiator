import os

def touch(path):
    with open(path, 'a'):
        os.utime(path, None)
        print('Created File:', path)

def mkdirs(basedir):
    if not os.path.exists(basedir):
        os.makedirs(basedir)
        print('Created directory:',basedir)

