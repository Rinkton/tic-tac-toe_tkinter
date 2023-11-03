from tkinter import *
from ui import UI
from field import Field


class Game:

    frame = None
    ui = None
    root = None
    first_is_person = False
    second_is_person = False
    field = None

    def __init__(self, root, first_is_person, second_is_person):
        self.root = root
        self.first_is_person = first_is_person
        self.second_is_person = second_is_person
        self.field = Field()

    def back_to_menu(self):
        self.frame.pack_forget()
        self.frame.destroy()

    def g(self, a, b):
        print(a, b)

    def on_cell_button_enter(self, event):
        obj, x, y = self.field.find_obj_by_widget(event.widget)
        obj = self.ui.change_button(obj, "imgs/x-to-put.png")
        self.field.cells[y][x] = obj
        obj.elem.bind('<Leave>', self.on_cell_button_leave)

    def on_cell_button_leave(self, event):
        obj, x, y = self.field.find_obj_by_widget(event.widget)
        obj = self.ui.change_button(obj, "imgs/cell.png")
        self.field.cells[y][x] = obj
        obj.elem.bind('<Enter>', self.on_cell_button_enter)

    def main(self):
        self.frame = Frame()
        self.frame.place(x=0, y=0)
        self.frame.pack(fill='both', expand=1)
        self.ui = UI(self.frame)

        self.ui.create_image("imgs/bg.png", 640, 360)
        for y in range(3):
            for x in range(3):
                cell_button = self.ui.create_button(
                    "imgs/cell.png", 467.5 + 180 * x, 220 + 180 * y, self.g, x, y)
                self.field.cells[y][x] = cell_button
                cell_button.elem.bind('<Enter>', self.on_cell_button_enter)
        self.ui.create_button("imgs/back.png", 90, 90, self.back_to_menu)

        self.root.mainloop()