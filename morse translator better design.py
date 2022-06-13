from tkinter import *
import webbrowser
import customtkinter


def switch(*args):
    ko = var.get() + " "
    mm = ko.replace("/ ", " ").replace(".----. ", "'").replace("-... ", "b").replace(
        "-.-. ", "c").replace("..-. ", "f").replace(".... ", "h").replace(
        ".--- ", "j").replace(".-.. ", "l").replace(
        ".--. ", "p").replace("--.- ", "q").replace(".-. ", "r").replace("... ", "s").replace("...- ", "v").replace(
        "-..- ", "x").replace("-.-- ", "y").replace(
        "--.. ", "z").replace(".-- ", "w").replace("--- ", "o").replace("--. ", "g").replace("-.- ", "k").replace(
        "-.. ", "d").replace("..- ", "u").replace(".- ", "a").replace("-- ", "m").replace("-. ", "n").replace(".. ",
                                                                                                              "i").replace(
        "- ", "t").replace(". ", "e")
    output.config()
    output.delete(0, END)
    output.insert(0, mm)


def change_label(*args):
    bo = var.get().lower()
    n = bo.replace(" ", "/ ").replace("'", ".----. ").replace("d", "-.. ").replace("a", ".- ").replace("b",
                                                                                                       "-... ").replace(
        "c", "-.-. ").replace("e", ". ").replace("f", "..-. ").replace("g", "--. ").replace("h", ".... ").replace("i",
                                                                                                                  ".. ").replace(
        "j", ".--- ").replace("k", "-.- ").replace("l", ".-.. ").replace("m", "-- ").replace("n", "-. ").replace("p",
                                                                                                                 ".--. ").replace(
        "o", "--- ").replace("q", "--.- ").replace("r", ".-. ").replace("s", "... ").replace("t", "- ").replace("u",
                                                                                                                "..- ").replace(
        "v", "...- ").replace("w", ".-- ").replace("x", "-..- ").replace("y", "-.-- ").replace("z", "--.. ")
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


font = "Libre Baskerville"
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
title = customtkinter.CTkLabel(master=frame_1, text="Morse code translator", text_font=(font, 28))
title.pack(pady=20, padx=60)
input_box = customtkinter.CTkEntry(master=frame_1, textvariable=var, width=600)
output = customtkinter.CTkEntry(master=frame_1, width=600, fg="red")
put = customtkinter.CTkLabel(master=frame_1, text="Input:", text_font=(font, 20))
put.pack(pady=10, padx=60)
input_box.pack(pady=5, padx=10)
out = customtkinter.CTkLabel(master=frame_1, text="Output:", text_font=(font, 20))
out.pack(pady=10, padx=10)
output.pack(pady=5, padx=10)

info = customtkinter.CTkLabel(master=frame_1, text="Morse code translator\nMade by Noor Osama")
info.place(x=220, y=385)
face = customtkinter.CTkButton(master=root, text="Facebook", command=facebook)
face.pack(padx=5, pady=5)
reverse = customtkinter.CTkButton(master=frame_1, text="Reverse operation", command=change)
reverse.place(x=221, y=300)
op = customtkinter.CTkLabel(master=frame_1, text=te, text_font=(font, 11))
op.place(x=0, y=110)
switch_2 = customtkinter.CTkSwitch(master=frame_1, text="Dark Mode", command=change_mode)
switch_2.place(x=10, y=400)
switch_2.select()
root.mainloop()
