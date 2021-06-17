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

        # Button for value 0
        self.button9 = Button(self, bg="#98DBC6", bd=12,
                              text="0",  padx=33, pady=25,
                              command=lambda: self.buttonClick(0), font=("Helvetica", 20, "bold"))
        self.button9.grid(row=5, column=0, sticky=W)

        # Button for value 1
        self.button7 = Button(self, bg="#98DBC6", bd=12,
                              text="1",  padx=33, pady=25,
                              command=lambda: self.buttonClick(1), font=("Helvetica", 20, "bold"))
        self.button7.grid(row=4, column=0, sticky=W)
