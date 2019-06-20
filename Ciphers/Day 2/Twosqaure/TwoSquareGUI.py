from twosqaure import encrypt,decrypt,matrix
import tkinter as tk
from tkinter import ttk
from wordsegment import load,segment

class Start:
    def __init__(self,master):
        self.frame = tk.Frame(master,width=700,height=200)
        self.frame.pack(pady=1,padx=10)
        labelA = tk.Label(self.frame,text="Key 1 ",fg="black",font="Arial 15")
        self.a = tk.Text(self.frame,height=1,width=15,font="Times 15")
        labelA.pack(side=tk.LEFT,padx=5)
        self.a.pack(side=tk.LEFT,padx=1)
        labelB = tk.Label(self.frame,text="Key 2 ",fg="black",font="Arial 15")
        self.b = tk.Text(self.frame,height=1,width=15,font="Times 15")
        labelB.pack(side=tk.LEFT,padx=5)
        self.b.pack(side=tk.LEFT,padx=1)

class Cipher:
    def __init__(self,master,obj):
        self.k1 = obj.a
        self.k2 = obj.b

        # for encrypt
        self.frame = tk.Frame(master,width=650,height=200,bd=1,relief=tk.RAISED)
        self.frame.pack(pady=25,padx=10,fill=tk.X)
        self.text = tk.Text(self.frame,height=4,width=50,fg="black",font="Times 15")
        self.text.pack(side=tk.LEFT,padx=10,pady=15)
        iframe = tk.Frame(self.frame)
        iframe.pack(expand=1)
        self.ebutton = tk.Button(iframe,text="Encrypt",command=self.enc,font="Arial 18")
        self.ebutton.pack(padx=10,pady=10)
        self.ebutton = tk.Button(iframe,text="Clear",command=lambda: self.clear(0),font="Arial 18")
        self.ebutton.pack(padx=10,pady=10)

        # for the squares
        self.frame = tk.Frame(master,width=650)
        self.frame.pack(pady=1,padx=10,fill=tk.X)
        # first row
        self.top = tk.Text(self.frame,height=5,width=11,fg="black",font="Times 15")
        self.top.pack(padx=100,pady=10)
        # second row
        self.bot = tk.Text(self.frame,height=5,width=11,fg="black",font="Times 15")
        self.bot.pack(padx=100,pady=10)


        # for decrypt
        self.frame = tk.Frame(master,width=650,height=200,bd=1,relief=tk.RAISED)
        self.frame.pack(pady=5,padx=10,fill=tk.X)
        self.etext = tk.Text(self.frame,height=4,width=50,fg="black",font="Times 15")
        self.etext.pack(side=tk.LEFT,padx=10,pady=15)
        eframe = tk.Frame(self.frame)
        eframe.pack(expand=1)
        self.dbutton = tk.Button(eframe,text="Decrypt",command=self.dec,font="Arial 18")
        self.dbutton.pack(padx=10,pady=10)
        self.dbutton = tk.Button(eframe,text="Clear",command=lambda: self.clear(1),font="Arial 18")
        self.dbutton.pack(padx=10,pady=10)
    
    def enc(self):
        text = get(self.text).upper()
        key1 = get(self.k1).upper()
        key2 = get(self.k2).upper()
        self.sett(key1,key2)
        etext = encrypt(text.upper(),key1,key2)
        self.etext.delete("1.0","end")
        self.etext.insert(tk.END,etext)
    
    def dec(self):
        etext = get(self.etext).upper()
        key1 = get(self.k1).upper()
        key2 = get(self.k2).upper()
        self.sett(key1,key2)
        text = decrypt(etext,key1,key2)
        text = segment(text)
        if 'x' in text[-1] and len(text[-1]) == 1:
            text = text[:-1]
        self.text.delete("1.0","end")
        self.text.insert(tk.END," ".join(text).lower())

    def clear(self,opt):
        if opt == 0:
            self.text.delete("1.0","end")
        else:
            self.etext.delete("1.0","end")
    
    def sett(self,key1,key2):
        # key 1 matrix
        mat1 = matrix(key1)
        self.top.delete("1.0","end")
        self.printMat(mat1,1)
        # key 2 matrix
        mat2 = matrix(key2)
        self.bot.delete("1.0","end")
        self.printMat(mat2,2)


    
    def printMat(self,mat,opt):
        for counter in range(5):
            put = mat[counter][0] + ' ' + mat[counter][1] + ' ' + mat[counter][2] + ' ' + mat[counter][3] + ' ' + mat[counter][4] + '\n'
            if opt == 1:
                self.top.insert(tk.END,put)
            else:
                self.bot.insert(tk.END,put)

def get(obj):
    return obj.get("1.0","end").strip()

if __name__ == "__main__":
    load()
    window = tk.Tk()
    window.title("TwoSquare Cipher")
    #window.geometry("700x700")
    sobj = Start(window)
    enc = Cipher(window,sobj)
    window.mainloop()
