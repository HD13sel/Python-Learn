from tkinter import *

class MyApp:
    def __init__(self, parent):
        # ------ constantes para controle do layout ------
        button_width = 10
        button_padx = "5m"
        button_pady = "5m"
        buttons_frame_padx = "10m"
        buttons_frame_pady = "10m"
        buttons_frame_ipadx = "5m"
        buttons_frame_ipady = "5m"
        # -------------- fim das constantes ----------------

        self.myParent = parent
        self.buttons_frame = Frame(parent)
        self.buttons_frame.pack(ipadx=buttons_frame_ipadx, ipady=buttons_frame_ipady, padx=buttons_frame_padx,
                                pady=buttons_frame_pady)

        self.button1 = Button(self.buttons_frame, command=self.button1Click)
        self.button1.configure(text="OK", background="green")
        self.button1.focus_force()
        self.button1.configure(width=button_width, padx=button_padx, pady=button_pady)
        self.button1.pack(side=LEFT)
        self.button1.bind("<Return>", self.button1Click_a)

        self.button2 = Button(self.buttons_frame, command=self.button2Click)
        self.button2.configure(text="Cancel", background="red")
        self.button2.configure(width=button_width, padx=button_padx, pady=button_pady)
        self.button2.pack(side=RIGHT)
        self.button2.bind("<Return>", self.button2Click_a)

    def button1Click(self):
        if self.button1["background"] == "green":
            self.button1["background"] = "yellow"
        else:
            self.button1["background"] = "green"

    def button2Click(self):
        self.myParent.destroy()

    def button1Click_a(self, event):
        self.button1Click()

    def button2Click_a(self, event):
        self.button2Click()


root = Tk()
myapp = MyApp(root)
root.mainloop()


