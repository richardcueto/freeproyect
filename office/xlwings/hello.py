# hello.py
import numpy as np
import xlwings as xw

def world():
    wb = xw.Book.caller()
    wb.sheets[0]['A1'].value = 'Hello World! yupt'

