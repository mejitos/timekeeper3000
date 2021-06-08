#!/bin/python3.6
"""
Simple tool for keeping track of the time spent on a project
"""


import csv
import datetime
import os
import tkinter as tk


class TimeKeeper3000:
    """ Main class for the application """

    def __init__(self):
        """ Initializes the program """

        # Window options
        self.root_tk = tk.Tk()
        self.root_tk.geometry('500x250+300+300')
        self.root_tk.resizable(width=False, height=False)
        self.root_tk.title('TimeKeeper3000')
        frame = tk.Frame(self.root_tk, width=500, height=250)
        
        # Logo and headers
        logo_img = tk.PhotoImage(file='logo.gif')
        tk.Label(frame, image=logo_img).grid(row=0, rowspan=2, column=0, columnspan=5, padx=10, pady=12)
        tk.Label(frame, text='Time').grid(row=2, column=0, columnspan=2, padx=10)
        tk.Label(frame, text='Comment').grid(row=2, column=3, padx=10)

        # Time shit
        self.start_time = None
        tk.Label(frame, text='Start Time: ').grid(row=3, column=0)
        self.start_time_value = tk.StringVar()
        tk.Label(frame, textvariable=self.start_time_value, width=10).grid(row=3, column=1)
        self.start_time_value.set('--:--:--')

        self.end_time = None
        tk.Label(frame, text='End Time: ').grid(row=4, column=0)
        self.end_time_value = tk.StringVar()
        tk.Label(frame, textvariable=self.end_time_value, width=10).grid(row=4, column=1)
        self.end_time_value.set('--:--:--')

        tk.Label(frame, text='Total Spent: ').grid(row=5, column=0)
        self.total_spent_value = tk.StringVar()
        tk.Label(frame, textvariable=self.total_spent_value, width=10).grid(row=5, column=1)
        self.total_spent_value.set('--:--:--')

        # Comment entry
        self.comment = tk.Text(frame, height=5, width=35)
        self.comment.grid(row=3, rowspan=3, column=3, padx=10)

        # Buttons
        self.btn_text = tk.StringVar()
        self.time_btn = tk.Button(frame, textvariable=self.btn_text, state='normal', width=10)
        self.btn_text.set('Start')
        self.time_btn.grid(row=6, column=0, columnspan=2, pady=5)
        self.time_btn.bind('<Button-1>', self.get_time)
        self.submit_btn = tk.Button(frame, text='Submit', state='disabled', width=10)
        self.submit_btn.grid(row=6, column=3, pady=5)
        self.submit_btn.bind('<Button-1>', self.submit_entry)
        
        # Pack and loop de loop
        frame.pack()
        self.root_tk.mainloop()

    
    def get_time(self, event):
        """ Gets the current time """

        if self.start_time_value.get() == '--:--:--':
            self.start_time = datetime.datetime.now()
            start_str = str(self.start_time)
            self.start_time_value.set(start_str[11:19])
            self.btn_text.set('End')
        elif self.end_time_value.get() == '--:--:--':
            self.end_time = datetime.datetime.now()
            end_str = str(self.end_time)
            self.end_time_value.set(end_str[11:19])
            self.btn_text.set('Start')
            self.time_btn.configure(state='disabled')
            self.submit_btn.configure(state='normal')
        if self.start_time != None and self.end_time != None:
            total = str(self.end_time - self.start_time)
            self.total_spent_value.set(total[:7])


    def submit_entry(self, event):
        """ Submits an entry to a CSV-file """

        fields = ['start time', 'end time', 'total spent', 'comment']
        entry = []
        file_name = 'tracking-timo.csv'

        start_time_str = str(self.start_time)
        entry.append(start_time_str[:19])
        end_time_str = str(self.end_time)
        entry.append(end_time_str[:19])
        entry.append(self.total_spent_value.get())
        entry.append(self.comment.get('1.0', 'end-1c'))

        if os.path.isfile(file_name):
            with open(file_name, 'a', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(entry)
        else:
            with open(file_name, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(fields)
                csv_writer.writerow(entry)
        
        self.start_time_value.set('--:--:--')
        self.end_time_value.set('--:--:--')
        self.total_spent_value.set('--:--:--')
        self.start_time = None
        self.end_time = None
        self.comment.delete('1.0', tk.END)
        self.time_btn.configure(state='normal')
        self.submit_btn.configure(state='disabled')


if __name__ == "__main__":
    TimeKeeper3000()
