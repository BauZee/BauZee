import ast
import tkinter


class DictVar(tkinter.Variable):
    """Value holder for strings variables."""
    _default = dict()

    def __init__(self, master=None, value=None, name=None):
        """Construct a string variable.

        MASTER can be given as master widget.
        VALUE is an optional value (defaults to "")
        NAME is an optional Tcl name (defaults to PY_VARnum).

        If NAME matches an existing variable and VALUE is omitted
        then the existing value is retained.
        """
        tkinter.Variable.__init__(self, master, value, name)

    def get(self):
        """Return value of variable as string."""

        value = self._tk.globalgetvar(self._name)
        if isinstance(value, dict):
            return value
        value = ast.literal_eval(value)
        return value