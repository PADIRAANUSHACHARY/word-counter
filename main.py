import tkinter as tk
from tkinter import messagebox

def opening_file():
  try:
    with open(rd_file.get(),"r") as f:
      text = f.read()
      s = len(text)
      result_label.config(text=f"Word Count: {s}", fg="black")
      error_label.config(text="")
  except Exception as e:
      error_message = f"Error: {e}"
      result_label.config(text="") 
      error_label.config(text=error_message, fg="red")


def reseting():
    rd_file.config(text="")
    result_label.config(text="Word Count: ", fg="black")
    error_label.config(text="")
    rd_file.delete(0, tk.END)

def close_window():
  if messagebox.askyesno("Exit", "Do you want to exit?"):
        main.destroy()
# opening a window
main = tk.Tk()
main.geometry('350x300')
# setting bg color
main.configure(bg="aqua")
# setting title
main.title("Application")
# setting a label
head = tk.Label(main,text="WORD COUNTER",font=("Helvetica",18,'bold'),bg="aqua")
head.pack(pady=10)

subtitle = tk.Label(main,text="Enter text file name: ",font=("Helvetica",12,'bold'),bg="aqua")
subtitle.pack(pady=10,padx=10)
rd_file = tk.Entry(main)
rd_file.pack(pady=5)
# creating buttons : submit,reset,end
subimt_but = tk.Button(main,text="SUBMIT",command=opening_file)
subimt_but.pack()

reset_button = tk.Button(main, text="Reset", command=reseting)
reset_button.pack(pady=10)

result_label = tk.Label(main,text="Word Count: ",font=("Helvetica",12,'bold'),bg="aqua")
result_label.pack()

# labeling error
error_label = tk.Label(main, text="", fg="red",bg="aqua")
error_label.pack()

end_button = tk.Button(main, text="End", command=close_window)
end_button.pack()
main.mainloop()
