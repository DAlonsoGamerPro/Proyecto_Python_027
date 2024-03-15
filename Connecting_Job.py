from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random

root = Tk()
root.geometry("900x500")
root.title("Connecting Jobs")

#/\/\/\Imagen/\/\/\#

image = ImageTk.PhotoImage(Image.open("CJ.jpeg"))
place_image = Label(root)
place_image["image"] = image
place_image.place(relx=0.7,rely=0.5,anchor=CENTER)

#/\/\/\Título de la App/\/\/\#

label = Label(root,text="Asignar Trabajos", font=("times",20,"bold"))
label.place(relx=0.12,rely=0.06,anchor=CENTER)

label_doctor = Label(root,text="Doctor(a): ")
label_doctor.place(relx=0.04,rely=0.15,anchor=CENTER)

entry_doctor = Entry(root)
entry_doctor.place(relx=0.25,rely=0.15,anchor=CENTER)

btn_doctor = Button(root,text="Mostrar el Hospital Asignado",fg="white",bg="blue")
btn_doctor.place(relx=0.1,rely=0.23,anchor=CENTER)

label_selected_doctor = Label(root)
label_selected_doctor.place(relx=0.1,rely=03.,anchor=CENTER)


label_teacher = Label(root,text="Profesor(a): ")
label_teacher.place(relx=0.04,rely=0.45,anchor=CENTER)

entry_teacher = Entry(root)
entry_teacher.place(relx=0.25,rely=0.45,anchor=CENTER)

btn_teacher = Button(root,text="Mostrar el Salón Asignado",fg="white",bg="blue")
btn_teacher.place(relx=0.1,rely=0.53,anchor=CENTER)

label_selected_teacher = Label(root)
label_selected_teacher.place(relx=0.1,rely=33.,anchor=CENTER)


label_engineer = Label(root,text="Ingeniero(a): ")
label_engineer.place(relx=0.04,rely=0.65,anchor=CENTER)

entry_engineer = Entry(root)
entry_engineer.place(relx=0.25,rely=0.65,anchor=CENTER)

btn_engineer = Button(root,text="Mostrar la Zona Asignada",fg="white",bg="blue")
btn_engineer.place(relx=0.1,rely=0.73,anchor=CENTER)

label_selected_engineer = Label(root)
label_selected_engineer.place(relx=0.1,rely=0.53,anchor=CENTER)

root.mainloop()