import sys
import os

from matplotlib import pyplot as plt

os.chdir('/home/paul/Documents/python-neo/')

sys.path.append('.')  # Add current directory to path
import neo
# from neo.io.openephysbinaryio import *
# from neo.rawio.openephysbinaryrawio import *

rec_path = '/mnt/g/To Process/PMA97/PMA97 2025-03-13 Session 1/PMA97 2025-03-13_12-21-42 Opto Config 2'

reader = neo.io.OpenEphysBinaryIO(rec_path)
blks = reader.read(lazy=False)
print(blks)
