import os
from tkinter import *
from tkinter import filedialog, colorchooser
from tkinter.messagebox import *
from tkinter.filedialog import *

def change_color_font():
    color = colorchooser.askcolor(title="Pilih Warna")
    colorhex = color[1]
    text_area.config(fg=colorhex)    

def change_color_bg():
    color = colorchooser.askcolor(title="Pilih Warna")
    colorhex = color[1]
    text_area.config(background=colorhex)

def change_fonts(font_name):
    text_area.config(font=(font_name, font_size.get()))

def change_size(size):
    text_area.config(font=(font_name.get(), size))
    
def reset():
    text_area.config(font=("consolas", 16) ,fg="#ffc800", background="#19325c")

def new_file():
    window.title("Untitled")
    text_area.delete(1.0, END)

def open_file():
    file = askopenfilename(title="Open File", defaultextension=".txt", file=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    try:
        window.title(os.path.basename(file))
        text_area.delete(1.0, END)
        file = open(file, "r")
        text_area.insert(1.0, file.read())
    except Exception:
        showerror(title="Error", message="File error tidak dapat dibuka")
    finally:
        file.close()
    
def save_files():
    file = filedialog.asksaveasfile(title="Save File", initialfile="Untitled", defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")], mode='w')
    if file is None:
        return
    else:
        try:
            window.title(os.path.basename(file.name))
            file.write(text_area.get(1.0, END))
            showinfo(title="File Saved", message="File berhasil disimpan")
        except Exception:
            showerror(title="Error", message="Gagal menyimpan file")
        finally:
            file.close()

def copy():
    text_area.event_generate("<<Copy>>")

def cut():
    text_area.event_generate("<<Cut>>")

def paste():
    text_area.event_generate("<<Paste>>")
    
def about():
    showinfo(title="About", message="Ini adalah program teks editor\nyang dibuat dari bahasa python")

def quit():
    if askyesno(title="Exit", message="Apakah anda yakin ingin keluar?"):
        window.destroy()

window = Tk()
icon_note = PhotoImage(file="Gambar\\notepad.png")
window.title("Notepad")
window.iconphoto(True, icon_note)

window_width = 900
window_height = 600
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

file = None

font_name = StringVar()
font_name.set("consolas")

font_size = StringVar()
font_size.set("16")

text_area = Text(window, font=(font_name.get(), font_size.get()), fg="#ffc800", background="#19325c", cursor="xterm", insertbackground="white")
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New File", command=new_file)
file_menu.add_command(label="Open File", command=open_file)
file_menu.add_command(label="Save File", command=save_files)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Paste", command=paste)
edit_menu.add_separator()
edit_menu.add_command(label="Color Font", command=change_color_font)
edit_menu.add_command(label="Color Background", command=change_color_bg)

font_families = ["Arial", "Calibri", "Cambria", "Comic Sans MS", "Consolas", "Courier New", "Georgia", "Helvetica", "Impact", "Lucida Console", "Lucida Sans Typewriter", "Microsoft Sans Serif", "Tahoma", "Times New Roman", "Verdana"]
font_menu = Menu(edit_menu, tearoff=0)
edit_menu.add_cascade(label="Font", menu=font_menu)
for font_family in font_families:
    font_menu.add_command(label=font_family, command=lambda font_family=font_family: change_fonts(font_family))

size_opt = [8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72]
size_menu = Menu(edit_menu, tearoff=0)
edit_menu.add_cascade(label="Size", menu=size_menu)
for size in size_opt:
    size_menu.add_command(label=str(size), command=lambda size=size: change_size(size))

edit_menu.add_separator()
edit_menu.add_command(label="Reset", command=reset)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

window.mainloop()