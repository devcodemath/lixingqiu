"""注册gif到屏幕里一行代码即可.py"""
from glob import glob
from turtle import Screen

screen = Screen()
[screen.addshape(image) for image in glob("images/*.gif")]
