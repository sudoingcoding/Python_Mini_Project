from tkinter import *
import requests
import json

pycrypto = Tk()
pycrypto.title("My Crypto Portfolio")

name = Label(pycrypto,text="Bitcoin",bg="black",fg="white") #label with text "Bitcoin" & background black and front color white
name.grid(row=0,column=0,sticky=N+S+E+W) #top-left grid and sticky(move to any direction)

pycrypto.mainloop()