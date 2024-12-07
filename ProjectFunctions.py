from tkinter import*
from tkinter import Message
import mysql.connector
import time

#Define confirmation message for each button (create_account_button, login_button, forgot_reset_password)
cnca_message = "Congrats, you have officially created a new account. You can now use your created account to login."
login_message1="Sorry, you were  unable to login"
login_message2 = "Successfully Logged In"
frp_message = "New password has been reset"

#Initialize variable for the database to store and retrieve user data info
cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        database= "databaseproject",
        password="RidinDirty06$"
    )

#Define the function to destroy window
def destroyWindow(widget):
    widget.destroy()

#Define the function for clicking new account button
def new_account_button_clicked():
    window_n_a = Toplevel()
    window_n_a.geometry("600x600")
    window_n_a.config(bg="#ffffff")

    #Display the title name of the app on the "new_account_button_clicked" window
    title_label2 = Label(window_n_a, text = "My Glucose Meter Tracker", font=("Californian FB", 20, "bold"), fg="#1197e0",bg="#ffffff")
    title_label2.grid(row=5, column=5, padx=30, pady=30)

    #Create label for the email including adding grid layouts
    email_label = Label(window_n_a, text = "Email", font=("Californian FB", 12, "bold"), fg="#1197e0",bg="#ffffff")
    email_label.grid(row=20, column=3, padx=20, pady=20)

    #Create entry text field for email including adding grid layouts
    entry_email1 = Entry(window_n_a, width=40)
    entry_email1.grid(row=20, column=5, padx=30, pady=30)
    entry_email1.config(bg="#ffffff")

    #Create label for the username including adding grid layouts
    username_label = Label(window_n_a, text = "Username", font=("Californian FB", 12, "bold"), fg="#1197e0",bg="#ffffff")
    username_label.grid(row=24, column=3, padx=20, pady=20)

    #Create entry text field for username including adding grid layouts
    entry_username = Entry(window_n_a, width=40)
    entry_username.grid(row=24, column=5, padx=30, pady=30)
    entry_username.config(bg="#ffffff")

    #Create label for the password including adding grid layouts
    password_label = Label(window_n_a, text = "Password", font=("Californian FB", 12, "bold"), fg="#1197e0",bg="#ffffff")
    password_label.grid(row=28, column=3, padx=20, pady=20)

    #Create entry text field for password including adding grid layouts
    entry_password1 = Entry(window_n_a, width=40)
    entry_password1.grid(row=28, column=5, padx=30, pady=30)
    entry_password1.config(bg="#ffffff")

    #Apply a "create new account" button
    create_account_button = Button(window_n_a, text = "Create New Account", font=("Californian FB", 12, "bold"), fg="#1197e0",bg="#ffffff", command= lambda:display_confirmation_message(window_n_a, cnca_message))
    create_account_button.grid(row=31, column=5, columnspan=3, padx=30, pady=20)

    #Create a back button for the "new_account_button_clicked" window
    back_button1 = Button(window_n_a, text="Back", font=("Californian FB", 12, "bold"), fg="#1197e0",bg="#ffffff", command=lambda: destroyWindow(window_n_a))
    back_button1.grid(row=1, column=0, padx=30, pady=20)

#Define the function to display that new account has been created including adding grid layouts
def display_confirmation_message(window_combine, display_message):
    window_cnca = Toplevel()
    window_cnca.geometry("700x200")
    window_cnca.config(bg="#ffffff")
    cnca_label = Label(window_cnca, text=display_message, font=("Californian FB", 12, "bold"), fg="#1197e0", bg="#ffffff")
    cnca_label.grid(row=28, column=3, padx=20, pady=20)
    window_cnca.after(3000, lambda: destroyWindow(window_cnca))
    window_combine.destroy()

#Define function for clicking login button
def login_button_clicked():
    window_login = Toplevel()
    window_login.geometry("600x600")
    window_login.config(bg="#ffffff")

    #Display the title name of the app on the "login_button_clicked" window
    title_label2 = Label(window_login, text = "My Glucose Meter Tracker", font=("Californian FB", 20, "bold"), fg="#1197e0",bg="#ffffff")
    title_label2.grid(row=5, column=5, padx=30, pady=30)

    #Create label for the email including adding grid layouts
    username_email_label = Label(window_login, text = "Username or Email", font=("Californian FB", 12, "bold"), fg="#1197e0",bg="#ffffff")
    username_email_label.grid(row=20, column=3, padx=20, pady=20)

    #Create entry text field for email including adding grid layouts
    entry_username_email = Entry(window_login, width=40)
    entry_username_email.grid(row=20, column=5, padx=30, pady=30)
    entry_username_email.config(bg="#ffffff")

    #Create label for the password including adding grid layouts
    password_label = Label(window_login, text = "Password", font=("Californian FB", 12, "bold"), fg="#1197e0",bg="#ffffff")
    password_label.grid(row=28, column=3, padx=20, pady=20)

    #Create entry text field for the password including adding grid layouts
    entry_password2 = Entry(window_login, width=40)
    entry_password2.grid(row=28, column=5, padx=30, pady=30)
    entry_password2.config(bg="#ffffff")

    #Create a login button including adding grid layouts
    login_button = Button(window_login, text = "Login", font=("Californian FB", 12, "bold"), fg="#1197e0",bg="#ffffff", command=lambda: login_process(entry_username_email, entry_password2, window_login))
    login_button.grid(row=31, column=5, columnspan=3, padx=30, pady=20)

    #Create a back button for the "login_button_clicked" window including adding grid layouts
    back_button2 = Button(window_login, text="Back", font=("Californian FB", 12, "bold"), fg="#1197e0", bg="#ffffff", command= lambda: destroyWindow(window_login))
    back_button2.grid(row=1, column=0, padx=30, pady=20)

