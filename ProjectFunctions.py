# header information
"""
author: Maurice Farr
date: 12/9/2024
assignment: SDEV-140 GUI Tkinter App Final Project
purpose: This .py file has the rest of the necessary functions to execute the GUI Tkinter App,
"My Glucose Meter Tracker".

"""
#ProjectFunctions.py

#Source Code of All files (.py):
from tkinter import*
from tkinter import Message
import time
import pandas as pd

#Define confirmation message for each button (create_account_button, login_button, forgot_reset_password)
cnca_message1 = "     Congrats, you have officially created an account. You can now use your created account to login."
cnca_message2 = "ERROR: PLEASE FILL OUT ALL THE ENTIRES"
login_message1= "Sorry, you were unable to login."
login_message2 = "     Successfully logged in."

#Path for file for to store and retrieve user data
path_for_file = "C:\\Users\\artvs\\OneDrive\\Documents\\SDEV 140 Final Project\\MauriceFarr-DatabaseForFinalProject.csv"

#Define the function to destroy a window
def destroyWindow(widget):
    widget.destroy()

#Define the function and add grid layouts for creating a window when clicking the new account button
def new_account_button_clicked():
    window_n_a = Toplevel()
    window_n_a.geometry("600x500")
    window_n_a.config(bg="#ffffff")

    #Display the title name of the app on the "new_account_button_clicked" window including adding its grid layouts
    title_label2 = Label(window_n_a, text = "My Glucose Meter Tracker", font=("Californian FB", 20, "bold"), fg="#1197e0",bg="#ffffff")
    title_label2.grid(row=5, column=5, padx=30, pady=30)

    #Create the label and add grid layouts for the email
    email_label = Label(window_n_a, text = "Email", font=("Californian FB", 12, "bold"), fg="#1197e0",bg="#ffffff")
    email_label.grid(row=20, column=3, padx=20, pady=20)

    #Create an entry text field and add grid layouts for the email
    entry_email1 = Entry(window_n_a, width=40)
    entry_email1.grid(row=20, column=5, padx=30, pady=30)
    entry_email1.config(bg="#ffffff")

    #Create the label and add grid layouts for the username
    username_label = Label(window_n_a, text = "Username", font=("Californian FB", 12, "bold"), fg="#1197e0",bg="#ffffff")
    username_label.grid(row=24, column=3, padx=20, pady=20)

    #Create an entry text field and add grid layouts for the username
    entry_username = Entry(window_n_a, width=40)
    entry_username.grid(row=24, column=5, padx=30, pady=30)
    entry_username.config(bg="#ffffff")

    #Create the label and add grid layouts for the password
    password_label = Label(window_n_a, text = "Password", font=("Californian FB", 12, "bold"), fg="#1197e0",bg="#ffffff")
    password_label.grid(row=28, column=3, padx=20, pady=20)

    #Create an entry text field and add grid layouts for the password
    entry_password1 = Entry(window_n_a, width=40)
    entry_password1.grid(row=28, column=5, padx=30, pady=30)
    entry_password1.config(bg="#ffffff")

    #Apply a "create new account" button including adding its grid layouts
    create_account_button = Button(window_n_a, text = "Create New Account", font=("Californian FB", 12, "bold"), fg="#1197e0",bg="#ffffff", command= lambda:display_confirmation_message(window_n_a, entry_email1, entry_username, entry_password1, cnca_message1,cnca_message2))
    create_account_button.grid(row=31, column=5, columnspan=3, padx=30, pady=20)

    #Create a back button and add grid layouts for the "new_account_button_clicked" window
    back_button1 = Button(window_n_a, text="Back", font=("Californian FB", 12, "bold"), fg="#1197e0",bg="#ffffff", command=lambda: destroyWindow(window_n_a))
    back_button1.grid(row=1, column=0, padx=30, pady=20)

