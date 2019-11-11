from tkinter import *

def DinarToEuro():
    try:
        ammountInDinar= int(entry_dinar.get())
        ammountInEuro=ammountInDinar/120
        lbl_result.configure(text = 'Ammount in EUR is: {:.2f} EUR  '.format(ammountInEuro))
        entry_dinar.delete(0,END)
    except ValueError :
        lbl_result.configure(text = "Please enter the numeric value." )

def EuroToDinar():
    try:
        iznos_u_Eurima = int(entry_euro.get())
        iznosEura_u_dinarima = iznos_u_Eurima * 120
        lbl_result.configure(text = 'Ammount in RSD is  : {:.2f} RSD  '.format(iznosEura_u_dinarima))
        entry_euro.delete(0,END)
    except ValueError :
        lbl_result.configure(text = "Please enter the numeric value." )

    
    

root = Tk()

root.title("EXCHANGE OFFICE RICH'S")
canvas = Canvas(width=10, height=10, bg='white')

photo=PhotoImage(file="logo3.gif")

Label(canvas,image=photo, bg="black").grid(row=0,column=0,sticky=E)

canvas.grid(row=0,column=0)

title_label = Label(text=" EXCHANGE OFFICE \n RICH'S ",font=('Verdana', 18))

title_label.grid(row=0, column=2 )


# convert RSD to EUR

lbl_ammount_rsd = Label(text='  Ennter the ammount in RSD:',font=('Verdana', 12))

lbl_ammount_rsd.grid(row=1, column=0)

entry_dinar = Entry(font=('Verdana', 12), width=10)

entry_dinar.grid(row=1, column=1)

btn_changeDinarToEuro = Button(text='Change', font=('Verdana', 12),command=DinarToEuro)
btn_changeDinarToEuro.grid(row=1, column=2)


# convert EUR to RSD

lbl_ammount_eur= Label(text='Ennter the ammount in EUR:',font=('Verdana', 12))

lbl_ammount_eur.grid(row=3, column=0)

entry_euro = Entry(font=('Verdana', 12), width=10)

entry_euro.grid(row=3, column=1)

btn_changeEuroUDinar = Button(text='Change', font=('Verdana', 12),command=EuroToDinar)
btn_changeEuroUDinar.grid(row=3, column=2)


lbl_result = Label(font=('Verdana', 12),bg='white')

lbl_result.grid(row=4, column=0, columnspan=3, padx=(3,100))




