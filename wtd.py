import tkinter as tk
from tkinter import ttk

class Wtd(tk.Frame):
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
		self.main_frame = tk.Frame(self,height = self.screen[0],width=self.screen[1],bg ='black')
		self.main_frame.pack(expand = True)

		self.label_Username = tk.Label(self.main_frame,text='Pick an item and then choose a brand.',font = ('Arial',18,"bold"),bg ='black',fg='white')
		self.label_Username.pack(fill='both')
		self.label2 =tk.Label(self.main_frame,text='Feel free to change however you please with the buttons given.',font = ('Arial',18,"bold"),bg ='black',fg='white')
		self.label2.pack(fill='both')
		self.btn_login = tk.Button(self.main_frame,text="Go Back",font=('Arial',18,'bold'),command = lambda: self.application.window.create_pages())
		self.btn_login.pack(pady=5)