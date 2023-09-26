import os


class Paths:
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    TEMP_DIR = os.path.join(ROOT_DIR, 'temp')
