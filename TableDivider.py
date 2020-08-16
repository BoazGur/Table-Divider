import tkinter as tk
from tkinter import filedialog
import pandas as pd

rows = 0
filename = ''
saved_filename = ''


def save():
    global rows
    global saved_filename
    rows = int(e1.get())
    saved_filename = filedialog.askdirectory(title='Choose Directory')
    master.quit()


def open():
    global filename
    filename = filedialog.askopenfilename(title='Choose File')


master = tk.Tk()
master.title('Table Divider')

tk.Label(master,
         text="Number of rows (for all write -1)").grid(row=0)

e1 = tk.Entry(master)

e1.grid(row=0, column=1)

tk.Button(master,
          text='Open', command=open).grid(row=3,
                                          column=0,
                                          sticky=tk.W,
                                          pady=4)
tk.Button(master,
          text='Save', command=save).grid(row=3,
                                          column=1,
                                          sticky=tk.W,
                                          pady=4)
tk.Button(master,
          text='Quit',
          command=master.quit).grid(row=3,
                                    column=2,
                                    sticky=tk.W,
                                    pady=4)

tk.mainloop()

# Pandas configurations
df = pd.read_csv(filename)

if rows == -1:
    rows = len(df)

for row in range(rows):
    new_df = df.iloc[row, :]
    new_df.to_csv(saved_filename + '/' + new_df['City'] + '.csv')

