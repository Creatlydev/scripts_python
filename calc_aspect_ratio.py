import tkinter as tk
from tkinter import ttk
from math import ceil


class NumberEntry(ttk.Entry):
    def __init__(self, master= None, value= 1080, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.var = tk.IntVar(value=value)
        self.configure(textvariable=self.var)
        
        self.configure(validate='key')
        self.configure(validatecommand=(
            self.register(self.validate_input), '%P'))

    def validate_input(self, input_text):
        if input_text.isdigit():
            return True
        else:
            return False
    
    def set(self, new_value):
        self.var.set(new_value)


def keep_aspect_ratio(
    size: tuple[int, int],
    new_size: tuple[int, int]
):
    """_summary_: Keep the aspect ratio of size.

    Args:
        width (int): _description_
        height (int): _description_
    """
    w, h = size
    n_w, n_h = new_size

    if n_w != w:
        n_h = int(n_w / w * h)
        return f"Nuevo Size= {n_w}x{n_h}"
    if n_h != h:
        n_w = int(n_h / h * w)
        return f"Nuevo Size= {n_w}x{n_h}"


class Frame(ttk.Frame):

    def __init__(self, master=None, **kw) -> None:
        super().__init__(master, **kw)
        self.master = master
        self.pack()
        
        self.width= 1080
        self.height= 1920

        self.create_widgets()

    def create_widgets(self):
        self.lb_title = ttk.Label(self.master, text="Mantener Aspect Ratio")
        self.input_width = NumberEntry(master= self.master)
        self.input_height = NumberEntry(master= self.master, value=self.height)

        # Ubicar elementos
        self.lb_title.pack(side=tk.TOP, pady=40)
        self.input_width.pack(pady=10)
        self.input_height.pack(pady=10)

        # Agregar eventos a los Entry
        self.input_width.bind("<KeyRelease>", self.on_enter_width)
        self.input_height.bind("<KeyRelease>", self.on_enter_height)

    def on_enter_width(self, event):
        new_width = int(event.widget.get())
        new_height= ceil(new_width / self.width * self.height)
        self.input_height.set(new_height)
        
    def on_enter_height(self, event):
        new_height= int(event.widget.get())
        new_width= ceil(new_height / self.height * self.width)
        self.input_width.set(new_width)
        


def center_window(
        root: tk.Tk,
        width: int,
        height: int
):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    return f'{width}x{height}+{x}+{y}'


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry(center_window(root, 300, 350))
    root.resizable(False, False)
    root.title("Aspect Ratio")

    app = Frame(root)

    root.mainloop()
