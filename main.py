import tkinter as tk
from configure import Config
from board2 import Apppage
from login_page import Login_Page
from about import About
from wtd import Wtd
from updatelog import Updatelog
from adddata_page2 import AddData_Page
from delete_page import DeleteData_Page

class Window(tk.Tk):
	def __init__(self,App):
		self.app = App
		self.config = self.app.config

		super().__init__()
		self.geometry(self.config.screen)
		self.title(self.config.title)

		self.create_container()
		self.pages = {}
		self.create_login_page()

	def create_container(self):
		self.container = tk.Frame(self)
		self.container.pack(fill="both", expand=True)

	def change_page(self,page):
		self.create_pages()
		page = self.pages[page]
		page.tkraise()

	def create_pages(self):
		self.pages['appPage'] = Apppage(self.app,self.container)
		self.create_menus()

	def create_adddata_page(self):
		self.pages['AddData_Page'] = AddData_Page(self.app, self.container)

	def create_login_page(self):
		self.pages['LoginPage'] = Login_Page(self.app, self.container)

	def create_about_page(self):
		self.pages['about'] = About(self.app, self.container)

	def create_wtd_page(self):
		self.pages['wtd'] = Wtd(self.app, self.container)

	def create_updatelog_page(self):
		self.pages['updatelog'] = Updatelog(self.app, self.container)

	def create_del_page(self):
		self.pages['Delete_Page'] = DeleteData_Page(self.app, self.container)

	def create_menus(self):
		self.menuBar = tk.Menu(self)
		self.configure(menu=self.menuBar)

		self.FileMenu = tk.Menu(self.menuBar, tearoff=0)
		self.FileMenu.add_command(label='New',command = self.create_adddata_page)
		self.FileMenu.add_command(label='Delete',command = self.create_del_page)

		self.helpMenu = tk.Menu(self.menuBar, tearoff=0)
		self.helpMenu.add_command(label="About", command=lambda:self.create_about_page())
		self.helpMenu.add_command(label="What To Do", command=lambda:self.create_wtd_page())
		self.helpMenu.add_command(label="UpdateLog", command=lambda:self.create_updatelog_page())

		self.menuBar.add_cascade(label='File', menu=self.FileMenu)
		self.menuBar.add_cascade(label="Help", menu=self.helpMenu)




class LibaryApp:
	def __init__(self) :
		self.config = Config()
		self.window = Window(self)

	def auth_login(self):
		if self.window.pages['LoginPage'].var_password.get() == 'jordan':
			self.Username = self.window.pages['LoginPage'].var_username.get()
			self.window.change_page('appPage')
		else:
			return True
			
	def run(self):
		self.window.mainloop()

if __name__ == '__main__':
	myLibaryApp = LibaryApp()
	myLibaryApp.run()