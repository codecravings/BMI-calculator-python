from tkinter import *

application = Tk()
application.geometry("1350x650+0+0")
application.resizable(0, 0)
application.title("BMI CALCULATOR")


def BodyMassIndex_Calculator():
    BMI_Height = float(variable2.get())
    BMI_Weight = float(variable1.get())
    BodyMassIndex = str('%.2f' % (BMI_Weight / (BMI_Height * BMI_Height)))
    lbl_res_bmi.config(text=BodyMassIndex)


variable1 = DoubleVar()
variable2 = DoubleVar()

Tops = Frame(application, width=1350, height=50, bd=8, relief="raise")
Tops.pack(side=TOP)

frame1 = Frame(application, width=600, height=600, bd=8, relief="raise")
frame1.pack(side=LEFT)

frame2 = Frame(application, width=300, height=700, bd=8, relief="raise")
frame2.pack(side=RIGHT)

frame1A = Frame(frame1, width=600, height=200, bd=20, relief="raise")
frame1A.pack(side=TOP)
frame1B = Frame(frame1, width=600, height=600, bd=20, relief='raise')
frame1B.pack(side=TOP)

lbl_T1 = Label(Tops, text="          BODY MASS INDEX          ", padx=16, pady=16, bd=16, fg='#000000',
               font=("arial", 54, 'bold'), bg="navajo white", relief='raise', width=32, height=1)
lbl_T1.pack()

lbl_w = Label(frame1A, text="Select Weight in Kilograms", font=('arial', 20, 'bold'), bd=20).grid(row=0, column=0)
b_w = Scale(frame1A, variable=variable1, from_=1, to=500, length=880, tickinterval=30, orient=HORIZONTAL)
b_w.grid(row=1, column=0)

lbl_h = Label(frame1B, text="Enter Height in Meters Square", font=('arial', 20, 'bold'), bd=20).grid(row=0, column=0)
t_h = Entry(frame1B, textvariable=variable2, font=('arial', 16, 'bold'), bd=16, width=22, justify='center')
t_h.grid(row=1, column=0)

lbl_res_bmi = Label(frame1B, padx=16, pady=16, bd=16, fg='#000000', font=('arial', 30, 'bold'), bg='navajo white',
                    relief='sunk', width=34, height=1)
lbl_res_bmi.grid(row=2, column=0)

lbl_table_bmi = Label(frame2, font=("arial", 20, 'bold'), text='BMI Table').grid(row=0, column=0)
bmi_tab_text_lbl = Text(frame2, height=12, width=38, bd=16, font=("arial", 12, 'bold'))
bmi_tab_text_lbl.grid(row=1, column=0)

bmi_tab_text_lbl.insert(END, 'Meaning \t\t' + "BMI \n\n")
bmi_tab_text_lbl.insert(END, 'Normal weight \t\t' + "19-24 \n\n")
bmi_tab_text_lbl.insert(END, 'Overwight \t\t' + "25-29,9 \n\n")
bmi_tab_text_lbl.insert(END, 'Obesity level I \t\t' + "30-34, 9 \n\n")
bmi_tab_text_lbl.insert(END, 'Obesity level II \t\t' + "35-39, 9\n\n")
bmi_tab_text_lbl.insert(END, 'Obesity level III \t\t' + ">= 40\n\n")

BMI_BUTTON = Button(frame2, text="Click to \nCheck Your \nBMI", padx=8, pady=8, bd=12, bg='navajo white', width=21,
                    font=("arial", 20, 'bold'), height=3, command=BodyMassIndex_Calculator)
BMI_BUTTON.grid(row=2, column=0)

application.mainloop()

