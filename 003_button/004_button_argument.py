from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title("Dynamic 'Hello' Button")
		# populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.grid(column = 0, row = 0, sticky = (N, W, E, S))
		self.config(padding = "10 5 10 20")
		# populate
		hello_label = HelloLabel(self)
		hello_button = HelloButton(self, hello_label)
		goodbye_button = GoodbyeButton(self, hello_label)
		# layout
		hello_label.grid(row = 0, column = 0, padx = 10, pady = 10, columnspan = 2)
		hello_button.grid(row = 1, column = 0, padx = 10, pady = 10)
		goodbye_button.grid(row = 1, column = 1, padx = 10, pady = 10)

class HelloLabel(ttk.Label):	
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.original_text = "Pick Your Choose"
		self.changeable = StringVar()
		self.changeable.set(self.original_text)
		# configure
		self.config(textvariable = self.changeable)

class GoodbyeButton(ttk.Button):
	def __init__(self, parent, label):
		super().__init__(parent)
		# object attributes
		self.text = "Say Good-bye"
		self.message = "Goodbye, World!\n (Closing in 2 seconds)"
		self.delay = 2000 # 1000 = 1 second
		self.window = self.winfo_toplevel() # access the top-level window from anywhere
		# configure
		self.config(text = self.text, command = lambda:self.say_goodbye(label))
	
	def say_goodbye(self, label):
		label.configure(text = self.message)

		if label.changeable.get() == label.original_text:
			label.changeable.set("You have to say, 'hello' first.")
			label.config(text = label.changeable.get())
		else:
			label.changeable.set(self.message)
			self.window.after(self.delay, self.window.destroy)

class HelloButton(ttk.Button):
	def __init__(self, parent, label):
		super().__init__(parent)
		# object attributes
		self.text = "Say Hello"
		self.message = "Hello, World!"
		self.label = label
		# configure
		self.config(text = self.text, command = self.say_hello)

	def say_hello(self):
		self.label.changeable.set(self.message)

if __name__ == "__main__":
	main()
