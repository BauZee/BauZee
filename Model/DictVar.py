import tkinter


class DictVar(tkinter.Variable):
    def __init__(self):
        super().__init__()
        self.value= {}