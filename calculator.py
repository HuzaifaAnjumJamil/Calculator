from tkinter import*

# Created Main class for Calculator


class Application(Frame):

    """Initialize the Frame """

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.tasks = " "
        self.UserIn = StringVar()
        self.grid()
        self.create_widget()

    def create_widget(self):
        """Buttons for Calculator"""

        self.user_input = Entry(self, bg="#5BC8AC", bd=29,
                                insertwidth=4, width=24,
                                font=("Verdana", 20, "bold"), textvariable=self.UserIn, justify=RIGHT)
        self.user_input.grid(columnspan=4)

        self.user_input.insert(0, "0")
