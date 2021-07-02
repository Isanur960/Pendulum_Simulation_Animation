#Author :: Isanur Sardar
import matplotlib.pyplot as plt
import numpy as np
import os, psutil , gc, sys

def AngToPos(th):
  xl = l * np.sin(th)
  yl = l * np.cos(th)
  xp = fx + xl
  yp = fy - yl
  return xp, yp
