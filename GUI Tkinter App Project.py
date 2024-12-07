from tkinter import*
from tkinter import Message
from ProjectFunctions import *
from timer import timer

if __name__=="__main__":

    #Create a window for the GUI app including adding the grid layouts
    window = Tk()
    window.title("My Glucose Meter Tracker")
    window.geometry("500x500")
    window.config(bg="#ffffff")

    #Create label and grid layout for the title of the app
    title_label1 = Label(window, text = "Welcome to", font=("Roboto", 16), fg="black",bg="#ffffff")
    title_label1.grid(row=5, column=5, columnspan=3, padx=20, pady=0)

    title_label2 = Label(window, text = "My Glucose Meter Tracker", font=("Californian FB", 22, "bold"), fg="#1197e0",bg="#ffffff")
    title_label2.grid(row=7, column=5, padx=30, pady=20)

    title_label3 = Label(window, text="Choose of one of the following options: ",font=("Californian FB", 14), fg="black", bg="#ffffff")
    title_label3.grid(row=30, column=5, padx=20, pady=0)

    #Create label and grid layout to create new account
    new_account_button = Button(window, text = " New User? Click Here to Create An Account  ", font=("Californian FB", 12, "bold"), fg="#1197e0",bg="#ffffff", command = new_account_button_clicked)
    new_account_button.grid(row=40, column=5, padx=100, pady=20)

    #Create label and add grid layouts for login button
    login_button = Button(window, text = "Already Have An Account? Click Here to Login", font=("Californian FB", 12, "bold"), fg="#1197e0",bg="#ffffff", command = login_button_clicked)
    login_button.grid(row=41, column=5, padx=100, pady=20)

    #Create label and grid layout to reset new password
    forgot_reset_password_button = Button(window, text = "      Forgot Password? Click Here to Reset It     ", font=("Californian FB", 12, "bold"), fg="#1197e0",bg="#ffffff",command = forgot_reset_password_button_clicked)
    forgot_reset_password_button.grid(row=42, column=5, padx=100, pady=20)

    #Run the application
    window.mainloop()


    """"
    #Define function
    def submit_glucose_level(user_glucose):
    
    
    #Initialize the target numbers for each glucose level
    high_glucose_level = 150 mg/dl or higher #Target numbers for high glucose levels
    normal_glucose_level = 100 mg/dl or 150 mg/dl #Target numbers for normal glucose levels
    borderline_low_level = 71 mg/dl to 99 mg/dl #Target numbers for borderline low glucose levels
    low_glucose_level = 70 mg/dl or below #Target numbers for low glucose level
    
    
    
    #Create a if else statement for the user's glucose levels
    if user_glucose >= 150:
        high = "Blood sugar is high"
        return high
    elif user_glucose >= 100 and user_glucose >= 150:
        normal =  "Blood sugar is normal"
        return normal
    elif user_glucose >= 71 and user_glucose <= 99:
        border_line_low = "Blood sugar is on the borderline of being low"
        return border_line_low
    else user_glucose < 70:
        low = "Blood sugar is low"
        return low
    
    
    #Submit blood glucose level
      =  label Enter your glucose
    glucose  =  entry 
    level_of_glucose = submit_glucose_level(glucose.get())
    
      =  label level_of_glucose
    """