#Define the function to open a new window to display the message that new account has been created including adding grid layouts
def display_confirmation_message(window_combine, entry_email1, entry_username, entry_password1, display_message1, display_message2):
    email = entry_email1.get()
    username = entry_username.get()
    password = entry_password1.get()

    #Conditional if-else statement to check if there any entries for creating new account
    if len(email) != 0 and len(username) != 0 and len(password) != 0:
        window_cnca = Toplevel()
        window_cnca.geometry("700x60")
        window_cnca.config(bg="#ffffff")
        cnca_label = Label(window_cnca, text=display_message1, font=("Californian FB", 12, "bold"), fg="#1197e0", bg="#ffffff")
        cnca_label.grid(row=28, column=3, padx=20, pady=20)
        window_cnca.after(3000, lambda: destroyWindow(window_cnca)) #Indication that the cnca_message will display for 3 seconds before disappearing
        window_combine.destroy() #Both windows (window_n_a and window_cnca) will disappear
    else: 
        window_cnca = Toplevel()
        window_cnca.geometry("600x65")
        window_cnca.config(bg="#ffffff")
        cnca_label = Label(window_cnca, text=display_message2, font=("Californian FB", 12, "bold"), fg="#1197e0", bg="#ffffff")
        cnca_label.grid(row=28, column=3, padx=20, pady=20)
        window_cnca.after(3000, lambda: destroyWindow(window_cnca))  # Indication that the new password will display for 3 seconds before disappearing
        window_combine.destroy()  # Both windows (window_frp and window_npw) will disappear

#Define the function to open a new window when clicking the login button including adding its grid layouts
def login_button_clicked():
    window_login = Toplevel()
    window_login.geometry("700x450")
    window_login.config(bg="#ffffff")

    #Display the title name of the app on the "login_button_clicked" window including adding its grid layouts
    title_label2 = Label(window_login, text = "My Glucose Meter Tracker", font=("Californian FB", 20, "bold"), fg="#1197e0",bg="#ffffff")
    title_label2.grid(row=5, column=5, padx=30, pady=30)

    #Create the label and add grid layouts for the email
    username_email_label = Label(window_login, text = "Username or Email", font=("Californian FB", 12, "bold"), fg="#1197e0",bg="#ffffff")
    username_email_label.grid(row=20, column=3, padx=20, pady=20)

    #Create the entry text field and add grid layouts for the mail
    entry_username_email = Entry(window_login, width=40)
    entry_username_email.grid(row=20, column=5, padx=30, pady=30)
    entry_username_email.config(bg="#ffffff")

    #Create the label and add grid layouts for the password
    password_label = Label(window_login, text = "Password", font=("Californian FB", 12, "bold"), fg="#1197e0",bg="#ffffff")
    password_label.grid(row=28, column=3, padx=20, pady=20)

    #Create the entry text field and add grid layouts for the password
    entry_password2 = Entry(window_login, width=40)
    entry_password2.grid(row=28, column=5, padx=30, pady=30)
    entry_password2.config(bg="#ffffff")

    #Create a login button including adding its grid layouts
    login_button = Button(window_login, text = "Login", font=("Californian FB", 12, "bold"), fg="#1197e0",bg="#ffffff", command=lambda: login_process(entry_username_email, entry_password2, window_login))
    login_button.grid(row=31, column=5, columnspan=3, padx=30, pady=20)

    #Create a back button for the "login_button_clicked" window including adding its grid layouts
    back_button2 = Button(window_login, text="Back", font=("Californian FB", 12, "bold"), fg="#1197e0", bg="#ffffff", command= lambda: destroyWindow(window_login))
    back_button2.grid(row=1, column=0, padx=30, pady=20)

#Define the function for the login process by including parameters (entry box for both username and password, and window_login) and the grid layouts
def login_process(username_entrybox, password_entrybox, window_login):
    username= username_entrybox.get()
    password= password_entrybox.get()

    #Import user data by reading the file using the cvs method
    df1 = pd.read_csv ("C:\\Users\\artvs\\OneDrive\\Documents\\SDEV 140 Final Project\\MauriceFarr-DatabaseForFinalProject.csv")

    #Identify if a character exist in username by connecting to the database
    if '@' in username:
        entries = df1[(df1["email"] == username) & (df1["password"] == password)]
    else:
        entries = df1[(df1["username"]==username) & (df1["password"]==password)]

    #Conditional if-else statement to check if whether there are any entries after clicking the login button
    if len(entries) == 0:
        display_confirmation_message(window_login, login_message1) #Window will display login_message1 for 3 seconds before disappearing
    else:
        display_confirmation_message(window_login, login_message2)  #Window will display login_message2 for 3 seconds before disappearing
        display_blood_glucose_level() #Transition to open a new window,"window_blood_glucose_level", after logging in

