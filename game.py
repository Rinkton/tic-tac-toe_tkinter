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

    def kok(self):
        self.frame.pack_forget()
        self.frame.destroy()

    def main(self):
        self.frame = Frame()
        self.frame.place(x=0, y=0)
        self.frame.pack(fill='both', expand=1)
        ui = UI(self.frame)
        
        ui.create_button("imgs/vs.png", 4, 4, self.kok)

        self.root.mainloop()