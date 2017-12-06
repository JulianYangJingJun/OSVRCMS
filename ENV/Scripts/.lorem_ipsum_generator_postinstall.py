#!C:\Program Files\Python25\python.exe

from os.path import abspath
from sys import prefix
from sys import argv

if len(argv) >= 2 and argv[1] == "-install":
	create_shortcut(abspath(prefix + '/pythonw.exe'), 'Generates random lorem ipsum text', abspath(get_special_folder_path('CSIDL_COMMON_PROGRAMS') + '/Lorem Ipsum Generator.lnk'), '"' + abspath(prefix + '/Scripts/lipsum') + '"')
