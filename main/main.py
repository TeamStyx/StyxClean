import os
import os.path
import tkinter as tk
import tempfile as tf

win = tk.Tk()
win.title("StyxClean")

status = "idle"

def smartclean(status):

    tempdir = tf.gettempdir()
    no_files = 0

    if status == "delete":
        os.remove(tempdir)

    for _ in os.walk(tempdir):
        for _ in tempdir:
            no_files += 1

    statusTxt["text"] = f"Temporary files detected: {no_files}"
    smartcleanBtn["text"] = "Delete files"
    status = "delete"
    return status

smartcleanBtn = tk.Button(win, text="Smart Clean", command=smartclean)
smartcleanBtn.pack()

statusTxt = tk.Label(win)
statusTxt.pack()

win.mainloop()