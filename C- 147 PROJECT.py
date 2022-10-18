from tkinter import*
root= Tk()
root.title("ascii")
root.geometry("400x400")
root.configure(background= "blue")
enter_word= Entry(root)
enter_word.place(relx=0.5,rely=0.4, anchor=CENTER)
label= Label(root, text= "name is ascii:",bg= "pink", fg= "black")
label2= Label(root, text= "name in encrypted:",bg= "pink", fg= "black")

def ascii():
    input_word= enter_word.get()
    for letter in input_word:
        label["text"]+=str(ord(letter))+"  "
        ascii= int(ord(letter))
        encrypted= ascii-1
        label2["text"]+= str(chr(encrypted))
btn= Button(root, text ="show text in ascii and encrypted form", bg="aqua", fg= "black",command= ascii)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)
label.place(relx=0.5, rely=0.6, anchor= CENTER)
label2.place(relx=0.5, rely=0.7, anchor=CENTER)
root.mainloop()