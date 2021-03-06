from Atbash import Encryptor,Decryptor
import tkinter as tk
from tkinter import ttk

class Cipher:
    def __init__(self,master):

        # for encrypt
        self.frame = tk.Frame(master,bd=1,relief=tk.RAISED)
        self.frame.pack(expand=1,side=tk.LEFT,pady=5,padx=10,fill=tk.X)
        iframe = tk.Frame(self.frame)
        iframe.pack(expand=1)
        label = tk.Label(iframe,text="Plain text",font="Times 20 bold")
        label.pack(padx=10)
        self.ebutton = tk.Button(iframe,text="Encrypt",command=self.enc,font="Arial 15")
        self.ebutton.pack(side=tk.LEFT,padx=10)
        self.ebutton = tk.Button(iframe,text="Clear",command=lambda: self.clear(0),font="Arial 15")
        self.ebutton.pack(padx=10)
        self.text = tk.Text(self.frame,height=40,width=65,fg="black",font="Times 15")
        self.text.pack(padx=10,pady=1)
        

        # for decrypt
        self.frame = tk.Frame(master,bd=1,relief=tk.RAISED)
        self.frame.pack(expand=1,pady=5,padx=10,fill=tk.X)
        eframe = tk.Frame(self.frame)
        eframe.pack(expand=1)
        label = tk.Label(eframe,text="Cipher text",font="Times 20 bold")
        label.pack(padx=10)
        self.dbutton = tk.Button(eframe,text="Decrypt",command=self.dec,font="Arial 15")
        self.dbutton.pack(side=tk.LEFT,padx=10)
        self.dbutton = tk.Button(eframe,text="Clear",command=lambda: self.clear(1),font="Arial 15")
        self.dbutton.pack(padx=10)
        self.etext = tk.Text(self.frame,height=40,width=65,fg="black",font="Times 15")
        self.etext.pack(padx=10,pady=1)
    
    def enc(self):
        text = get(self.text)
        #text = re.sub(r'[^A-Za-z]',"",text)
        etext = Encryptor(text.upper())
        self.etext.delete("1.0","end")
        self.etext.insert(tk.END,etext)
    
    def dec(self):
        etext = get(self.etext)
        #etext = re.sub(r'[^A-Za-z]',"",etext)
        text = Decryptor(etext.lower())
        self.text.delete("1.0","end")
        self.text.insert(tk.END,text)

    def clear(self,opt):
        if opt == 0:
            self.text.delete("1.0","end")
        else:
            self.etext.delete("1.0","end")

def get(obj):
    return obj.get("1.0","end").strip()

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Atbash Cipher")
    #window.geometry("700x700")
    enc = Cipher(window)
    window.mainloop()