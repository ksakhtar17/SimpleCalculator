import tkinter as tk

class Calculator:
    def __init__(self):
        """Set up the initial state of the calculator
        and call the method to display the calculator window."""
        self.current_expression = ""  # Stores the current expression to be displayed
        self.show_calculator()         # Set up and show the calculator window

    def show_calculator(self):
        """
        Create and configure the main calculator window, including the screen and buttons.
        """
        # Create the main window
        root = tk.Tk()
        root.geometry('355x395+400+50')  # Set window size and position
        root.title("Calculator")         # Set the window title
        root.config(background='#D3D3D3')  # Set the background color

        # Set icon of the calculator
        icon_img = tk.PhotoImage(file='calc_icon.png')  # Load the icon image
        root.iconphoto(False, icon_img)  # Set the icon for the window

        # Create and display the calculator screen
        self.screen = tk.Text(root, height=2, width=17, font=('Arial', 24), state='disabled',
                              bg='#F0F0F0', fg='black', bd=5, relief='sunken', padx=10, pady=10)
        self.screen.grid(columnspan=5, padx=7, pady=7)

        # Button configuration
        button_config = {'width': 7, 'height': 2, 'font': 'bold'}
        buttons = [
            ('7', 2, 1), ('8', 2, 2), ('9', 2, 3), ('C', 2, 4),
            ('4', 3, 1), ('5', 3, 2), ('6', 3, 3), ('+', 4, 4),
            ('1', 4, 1), ('2', 4, 2), ('3', 4, 3), ('-', 5, 4),
            ('.', 5, 1), ('0', 5, 2), ('*', 5, 3), ('/', 6, 4),
            ('=', 6, 1), ('(', 6, 2), (')', 6, 3)
        ]

        # Create and place buttons in the grid
        for (text, row, col) in buttons:
            if text == 'C':
                # Special button to clear the screen
                tk.Button(root, width=7, height=5, font='bold', text=text, bg="grey", fg='white',
                          command=self.clear_screen).grid(rowspan=2, row=row, column=col, padx=2, pady=2)
            elif text == '=':
                # Special button to calculate the result
                tk.Button(root, **button_config, text=text, bg="grey", fg='white', command=self.calculate_result).grid(
                    row=row, column=col, padx=2, pady=2)
            else:
                # Regular buttons for numbers and operators
                tk.Button(root, **button_config, text=text, command=lambda t=text: self.on_button_click(t)).grid(
                    row=row, column=col, padx=2, pady=2)


        root.mainloop()

    def on_button_click(self, char):
        """
        Handle button click events. Append the clicked button's text to the current expression
        and update the screen.
        """
        self.current_expression += str(char)  # Append the clicked character to the expression
        self.update_screen()  # Update the screen to reflect the new expression

    def clear_screen(self):
        """Clear the current expression and update the screen."""
        self.current_expression = ""  # Reset the expression
        self.update_screen()  # Update the screen to reflect the cleared expression

    def update_screen(self):
        """Update the calculator screen to display the current expression."""

        self.screen.config(state='normal')  # Enable text modification on the screen
        self.screen.delete('1.0', tk.END)   # Remove existing content on the screen
        self.screen.insert(tk.END, self.current_expression)  # Insert the current expression
        self.screen.config(state='disabled')   # Disable text modification to prevent user input

    def calculate_result(self):
        """Evaluate the current expression and display the result on the screen."""
        try:
            result = str(eval(self.current_expression))  # Evaluate the expression
            self.current_expression = result  # Update the expression with the result
            self.update_screen()  # Update the screen to show the result

        except:
            self.current_expression = "Error"  # Display 'Error' if evaluation fails
            self.update_screen()  # Update the screen to show the error

# Create an instance of the Calculator class to run the application
c = Calculator()
