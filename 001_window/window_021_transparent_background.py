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
		self.title("Transparent Window Background")
		# configure
		self.config(bg = 'grey')
		self.wm_attributes('-transparentcolor', 'grey')
		# populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.config(padding = "20 10 20 20")
		self.grid(column = 0, row = 0, sticky = (N, W, E, S))
		# populate
		message_label = MessageLabel(self)
		# layout
		message_label.grid(column = 0, row = 0)

class MessageLabel(ttk.Label):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.text = "The alpha channel of the image is transparent."
		self.width = len(self.text) # width is in characters
		self.photo = RelativePath.get_image_path("images/example.png")
		# configure
		self.config(text = self.text, image = self.photo, compound = 'bottom', width = self.width)
		self.config(background = parent.master.cget('background'))


if __name__ == "__main__":
	main()
