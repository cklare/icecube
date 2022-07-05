# take 2 - the last file got corrupted
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
from icecube import dataio, dataclasses
from I3Tray import *
from glob import glob

tray = I3Tray()
tray.Add("I3Reader", filename="evel2_IC86.2020_NuTau.021989.000031.i3")
tray.Add("Dump","dump")
tray.Execute()


