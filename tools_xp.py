from tkinter import *
import tkinter.ttk as ttk

# Full Screen Window
def cwindow(titlename, content_frame, display_frame):
	"""
	titlename (str): Specifiy title name 
	content_frame (tk.Frame): Specify frame to show on the display_frame
	display_frame (tk.Frame): Root body

	# CONCEPT #
	create a main window, to run the toolbar (which is the exit_btn, 
	and toolbartext) and to use the rest of the screen to run the app, 
	coded in the main file.

	"""

	display_frame.pack(padx=37, pady=37, fill='both', expand=1)

	# Toolbar
	toolbar = Frame(display_frame, bg='#2259E1', bd=0)
	toolbar.pack(side='top', fill='x')
		
	# Exit button
	exit_btn = Button(toolbar, bd=0, text=' ✕ ', fg='white', bg='#FF4900', font=("ubuntu", 10), activebackground='#FF4900', activeforeground='white', command=lambda:display_frame.pack_forget())
	exit_btn.pack(side='right')

	# Toolbar text
	toolbartext = Label(toolbar, bd=0, text=titlename, font=('ubuntu', 12), bg='#2259E1', fg='white')
	toolbartext.pack(ipady=1)

	# Frame
	content_frame.pack(fill='both', expand=1)

# Window custom size
def dwindow(titlename, content_frame, display_frame):
	"""
	titlename (str): Specifiy title name 
	content_frame (tk.Frame): Specify frame to show on the display_frame
	display_frame (tk.Frame): Root body

	# CONCEPT #
	create a main window, to run the toolbar (which is the exit_btn, 
	and toolbartext) and to use the rest of the screen to run the app, 
	coded in the main file.

	"""

	display_frame.pack(padx=37, pady=37)
	
	# Toolbar
	toolbar = Frame(display_frame, bg='#2259E1', bd=0)
	toolbar.pack(side='top', fill='x')
		
	# Exit button
	exit_btn = Button(toolbar, bd=0, text=' ✕ ', fg='white', bg='#FF4900', font=("ubuntu", 10), activebackground='#FF4900', activeforeground='white', command=lambda:display_frame.pack_forget())
	exit_btn.pack(side='right')

	# Toolbar text
	toolbartext = Label(toolbar, bd=0, text=titlename, font=('ubuntu', 12), bg='#2259E1', fg='white')
	toolbartext.pack(ipady=1)

	# Frame
	content_frame.pack(fill='both', expand=1)

#HELLOWORLD
# Window custom size
def messagebox_info(titlename, info, root):
	"""
	titlename (str): Specifiy title name 
	info (tk.Frame): Root body

	# CONCEPT #
	create a messagebox

	"""

	newframe = Frame(root)
	
	# Toolbar
	toolbar = Frame(newframe, bg='#2259E1', bd=0)
	toolbar.pack(side='top', fill='x')

	# Toolbar text
	toolbartext = Label(toolbar, bd=0, text=titlename, font=('ubuntu', 12), bg='#2259E1', fg='white')
	toolbartext.pack(ipady=1, ipadx=5, pady=3)

	newframe.place(relx=0.5, rely=0.5, anchor=CENTER)
	
	# Info label
	info_label = Label(newframe, text=info, font=("ubuntu", 11))
	info_label.pack(side='top')

	# Ok button
	ok_btn = ttk.Button(newframe, text='Ok')
	ok_btn.pack(side='bottom', anchor='e', pady=3, padx=3)

	def amongus(event):
		newframe.destroy()

	ok_btn.bind('<Button-1>', amongus)

# Messagebox error
def messagebox_error(titlename, info, root):
	"""
	titlename (str): Specifiy title name 
	info (tk.Frame): Root body

	# CONCEPT #
	create a messagebox

	"""

	newframe = Frame(root)
	
	# Toolbar
	toolbar = Frame(newframe, bg='#d64b4b', bd=0)
	toolbar.pack(side='top', fill='x')

	# Toolbar text
	toolbartext = Label(toolbar, bd=0, text=titlename, font=('ubuntu', 12), bg='#d64b4b', fg='white')
	toolbartext.pack(ipady=1, ipadx=5, pady=3)

	newframe.place(relx=0.5, rely=0.5, anchor=CENTER)
	
	# Info label
	info_label = Label(newframe, text=info, font=("ubuntu", 11))
	info_label.pack(side='top')

	# Ok button
	def amongus():
		newframe.destroy()

	ok_btn = ttk.Button(newframe, text='Ok', command=amongus)
	ok_btn.pack(side='bottom', anchor='e', pady=3, padx=3)

# Messagebox error
def messagebox_warning(titlename, info, root):
	"""
	titlename (str): Specifiy title name 
	info (tk.Frame): Root body

	# CONCEPT #
	create a messagebox

	"""

	newframe = Frame(root)
	
	# Toolbar
	toolbar = Frame(newframe, bg='#FF7901', bd=0)
	toolbar.pack(side='top', fill='x')

	# Toolbar text
	toolbartext = Label(toolbar, bd=0, text=titlename, font=('ubuntu', 12), bg='#FF7901', fg='black')
	toolbartext.pack(ipady=1, ipadx=5, pady=3)

	newframe.place(relx=0.5, rely=0.5, anchor=CENTER)
	
	# Info label
	info_label = Label(newframe, text=info, font=("ubuntu", 11))
	info_label.pack(side='top')

	# Ok button
	def amongus():
		newframe.destroy()

	ok_btn = ttk.Button(newframe, text='Ok', command=amongus)
	ok_btn.pack(side='bottom', anchor='e', pady=3, padx=3)