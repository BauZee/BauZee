import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

from View.MainGUI import PyjamaParty

if __name__ == "__main__":
    app=PyjamaParty()
    app.mainloop()