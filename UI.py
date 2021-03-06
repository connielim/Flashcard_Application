#!/usr/bin/python
from tkinter import *

class Window(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
         
        self.parent = parent
        
        self.initUI()
        
    
    def initUI(self):
      
        self.parent.title("Flashcard Application")
        self.pack(fill=BOTH, expand=1)
    

def main():
  
    root = Tk()
    root.geometry("600x600+150+50")
    app = Window(root)
    root.mainloop()  

if __name__ == '__main__':
    main()
