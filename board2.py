import tkinter as tk
from tkinter import ttk

class Apppage(tk.Frame):

	def __init__(self,App,Parent):
		self.app = App
		self.settings = App.config

		super().__init__(Parent)
		self.Num = 0
		self.Nums = 0
		self.Nums_Volume = 0
		self.Brand_list =None
		self.features = None
		self.feature_new = None
		self.Volumetypes = ['']

		

		self.grid(row=0, column=0, sticky="nsew")

		Parent.grid_rowconfigure(0, weight=1)
		Parent.grid_columnconfigure(0, weight=1)

		self.create_left_frame()
		self.create_right_frame()
		self.config_left_and_right_frame()

	# Def Search
	def Plus_Number(self,number,info):
		
		Number = self.var[info][0].get()
		self.update_table_info[info][number].delete(0,'end')
		try:
			self.update_table_info[info][number].insert('end',(int(Number)+1))
		except ValueError:
			self.update_table_info[info][number].insert('end',('Format angka'))

	def Minus_Number(self,number,info):
		
		Number = self.var[info][0].get()
		self.update_table_info[info][number].delete(0,'end')
		try:
			self.update_table_info[info][number].insert('end',(int(Number)-1))
		except ValueError:
			self.update_table_info[info][number].insert('end',('Format angka'))

	def Delete_Size(self):
		for every_object in self.settings.data[self.index]:
			del self.settings.data[self.index][every_object]['Brand'][self.Brand][self.Volume]
		self.refresh_frame()
		self.settings.Write_Data()

	def Delete_Types(self):
		del self.settings.data[self.index]
		self.settings.Write_Data()
		self.refresh_frame()

	def Volume_word_Debugging(self,volume):
		self.SatuanWord = ''
		self.VolumeNumber = ''
		Volume = []
		Satuan = []
		Volume_word = 0
	
		try:
			for all_word in volume:
				Volume.append(int(all_word))
				Volume_word += 1
		except ValueError:
			Step_2 = len(volume)
			for step in range(Volume_word,Step_2):
				Satuan.append(volume[step])

		for all_word in Volume:
			self.VolumeNumber+= str(all_word)


		for all_word in Satuan:
			if all_word != '':
				self.SatuanWord += str(all_word)
			else:
				return

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

	def Find_Types(self):
		Find_Types = self.var_name.get()
		if Find_Types != '':
			for all_index in self.settings.data:
				for all_types in all_index:
					self.List_1_box.delete('active')
			for all_index in self.settings.data:
				for all_types in all_index:
					if all_types.lower() == Find_Types.lower():
						self.List_1_box.insert('end',all_types)
		else:
			for all_index in self.settings.data:
				for all_types in all_index:
					self.List_1_box.delete('active')
			for all_index in self.settings.data:
				for all_types in all_index:				
					self.List_1_box.insert('end',all_types)

	def Find_Brand(self):
		Find_Types = self.var_name_2.get()
		if Find_Types != '':
			for all_index,info in self.settings.data[self.index].items():
				for Brand,Brand_info in info.items():
					for Brand_Name, Brand_infos in Brand_info.items():
						self.List_2_box.delete('active')
			for all_index,info in self.settings.data[self.index].items():
				for Brand,Brand_info in info.items():
					for Brand_Name, Brand_infos in Brand_info.items():
						if Brand_Name.lower() == Find_Types.lower():
							self.List_2_box.insert('end',Brand_Name)
		else:
			for all_index,info in self.settings.data[self.index].items():
				for Brand,Brand_info in info.items():
					for Brand_Name, Brand_infos in Brand_info.items():
						self.List_2_box.delete('active')
			for all_index,info in self.settings.data[self.index].items():
				for Brand,Brand_info in info.items():
					for Brand_Name, Brand_infos in Brand_info.items():			
						self.List_2_box.insert('end',Brand_Name)

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
			
			if self.ComboDatas:
				pass
			
	def Add_Data(self):

		satuan = self.Volumetypes_add_Combo.get()
		self.Datas = self.add_Debugging()
		if self.Datas != None:
			for all_data in self.settings.data:
				for types,info in all_data.items():
					if types == self.ComboDatas[0]:
						self.index = self.settings.data.index(all_data) 

			data = self.settings.data[self.index]

			if self.Brand_list != None :
				if self.ComboDatas[0] in self.product_type  and self.ComboDatas[1] not in self.Brand_list :
					New_datas = {self.ComboDatas[1]:{str(self.Datas[2][0])+satuan: {"Stock" : str(self.Datas[0][0]),"Harga" : str(self.Datas[1][0])}}}
					self.settings.data[self.index][self.ComboDatas[0]]['Brand'].update(New_datas)



				elif self.ComboDatas[0] in self.product_type and self.ComboDatas[1] in self.Brand_list:
					New_datas = {str(self.Datas[2][0])+satuan: {"Stock" : str(self.Datas[0][0]),"Harga" : str(self.Datas[1][0])}}
					self.settings.data[self.index][self.ComboDatas[0]]['Brand'][self.ComboDatas[1]].update(New_datas)


			else:
				New_datas = {self.ComboDatas[0]:{'Brand':{self.ComboDatas[1]:{str(self.Datas[2][0])+satuan: {"Stock" : str(self.Datas[0][0]),"Harga" : str(self.Datas[1][0])}}}}}
				self.settings.data.append(New_datas)


			self.settings.Write_Data()
			self.refresh_frame()
		
	def Int_Debugging(self):
			
		try:
			Datas = []
			
			for every_index in self.var:
				if self.var.index(every_index) <= 2 :
					datas = []	
					Error_enter = self.var.index(every_index)	
					data = int(self.var[self.var.index(every_index)][0].get()) 
				else:
					datas = []	
					data = self.var[self.var.index(every_index)][0].get()
				datas.append(data)
				Datas.append(datas)
			return Datas
			
		except ValueError:	
			if Error_enter <= 1:					
				self.update_table_info[0][1].delete(0,'end')
				self.update_table_info[0][1].insert('end','Format Angka')

				self.update_table_info[1][1].delete(0,'end')
				self.update_table_info[1][1].insert('end','Format Angka')
		

			else:
				self.Volume_Types_Label.delete(0,'end')
				self.Volume_Types_Label.insert('end','Angka')

			
	def Update_Data(self):	
		self.Datas =  self.Int_Debugging()
		Satuan = self.Volumetypes_Combo.get()
		data = self.settings.data[self.index]
		
		if self.Datas != None:

			if self.Datas[3][0] != self.Brand:
				for Types,info in data.items():
					old_Data = self.settings.data[self.index][Types]['Brand'][self.Brand]
					del self.settings.data[self.index][Types]['Brand'][self.Brand]


					self.settings.data[self.index][Types]['Brand'].update({self.Datas[3][0] : old_Data})
					self.settings.data[self.index][Types]['Brand'][self.Datas[3][0]].update({str(self.Datas[2][0])+Satuan : {
																								"Stock" : str(self.Datas[0][0]),
																								"Harga" : str(self.Datas[1][0])}})

			elif self.Datas[2][0] == self.Volume:	

				for Types,info in data.items():
					
					self.settings.data[self.index][Types]['Brand'][self.Brand][self.Volume]['Harga'] = str(self.Datas[0][0])
					self.settings.data[self.index][Types]['Brand'][self.Brand][self.Volume]['Stock'] =  str(self.Datas[1][0])

			elif self.Datas[2][0] != self.Volume:

				for Types,info in data.items():
					del self.settings.data[self.index][Types]['Brand'][self.Brand][self.Volume]
					self.settings.data[self.index][Types]['Brand'][self.Brand][str(self.Datas[2][0])+Satuan] = {
																								"Stock" : str(self.Datas[0][0]),
																								"Harga" : str(self.Datas[1][0])}



			self.settings.Write_Data()
			self.refresh_frame()
  
	def Update_page(self):
		self.right_update_frame = tk.Frame(self, bg="white", width=2*self.settings.width//3)
		self.right_update_frame.grid(row=0, column=1, sticky="nsew")
		


		self.create_Update_header()
		self.create_Update_content()
		self.create_Update_footer()

	def Create_add_frame(self):
		self.right_add_frame = tk.Frame(self, bg="white", width=2*self.settings.width//3)
		self.right_add_frame.grid(row=0, column=1, sticky="nsew")
		


		self.create_Add_header()
		self.create_Add_content()
		self.create_Add_footer()

	def refresh_frame(self):
		self.create_left_frame()
		self.create_right_frame()

	def Delete_Brand(self):
		for every_object in self.settings.data[self.index]:
			del self.settings.data[self.index][every_object]['Brand'][self.Brand]
		self.refresh_frame()
		self.settings.Write_Data()

	def get(self,event):
		self.Types = self.List_1_box.get('anchor')	

		for all_data in self.settings.data:
			for title,info in all_data.items():
				if title == self.Types:
					self.index = self.settings.data.index(all_data) 

		for step in range(self.Num):
			self.List_2_box.delete('active')
		self.Num = 0

		for all_data,all_info in self.settings.data[self.index].items():
			for Brand,info in all_info.items():
				for all_brand in info:
					self.List_2_box.insert('end',all_brand)
					self.Num += 1

		if self.feature_new == None:
			self.features = ['Delete','Add New']
			if self.Nums == 0 :
				self.create_right_footer()
				self.Nums+= 1
			else:
				self.right_footer.destroy()
				self.create_right_footer()	
				self.button_features[0][0].configure(command=self.Delete_Types)
				self.button_features[1][0].configure(command=self.Create_add_frame)	
		else:
			self.feature_new = None
				

		self.button_search_2.configure(command=self.Find_Brand)

		self.List_2_box.bind('<<ListboxSelect>>',self.get_listbox2)

	def ComboCommand(self,event):
		self.Volume = self.Volume_choose.get()
		self.Volumeindex = self.Volumetypes.index(self.Volume)
		self.Stock = self.StockTypes[self.Volumeindex]
		self.Harga = self.HargaTypes[self.Volumeindex]
		info = [self.Stock,self.Harga]
		for step in range(2):
			self.table_info[step][1].configure(text=info[step])

	def get_listbox2(self,event):
		data_stock = self.settings.data
		data = data_stock[self.index]
		Brand_Name = self.List_2_box.get('anchor')

		if Brand_Name != '': 
			self.Volumetypes = []
			self.StockTypes = []
			self.HargaTypes = []
			for Types,info in data.items():
				for Brand,infos in info.items():
					self.Brand = Brand_Name
				
					for Volume, Volumeinfo in infos[Brand_Name].items():

						self.StockTypes.append(Volumeinfo['Stock'])
						self.HargaTypes.append(Volumeinfo['Harga'])
						self.Volumetypes.append(Volume)
						

				self.brand_label.configure(text=self.Brand)
			if self.Volumetypes == []:
				self.Volumetypes = ['']
				self.StockTypes = ['']
				self.HargaTypes = ['']

			self.Stock = self.StockTypes[0]
			self.Harga = self.HargaTypes[0]
			self.Volume = self.Volumetypes[0]

			info = [
			['Stock :',self.Stock],
			['Harga :',self.Harga]
			]
			
			rows,columns = len(info),len(info[0])
			for row in range(rows):
				for column in range(columns):

					self.table_info[row][column].configure(text=info[row][column])
			self.feature_new = ['Update','Delete Brand','Delete Size','Add New']
			if self.Nums_Volume == 0 :
				self.right_footer.destroy()
				self.create_right_footer()

				self.Volume_choose = ttk.Combobox(self.detail_header,width=4,text=('Arial',20))
				self.Volume_choose['values']= self.Volumetypes
				self.Volume_choose.current(0)
				self.Volume_choose.pack(fill='x')
				self.Nums_Volume += 1
			else:
				self.Volume_choose.destroy()
				self.right_footer.destroy()
				self.create_right_footer()
				self.Volume_choose = ttk.Combobox(self.detail_header,width=4,text=('Arial',20))
				self.Volume_choose['values']= self.Volumetypes
				self.Volume_choose.current(0)
				self.Volume_choose.pack(fill='x')			

		else:
			pass

			
	
		self.Volume_choose.bind('<<ComboboxSelected>>',self.ComboCommand)

	#Def Frame

	def create_left_frame(self):
		self.left_frame = tk.Frame(self, bg="pink")
		self.left_frame.grid(row=0, column=0, sticky="nsew")

		self.create_left_content_1()
		self.create_left_content_2()

	def create_right_frame(self):
		self.right_frame = tk.Frame(self, bg="white", width=2*self.settings.width//3)
		self.right_frame.grid(row=0, column=1, sticky="nsew")

		self.create_right_header()
		self.create_right_content()
		#self.create_right_footer()

	def config_left_and_right_frame(self):
		self.grid_columnconfigure(0, weight=1) # 1/3
		self.grid_columnconfigure(1, weight=2) # 2/3
		self.grid_rowconfigure(0, weight=1)
		
	def create_left_content_1(self):
		frame_w = self.settings.width//3
		frame_h = self.settings.height//2

		self.product_type = []

		self.search_box_frame = tk.Frame(self.left_frame, bg="black", width=frame_w, height=frame_h//4)
		self.search_box_frame.pack(fill="x")

		self.left_header = tk.Frame(self.left_frame, width=frame_w, height=frame_h,bg='white')
		self.left_header.pack(fill='both')

		self.List_1_box = tk.Listbox(self.left_header, font=("Arial", 15),bd=0)
		self.List_1_box.pack(expand=True,side='left',fill='both')

		for all_products in self.settings.data:
			for all_product in all_products:
				self.List_1_box.insert('end',all_product)
				self.product_type.append(all_product)

		self.Box_1_scroll = tk.Scrollbar(self.left_header)
		self.Box_1_scroll.pack(side="right", fill="y")

		self.var_name = tk.StringVar()
		self.entry_search = tk.Entry(self.search_box_frame, bg="black", fg="white", font=("Arial", 12),textvariable=self.var_name,width=40)
		self.entry_search.grid(row=0, column=0)

		self.button_search = tk.Button(self.search_box_frame, bg="black", fg="white", text="Find", font=("Arial", 12),command=self.Find_Types)
		self.button_search.grid(row=0, column=1)

		self.List_1_box.configure(yscrollcommand=self.Box_1_scroll.set) # set di Scroll
		self.Box_1_scroll.configure(command=self.List_1_box.yview) # yview di Listbox
		if self.settings.data != []:
			self.List_1_box.bind('<<ListboxSelect>>',self.get)
		
		self.search_box_frame.grid_columnconfigure(0, weight=3)
		self.search_box_frame.grid_columnconfigure(1, weight=1)

	def create_left_content_2(self):
		frame_w = self.settings.width//3
		frame_h = self.settings.height//2

		self.search_box_frame_2 = tk.Frame(self.left_frame,width=frame_w,height=frame_h//4,bg='black')
		self.search_box_frame_2.pack(fill='x')

		self.var_name_2 = tk.StringVar()
		self.entry_search_2 = tk.Entry(self.search_box_frame_2, bg="black", fg="white", font=("Arial", 12),textvariable=self.var_name_2,width=40)
		self.entry_search_2.grid(row=0, column=0)

		self.button_search_2 = tk.Button(self.search_box_frame_2, bg="black", fg="white", text="Find", font=("Arial", 12))
		self.button_search_2.grid(row=0, column=1)

		self.left_content = tk.Frame(self.left_frame,width=frame_w,height=frame_h,bg='white')
		self.left_content.pack(fill='both')

		self.List_2_box = tk.Listbox(self.left_content,font=('Arial',12),height=frame_h//20+20)
		self.List_2_box.pack(fill='both',side='left',expand=True)

		self.Box_2_scroll = tk.Scrollbar(self.left_content)
		self.Box_2_scroll.pack(side='right',fill='both')

		self.search_box_frame_2.grid_rowconfigure(0,weight=2)
		self.search_box_frame_2.grid_columnconfigure(0,weight=3)

		self.List_2_box.configure(yscrollcommand=self.Box_2_scroll.set)
		self.Box_2_scroll.configure(command= self.List_2_box.yview)


	def create_right_header(self):
		frame_w = 2*self.settings.width//3
		frame_h = self.settings.height//5

		self.right_header = tk.Frame(self.right_frame, width=frame_w, height=frame_h,bg='white')
		self.right_header.pack(expand=True)

		self.detail_header = tk.Frame(self.right_header,width=frame_w,height=frame_h,bg='white')
		self.detail_header.grid(row=0,column=0,sticky='nsew')

		self.virtual_image = tk.PhotoImage(width=1,height=1)


		self.brand_label = tk.Label(self.detail_header,text=None,font=('Arial',26),width=frame_w,height=frame_h,image=self.virtual_image,compound='c',bg='white')
		self.brand_label.pack(fill='x')

		self.right_header.grid_rowconfigure(0,weight=1)
		self.right_header.grid_columnconfigure(0,weight=1)	

	def create_right_content(self):
		frame_w = 2*self.settings.width//3
		frame_h = 4*self.settings.height//7
		self.right_content = tk.Frame(self.right_frame, width=frame_w, height=frame_h, bg="white")
		self.right_content.pack(expand=True,pady=100)

		self.detail_content = tk.Frame(self.right_content,width = frame_w,height=frame_h,bg='white')
		self.detail_content.grid(row=0,column=0)

		self.table_info = []
		rows,columns = 2,2
		for row in range(rows):
			aRow = []
			for column in range(columns):
				label = tk.Label(self.detail_content,text = None,font=('Arial',22),bg='white')
				aRow.append(label)
				if column == 0:
					sticky='e'
				else:
					sticky = 'w'
				label.grid(row=row,column=column,sticky=sticky)

			self.table_info.append(aRow)

		self.right_content.grid_rowconfigure(0,weight=1)
		self.right_content.grid_columnconfigure(0,weight=1)

	def create_right_footer(self):
		frame_w = 2*self.settings.width//3
		frame_h = (4*self.settings.height//5)//4

		self.right_footer = tk.Frame(self.right_frame, width=frame_w, height=frame_h, bg="white")
		self.right_footer.pack(expand=True)

		self.detail_footer = tk.Frame(self.right_footer,width=frame_w, height=frame_h, bg="white")
		self.detail_footer.grid(row=0,column=0)

		if self.feature_new != None:
			self.features = self.feature_new

		self.button_features = []
		for feature in self.features:
			if self.Volumetypes != ['']: 
				if self.features.index(feature) == 0:
					if feature == 'Update':
						command = self.Update_page
					else:
						command = self.Delete_Types
				elif self.features.index(feature) == 2:
					command = self.Delete_Size
			else:
				if self.features.index(feature) == 0:
					command = None
				elif self.features.index(feature) == 2:
					command = None

			if self.features.index(feature) == 1:
				if feature == 'Delete Brand' :
					command = self.Delete_Brand
				else:
					command = self.Create_add_frame

			elif self.features.index(feature) == 3:
				command = self.Create_add_frame

			button = tk.Button(self.detail_footer,text = feature,bg='white',bd=0,fg='black',font=('Arial',12,'bold'),command=command)
			button.grid(row=0,column=self.features.index(feature),sticky='nsew',padx=5)
			self.button_features.append([button])



		self.right_footer.grid_rowconfigure(0,weight=1)
		self.right_footer.grid_columnconfigure(0,weight=1)

	def create_Update_header(self):
		frame_w = 2*self.settings.width//3
		frame_h = self.settings.height//5
		self.var_2 = []

		self.right_header = tk.Frame(self.right_update_frame, width=frame_w, height=frame_h,bg='white')
		self.right_header.pack(expand=True)

		self.detail_update_header = tk.Frame(self.right_header,width=frame_w,height=frame_h,bg='white')
		self.detail_update_header.grid(row=0,column=0,sticky='nsew')

		self.Volume_word_Debugging(self.Volume)

		
		brand_var = tk.StringVar()
		self.Brand_Name_Label = tk.Entry(self.detail_update_header,font=('Arial',22,),bg='white',bd=0,width=10 ,textvariable=brand_var)
		self.Brand_Name_Label.insert('end',self.Brand)
		self.Brand_Name_Label.grid(row=0,column=0,sticky='nsew')	
	
		
		volume_var = tk.StringVar()
		self.Volume_Types_Label = tk.Entry(self.detail_update_header,font=('Arial',22),bg='white',bd=0,width=3,textvariable=volume_var)
		self.Volume_Types_Label.insert('end',self.VolumeNumber)
		self.Volume_Types_Label.grid(row=1,column=0,sticky='nsew')

		self.Volumetypes_Combo = ttk.Combobox(self.detail_update_header,height=1)
	
		Satuan_list = ['Cm','M','L','mL']

		for all_satuan in Satuan_list:
			if self.SatuanWord == all_satuan:
				index_Satuan = Satuan_list.index(all_satuan)
		

		self.Volumetypes_Combo['values'] = Satuan_list
		self.Volumetypes_Combo.current(index_Satuan)
		self.Volumetypes_Combo.grid(row=1,column=1,sticky='nsew')	


		self.var_2.append([volume_var])
		self.var_2.append([brand_var])


		self.right_header.grid_rowconfigure(0,weight=1)
		self.right_header.grid_columnconfigure(0,weight=1)	

	def create_Update_content(self):
		frame_w = 2*self.settings.width//3
		frame_h = 4*self.settings.height//7
		self.right_update_content = tk.Frame(self.right_update_frame, width=frame_w, height=frame_h, bg="white")
		self.right_update_content.pack(expand=True,pady=100)

		self.detail_update_content = tk.Frame(self.right_update_content,width = frame_w,height=frame_h,bg='white')
		self.detail_update_content.grid(row=0,column=0)

		self.update_table_info = []
		self.var=[]


		info = [
		['Stock :',self.Stock],
		['Harga :',self.Harga]
		]

		rows,columns = len(info),len(info[0])

		for row in range(rows):
			aRow = []
			var = []
			for column in range(columns):
			
				if column == 0:
					Entry = tk.Label(self.detail_update_content,text =info[row][column],font=('Arial',22),bg='white',image=self.virtual_image,compound='c')
					aRow.append(Entry)
					sticky='e'
				else:
					var_entry = tk.StringVar()
					Entry = tk.Entry(self.detail_update_content,font=('Arial',22),bg='white',bd=0,width=13,textvariable = var_entry)
					Entry.insert('end',info[row][column])
					aRow.append(Entry)
					var.append(var_entry)
					sticky = 'w'
				Entry.grid(row=row,column=column,sticky=sticky)
			self.update_table_info.append(aRow)
			self.var.append(var)

		features = [['+',"-"],
					['+',"-"]]

		rows,columns = len(features),len(info[0])

		for row in range(rows):
			for column in range(columns):	
				if row == 0:	
					button = tk.Button(self.detail_update_content ,text = features[row][column],bg='white',bd=0,fg='black',font=('Arial',12,'bold'))
					if column == 0:
						button.configure(command=lambda:self.Plus_Number(column,0))
					else:
						button.configure(command=lambda:self.Minus_Number(column,0))
					button.grid(row=row,column=column+2)
				elif row >= 1:	
					button_2 = tk.Button(self.detail_update_content ,text = features[row][column],bg='white',bd=0,fg='black',font=('Arial',12,'bold'))
					if column == 0:
						button_2.configure(command=lambda:self.Plus_Number(column,1))
					else:
						button_2.configure(command=lambda:self.Minus_Number(column,1))
					button_2.grid(row=row,column=column+2)


			
		for all_var in self.var_2:
			self.var.append(all_var)


		self.right_update_content.grid_rowconfigure(0,weight=1)
		self.right_update_content.grid_columnconfigure(0,weight=1)

	def create_Update_footer(self):
		frame_w = 2*self.settings.width//3
		frame_h = (4*self.settings.height//5)//4

		self.right_update_footer = tk.Frame(self.right_update_frame, width=frame_w, height=frame_h, bg="white")
		self.right_update_footer.pack(expand=True)

		self.detail_update_footer = tk.Frame(self.right_update_footer,width=frame_w, height=frame_h, bg="white")
		self.detail_update_footer.grid(row=0,column=0)

		features = ['Save','Cancel']
		self.button_update_features = []
		for feature in features:
			button = tk.Button(self.detail_update_footer ,text = feature,bg='white',bd=0,fg='black',font=('Arial',12,'bold'))
			if features.index(feature) == 0:
				button.configure(command=self.Update_Data)
			else:
				button.configure(command=self.refresh_frame)


			button.grid(row=0,column=features.index(feature),sticky='nsew',padx=5)
			self.button_update_features.append(button)

		self.right_update_footer.grid_rowconfigure(0,weight=1)
		self.right_update_footer.grid_columnconfigure(0,weight=1)

	def create_Add_header(self):
		frame_w = 2*self.settings.width//3
		frame_h = self.settings.height//5
		self.var_2 = []
		self.Combobox_list = []
		self.Label_add_list = [] 

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
				button.configure(command=self.refresh_frame)


			button.grid(row=0,column=features.index(feature),sticky='nsew',padx=5)
			self.button_add_features.append(button)

		self.right_add_footer.grid_rowconfigure(0,weight=1)
		self.right_add_footer.grid_columnconfigure(0,weight=1)


