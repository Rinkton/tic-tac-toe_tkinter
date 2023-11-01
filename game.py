from tkinter import *
from ui import UI


class Game:

    frame = None
    root = None
    first_is_person = False
    second_is_person = False

    def __init__(self, root, first_is_person, second_is_person):
        self.root = root
        self.first_is_person = first_is_person
        self.second_is_person = second_is_person

    def back_to_menu(self):
        self.frame.pack_forget()
        self.frame.destroy()

    def g(self, a, b):
        print(a, b)

    def main(self):
        self.frame = Frame()
        self.frame.place(x=0, y=0)
        self.frame.pack(fill='both', expand=1)
        ui = UI(self.frame)

        ui.create_image("imgs/bg.png", 640, 360)
        for y in range(3):
            for x in range(3):
                ui.create_button("imgs/cell.png", 467.5 + 180 * x, 220 + 180 * y, self.g, x, y)
        ui.create_button("imgs/back.png", 90, 90, self.back_to_menu)

        self.root.mainloop()