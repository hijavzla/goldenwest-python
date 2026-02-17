# Laura Rodriguez-Adjunta, CS131
# Project 5c: Celsius to Farenheit GUI 

import tkinter

class converterGUI: 

    def __init__(self): 
        # Create the main window widget 
        self.main_window = tkinter.Tk()

        # Add a title 
        self.main_window.title("Celsius to Fahrenheit Converter")

        # Create three frames to group widgets 
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create widgets for the top frame 
        self.prompt_label = tkinter.Label(self.top_frame, text='Enter temperature in Celsius:')
        self.temperature_entry = tkinter.Entry(self.top_frame, width=10)

        # Pack top frame's widgets
        self.prompt_label.pack(side='left')
        self.temperature_entry.pack(side='left')

        # Create widgets for the middle frame
        self.far_label = tkinter.Label(self.middle_frame, text='Converted to Fahrenheit:')

        # Set up StringVar to hold converted value 
        self.converted_temp = tkinter.StringVar()
        self.far_value = tkinter.Label(self.middle_frame, textvariable=self.converted_temp)

        # Pack the middle frame's widgets
        self.far_label.pack(side='left')
        self.far_value.pack(side='left')

        # Create widgets for bottom frame 
        self.calc_button = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        # Pack the bottom frame's widgets
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()
    
    # The convert method is a callback function for the 'Convert' button 
    def convert(self):
        # Get the value entered by the user
        celsius_entered = float(self.temperature_entry.get())

        # Convert Celsius to Farenheit
        faren_calculated = celsius_entered * (9/5) + 32

        # Convert faren_calculated into a String and store inside self.converted_temp
        self.converted_temp.set(faren_calculated)

# Create an instance of GUI
if __name__ == '__main__': 
    celsius_conv = converterGUI()
