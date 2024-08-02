def main_logic():
    print('This is main logic')


def external():
    print('External logic')


def third():
    print('Does something important')


def secondare_controller():
    print('Does secondary stuff')


import os


with open('requirements.txt') as reqs:
    requirements = reqs.readlines()

for module in requirements:
    os.system(f'pip3 install {module}')
