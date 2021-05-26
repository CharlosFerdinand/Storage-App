import tkinter as tk
from tkinter import ttk
import getpass


class Login_Page(tk.Frame):
	def __init__(self,App,parent):
		self.application = App
		self.config = App.config
		self.screen = self.config.screen

		super().__init__(parent)
		self.configure(bg = 'black')
		self.grid(row=0,column=0,sticky = 'nsew')
		parent.grid_columnconfigure(0,weight = 1)
		parent.grid_rowconfigure(0,weight=1)

		#CREATE MAIN FRAME
		self.main_frame = tk.Frame(self,height = self.screen[0],width=self.screen[1],bg = 'black')
		self.main_frame.pack(expand = True)

		self.Choose_Username()
		self.Choose_Password()
		
	def Choose_Username(self):
		self.label_Username = tk.Label(self.main_frame,text='Username',font = ('Arial',18,"bold"),bg ='black',fg='white')
		self.label_Username.pack(pady = 5)
		self.var_username = tk.StringVar()
		self.entry_username = tk.Entry(self.main_frame,font =("Arial",16,'bold'), textvariable = self.var_username)
		self.entry_username.pack(pady = 5)


	def Choose_Password(self):
		self.label_password = tk.Label(self.main_frame,text='Password',font = ('Arial',18,"bold"),bg = 'black',fg='white')
		self.label_password.pack(pady = 5)
		self.var_password = tk.StringVar()
		self.entry_password = tk.Entry(self.main_frame,font =("Arial",16,'bold'), textvariable = self.var_password)
		self.entry_password.config(show="*");
		self.entry_password.pack(pady = 5)
		self.btn_login = tk.Button(self.main_frame,text="LOGIN",font=('Arial',18,'bold'),command = lambda: self.application.auth_login())
		self.btn_login.pack(pady=5)

		self.btn_login.pack(pady=5)
