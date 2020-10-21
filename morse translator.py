from tkinter import *
import webbrowser
def change_label(*args):
    n = var.get().replace("d", "_.. ").replace("a", "._ ").replace("b", "_... ").replace("c", "_._. ").replace("e", ". ").replace("f", ".._. ").replace("g", "__. ").replace("h", ".... ").replace("i", ".. ").replace("j", ".___ ").replace("k", "_._ ").replace("l", "._.. ").replace("m", "__ ").replace("n", "_. ").replace("p", ".__. ").replace("o", "___ ").replace("q", "__._ ").replace("r", "._. ").replace("s", "... ").replace("t", "_ ").replace("u", ".._ ").replace("v", "..._ ").replace("w", ".__ ").replace("x", "_.._ ").replace("y", "_.__ ").replace("z", "__.. ")
    output.config()
    output.delete(0, END)
    output.insert(0, n)

def facebook():
    url = 'https://www.facebook.com/profile.php?id=100008506127598'
    webbrowser.open(url)


root = Tk()
root.geometry("700x500")
root.title("morse code to text")
root.iconbitmap(r"C:\Users\EH\Downloads\lego_h2l_icon.ico")
root.configure(bg="cyan")
var = StringVar()
var.trace('w', change_label)
input_box = Entry(root, textvariable=var, width=100)
input_box.place(x=50, y=150)
trans = Label(root, bg="cyan")
output = Entry(root, width=100, fg="red")
put = Label(root, text="input:", fg="black", font=("", "20"), bg="cyan")
put.place(x=310, y=90)
out = Label(root, text="output:", fg="black", font=("", "20"), bg="cyan")
trans.pack()
out.place(x=300, y=200)
output.place(x=50, y=250)
title = Label(root, text="morse code translator", font=("", "25"), fg="#8300fe", bg="cyan")
title.place(x=195, y=30)
info = Label(root, text="morse code translator\nmade by noor osama")
info.place(x=0, y=465)
face = Button(root, text="facebook", bg="blue", fg="white", font=("", "13"), command=facebook)
face.place(x=620, y=467)
root.mainloop()
