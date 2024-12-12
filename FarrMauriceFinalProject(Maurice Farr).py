# header information
"""
author: Maurice Farr
date: 12/9/2024
assignment: SDEV-140 GUI Tkinter App Final Project
purpose: We need to create a GUI Tkinter application that monitors individuals blood glucose level by inputting that inside the app. Within this app, a separate file called
Project Functions.py, will need to be with the rest of the necessary functions to successfully run this application.

"""
#FarrMauriceFinalProject(“My Glucose Meter Tracker”).py

#Source Code of All files (.py):
from tkinter import*
from tkinter import Message
from ProjectFunctions import *

if __name__=="__main__":

    #Create an opening window to welcome users to the GUI app including adding the grid layouts
    window = Tk()
    window.title("My Glucose Meter Tracker")
    window.geometry("500x500")
    window.config(bg="#ffffff")

    #Create title labels and grid layouts for the title of the application
    title_label1 = Label(window, text = "Welcome to", font=("Roboto", 16), fg="black",bg="#ffffff")
    title_label1.grid(row=5, column=5, columnspan=3, padx=20, pady=0)

    title_label2 = Label(window, text = "My Glucose Meter Tracker", font=("Californian FB", 22, "bold"), fg="#1197e0",bg="#ffffff")
    title_label2.grid(row=7, column=5, padx=30, pady=20)

    #Create a label for choosing options to access the application
    title_label3 = Label(window, text="Choose of one of the following options: ",font=("Californian FB", 14), fg="black", bg="#ffffff")
    title_label3.grid(row=30, column=5, padx=20, pady=0)

    #Create label and add grid layouts to create new account button
    new_account_button = Button(window, text = " New User? Click Here to Create An Account  ", font=("Californian FB", 12, "bold"), fg="#1197e0",bg="#ffffff", command = new_account_button_clicked)
    new_account_button.grid(row=40, column=5, padx=100, pady=20)

    #Create label and add grid layouts for the login button
    login_button = Button(window, text = "Already Have An Account? Click Here to Login", font=("Californian FB", 12, "bold"), fg="#1197e0",bg="#ffffff", command = login_button_clicked)
    login_button.grid(row=41, column=5, padx=100, pady=20)

    #Create label and add grid layouts to reset new password button
    forgot_reset_password_button = Button(window, text = "      Forgot Password? Click Here to Reset It     ", font=("Californian FB", 12, "bold"), fg="#1197e0",bg="#ffffff",command = forgot_reset_password_button_clicked)
    forgot_reset_password_button.grid(row=42, column=5, padx=100, pady=20)

    #Run the application
    window.mainloop()
