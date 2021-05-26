import tkinter as tk
from tkinter import ttk

class DeleteData_Page(tk.Frame):

	def __init__(self,App,Parent):
		self.app = App
		self.settings = App.config

		super().__init__(Parent)
		self.Num = 0
		self.Nums = 0
		self.Brand_list =None

		self.grid(row=0, column=0, sticky="nsew")

		Parent.grid_rowconfigure(0, weight=1)
		Parent.grid_columnconfigure(0, weight=1)

		self.Create_Delete_frame()

	def Get_Volume_name(self,event):
		self.Brand = self.Brand_Name_Label_Choose_combobox.get()
		Volume_list = []
		for all_data in self.settings.data:
			for types,info in all_data.items():
				if types == self.Types:
					for all_brand,Brand_name in info.items():
						for brand,VolumeInfos in Brand_name.items():
							if brand == self.Brand:
								for Volume in VolumeInfos:
									Volume_list.append(Volume)
		Volume_list.append('')
		self.Volumetypes_Delete_Combo['values'] = Volume_list

	def Get_Brand_name(self,event):
		self.Types = self.Type_Name_Label_Choose_combobox.get()
		self.Brand_list = []

		for all_data in self.settings.data:
			for types,info in all_data.items():
				if types == self.Types:
					self.index = self.settings.data.index(all_data) 
					for all_brand,Brand_name in info.items():
						for brand in Brand_name:
							self.Brand_list.append(brand)


		self.Brand_list.append('')
		self.Brand_Name_Label_Choose_combobox['value'] = self.Brand_list

	def Destroy_Warning_Label(self):
		for all_index in self.button_Delete_features:
			for all_button in all_index:
				all_button.destroy()
		self.Warning_Label.destroy()

	def save_data(self):
		self.settings.Write_Data()
		self.app.window.change_page('appPage')


	def delete_All(self):
		for all_data in self.settings.data:
			self.index = self.settings.data.index(all_data)
			del self.settings.data[self.index]
		self.Warning_Label = tk.Label(self.detail_Delete_header,font=('Arial',22),bg='white',image=self.virtual_image,compound='c',text = 'Are You Sure To Delete All Data')
		self.Warning_Label.grid(row=6,column=0,columnspan=2)
		features = ['Yes','No']
		self.button_Delete_features = []
		for feature in features:
			button = tk.Button(self.detail_Delete_header ,text = feature,bg='white',bd=0,fg='black',font=('Arial',12,'bold'))
			if features.index(feature) == 0:
				button.configure(command=self.save_data)
			else:
				button.configure(command = self.Destroy_Warning_Label )
			button.grid(row=7,column=features.index(feature))
			self.button_Delete_features.append([button])

			
			
	def Delete_Data(self):

		satuan = self.Volumetypes_Delete_Combo.get()
		self.ComboDatas = []

		for all_combo in self.Combobox_list:
			for all_type in all_combo:						
				self.ComboDatas.append(all_type.get())

		for all_data in self.settings.data:
			for types,info in all_data.items():
				if types == self.ComboDatas[0]:
					self.index = self.settings.data.index(all_data) 


		if self.Brand_list != None:
			data = self.settings.data[self.index]


			if self.ComboDatas[0] != '' and self.ComboDatas[1] != '' and self.ComboDatas[2] !='':
				del self.settings.data[self.index][self.ComboDatas[0]]['Brand'][self.ComboDatas[1]][self.ComboDatas[2]]

			elif self.ComboDatas[0] != '' and self.ComboDatas[1] != '':
				for every_object in self.settings.data[self.index]:
					del self.settings.data[self.index][self.ComboDatas[0]]['Brand'][self.ComboDatas[1]]
			else:
				del self.settings.data[self.index]

		else:
			del self.settings.data[self.index][self.ComboDatas[0]]

		self.settings.Write_Data()
		self.app.window.change_page('appPage')

	def Create_Delete_frame(self):
		self.right_Delete_frame = tk.Frame(self, bg="white", width=self.settings.width,height=self.settings.height)
		self.right_Delete_frame.pack(expand=True,fill='both')
		


		self.create_Delete_header()
		self.create_Delete_footer()

	def create_Delete_header(self):
		frame_w = 2*self.settings.width//3
		frame_h = self.settings.height//5
		self.Combobox_list = []
		self.product_type = []
		self.virtual_image = tk.PhotoImage(width=1,height=1)

		for all_products in self.settings.data:
			for all_product in all_products:
				self.product_type.append(all_product)

		self.right_header = tk.Frame(self.right_Delete_frame, width=frame_w, height=frame_h,bg='white')
		self.right_header.pack(expand=True)

		self.detail_Delete_header = tk.Frame(self.right_header,width=frame_w,height=frame_h,bg='white')
		self.detail_Delete_header.grid(row=0,column=0,sticky='nsew') 
		
		Type_Delete_var = tk.StringVar()
		self.Type_Name_Label_Choose_combobox_Label =  tk.Label(self.detail_Delete_header,font=('Arial',22),bg='white',image=self.virtual_image,compound='c',text = 'Type Choose')
		self.Type_Name_Label_Choose_combobox_Label.grid(row=0,column=0,sticky='nsew')
		self.Type_Name_Label_Choose_combobox = ttk.Combobox(self.detail_Delete_header)
		self.product_type.append('')
		self.Type_Name_Label_Choose_combobox['value'] = self.product_type
		self.Type_Name_Label_Choose_combobox.grid(row=0,column=1,sticky='nsew')

		brand_Delete_var = tk.StringVar()
		self.Brand_Name_Label_Choose_Label = tk.Label(self.detail_Delete_header,font=('Arial',22),bg='white',image=self.virtual_image,compound='c',text = 'Brand Choose')
		self.Brand_Name_Label_Choose_Label.grid(row=1,column=0,sticky='nsew')
		self.Brand_Name_Label_Choose_combobox = ttk.Combobox(self.detail_Delete_header)
		self.Brand_Name_Label_Choose_combobox.grid(row=1,column=1,sticky='nsew')
		
		volume_Delete_var = tk.StringVar()
		self.Volume_Delete_Types_Label = tk.Label(self.detail_Delete_header,font=('Arial',22),bg='white',image=self.virtual_image,compound='c',text = 'Volume Choose')
		self.Volume_Delete_Types_Label .grid(row=2,column=0,sticky='nsew')

		self.Volumetypes_Delete_Combo = ttk.Combobox(self.detail_Delete_header,height=1)
		self.Volumetypes_Delete_Combo.grid(row=2,column=1,sticky='nsew')	


		self.Combobox_list.append([self.Type_Name_Label_Choose_combobox])
		self.Combobox_list.append([self.Brand_Name_Label_Choose_combobox])
		self.Combobox_list.append([self.Volumetypes_Delete_Combo ])

		self.Volume_Radiobutton = tk.Radiobutton(self.detail_Delete_header,text='Delete all data',command=self.delete_All)
		self.Volume_Radiobutton.grid(row=5,sticky='nsew',columnspan=2)


		self.Type_Name_Label_Choose_combobox.bind('<<ComboboxSelected>>',self.Get_Brand_name)
		self.Brand_Name_Label_Choose_combobox.bind('<<ComboboxSelected>>',self.Get_Volume_name)

		

		self.right_header.grid_rowconfigure(0,weight=1)
		self.right_header.grid_columnconfigure(0,weight=1)	

	def create_Delete_footer(self):
		frame_w = 2*self.settings.width//3
		frame_h = (4*self.settings.height//5)//4

		self.right_Delete_footer = tk.Frame(self.right_Delete_frame, width=frame_w, height=frame_h, bg="white")
		self.right_Delete_footer.pack(expand=True)

		self.detail_Delete_footer = tk.Frame(self.right_Delete_footer,width=frame_w, height=frame_h, bg="white")
		self.detail_Delete_footer.grid(row=0,column=0)

		features = ['Save','Cancel']
		self.button_Delete_features = []
		for feature in features:
			button = tk.Button(self.detail_Delete_footer ,text = feature,bg='white',bd=0,fg='black',font=('Arial',12,'bold'))
			if features.index(feature) == 0:
				button.configure(command=self.Delete_Data)
			else:
				button.configure(command = lambda: self.app.window.change_page('appPage'))


			button.grid(row=0,column=features.index(feature),sticky='nsew',padx=5)
			self.button_Delete_features.append(button)

		self.right_Delete_footer.grid_rowconfigure(0,weight=1)
		self.right_Delete_footer.grid_columnconfigure(0,weight=1)

