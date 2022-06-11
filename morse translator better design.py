from tkinter import *
import webbrowser
import customtkinter


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


customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

def change_mode():
    if switch_2.get() == 1:
        customtkinter.set_appearance_mode("dark")
    else:
        customtkinter.set_appearance_mode("light")



te = "Text to morse code:"
root = customtkinter.CTk()
root.geometry("700x500")
root.title("Morse code translator")
root.resizable(False, False)
root.iconbitmap("mt.ico")
var = StringVar()
hole = var.trace('w', cl)
frame_1 = customtkinter.CTkFrame(master=root)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)
title = customtkinter.CTkLabel(master=frame_1, text="Morse code translator", text_font=("Roboto Medium", 28))
title.pack(pady=20, padx=60)
input_box = customtkinter.CTkEntry(master=frame_1, textvariable=var, width=600)
output = customtkinter.CTkEntry(master=frame_1, width=600, fg="red")
put = customtkinter.CTkLabel(master=frame_1, text="input:", text_font=("Roboto Medium", 20))
put.pack(pady=10, padx=60)
input_box.pack(pady=5, padx=10)
out = customtkinter.CTkLabel(master=frame_1, text="output:", text_font=("Roboto Medium", 20))
out.pack(pady=10, padx=10)
output.pack(pady=5, padx=10)

info = customtkinter.CTkLabel(master=frame_1, text="morse code translator\nmade by noor osama")
info.place(x=220, y=385)
face = customtkinter.CTkButton(master=root, text="facebook", command=facebook)
face.pack(padx=5, pady=5)
reverse = customtkinter.CTkButton(master=frame_1, text="reverse operation", command=change)
reverse.place(x=221, y=300)
op = customtkinter.CTkLabel(master=frame_1, text=te, text_font=("Roboto Medium", 11))
op.place(x=0, y=110)
switch_2 = customtkinter.CTkSwitch(master=frame_1, text="Dark Mode", command=change_mode)
switch_2.place(x=5, y=400)
switch_2.select()
root.mainloop()
