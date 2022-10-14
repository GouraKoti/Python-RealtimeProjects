pip install tkinter                               #to build a GUI application.
pip install pytube                                #to download videos from youtube

from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("YouTube Downloader built by Goura')

Label(root, text = "Successfully Downloaded. Enjoy!", font = 'arial 20 bold').pack()

link =StringVar()

Label(root, text="Paste Link Here:", font = 'arial  15 bold').place(x = 160,y = 60)
link_enter = Entry(root, width =70, textvariable = link).place(x = 32, y = 90)

def Downloader():
    url = YouTube(string(link.get())
    
