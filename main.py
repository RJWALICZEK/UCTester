import tkinter as tk

window = tk.Tk()
window.geometry("400x250")
window.title("UCTester")

device_name = tk.StringVar

status_frame = tk.Frame(window)


dev_label = tk.Label(status_frame, text="Device: ")
dev_name = tk.Label(status_frame, textvariable=device_name )

window.call()
status_frame.grid()
dev_label.grid(row=0, column=0)
dev_name.grid(row=0, column=1)

window.mainloop()