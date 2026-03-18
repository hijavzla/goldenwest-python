# Laura Rodriguez-Adjunta, CS131
# Project 10 (Long Distance Calls pg. 715)

import tkinter
import tkinter.messagebox

class myGUI: 

    def __init__(self): 
        # Create the main window widget 
        self.main_window = tkinter.Tk()

        # Add a title 
        self.main_window.title("Long Distance Call Calculator")

        # Create three frames to group widgets 
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        ## Create widgets for the top frame 
        # First, create a label widget that tells user the telephone rates are as follows
        self.label1 = tkinter.Label(self.top_frame, text='Telephone rates:')

        # Next, create three Radiobuttons buttons with an IntVar initialized 
        # Radiobuttons must have an IntVar object to hold the value of the selected Radiobutton 
        self.radio_var = tkinter.IntVar() 

        # Set the IntVar object to the first option initially 
        self.radio_var.set(1)

        # Create the Radiobutton widgets
        self.rb1 = tkinter.Radiobutton(self.top_frame, text='Daytime (6:00am-5:59pm)', variable=self.radio_var, value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame, text='Evening (6:00pm-11:59pm)', variable=self.radio_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame, text='Off-Peak (midnight-5:59am)',variable=self.radio_var, value=3)

        # Pack the top frame's 4 widgets on top of eachother
        self.label1.pack()
        self.rb1.pack() 
        self.rb2.pack()
        self.rb3.pack()

        ## Create widgets for the middle frame
        # First, create a label widget, that asks the user for the number of minutes
        self.prompt_label = tkinter.Label(self.middle_frame, text='Enter the number of minutes:')

        # Next, create an entry widget for the user to input the number of minutes
        self.minutes_entry = tkinter.Entry(self.middle_frame, width=10)

        # Pack the middle frame's 2 widgets next to each other
        self.prompt_label.pack(side='left')
        self.minutes_entry.pack(side='left')
        
        
        ## Create widgets for the bottom frame 
        # First, create button widget with 'OK' that calls the calculate method with the input value 
        self.ok_button = tkinter.Button(self.bottom_frame, text='OK',command=self.calculate)

        # Then, create button widget with 'Quit' that lets the user exit the program 
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        # Pack bottom frame's 2 widgets next to eachother 
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        ## Pack all of the frames  
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop
        tkinter.mainloop() 

    # The calculate method is a callback function for the OK button
    def calculate(self): 
        # get the minutes entered by the user
        minutes = float(self.minutes_entry.get())

        # Determine minute cost depending on which radio button is selected 
        multiplier = 0 
        if self.radio_var.get() == 1: 
            multiplier = .07
        if self.radio_var.get() == 2: 
            multiplier = .12
        if self.radio_var.get() == 3: 
            multiplier = .05

        # multiply minutes by the time selected in the radio buttons
        total_price = minutes * multiplier

        # Display results in an info dialog box
        tkinter.messagebox.showinfo('Results', f'Your total cost is: ${total_price:.2f}')

# Create an instance of myGUI
if __name__ == '__main__': 
    my_gui = myGUI()