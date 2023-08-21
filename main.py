import customtkinter
from tkinter import *
from tkinter import font
import json




customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


window = customtkinter.CTk()
window.geometry("800x600")
window.title("Register")
window.resizable(False, False) #not manipulate the window

#FONTS
font= customtkinter.CTkFont(family="Consolas", size=20, weight="bold", slant="roman") 
fontwo= customtkinter.CTkFont(family="Consolas", size=25, weight="bold", slant="roman")   
font2= customtkinter.CTkFont(family="Ivy", size=12, weight="bold", slant="roman")
font3= customtkinter.CTkFont(family="Bodoni", size=9, weight="bold", slant="roman")     
font4= customtkinter.CTkFont(family="Times", size=25, weight="bold", slant="italic") 


#STRING VARS / STORE THE ENTRYS
name_var = customtkinter.StringVar()
cpf_var = customtkinter.StringVar()
email_var = customtkinter.StringVar()
password_var = customtkinter.StringVar()
confirm_password_var = customtkinter.StringVar()


#FUNCTIONS
#function that inserts a a new register
def insert(cpf, name, email, password):
    #data path
    _path = "data/data.txt"

    #try create de file and add the register
    try:
        f = open(_path, "x")
        newData = [{f"cpf" : cpf, "name" : name, "email" : email, "password" : password}]
        f = open(_path, "w")
        f.write(json.dumps(newData))
        f.close()
        
    #error handling, if exists, just read instead of creating
    except:
        f = open(_path, "r")
        data = json.loads(f.read())
        newData = {f"cpf" : cpf, "name" : name, "email" : email, "password" : password}
        data.append(newData)
        f = open(_path, "w")
        f.write(json.dumps(data))
        f.close()


def finalWind():
    nameP = name_var.get()
    cpfP = cpf_var.get()
    emailP = email_var.get()
    passwordP = password_var.get()

    insert(cpfP, nameP, emailP, passwordP)

    finalWindow = customtkinter.CTkToplevel(window, fg_color="black")
    finalWindow.geometry("500x400")
    finalWindow.title("Success!")
    finalWindow.resizable(False, False)

    congratulations_label = customtkinter.CTkLabel(finalWindow, text=f"Congrats, welcome onboard.", font=fontwo)
    congratulations_label.pack(pady=25)  

    MugiLogo2 = PhotoImage(file="images\mugi.png")
    MugiLogo2 = MugiLogo2.subsample(2,2)
    MugiLogo2Label= Label(finalWindow, image=MugiLogo2, bg="black")

    MugiLogo2Label.place(x=50, y=100)


    finalWindow.mainloop()



def showPass():

    if checkbox_var.get() == True:
        Thirdentry = customtkinter.CTkEntry(master=frame, width=300).place(x=50, y=330)
        # label3 = customtkinter.CTkLabel(master=frame, text="required field", text_color="red").place(x=52,y=360)
        fourthentry = customtkinter.CTkEntry(master=frame, width=300).place(x=50, y=400)
    else:
        Thirdentry = customtkinter.CTkEntry(master=frame, width=300,show='*').place(x=50, y=330)
        # label3 = customtkinter.CTkLabel(master=frame, text="required field", text_color="red").place(x=52,y=360)
        fourthentry = customtkinter.CTkEntry(master=frame, width=300,show='*').place(x=50, y=400)




#FRAME 1
frame = customtkinter.CTkFrame(master=window, width=400, height=595)
frame.pack(side= RIGHT)


#FRAME 2
frameTwo = customtkinter.CTkFrame(master=window, width=397, height=595, fg_color="#141414")
frameTwo.pack(side=LEFT)


#FRAME WD 
label = customtkinter.CTkLabel(master=frame, text="Create Account", font = font)
label.place(x=110, y=40)


#NAME LABEL ENTRY
labelName = customtkinter.CTkLabel(master=frame, text="name", font = font2)
labelName.place(x=50, y=90)
name = customtkinter.CTkEntry(master=frame,width=300, textvariable=name_var)
name.place(x=50, y=120)


#CPF LABEL ENTRY
labelCpf = customtkinter.CTkLabel(master=frame, text="CPF", font = font2)
labelCpf.place(x=50, y=160)
Firstentry = customtkinter.CTkEntry(master=frame, width=300, textvariable=cpf_var)
Firstentry.place(x=50, y=190)


#Email LABEL ENTRY
labelEmail = customtkinter.CTkLabel(master=frame, text="Email", font = font2)
labelEmail.place(x=50, y=230)
Secondentry = customtkinter.CTkEntry(master=frame, width=300, textvariable=email_var)
Secondentry.place(x=50, y=260)


#3 PASSWORDS LABEL'S ENTRY
checkbox_var = customtkinter.BooleanVar()
checkbox = customtkinter.CTkCheckBox(master=frame,text="Show password", font=font2, variable=checkbox_var, command=showPass)
checkbox.place(x=50,y=450)

labelPass = customtkinter.CTkLabel(master=frame, text="Password", font = font2)
labelPass.place(x=50, y=300)
Thirdentry = customtkinter.CTkEntry(master=frame,width=300, show='*',textvariable=password_var)
Thirdentry.place(x=50, y=330)

labelPass2 = customtkinter.CTkLabel(master=frame, text="Confirm Password", font = font2)
labelPass2.place(x=50, y=370)
fourthentry = customtkinter.CTkEntry(master=frame,width=300, show='*',textvariable=confirm_password_var)
fourthentry.place(x=50, y=400)



###BUTTON
button = customtkinter.CTkButton(master=frame, text="REGISTER", font=font2, width=200, command=finalWind).place(x=104, y= 520)


###INFOS

label2 = customtkinter.CTkLabel(master=frameTwo, text="Mugiwara's corp.", font=font4)
label2.place(x=105, y=20)

label3 = customtkinter.CTkLabel(master=frameTwo, text="All Rights reserved ©", font = font3)
label3.place(x=10, y=560)



#FAJ LOGO
# logo = PhotoImage(file="images/faj (1).png")
# logo = logo.subsample(5,5)
# logoLabel = Label(image=logo, bg= "#141414")

#MUGI
MugiLogo = PhotoImage(file="images/mugi.png")
MugiLogo = MugiLogo.subsample(3,3)
MugiLogoLabel= Label(image=MugiLogo, bg="#141414")


MugiLogoLabel.place(x=55, y=140)
#logoLabel.place(x=20, y=10)

window.mainloop()