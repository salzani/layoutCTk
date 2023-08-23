import customtkinter
from tkinter import *
from tkinter import font
import json
import os

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
font5= customtkinter.CTkFont(family="Ivy", size=12, weight="bold", slant="roman")

#STRING VARS / STORE THE ENTRYS
name_var = customtkinter.StringVar()
cpf_var = customtkinter.StringVar()
email_var = customtkinter.StringVar()
password_var = customtkinter.StringVar()
confirm_password_var = customtkinter.StringVar()
cpfSearch_var = customtkinter.StringVar()


#FUNCTIONS
#function to validate cpf txt
def validatecpf(cpf):
    
    #sorting out the first nine numbers on a variable
    first =cpf[:9]

    #creating a var with invert numbers and a variable(RESULT) with the value 0
    invert2 = 10
    result2 = 0

    for number2 in first:
        result2+=int(number2)*invert2
        invert2 -= 1

    ver1 = result2*10%11
    if ver1 >= 10:
        ver1 = 0

        


    ###############

    #sorting out the first teen numbers on a variable
    second = cpf[:10]

    #creating a var with invert numbers and a variable(RESULT) with the value 0
    invertwo2 = 11
    resultwo2 = 0

    for numbertwo2 in second:
        resultwo2 += int(numbertwo2)
        invertwo2 -= 1

    ver2 = resultwo2*10%11
    if ver2 >= 10:
        ver2 = 0
    else: 
        ver2


    #REBUILDING THE cpf
    cpfgen = f'{first}{ver1}{ver2}'

    #VALIDATING THE cpf
    if cpf == cpfgen:
        return(True)
    else:
        return(False)




#data path
_path = "data/data.txt"

#function that inserts a a new register
def insert(cpf, name, email, password):
    #try create de file and add the register
    try:
        directory = "data"
        parent_dir = "./"
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
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
    cpasswordP = confirm_password_var.get()

    if len(nameP) > 0 and len(cpfP) > 0 and len(emailP) > 0 and len(passwordP) > 0 and len(cpasswordP) > 0:
        if validatecpf(cpfP):
            if(cpasswordP == passwordP):
                insert(cpfP, nameP, emailP, passwordP)

                emptyFields.destroy()
                equalPasswords.destroy()
                invalidCpf.destroy()

                name.delete(0, 'end')
                Firstentry.delete(0, 'end')
                Secondentry.delete(0, 'end')
                Thirdentry.delete(0, 'end')
                fourthentry.delete(0, 'end')
                global finalWindow
                finalWindow = customtkinter.CTkToplevel(window, fg_color="#2b2a2e")
                finalWindow.attributes('-topmost', 1)
                #finalWindow.attributes('-topmost', 0)
                finalWindow.geometry("500x400")
                finalWindow.title("Success!")
                finalWindow.resizable(False, False)

                congratulations_label = customtkinter.CTkLabel(finalWindow, text=f"Congrats, welcome onboard.", font=fontwo)
                congratulations_label.pack(pady=25)  

                button2 = customtkinter.CTkButton(finalWindow, text="return", font=font2, width=200, command=returnFinalWind)
                button2.pack(pady = 45)

                MugiLogo2 = PhotoImage(file="images\luffynika.png")
                MugiLogo2 = MugiLogo2.subsample(2,2)
                MugiLogo2Label= Label(finalWindow, image=MugiLogo2, bg="#2b2a2e")

                MugiLogo2Label.place(x=140, y=210)

                finalWindow.mainloop()
            else:
                emptyFields.destroy()   
                invalidCpf.destroy()
                equalPasswords.place(x=110, y=485)
        else:
            emptyFields.destroy()
        
            invalidCpf.place(x=110, y=485)

    else:
        emptyFields.place(x=140, y=485)


def showPass():

    if checkbox_var.get() == True:
        Thirdentry = customtkinter.CTkEntry(master=frame, width=300, textvariable=password_var).place(x=50, y=330)
        # label3 = customtkinter.CTkLabel(master=frame, text="required field", text_color="red").place(x=52,y=360)
        fourthentry = customtkinter.CTkEntry(master=frame, width=300, textvariable=confirm_password_var).place(x=50, y=400)
    else:
        Thirdentry = customtkinter.CTkEntry(master=frame, width=300,show='*', textvariable=password_var).place(x=50, y=330)
        # label3 = customtkinter.CTkLabel(master=frame, text="required field", text_color="red").place(x=52,y=360)
        fourthentry = customtkinter.CTkEntry(master=frame, width=300,show='*', textvariable=confirm_password_var).place(x=50, y=400)


def returnFinalWind():
    finalWindow.destroy()