#Define the function to create window for the blood glucose level including adding grid layouts
def display_blood_glucose_level():
    window_blood_glucose_level = Toplevel()
    window_blood_glucose_level.geometry("600x250")
    window_blood_glucose_level.config(bg="#ffffff")

    #Display the title label and add grid layouts for the "blood_glucose_level" window
    title_label3 = Label(window_blood_glucose_level, text = "Please enter your blood glucose level", font=("Californian FB", 18, "bold"), fg="#1197e0",bg="#ffffff")
    title_label3.grid(row=5, column=2, padx=(140,10), pady=30)

    #Create entry text field and add grid layouts for blood glucose level
    entry_blood_glucose_level = Entry(window_blood_glucose_level, width=20)
    entry_blood_glucose_level.grid(row=15, column=2, padx=(140,20), pady=20)
    entry_blood_glucose_level.config(bg="#ffffff")

    #Display the title label of the measurement units, milligrams (mg) per decilitre (dL), including adding its grid layouts
    title_label4 = Label(window_blood_glucose_level, text="mg/dL",font=("Californian FB", 12, "bold"), fg="#1197e0", bg="#ffffff")
    title_label4.grid(row=15, column=2, padx=(350,20), pady=20)

    #Apply a "submit" button for the blood glucose level including adding its grid layouts
    submit_button = Button(window_blood_glucose_level, text="Submit", font=("Californian FB", 12, "bold"), fg="#1197e0",bg="#ffffff", command= lambda: submit_blood_glucose (window_blood_glucose_level,entry_blood_glucose_level.get()))
    submit_button.grid(row=20, column=2, columnspan=1, padx=(140,10), pady=20)

