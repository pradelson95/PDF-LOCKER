from tkinter import *
from tkinter import filedialog, messagebox
from PyPDF2 import PdfWriter, PdfReader
import os

window = Tk()
window.geometry("900x570")
window.config(background="snow")


def delete_fields():
    entry_pdf_path.configure(state="normal")
    entry_pdf_path.delete(0, END)
    entry_pdf_name.delete(0, END)
    entry_pdf_password.delete(0, END)


def browse_file():
    upload_pdf = filedialog.askopenfilename(defaultextension=".pdf", initialdir="C:/",
                                            filetypes=[('pdf file', '*.pdf')])
    entry_pdf_path.insert(END, upload_pdf)  # insertar la ruta del direcotrio donde esta el pdf en el primer campo
    entry_pdf_path.configure(state="disabled")  # deshabilitar el campo


def lock_pdf():
    path = entry_pdf_path.get()
    pwd = entry_pdf_password.get()
    pdf_name = entry_pdf_name.get()

    if not os.path.exists(path):
        messagebox.showerror("Error", "The path that you have entered does not exist")

    if path == "" and pwd == "" and pdf_name == "":
        messagebox.showerror("Invalid", "Both fields are empty!!")

    elif path == "":
        messagebox.showerror("Invalid", "The path field must not be empty")

    elif pwd == "":
        messagebox.showerror("Invalid", "The password field must not be empty")

    elif pdf_name == "":
        messagebox.showerror("Invalid", "The pdf name field must not be empty")

    else:
        try:
            reader = PdfReader(path)
            writer = PdfWriter()

            # Add all pages to the writer
            for page in reader.pages:
                writer.add_page(page)

            # Add a password to the new PDF
            writer.encrypt(pwd)

            # Save the new PDF to a file
            with open(pdf_name+".pdf", "wb") as f:
                writer.write(f)
                messagebox.showinfo("Info", f"The pdf file has been encrypted successfully in the following path: {os.path.abspath(pdf_name)}"+".pdf")

        except EXCEPTION as error:
            print(error)


frame = Frame(window, width=900, height=115, background="cyan")
frame.place(x=0, y=0)

img_1 = PhotoImage(file="candado_2.png")
show_img_1 = Label(window, image=img_1, bg="cyan")
show_img_1.place(x=10, y=5)

lbl_title = Label(window,
                  text="Free Pdf File Locker",
                  font=("Roboto", 40, "bold"),
                  bg="cyan")
lbl_title.place(x=190, y=20)

frame_line = Frame(window,
                   width=850,
                   height=400,
                   highlightbackground="black",
                   highlightthickness=3,
                   background="snow")
frame_line.place(x=25, y=140)

lbl_select_pdf_file = Label(frame_line,
                            text="Select PDF File:",
                            font=("Comic Sans", 15),
                            bg="snow")
lbl_select_pdf_file.place(x=40, y=50)

lbl_pdf_name = Label(frame_line,
                     text="Pdf Name:",
                     font=("Comic Sans", 15),
                     bg="snow")
lbl_pdf_name.place(x=40, y=100)

entry_pdf_name = Entry(frame_line,
                       width=35,
                       font=("McLaren", 15),
                       highlightbackground="black",
                       highlightcolor="black",
                       highlightthickness=1)
entry_pdf_name.place(x=230, y=100)

lbl_set_password = Label(frame_line,
                         text="Type The Password:",
                         font=("Comic Sans", 15),
                         bg="snow")
lbl_set_password.place(x=40, y=150)

entry_pdf_path = Entry(frame_line,
                       width=35,
                       font=("McLaren", 15),
                       highlightbackground="black",
                       highlightcolor="black",
                       highlightthickness=1)
entry_pdf_path.place(x=230, y=50)

entry_pdf_password = Entry(frame_line,
                           width=35,
                           font=("McLaren", 15),
                           highlightbackground="black",
                           highlightcolor="black",
                           highlightthickness=1)

entry_pdf_password.place(x=230, y=150)

img_2 = PhotoImage(file="subir.png")
show_img_2 = Button(frame_line,
                    text="Upload File",
                    image=img_2,
                    bg="snow",
                    compound="top",
                    foreground="red",
                    command=browse_file)
show_img_2.place(x=740, y=45)

img_3 = PhotoImage(file="lock_3.png")
lock_pdf_btn = Button(frame_line,
                      text="Protect Pdf File",
                      font=("Roboto", 18, "bold"),
                      image=img_3,
                      bg="white",
                      compound="left",
                      state="active",
                      command=lock_pdf)
lock_pdf_btn.place(x=300, y=240)

img_4 = PhotoImage(file="trash_original.png")
show_img_4 = Button(frame_line,
                    text="Delete Fields",
                    image=img_4,
                    bg="snow",
                    compound="top",
                    foreground="red",
                    command=delete_fields)
show_img_4.place(x=740, y=170)

window.mainloop()
