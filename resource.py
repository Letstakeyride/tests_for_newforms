from imghdr import tests
from pathlib import Path

file_name = 'test.jpg'


def path(file_name):
    return str((Path().joinpath(f'resources/{file_name}').absolute()))