#Define the function for the results when the user submit their blood glucose level including adding its parameters (window_combine, user_glucose) and grid layouts
def submit_blood_glucose(window_combine, user_glucose):
    if len(user_glucose) == 0:  #Check to see if there are any empty entries
        window_error1 = Toplevel()
        window_error1.geometry("490x60")
        window_error1.config(bg="#ffffff")
        error1_label = Label(window_error1, text="     ERROR: PLEASE ENTER YOUR BLOOD GLUCOSE LEVEL!",font=("Californian FB", 12, "bold"), fg="#1197e0", bg="#ffffff")
        error1_label.grid(row=28, column=3, padx=20, pady=20)
        window_error1.after(3000, lambda: destroyWindow(window_error1))   #The "error_1" message will display for 3 seconds before disappearing
        window_combine.destroy() #Both windows (window_error1 and window_blood_glucose_level) will disappear
    else:
        user_glucose = float(user_glucose) #Indication we can now enter a number
        if user_glucose < 0: #Determine if blood glucose level is less than zero
            window_error2 = Toplevel()
            window_error2.geometry("455x60")
            window_error2.config(bg="#ffffff")
            error2_label = Label(window_error2, text="     ERROR: YOU CANNOT HAVE A NEGATIVE VALUE!", font=("Californian FB", 12, "bold"), fg="#1197e0", bg="#ffffff")
            error2_label.grid(row=28, column=3, padx=20, pady=20)
            window_error2.after(3000, lambda: destroyWindow(window_error2))  #The "error_2" message will display for 3 seconds before disappearing
            window_combine.destroy() #Both windows (window_error2 and window_blood_glucose_level) will disappear
        if user_glucose != int(user_glucose):  #Determine if blood glucose level is a decimal number
            window_error3 = Toplevel()
            window_error3.geometry("455x60")
            window_error3.config(bg="#ffffff")
            error3_label = Label(window_error3, text="      ERROR: YOU CANNOT HAVE A DECIMAL VALUE!", font=("Californian FB", 12, "bold"), fg="#1197e0", bg="#ffffff")
            error3_label.grid(row=28, column=3, padx=20, pady=20)
            window_error3.after(3000, lambda: destroyWindow(window_error3))  #The "error_3" message will display for 3 seconds before disappearing
            window_combine.destroy() #Both windows (window_error3 and window_blood_glucose_level) will disappear
        if user_glucose >=150: #The range for target numbers for high blood glucose levels
            window_high = Toplevel()
            window_high.geometry("250x60")
            window_high.config(bg="#ffffff")
            high_label = Label(window_high, text="   Blood glucose is TOO HIGH.", font=("Californian FB", 12, "bold"), fg="#1197e0",bg="#ffffff")
            high_label.grid(row=28, column=3, padx=20, pady=20)
            window_high.after(3000, lambda: destroyWindow(window_high))  #The high message will display for 3 seconds before disappearing
            window_combine.destroy() #Both windows (window_high and window_blood_glucose_level) will disappear
        elif user_glucose >= 100 and user_glucose <= 150: #The range for target numbers for normal blood glucose levels
            window_normal = Toplevel()
            window_normal.geometry("250x60")
            window_normal.config(bg="#ffffff")
            normal_label = Label(window_normal, text="      Blood glucose is NORMAL.", font=("Californian FB", 12, "bold"),fg="#1197e0", bg="#ffffff")
            normal_label.grid(row=28, column=3, padx=20, pady=20)
            window_normal.after(3000, lambda: destroyWindow(window_normal))  #The "normal" message will display for 3 seconds before disappearing
            window_combine.destroy() #Both windows (window_normal and window_blood_glucose_level) will
        elif user_glucose >= 71 and user_glucose <= 99:  #The range target numbers for borderline low blood glucose levels
            window_borderline = Toplevel()
            window_borderline.geometry("330x60")
            window_borderline.config(bg="#ffffff")
            borderline_label = Label(window_borderline, text="      Blood glucose is BORDERLINE LOW.", font=("Californian FB", 12, "bold"),fg="#1197e0", bg="#ffffff")
            borderline_label.grid(row=28, column=3, padx=20, pady=20)
            window_borderline.after(3000, lambda: destroyWindow(window_borderline))  #The "borderline low" message will display for 3 seconds before disappearing
            window_combine.destroy() #Both windows (window_borderline and window_blood_glucose_level) will disappear
        elif user_glucose <= 70: #The range for target numbers for low blood glucose levels
            window_low = Toplevel()
            window_low.geometry("230x60")
            window_low.config(bg="#ffffff")
            low_label = Label(window_low, text="     Blood glucose is LOW.", font=("Californian FB", 12, "bold"), fg="#1197e0", bg="#ffffff")
            low_label.grid(row=28, column=3, padx=20, pady=20)
            window_low.after(3000, lambda: destroyWindow(window_low))  #The "low" message display for 3 seconds before disappearing
            window_combine.destroy() #Both windows (window_low and window_blood_glucose_level) will disappear

