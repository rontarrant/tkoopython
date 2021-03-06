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
		state_label = StateLabel(self)
		hello_button = HelloButton(self, state_label)
		activator_button = ActivatorButton(self, hello_button)
		# layout
		state_label.grid(row = 0, column = 0, padx = 10, pady = 10, columnspan = 2)
		hello_button.grid(row = 1, column = 0, padx = 10, pady = 10)
		activator_button.grid(row = 1, column = 1, padx = 10, pady = 10)

class StateLabel(ttk.Label):	
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.enabled_text = "Hello Button is enabled"
		self.disabled_text = "Hello Button is disabled"
		self.hello_message = "Hello, World!"
		self.changeable = StringVar()
		self.changeable.set(self.enabled_text)
		# configure
		self.config(textvariable = self.changeable)

	def set_disabled(self):
		self.changeable.set(self.disabled_text)
	
	def set_enabled(self):
		self.changeable.set(self.enabled_text)
	
	def set_hello(self):
		self.changeable.set(self.hello_message)
		
class ActivatorButton(ttk.Button):
	def __init__(self, parent, button):
		super().__init__(parent)
		# object attributes
		self.text = StringVar()
		self.deactivate_text = "Deactivate Hello Button"
		self.activate_text = "Activate Hello Button"
		# configure
		self.text.set(self.deactivate_text)
		self.config(textvariable = self.text)
		self.config(text = self.text, command = lambda:self.switch_state(button))
	
	def switch_state(self, button):
		button.toggle_button_state() # activate/deactivate the HelloButton
		
		if self.text.get() == self.deactivate_text: # switch ActivatorButton text
			self.text.set(self.activate_text)
		else:
			self.text.set(self.deactivate_text) 

class HelloButton(ttk.Button):
	def __init__(self, parent, label):
		super().__init__(parent)
		# object attributes
		self.text = "Say Hello"
		self.label = label
		# configure
		self.config(text = self.text, command = self.say_hello)

	def say_hello(self):
		self.label.set_hello()

	def toggle_button_state(self):
		if self.instate(['!disabled']) == True:
			self.label.set_disabled()
			self.state(['disabled'])
		else:
			self.state(['!disabled'])
			self.label.set_enabled()

if __name__ == "__main__":
	main()

'''
WIDGET STATES
The widget state is a bitmap of independent state flags. All widgets have the same state flags, but not all flags are meaningful for all widgets. Widget state flags include:

active - The mouse cursor is over the widget and pressing a mouse button will cause some action to occur. (aka ???prelight??? (Gnome), ???hot??? (Windows), ???hover???).

disabled - Widget is disabled under program control (aka ???unavailable???, ???inactive???).

focus - Widget has keyboard focus.

pressed - Widget is being pressed (aka ???armed??? in Motif).

selected - ???On???, ???true???, or ???current??? for things like checkbuttons and radiobuttons.

background - Windows and the Mac have a notion of an ???active??? or foreground window. The background state is set for widgets in a background window, and cleared for those in the foreground window.

readonly - Widget should not allow user modification.

alternate - A widget-specific alternate display format. For example, used for checkbuttons and radiobuttons in the ???tristate??? or ???mixed??? state, and for buttons with -default active.

invalid - The widget's value is invalid. (Potential uses: scale widget value out of bounds, entry widget value failed validation.)

hover - The mouse cursor is within the widget. This is similar to the active state; it is used in some themes for widgets that provide distinct visual feedback for the active widget in addition to the active element within the widget.

A state specification or stateSpec is a list of state names, optionally prefixed with an exclamation point (!) indicating that the bit is off. 
'''