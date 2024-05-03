from tkinter import *

#create pycrypto as tkinter for GUI
pycrypto = Tk()
#title
pycrypto.title("My Crypto Portfolio")

#"Bitcoin" label in body & in next line told to put output on top-middle grid 
name = Label(pycrypto,text="Bitcoin")
name.pack()

#end
pycrypto.mainloop()
