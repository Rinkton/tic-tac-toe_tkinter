from tkinter import *
from ui import UI


class Game:

    frame = None

    def kok(self):
        self.frame.pack_forget()
        self.frame.destroy()

    def main(self, root):
        self.frame = Frame()
        self.frame.place(x=0, y=0)
        self.frame.pack(fill='both', expand=1)
        ui = UI(self.frame)
        
        ui.create_button("imgs/vs.png", 4, 4, self.kok, )

        root.mainloop()