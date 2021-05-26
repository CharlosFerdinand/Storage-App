from json import load,dump

class Config:
	def __init__(self):
		self.title = "Storage"
		self.data_place = "data_stock.json"

		#WINDOW CONF
		base = 100
		ratio = (9, 6)
		self.width = base*ratio[0]
		self.height = base*ratio[1]
		self.screen = f"{self.width}x{self.height}+500+500"
		self.Read_data()

	def Read_data(self):
		with open(self.data_place,'r') as data_place:
			self.data = load(data_place)

	def Write_Data(self):	
		with open(self.data_place,'w') as data_place:
			dump(self.data,data_place)