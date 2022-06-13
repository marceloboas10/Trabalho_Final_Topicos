
from cProfile import label
from optparse import Values
import os
from tkinter import messagebox
os.system('cls')
from distutils.cmd import Command
from tkinter import *
from tkinter import ttk
import sqlite3
import time
from turtle import end_fill
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import datetime
import webbrowser
import pycep_correios
import json
#from matplotlib.pyplot import text  # Importação da biblioteca do Tkinter