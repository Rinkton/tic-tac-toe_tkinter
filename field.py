class Field:
    cells = []


    def __init__(self):
        for i in range(3):
            self.cells.append([None, None, None])

    def find_obj_by_widget(self, widget):
        y = 0
        for row in self.cells:
            x = 0
            for cell in row:
                if cell.elem == widget:
                    return cell, x, y
                x += 1
            y += 1