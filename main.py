from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from ui import UI


if __name__ == '__main__':
    root = Tk()
    root.title("Приложение на Tkinter")

    ui = UI()
    geometry_s = ui.get_root_geometry()
    root.geometry(geometry_s)

    ui.create_image("Folder.png", 0.5, 0)

    root.mainloop()
