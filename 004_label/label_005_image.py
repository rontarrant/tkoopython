from tkinter import *
from tkinter import ttk
from relative import RelativePath

def main():
	window = Window()
	window.mainloop()
	
class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title_text = "Label with Colour"
		self.width = 270
		self.height = 270
		# configure
		self.config(width = self.width, height = self.height)
		self.title(self.title_text)
		self.grid_propagate(False) # without this, window size is ignored
		# populate
		mainframe = MainFrame(self)
		# centering
		mainframe.grid(column = 0, row = 0)
		mainframe.update()
		xbias = (self.winfo_width() - mainframe.winfo_width()) / 2
		mainframe.grid(padx = xbias)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.grid()
		# populate
		hello_label = ImageLabel(self)
		# layout
		hello_label.grid(column = 0, row = 0)

class ImageLabel(ttk.Label):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		self.text = "A Label with an Image"
		self.image = RelativePath.get_image_path('./images/head.png')
		# configure
		self.grid(column = 0, row = 0)
		self.rowconfigure(0, weight = 1)
		self.columnconfigure(0, weight = 1)
		self.config(padding = "20 10 20 20")
		self.config(image = self.image)


if __name__ == "__main__":
	main()
