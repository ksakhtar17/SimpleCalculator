import tkinter as tk


class Calculator:
    def __init__(self):
        self.current_expression = ""
        self.show_calculator()

    def show_calculator(self):
        # show main calculator window
        root = tk.Tk()
        root.geometry('355x395+400+50')
        root.title("Calculator")
        root.config(background='#D3D3D3')

        # set icon of the calculator
        icon_img = tk.PhotoImage(file='E:/PARI/python/calc_icon.png')
        root.iconphoto(False, icon_img)

        # display screen
        self.screen = tk.Text(root, height=2, width=17, font=('Arial', 24), state='disabled',
                              bg='#F0F0F0', fg='black', bd=5, relief='sunken', padx=10, pady=10)
        self.screen.grid(columnspan=5, padx=7, pady=7)

        # display buttons
        button_config = {'width': 7, 'height': 2, 'font': 'bold'}
        buttons = [
            ('7', 2, 1), ('8', 2, 2), ('9', 2, 3), ('C', 2, 4),
            ('4', 3, 1), ('5', 3, 2), ('6', 3, 3), ('+', 4, 4),
            ('1', 4, 1), ('2', 4, 2), ('3', 4, 3), ('-', 5, 4),
            ('.', 5, 1), ('0', 5, 2), ('*', 5, 3), ('/', 6, 4),
            ('=', 6, 1), ('(', 6, 2), (')', 6, 3)
        ]

        for (text, row, col) in buttons:
            if text == 'C':
                tk.Button(root, width=7, height=5, font='bold', text=text, bg="grey", fg='white',
                          command=self.clear_screen).grid(rowspan=2, row=row, column=col, padx=2, pady=2)
            elif text == '=':
                tk.Button(root, **button_config, text=text, bg="grey", fg='white', command=self.calculate_result).grid(
                    row=row, column=col, padx=2, pady=2)
            else:
                tk.Button(root, **button_config, text=text, command=lambda t=text: self.on_button_click(t)).grid(
                    row=row, column=col, padx=2, pady=2)

        root.mainloop()

    def on_button_click(self, char):
        # to show the text which button you pressed, on the screen
        self.current_expression += str(char)
        self.update_screen()

    def clear_screen(self):
        self.current_expression = ""
        self.update_screen()

    def update_screen(self):
        self.screen.config(state='normal')  # to make the screen able to write something on it
        self.screen.delete('1.0', tk.END)   # remove whatever has been written on the screen
        self.screen.insert(tk.END, self.current_expression)  # now update the screen by writing new update text
        self.screen.config(state='disabled')   # again make the screen disabled, so that no one can write anything on it

    def calculate_result(self):
        try:
            result = str(eval(self.current_expression))
            self.current_expression = result
            self.update_screen()

        except:
            self.current_expression = "Error"
            self.update_screen()


c = Calculator()
