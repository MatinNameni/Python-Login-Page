import customtkinter as ctk
import tkinter as tk
from commands import *

class LoginPage:
    def __init__(self):
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('blue')

        self.root = ctk.CTk()
        self.root.geometry('300x320')
        self.root.eval('tk::PlaceWindow . center')
        self.root.resizable(False, False)
        self.root.title('Login')

        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack(padx=20, pady=20, fill='both', expand=True)

        self.label = ctk.CTkLabel(self.frame, text='Login', font=('Showcard Gothic', 30), text_color='#2275b7')
        self.label.pack(padx=10, pady=10)

        self.username_entry = ctk.CTkEntry(self.frame, placeholder_text='Username', font=('Ink Free', 15))
        self.username_entry.pack(padx=10, pady=10, fill='x')

        self.password_entry = ctk.CTkEntry(self.frame, placeholder_text='Password', show='*', font=('Ink Free', 15))
        self.password_entry.pack(padx=10, fill='x')

        self.showpass_checkbox = ctk.CTkCheckBox(self.frame, text='Show Password', font=('Segoe Print', 12), checkbox_height=20, checkbox_width=20, command=self.show_password)
        self.showpass_checkbox.pack(padx=10, pady=10, anchor=ctk.W)
        
        self.signup_label = ctk.CTkLabel(self.frame, text="don't have an account yet? SignUp",font=('Segoe Print', 13), text_color="cyan", cursor="hand2")
        self.signup_label.pack(padx=10, pady=10, anchor=ctk.W)
        self.signup_label.bind("<Button-1>", self.lunch_signup_page)

        self.login_button = ctk.CTkButton(self.frame, text='Login', font=('Segoe Print', 25), command=self.login)
        self.login_button.pack(padx=10, fill='x')

    def show_password(self):
        if self.showpass_checkbox.get() == 0:
            self.password_entry.configure(show='*')
        else:
            self.password_entry.configure(show='')

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if ' ' in username or ' ' in password:
            tk.messagebox.showerror(title="Error", message="You can't use space for username or password")
        elif username == '' or password == '':
            tk.messagebox.showerror(title="Error", message="Please enter all required information")        
        else:
            user = User(username, password)
            state = user.login_status()
            if state == 1:
                tk.messagebox.showinfo(message="You have successfully logged in")
            else:
                tk.messagebox.showerror(title="Error", message="Wrong username or password")        

    def lunch_signup_page(self, event):
        self.destroy()
        signup_page = SignUpPage()
        signup_page.mainloop()

    def mainloop(self):
        return self.root.mainloop()
    
    def destroy(self):
        return self.root.destroy()




class SignUpPage:
    def __init__(self):
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('green')

        self.root = ctk.CTk()
        self.root.geometry('300x380')
        self.root.eval('tk::PlaceWindow . center')
        self.root.resizable(False, False)
        self.root.title('Sign Up')

        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack(padx=20, pady=20, fill='both', expand=True)

        self.label = ctk.CTkLabel(self.frame, text='Sign Up', font=('Showcard Gothic', 30), text_color='#35bf83')
        self.label.pack(padx=10, pady=20)

        self.username_entry = ctk.CTkEntry(self.frame, placeholder_text='Username', font=('Ink Free', 15))
        self.username_entry.pack(padx=10, fill='x')

        self.password_entry = ctk.CTkEntry(self.frame, placeholder_text='Password', show='*', font=('Ink Free', 15))
        self.password_entry.pack(padx=10, pady=10, fill='x')

        self.retype_password_entry = ctk.CTkEntry(self.frame, placeholder_text='Retype Password', show='*', font=('Ink Free', 15))
        self.retype_password_entry.pack(padx=10, fill='x')

        self.showpass_checkbox = ctk.CTkCheckBox(self.frame, text='Show Password', font=('Segoe Print', 12), checkbox_height=20, checkbox_width=20, command=self.show_password)
        self.showpass_checkbox.pack(padx=10, pady=10, anchor=ctk.W)

        self.login_label = ctk.CTkLabel(self.frame, text="Already have an account? Login",font=('Segoe Print', 13), text_color="lightgreen", cursor="hand2")
        self.login_label.pack(padx=10, pady=10, anchor=ctk.W)
        self.login_label.bind("<Button-1>", self.lunch_login_page)
        
        self.signup_button = ctk.CTkButton(self.frame, text='Sign Up', font=('Segoe Print', 25), command=self.signup)
        self.signup_button.pack(padx=10, fill='x')

    def show_password(self):
        if self.showpass_checkbox.get() == 0:
            self.password_entry.configure(show='*')
            self.retype_password_entry.configure(show='*')
        else:
            self.password_entry.configure(show='')
            self.retype_password_entry.configure(show='')

    def signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        re_password = self.retype_password_entry.get()

        if ' ' in username or ' ' in password or ' ' in re_password:
            tk.messagebox.showerror(title="Error", message="You can't use space for username or password")
        elif username == '' or password == '' or re_password == '':
            tk.messagebox.showerror(title="Error", message="Please fill all required information")
        elif password != re_password:
            tk.messagebox.showerror(title="Error", message="Password and Retype password are not the same")
        else:
            user = User(username, password)
            if user.signup() != 0:
                tk.messagebox.showinfo(message='account created! you can login now')
                

    def lunch_login_page(self, event):
        self.destroy()
        login_page = LoginPage()
        login_page.mainloop()
        

    def mainloop(self):
        return self.root.mainloop()

    def destroy(self):
        return self.root.destroy()
