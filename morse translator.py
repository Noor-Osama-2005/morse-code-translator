from tkinter import *
import webbrowser


def switch(*args):
    mm = var.get().replace(" / ", " ").replace(".----. ", "'").replace("_... ", "b").replace(
        "_._. ", "c").replace(".._. ", "f").replace(".... ", "h").replace(
        ".___ ", "j").replace("._.. ", "l").replace(
        ".__. ", "p").replace("__._ ", "q").replace("._. ", "r").replace("... ", "s").replace("..._ ", "v").replace("_.._ ", "x").replace("_.__ ", "y").replace(
        "__.. ", "z").replace(".__ ", "w").replace("___ ", "o").replace("__. ", "g").replace("_._ ", "k").replace("_.. ", "d").replace(".._ ", "u").replace("._ ", "a").replace("__ ", "m").replace("_. ", "n").replace(".. ", "i").replace("_ ", "t").replace(". ", "e")
    output.config()
    output.delete(0, END)
    output.insert(0, mm)


def change_label(*args):
    n = var.get().replace(" ", " / ").replace("'", ".----. ").replace("d", "_.. ").replace("a", "._ ").replace("b",
                                                                                                               "_... ").replace(
        "c", "_._. ").replace("e", ". ").replace("f", ".._. ").replace("g", "__. ").replace("h", ".... ").replace("i",
                                                                                                                  ".. ").replace(
        "j", ".___ ").replace("k", "_._ ").replace("l", "._.. ").replace("m", "__ ").replace("n", "_. ").replace("p",
                                                                                                                 ".__. ").replace(
        "o", "___ ").replace("q", "__._ ").replace("r", "._. ").replace("s", "... ").replace("t", "_ ").replace("u",
                                                                                                                ".._ ").replace(
        "v", "..._ ").replace("w", ".__ ").replace("x", "_.._ ").replace("y", "_.__ ").replace("z", "__.. ")
    output.config()
    output.delete(0, END)
    output.insert(0, n)


def facebook():
    url = 'https://www.facebook.com/profile.php?id=100008506127598'
    webbrowser.open(url)


cl = change_label


def change():
    global cl, var, hole, te
    try:
        var.trace_vdelete("w", hole)
    except (TclError, NameError):
        pass
    if cl == switch:
        cl = change_label
    else:
        cl = switch
    hole = var.trace('w', cl)
    if te == "Text to morse code:":
        te = "Morse code to text:"
    else:
        te = "Text to morse code:"

    op.config(text=te)



te = "Text to morse code:"
root = Tk()
root.geometry("700x500")
root.title("Morse code to text")
root.resizable(False, False)
root.configure(bg="cyan")
root.iconbitmap("mt.ico")
var = StringVar()
hole = var.trace('w', cl)
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
title = Label(root, text="Morse code translator", font=("", "25"), fg="#8300fe", bg="cyan")
title.place(x=195, y=30)
info = Label(root, text="morse code translator\nmade by noor osama")
info.place(x=0, y=465)
face = Button(root, text="facebook", bg="blue", fg="white", font=("", "13"), command=facebook)
face.place(x=620, y=467)
reverse = Button(root, text="reverse operation", command=change)
reverse.place(x=293, y=300)
op = Label(root, text=te, bg="cyan", font=("", "10"))
op.place(x=50, y=120)
root.mainloop()
