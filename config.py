from configparser import ConfigParser

file = 'config.ini'
config = ConfigParser()
config.read(file)

blue = '\033[94m'
endc = '\033[0m'
green = '\033[92m'
red = '\033[91m'
yellow = '\033[93m'