def login_process(username_entrybox, password_entrybox, window_login):
    username= username_entrybox.get()
    password= password_entrybox.get()

    #Indicate if a character exist in username
    if '@' in username:
        query = ("SELECT * "
                 "FROM userinfo "
                 "WHERE email = '" + username + "' "
                 "AND password = '" + password + "' "
                 )
    else:
        #Indicate if the character is not present
        query = ("SELECT * "
                 "FROM userinfo "
                 "WHERE username = '" + username + "' "
                  "AND password = '" + password + "' "
                 )
    cursor = cnx.cursor()
    cursor.execute(query)
    entries = cursor.fetchall()
    if len(entries) == 0:
        display_confirmation_message(window_login, login_message1)
    else:
        display_confirmation_message(window_login, login_message2)


    pass
    pass
#Define function for clicking to reset new password button
def forgot_reset_password_button_clicked():
    window_frp = Toplevel()
    window_frp.geometry("600x700")
    window_frp.config(bg="#ffffff")

    #Display the title name of the app on the "forgot_reset_password_clicked" window
    title_label2 = Label(window_frp, text = "My Glucose Meter Tracker", font=("Californian FB", 20, "bold"), fg="#1197e0",bg="#ffffff")
    title_label2.grid(row=5, column=2, columnspan=1, padx=30, pady=40)

    #Create label for the email including adding grid layouts
    email_label2 = Label(window_frp, text="Email", font=("Californian FB", 12, "bold"), fg="#1197e0", bg="#ffffff")
    email_label2.grid(row=20, column=1, columnspan=1, padx=20, pady=20)

    #Create entry text field for email including adding grid layouts
    entry_email2= Entry(window_frp, width=40)
    entry_email2.grid(row=20, column=2, padx=30, pady=30)
    entry_email2.config(bg="#ffffff")

    #Create label to reset the password including adding grid layouts
    reset_password_label = Label(window_frp, text = "Type New Password", font=("Californian FB", 12, "bold"), fg="#1197e0",bg="#ffffff")
    reset_password_label.grid(row=23, column=1, columnspan=1, padx=20, pady=20)

    #Create entry text field to type new password including adding grid layouts
    entry_password3=Entry(window_frp, width=40)
    entry_password3.grid(row=23, column=2, padx=30, pady=30)
    entry_password3.config(bg="#ffffff")

    #Create label to confirm new the password including adding grid layouts
    confirm_new_password_label = Label(window_frp, text = "Retype New Password", font=("Californian FB", 12, "bold"), fg="#1197e0",bg="#ffffff")
    confirm_new_password_label.grid(row=26, column=1, columnspan=1, padx=20, pady=20)

    #Create entry text field to confirm new password including adding grid layouts
    entry_confirm_new_password = Entry(window_frp, width=40)
    entry_confirm_new_password.grid(row=26, column=2, padx=30, pady=30)
    entry_confirm_new_password.config(bg="#ffffff")

    #Apply a "create new password" button including adding grid layouts
    create_new_password_button = Button(window_frp, text = "Create New Password", font=("Californian FB", 12, "bold"), fg="#1197e0",bg="#ffffff", command= lambda: update_password(entry_email2, entry_password3,entry_confirm_new_password))
    create_new_password_button.grid(row=27, column=2, columnspan=5, padx=30, pady=20)

    #Create a back button for the "forgot_reset_password_button_clicked" window including adding grid layouts
    back_button3 = Button(window_frp, text="Back", font=("Californian FB", 12, "bold"), fg="#1197e0", bg="#ffffff",command=lambda: destroyWindow(window_frp))
    back_button3.grid(row=1, column=0, padx=30, pady=20)

#Define the function to reset new password by using the SQLite database
def update_password(email_entrybox, password_entrybox, retype_password_entrybox):
        email = email_entrybox.get()
        password = password_entrybox.get()
        retype_password = retype_password_entrybox.get()
        query = ("UPDATE userinfo "
                 "SET password  = '" + password + "' "
                 "WHERE email = '" + email + "' "
                 )
        cursor = cnx.cursor()
        cursor.execute(query)
        cnx.commit()