def searchByCpf(cpf, canvas):
    canvas.delete("all")
    f = open(_path, "r")
    data = json.loads(f.read())
    y = 30

    for x in data:
        if cpf == x["cpf"]:
            canvas.create_text(300, y, text=f"CPF: {x['cpf']}", font=font2)
            y += 20
            canvas.create_text(300, y, text=f"Name: {x['name']}", font=font2)
            y += 20
            canvas.create_text(300, y, text=f"Email: {x['email']}", font=font2)
            y += 20
            canvas.create_text(300, y, text="-------------------------------------", font=font2)
            y += 20

def searchAll(canvas):
    canvas.delete("all")
    f = open(_path, "r")
    data = json.loads(f.read())
    y = 30

    for x in data:
        canvas.create_text(300, y, text=f"CPF: {x['cpf']}", fill="black", font=font2)
        y += 20
        canvas.create_text(300, y, text=f"Name: {x['name']}", fill="black", font=font2)
        y += 20
        canvas.create_text(300, y, text=f"Email: {x['email']}", fill="black", font=font2)
        y += 20
        canvas.create_text(300, y, text="-------------------------------------", fill="black", font=font2)
        y += 20

def openSearch():
    searchWindow = customtkinter.CTkToplevel(window, fg_color="#2b2a2e")
    searchWindow.attributes('-topmost', 1)
    #searchWindow.attributes('-topmost', 0)
    searchWindow.geometry("700x550")
    searchWindow.title("Search Data")
    searchWindow.resizable(False, False)

    labelCpfSearch = customtkinter.CTkLabel(searchWindow, text="CPF", font = font2)
    labelCpfSearch.place(x=30, y=5)
    FirstentrySearch = customtkinter.CTkEntry(searchWindow, width=300, textvariable=cpfSearch_var)
    FirstentrySearch.place(x=30, y=30)


    ###BUTTON
    buttonSearchCpf = customtkinter.CTkButton(searchWindow, text="SEARCH", font=font2, width=130, command= lambda : searchByCpf(cpfSearch_var.get(), canvas)).place(x=370, y= 30)
    buttonSearchAll = customtkinter.CTkButton(searchWindow, text = "SEARCH ALL", font = font2, width= 130, command= lambda : searchAll(canvas)).place(x =530, y = 30 )

    ###DATA LAYOUT

    canvas = customtkinter.CTkCanvas(searchWindow, width=640, height=430)
    canvas.place(x=30, y=70)

    
    canvas_scrollbar = customtkinter.CTkScrollbar(searchWindow, command=canvas.yview, height=355)
    canvas_scrollbar.place(x=680, y=70)
    canvas.configure(yscrollcommand=canvas_scrollbar.set)
    canvas.configure(scrollregion=canvas.bbox("all"))

    ###INFOS

    label2 = customtkinter.CTkLabel(searchWindow, text="Mugiwara's corp.", font=font4)
    label2.place(x=10, y=560)

    label3 = customtkinter.CTkLabel(searchWindow, text="All Rights reserved ©", font = font3)
    label3.place(x=210, y=565)

    searchWindow.mainloop()



#FRAME 1
frame = customtkinter.CTkFrame(master=window, width=400, height=595)
frame.pack(side= RIGHT)

emptyFields = customtkinter.CTkLabel(master=frame, text="Please fill all the fields", font = font2, text_color='red')
equalPasswords = customtkinter.CTkLabel(master=frame, text="Please digit the same password", font = font2, text_color='red')
invalidCpf = customtkinter.CTkLabel(master=frame, text="Please insert a valid CPF", font = font2, text_color='red')

#FRAME 2
frameTwo = customtkinter.CTkFrame(master=window, width=397, height=595, fg_color="#141414")
frameTwo.pack(side=LEFT)


#FRAME WD 
label = customtkinter.CTkLabel(master=frame, text="Create Account", font = font)
label.place(x=110, y=40)


#NAME LABEL ENTRY
labelName = customtkinter.CTkLabel(master=frame, text="Name", font = font2)
labelName.place(x=50, y=90)
name = customtkinter.CTkEntry(master=frame,width=300, textvariable=name_var)
name.place(x=50, y=120)


#cpf LABEL ENTRY
labelcpf = customtkinter.CTkLabel(master=frame, text="CPF (just letters)", font = font2)
labelcpf.place(x=50, y=160)
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
buttonSearch = customtkinter.CTkButton(master=frameTwo, text="SEARCH", font=font3, width=100, command=openSearch).place(x=140, y= 420)


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
MugiLogo = PhotoImage(file="images\mugi.png")
MugiLogo = MugiLogo.subsample(3,3)
MugiLogoLabel= Label(image=MugiLogo, bg="#141414")


MugiLogoLabel.place(x=55, y=140)
#logoLabel.place(x=20, y=10)

window.mainloop()