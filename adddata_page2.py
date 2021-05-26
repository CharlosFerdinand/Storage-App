import tkinter as tk
from tkinter import ttk

class AddData_Page(tk.Frame):

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

		self.Create_add_frame()

	def add_Brand_name(self,event):
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

	def add_Debugging(self):
		try:
			Datas = []
			self.ComboDatas = []

			for all_combo in self.Combobox_list:
				for all_type in all_combo:
					if all_type.get() == '':						
						if self.var[3][0].get() != 'Write In this Label for New Type' and self.var[3][0].get() != 'Write the correct Type' and self.var[3][0].get() != '':	
							self.ComboDatas.append(self.var[3][0].get())
						else:
							self.Label_add_list[0].delete(0,'end')
							self.Label_add_list[0].insert('end','Write the correct Type')
						if self.var[4][0].get() != 'Write In this Label for New Brand' and self.var[4][0].get() !=  'Write the correct Brand' and self.var[4][0].get() != '' :
							self.ComboDatas.append(self.var[4][0].get())
						else:
							self.Label_add_list[1].delete(0,'end')
							self.Label_add_list[1].insert('end','Write the correct Brand')
					else:
						self.ComboDatas.append(all_type.get())

			
			for every_index in self.var:
				datas = []
				if self.var.index(every_index) <= 2 :
					Error_enter = self.var.index(every_index) 			
					data = int(self.var[self.var.index(every_index)][0].get())
				else:
					data = self.var[self.var.index(every_index)][0].get()
				datas.append(data)
				Datas.append(datas)
			return Datas
				
				
		except ValueError:
			if Error_enter <= 1:					
				self.add_table_info[0][1].delete(0,'end')
				self.add_table_info[0][1].insert('end','Format Angka')

				self.add_table_info[1][1].delete(0,'end')
				self.add_table_info[1][1].insert('end','Format Angka')

			if Error_enter >= 2:			
				self.Label_add_list[2].delete(0,'end')
				self.Label_add_list[2].insert('end','Format Angka')
			
			
	def Add_Data(self):

		satuan = self.Volumetypes_add_Combo.get()
		self.Datas = self.add_Debugging()
		if self.Datas != None:

			for all_data in self.settings.data:
				for types,info in all_data.items():
					if types == self.ComboDatas[0]:
						self.index = self.settings.data.index(all_data) 


			if self.Brand_list != None:
				data = self.settings.data[self.index]
				if self.ComboDatas[0] in self.product_type  and self.ComboDatas[1] not in self.Brand_list and self.Datas[2][0] != self.VolumeNumber:
					New_datas = {self.ComboDatas[1]:{str(self.Datas[2][0])+satuan: {"Stock" : str(self.Datas[0][0]),"Harga" : str(self.Datas[1][0])}}}
					self.settings.data[self.index][self.ComboDatas[0]]['Brand'].update(New_datas)



				elif self.ComboDatas[0] in self.product_type and self.ComboDatas[1] in self.Brand_list:
					New_datas = {str(self.Datas[2][0])+satuan: {"Stock" : str(self.Datas[0][0]),"Harga" : str(self.Datas[1][0])}}
					self.settings.data[self.index][self.ComboDatas[0]]['Brand'][self.ComboDatas[1]].update(New_datas)

				elif self.ComboDatas[0] in self.product_type and self.ComboDatas[1] in self.Brand_list and self.Datas[2][0] == self.VolumeNumber:	

					for Types,info in data.items():
						
						self.settings.data[self.index][self.ComboDatas[0]]['Brand'][self.ComboDatas[1]][self.Datas[2][0]]['Harga'] = str(self.Datas[0][0])
						self.settings.data[self.index][self.ComboDatas[0]]['Brand'][self.ComboDatas[1]][self.Datas[2][0]]['Stock'] =  str(self.Datas[1][0])

			else:
				New_datas = {self.ComboDatas[0]:{'Brand':{self.ComboDatas[1]:{str(self.Datas[2][0])+satuan: {"Stock" : str(self.Datas[0][0]),"Harga" : str(self.Datas[1][0])}}}}}
				self.settings.data.append(New_datas)


			self.settings.Write_Data()
			self.app.window.change_page('appPage')

	def Create_add_frame(self):
		self.right_add_frame = tk.Frame(self, bg="white", width=self.settings.width,height=self.settings.height)
		self.right_add_frame.pack(expand=True,fill='both')
		


		self.create_Add_header()
		self.create_Add_content()
		self.create_Add_footer()

	def create_Add_header(self):
		frame_w = 2*self.settings.width//3
		frame_h = self.settings.height//5
		self.var_2 = []
		self.Combobox_list = []
		self.Label_add_list = [] 
		self.product_type = []
		self.virtual_image = tk.PhotoImage(width=1,height=1)

		for all_products in self.settings.data:
			for all_product in all_products:
				self.product_type.append(all_product)

		self.right_header = tk.Frame(self.right_add_frame, width=frame_w, height=frame_h,bg='white')
		self.right_header.pack(expand=True)

		self.detail_add_header = tk.Frame(self.right_header,width=frame_w,height=frame_h,bg='white')
		self.detail_add_header.grid(row=0,column=0,sticky='nsew') 
		
		Type_add_var = tk.StringVar()
		self.Type_Name_Label_Choose_combobox_Label =  tk.Label(self.detail_add_header,font=('Arial',22),bg='white',image=self.virtual_image,compound='c',text = 'Type Choose')
		self.Type_Name_Label_Choose_combobox_Label.grid(row=0,column=0,sticky='nsew')
		self.Type_Name_Label_Choose_combobox = ttk.Combobox(self.detail_add_header)
		self.product_type.append('')
		self.Type_Name_Label_Choose_combobox['value'] = self.product_type
		self.Type_Name_Label_Choose_combobox.grid(row=0,column=1,sticky='nsew')
		self.Type_Name_Label_Choose = tk.Entry(self.detail_add_header,font=('Arial',22,),bg='white',width=30 ,textvariable=Type_add_var)
		self.Type_Name_Label_Choose.insert('end','Write In this Label for New Type')
		self.Type_Name_Label_Choose.grid(row=1,column=0,sticky='nsew',columnspan = 2)	

		brand_add_var = tk.StringVar()
		self.Brand_Name_Label_Choose_Label = tk.Label(self.detail_add_header,font=('Arial',22),bg='white',image=self.virtual_image,compound='c',text = 'Brand Choose')
		self.Brand_Name_Label_Choose_Label.grid(row=2,column=0,sticky='nsew')
		self.Brand_Name_Label_Choose_combobox = ttk.Combobox(self.detail_add_header)
		self.Brand_Name_Label_Choose_combobox.grid(row=2,column=1,sticky='nsew')
		self.Brand_Name_Label_Choose = tk.Entry(self.detail_add_header,font=('Arial',22,),bg='white',width=30 ,textvariable=brand_add_var)
		self.Brand_Name_Label_Choose.insert('end','Write In this Label for New Brand')
		self.Brand_Name_Label_Choose.grid(row=3,column=0,sticky='nsew',columnspan = 2)	
	
		
		volume_add_var = tk.StringVar()
		self.Volume_add_Types_Label = tk.Entry(self.detail_add_header,font=('Arial',22),bg='white',width=3,textvariable=volume_add_var)
		self.Volume_add_Types_Label .grid(row=4,column=0,sticky='nsew')

		self.Volumetypes_add_Combo = ttk.Combobox(self.detail_add_header,height=1)
	
	
		self.Volumetypes_add_Combo['values'] = ['Cm','M','L','Ml']
		self.Volumetypes_add_Combo.current(0)
		self.Volumetypes_add_Combo.grid(row=4,column=1,sticky='nsew')	

		self.Label_add_list.append(self.Type_Name_Label_Choose)
		self.Label_add_list.append(self.Brand_Name_Label_Choose)
		self.Label_add_list.append(self.Volume_add_Types_Label)

		self.Combobox_list.append([self.Type_Name_Label_Choose_combobox])
		self.Combobox_list.append([self.Brand_Name_Label_Choose_combobox])
		self.var_2.append([volume_add_var])
		self.var_2.append([Type_add_var])
		self.var_2.append([brand_add_var])

		self.Type_Name_Label_Choose_combobox.bind('<<ComboboxSelected>>',self.add_Brand_name)

		

		self.right_header.grid_rowconfigure(0,weight=1)
		self.right_header.grid_columnconfigure(0,weight=1)	

	def create_Add_content(self):
		frame_w = 2*self.settings.width//3
		frame_h = 4*self.settings.height//7
		self.right_add_content = tk.Frame(self.right_add_frame, width=frame_w, height=frame_h, bg="white")
		self.right_add_content.pack(expand=True,pady=100)

		self.detail_add_content = tk.Frame(self.right_add_content,width = frame_w,height=frame_h,bg='white')
		self.detail_add_content.grid(row=0,column=0)

		self.add_table_info = []
		self.var=[]


		info = [
		['Stock :',''],
		['Harga :','']
		]

		rows,columns = len(info),len(info[0])

		for row in range(rows):
			aRow = []
			var = []
			for column in range(columns):
			
				if column == 0:
					Entry = tk.Label(self.detail_add_content,text =info[row][column],font=('Arial',22),bg='white',image=self.virtual_image,compound='c')
					aRow.append(Entry)
					sticky='e'
				else:
					var_entry = tk.StringVar()
					Entry = tk.Entry(self.detail_add_content,font=('Arial',22),bg='white',width=18,textvariable = var_entry)
					Entry.insert('end',info[row][column])
					aRow.append(Entry)
					var.append(var_entry)
					sticky = 'w'
				Entry.grid(row=row,column=column,sticky=sticky)

			self.add_table_info.append(aRow)
			self.var.append(var)
		for all_var in self.var_2:
			self.var.append(all_var)

	def create_Add_footer(self):
		frame_w = 2*self.settings.width//3
		frame_h = (4*self.settings.height//5)//4

		self.right_add_footer = tk.Frame(self.right_add_frame, width=frame_w, height=frame_h, bg="white")
		self.right_add_footer.pack(expand=True)

		self.detail_add_footer = tk.Frame(self.right_add_footer,width=frame_w, height=frame_h, bg="white")
		self.detail_add_footer.grid(row=0,column=0)

		features = ['Save','Cancel']
		self.button_add_features = []
		for feature in features:
			button = tk.Button(self.detail_add_footer ,text = feature,bg='white',bd=0,fg='black',font=('Arial',12,'bold'))
			if features.index(feature) == 0:
				button.configure(command=self.Add_Data)
			else:
				button.configure(command = lambda: self.app.window.change_page('appPage'))


			button.grid(row=0,column=features.index(feature),sticky='nsew',padx=5)
			self.button_add_features.append(button)

		self.right_add_footer.grid_rowconfigure(0,weight=1)
		self.right_add_footer.grid_columnconfigure(0,weight=1)