#Define the function for clicking the reset new password button including adding grid layouts
def forgot_reset_password_button_clicked():
    window_frp = Toplevel()
    window_frp.geometry("750x520")
    window_frp.config(bg="#ffffff")

    #Display the title name of the app on the "forgot_reset_password_clicked" window including adding its grid layouts
    title_label2 = Label(window_frp, text = "My Glucose Meter Tracker", font=("Californian FB", 20, "bold"), fg="#1197e0",bg="#ffffff")
    title_label2.grid(row=5, column=2, columnspan=1, padx=30, pady=40)

    #Create the label and add grid layouts  for the email
    email_label2 = Label(window_frp, text="Email", font=("Californian FB", 12, "bold"), fg="#1197e0", bg="#ffffff")
    email_label2.grid(row=20, column=1, columnspan=1, padx=20, pady=20)

    #Create the entry text field and add grid layouts for the email
    entry_email2= Entry(window_frp, width=40)
    entry_email2.grid(row=20, column=2, padx=30, pady=30)
    entry_email2.config(bg="#ffffff")

    #Create the label and add grid layouts to reset the password
    reset_password_label = Label(window_frp, text = "Type New Password", font=("Californian FB", 12, "bold"), fg="#1197e0",bg="#ffffff")
    reset_password_label.grid(row=23, column=1, columnspan=1, padx=20, pady=20)

    #Create the entry text field and add grid layouts to type the new password
    entry_password3=Entry(window_frp, width=40)
    entry_password3.grid(row=23, column=2, padx=30, pady=30)
    entry_password3.config(bg="#ffffff")

    #Create the label and add grid layouts to confirm new the password
    confirm_new_password_label = Label(window_frp, text = "Retype New Password", font=("Californian FB", 12, "bold"), fg="#1197e0",bg="#ffffff")
    confirm_new_password_label.grid(row=26, column=1, columnspan=1, padx=20, pady=20)

    #Create the entry text field and add grid layouts to confirm new password including
    entry_confirm_new_password = Entry(window_frp, width=40)
    entry_confirm_new_password.grid(row=26, column=2, padx=30, pady=30)
    entry_confirm_new_password.config(bg="#ffffff")

    #Apply a "create new password" button including adding its grid layouts
    create_new_password_button = Button(window_frp, text = "Create New Password", font=("Californian FB", 12, "bold"), fg="#1197e0",bg="#ffffff", command= lambda: update_password(window_frp, path_for_file, entry_email2, entry_password3,entry_confirm_new_password))
    create_new_password_button.grid(row=27, column=2, columnspan=5, padx=30, pady=20)

    #Create a back button for the "forgot_reset_password_button_clicked" window including adding its grid layouts
    back_button3 = Button(window_frp, text="Back", font=("Californian FB", 12, "bold"), fg="#1197e0", bg="#ffffff",command=lambda: destroyWindow(window_frp))
    back_button3.grid(row=1, column=0, padx=30, pady=20)

#Define the function to reset new password using parameters (email, password, and retype password) for the entry box by connecting to the database
def update_password(window_combine, path_for_file, email_entrybox, new_password_entrybox, retype_new_password_entrybox):
        email = email_entrybox.get() #Get the user to enter their email in the entrybox
        new_password = new_password_entrybox.get() ##Get the user to enter new password in the entrybox
        retype_new_password = retype_new_password_entrybox.get() #Get the user to reenter their new password in the entrybox for confirmation

        #Import user data by reading the file using the cvs method
        df1 = pd.read_csv("C:\\Users\\artvs\\OneDrive\\Documents\\SDEV 140 Final Project\\MauriceFarr-DatabaseForFinalProject.csv")

        #If-else
        if (len (new_password) != 0
        and len (retype_new_password) != 0
        and new_password == retype_new_password):
            #Identify if a character exist in email by connecting to the database
            df1.loc[df1["email"] == email, 'password'] = retype_new_password
            df1.to_csv(path_for_file, index=False)

            # Create a window to display the message that the new password has been created including adding its grid layouts
            window_npw = Toplevel()
            window_npw.geometry("600x65")
            window_npw.config(bg="#ffffff")
            pw_label = Label(window_npw,text="         New password has been reset. You can now use your new password to login.",font=("Californian FB", 12, "bold"), fg="#1197e0", bg="#ffffff")
            pw_label.grid(row=28, column=3, padx=20, pady=20)
            window_npw.after(3000, lambda: destroyWindow(window_npw))  # Indication that the new password will display for 3 seconds before disappearing
            window_combine.destroy()  # Both windows (window_frp and window_npw) will disappear
        else:
            window_npw = Toplevel()
            window_npw.geometry("600x65")
            window_npw.config(bg="#ffffff")
            pw_label = Label(window_npw,text="ERROR",font=("Californian FB", 12, "bold"), fg="#1197e0", bg="#ffffff")
            pw_label.grid(row=28, column=3, padx=20, pady=20)
            window_npw.after(3000, lambda: destroyWindow(window_npw))  # Indication that the new password will display for 3 seconds before disappearing
            window_combine.destroy()  # Both windows (window_frp and window_npw) will disappear




