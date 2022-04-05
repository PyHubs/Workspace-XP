# -*- coding: utf-8 -*-
from tkinter import *
import tkinter as tk
from tkinter import ttk
from subprocess import *
from tkcalendar import *
import tkinter.ttk as ttk
from random import randint
from functools import partial
from PIL import ImageTk, Image
from tkinter import filedialog, messagebox, colorchooser
import os, center_tk_window, sys, pygame, webbrowser, time, psutil, pyttsx3, random
from tools_xp import cwindow, dwindow, messagebox_info, messagebox_error, messagebox_warning

# Main Window
root = Tk()
root.title("Workspace XP")
root.geometry("1020x500")
root.config(bg='lightblue')
root.iconbitmap("Icons\\logo.ico")

# Ex full screen
def exit_view(viewbtn):
	root.attributes('-fullscreen', False)	
	viewbtn.config(command=lambda:full_view(viewbtn), text='FullScreen')

# Full screen
def full_view(viewbtn):
	root.attributes('-fullscreen', True)
	viewbtn.config(command=lambda:exit_view(viewbtn), text='Exit FullScreen')

# Exit program
def workspace_exit():
	root.destroy()

# Exit start menu
def startoof(start_frame):
	start_frame.pack_forget()
	start.config(comman=startmenu)

# About text
about_txt = """\nIPP Workspace XP

	Version XP (Build XP-DEV-112721D)
	IPP Workspace ® Codename ® eXPerience

	2021/2022 Izkaan Python Productions. 
	Please give me credit. Else i will get sad, and email you a virus

	# -- NEW FEATURES -- #
	- Re-written kernal
	- New GUI (hope you all xp fans are happy)
	- Text Editor XP
	- Calculator
	- Rock Paper Scissors (With AI)

	If this gets traction, i will allow 3rd party softwares easy developement :)
"""

# Exit about_workspace
def about_exit():
	about_win.pack_forget()

def tedit_exit():
	tedit_win.pack_forget()

# eee
def tmrf():
	# Return a frame window
	tmrw = Frame(bd=0, bg='#0C0C0C')
	tmrw.pack(padx=50, pady=37)

	# Toolbar
	toolbar = Frame(tmrw, bg='#2259E1', bd=0)
	toolbar.pack(side='top', fill='x')

	# Exit button
	exit_btn = Button(toolbar, bd=0, text=' ✕ ', fg='white', bg='#FF4900', font=("ubuntu", 10), activebackground='#FF4900', activeforeground='white', command=lambda:tmrw.pack_forget())
	exit_btn.pack(side='right')

	# Toolbar text
	toolbartext = Label(toolbar, bd=0, text='Rock Paper Scissors', font=('ubuntu', 12), bg='#2259E1', fg='white')
	toolbartext.pack(ipady=1)

	# Sidebar one
	cframe = Frame(tmrw, bg='#323232')
	cframe.pack(side='top', fill='x')

	rock_ =1
	paper_ = 2
	scissor_ = 3

	def rpc(opt):
		print(opt)
		AI = random.randint(1, 3)

		if opt == 1 and AI == 1:
			iid.config(text='Rock + Rock = TIE', bg='lightgrey')
		elif opt == 1 and AI == 2:
			iid.config(text='Rock + Paper = You Win', bg='green')
		elif opt == 1 and AI == 3:
			iid.config(text='Rock + Scissor = You Win', bg='green')

		if opt == 2 and AI == 1:
			iid.config(text='Paper + Rock = AI Wins', bg='red')
		elif opt == 2 and AI == 2:
			iid.config(text='Paper + Paper = TIE', bg='lightgrey')
		elif opt == 3 and AI == 3:
			iid.config(text='Paper + Scissor = AI Wins', bg='red')

		if opt == 3 and AI == 1:
			iid.config(text='Scissor + Rock = AI Wins', bg='red')
		elif opt == 3 and AI == 2:
			iid.config(text='Scissor + Paper = You Win', bg='green')
		elif opt == 3 and AI == 3:
			iid.config(text='Scissor + Scissor = TIE', bg='lightgrey')

	rock = Button(cframe, bg='#323232', text='  ROCK  ', activeforeground='lightgrey', bd=0, font=('ubuntu', 14), fg='white', activebackground='#323232', command=lambda: rpc(rock_))
	rock.grid(row=0, column=0)

	paper = Button(cframe, bg='#323232', text='  PAPER  ', activeforeground='lightgrey', bd=0, font=('ubuntu', 14), fg='white', activebackground='#323232', command=lambda: rpc(paper_))
	paper.grid(row=0, column=1)

	scissor = Button(cframe, bg='#323232', text='  SCISSOR  ', activeforeground='lightgrey', bd=0, font=('ubuntu', 14), fg='white', activebackground='#323232', command=lambda: rpc(scissor_))
	scissor.grid(row=0, column=2)

	iid = Label(tmrw, bg='#323232', fg='white', text='', font=('ubuntu', 14))
	iid.pack(fill='x')

# Tic tac toe (....)
def ttc():
	global clicked, count
	mwind = Frame(bd=0)
	window = Frame(mwind, bd=0)

	# X starts so true
	clicked = True
	count = 0

	def Reset():
		global b1, b2, b3, b4, b5, b6, b7, b8, b9
		global clicked, count
		clicked = True
		count = 0

		#confuring a bg
		b1.configure(text=" ", bg="#4EC050", borderwidth=0, state="normal")
		b2.configure(text=" ", bg="#4EC050", borderwidth=0, state="normal")
		b3.configure(text=" ", bg="#4EC050", borderwidth=0, state="normal")
		b4.configure(text=" ", bg="#4EC050", borderwidth=0, state="normal")
		b5.configure(text=" ", bg="#4EC050", borderwidth=0, state="normal")
		b6.configure(text=" ", bg="#4EC050", borderwidth=0, state="normal")
		b7.configure(text=" ", bg="#4EC050", borderwidth=0, state="normal")
		b8.configure(text=" ", bg="#4EC050", borderwidth=0, state="normal")
		b9.configure(text=" ", bg="#4EC050", borderwidth=0, state="normal")


	def disable_all_buttons():
		b1.config(state=DISABLED)
		b2.config(state=DISABLED)
		b3.config(state=DISABLED)
		b4.config(state=DISABLED)
		b5.config(state=DISABLED)
		b6.config(state=DISABLED)
		b7.config(state=DISABLED)
		b8.config(state=DISABLED)
		b9.config(state=DISABLED)

	#check to see if somone won
	def checkifwon():
		global winner
		winner = False

		if b1['text'] == "X" and b4['text'] == 'X' and b7 ['text'] == 'X':
			b1.config(bg="#87A96B")
			b4.config(bg="#87A96B")
			b7.config(bg="#87A96B")
			winner = True
			messagebox_info("Winner", "    CONGRATULATIONS!, X WINS   ", root)
			disable_all_buttons()

		elif b2['text'] == "X" and b5['text'] == 'X' and b8 ['text'] == 'X':
			b2.config(bg="#87A96B")
			b5.config(bg="#87A96B")
			b8.config(bg="#87A96B")
			winner = True
			messagebox_info("Winner", "    CONGRATULATIONS!, X WINS   ", root)
			disable_all_buttons()

		elif b3['text'] == "X" and b6['text'] == 'X' and b9 ['text'] == 'X':
			b3.config(bg="#87A96B")
			b6.config(bg="#87A96B")
			b9.config(bg="#87A96B")
			winner = True
			messagebox_info("Winner", "    CONGRATULATIONS!, X WINS   ", root)
			disable_all_buttons()

		elif b1['text'] == "X" and b5['text'] == 'X' and b9 ['text'] == 'X':
			b1.config(bg="#87A96B")
			b5.config(bg="#87A96B")
			b9.config(bg="#87A96B")
			winner = True
			messagebox_info("Winner", "    CONGRATULATIONS!, X WINS   ", root)
			disable_all_buttons()

		elif b3['text'] == "X" and b5['text'] == 'X' and b7 ['text'] == 'X':
			b3.config(bg="#87A96B")
			b5.config(bg="#87A96B")
			b7.config(bg="#87A96B")
			winner = True
			messagebox_info("Winner", "    CONGRATULATIONS!, X WINS   ", root)
			disable_all_buttons()

		elif b1['text'] == "X" and b2['text'] == 'X' and b3 ['text'] == 'X':
			b1.config(bg="#87A96B")
			b2.config(bg="#87A96B")
			b3.config(bg="#87A96B")
			winner = True
			messagebox_info("Winner", "    CONGRATULATIONS!, X WINS   ", root)
			disable_all_buttons()

		elif b4['text'] == "X" and b5['text'] == 'X' and b6['text'] == 'X':
			b4.config(bg="#87A96B")
			b5.config(bg="#87A96B")
			b6.config(bg="#87A96B")
			winner = True
			messagebox_info("Winner", "    CONGRATULATIONS!, X WINS   ", root)
			disable_all_buttons()

		elif b7['text'] == "X" and b8['text'] == 'X' and b9['text'] == 'X':
			b7.config(bg="#87A96B")
			b8.config(bg="#87A96B")
			b9.config(bg="#87A96B")
			winner = True
			messagebox_info("Winner", "    CONGRATULATIONS!, X WINS   ", root)
			disable_all_buttons()

		elif b1['text'] == "O" and b4['text'] == 'O' and b7 ['text'] == 'O':
			b1.config(bg="#87A96B")
			b4.config(bg="#87A96B")
			b7.config(bg="#87A96B")
			winner = True
			messagebox_info("Winner", "    CONGRATULATIONS!, O WINS   ", root)
			disable_all_buttons()

		elif b2['text'] == "O" and b5['text'] == 'O' and b8 ['text'] == 'O':
			b2.config(bg="#87A96B")
			b5.config(bg="#87A96B")
			b8.config(bg="#87A96B")
			winner = True
			messagebox_info("Winner", "    CONGRATULATIONS!, O WINS   ", root)
			disable_all_buttons()

		elif b3['text'] == "O" and b6['text'] == 'O' and b9 ['text'] == 'O':
			b3.config(bg="#87A96B")
			b6.config(bg="#87A96B")
			b9.config(bg="#87A96B")
			winner = True
			messagebox_info("Winner", "    CONGRATULATIONS!, O WINS   ", root)
			disable_all_buttons()

		elif b1['text'] == "O" and b5['text'] == 'O' and b9 ['text'] == 'O':
			b1.config(bg="#87A96B")
			b5.config(bg="#87A96B")
			b9.config(bg="#87A96B")
			winner = True
			messagebox_info("Winner", "    CONGRATULATIONS!, O WINS   ", root)
			disable_all_buttons()

		elif b3['text'] == "O" and b5['text'] == 'O' and b7 ['text'] == 'O':
			b3.config(bg="#87A96B")
			b5.config(bg="#87A96B")
			b7.config(bg="#87A96B")
			winner = True
			messagebox_info("Winner", "    CONGRATULATIONS!, O WINS   ", root)
			disable_all_buttons()

		elif b1['text'] == "O" and b2['text'] == 'O' and b3 ['text'] == 'O':
			b1.config(bg="#87A96B")
			b2.config(bg="#87A96B")
			b3.config(bg="#87A96B")
			winner = True
			messagebox_info("Winner", "    CONGRATULATIONS!, O WINS   ", root)
			disable_all_buttons()

		elif b4['text'] == "O" and b5['text'] == 'O' and b6['text'] == 'O':
			b4.config(bg="#87A96B")
			b5.config(bg="#87A96B")
			b6.config(bg="#87A96B")
			winner = True
			messagebox_info("Winner", "    CONGRATULATIONS!, O WINS   ", root)
			disable_all_buttons()

		elif b7['text'] == "O" and b8['text'] == 'O' and b9['text'] == 'O`':
			b7.config(bg="#87A96B")
			b8.config(bg="#87A96B")
			b9.config(bg="#87A96B")
			winner = True
			messagebox_info("Winner", "    CONGRATULATIONS!, O WINS   ", root)
			disable_all_buttons()

		elif count == 9 and winner == False:
				messagebox_info("Winner", "It is a tie!\nno one wins, try starting a new match", root)
				disable_all_buttons()

	def b_click(b):
		global clicked, count

		if b["text"] == " " and clicked == True:
			b["text"] = 'X'
			clicked = False
			count += 1
			checkifwon()
		elif b["text"] == " " and clicked == False:
			b["text"] = 'O'
			clicked = True
			count += 1
			checkifwon()
		else:
			messagebox_error("Error", "That box has already been used. Use another box", root)

	#buttons
	b1= Button(window, text=" ", borderwidth=0, font=("Arial", 20), height=3, width=6, bg="#4EC050",command= lambda: b_click(b1))
	b2= Button(window, text=" ", borderwidth=0, font=("Arial", 20), height=3, width=6, bg="#4EC050",command= lambda: b_click(b2))
	b3= Button(window, text=" ", borderwidth=0, font=("Arial", 20), height=3, width=6, bg="#4EC050",command= lambda: b_click(b3))

	b4= Button(window, text=" ", borderwidth=0, font=("Arial", 20), height=3, width=6, bg="#4EC050",command= lambda: b_click(b4))
	b5= Button(window, text=" ", borderwidth=0, font=("Arial", 20), height=3, width=6, bg="#4EC050",command= lambda: b_click(b5))
	b6= Button(window, text=" ", borderwidth=0, font=("Arial", 20), height=3, width=6, bg="#4EC050",command= lambda: b_click(b6))

	b7= Button(window, text=" ", borderwidth=0, font=("Arial", 20), height=3, width=6, bg="#4EC050",command= lambda: b_click(b7))
	b8= Button(window, text=" ", borderwidth=0, font=("Arial", 20), height=3, width=6, bg="#4EC050",command= lambda: b_click(b8))
	b9= Button(window, text=" ", borderwidth=0, font=("Arial", 20), height=3, width=6, bg="#4EC050",command= lambda: b_click(b9))

	def about_command():
		messagebox_info("About", 'tic tac toe is a simple tic tac toe game made by izkaan and dad python productions®', root)

	def show_help_command():
		messagebox_info('Help', "Mail izooizkaan@gmail.com for help", root)

	#grid buttons
	b1.grid(row=0, column=0)
	b2.grid(row=0, column=1)
	b3.grid(row=0, column=2)

	b4.grid(row=1, column=0)
	b5.grid(row=1, column=1)
	b6.grid(row=1, column=2)

	b7.grid(row=2, column=0)
	b8.grid(row=2, column=1)
	b9.grid(row=2, column=2)

	#confuring a bg
	b1.configure(bg="#4EC050", fg='white', borderwidth=0, activebackground='#4EC050', activeforeground='red')
	b2.configure(bg="#4EC050", fg='white', borderwidth=0, activebackground='#4EC050', activeforeground='red')
	b3.configure(bg="#4EC050", fg='white', borderwidth=0, activebackground='#4EC050', activeforeground='red')
	b4.configure(bg="#4EC050", fg='white', borderwidth=0, activebackground='#4EC050', activeforeground='red')
	b5.configure(bg="#4EC050", fg='white', borderwidth=0, activebackground='#4EC050', activeforeground='red')
	b6.configure(bg="#4EC050", fg='white', borderwidth=0, activebackground='#4EC050', activeforeground='red')
	b7.configure(bg="#4EC050", fg='white', borderwidth=0, activebackground='#4EC050', activeforeground='red')
	b8.configure(bg="#4EC050", fg='white', borderwidth=0, activebackground='#4EC050', activeforeground='red')
	b9.configure(bg="#4EC050", fg='white', borderwidth=0, activebackground='#4EC050', activeforeground='red')

	dwindow("Tic Tac Toe", window, mwind)
	"""
	"""
	
# Calculator
def calcs():
	global num
	ws = Frame(bd=0, bg='#585953')
	dowin = Frame(ws, bd=0, bg='#585953')
	
	dwindow(" Calculator (3rd party software) ", dowin, ws)

	# global variables
	num = ''

	# functions
	def display(number):
		global num 
		num = num + str(number)
		scr_lbl['text'] = num
		

	def clear_scr():
		global num
		num = ''
		scr_lbl['text'] = num


	def equal_btn():
		global num
		add=str(eval(num))
		scr_lbl['text'] = add
		num=''
	def equal_btn():
		global num
		sub=str(eval(num))
		scr_lbl['text'] = sub
		num=''     
	def equal_btn():
		global num
		mul=str(eval(num))
		scr_lbl['text'] = mul
		num=''
	def equal_btn():
		global num
		div=str(eval(num))
		scr_lbl['text'] = div
		num=''    

	var = StringVar()

	# frames 
	frame_1 = Frame(ws) 
	frame_1.pack(expand=True, fill=BOTH)

	frame_2 = Frame(ws)
	frame_2.pack(expand=True, fill=BOTH)

	frame_3 = Frame(ws)
	frame_3.pack(expand=True, fill=BOTH)

	frame_4 = Frame(ws)
	frame_4.pack(expand=True, fill=BOTH)

	# label
	scr_lbl = Label(
		frame_1,
		textvariable='',
		font=('Arial', 20),
		anchor = SE,
		bg = '#595954',
		fg = 'white' 
		)

	scr_lbl.pack(expand=True, fill=BOTH)

	# buttons
	key_1 = Button(
		frame_1,
		text='1',
		font=('Arial', 22),
		border = 0,
		relief = GROOVE,
		bg = '#2E2E2B',
		fg = 'white',
		command = lambda: display(1)
		)

	key_1.pack(expand=True, fill=BOTH, side=LEFT)

	key_2 = Button(
		frame_1,
		text='2',
		font=('Arial', 22),
		border = 0,
		relief = GROOVE,
		bg = '#2E2E2B',
		fg = 'white',
		command = lambda: display(2)
		)

	key_2.pack(expand=True, fill=BOTH, side=LEFT)

	key_3 = Button(
		frame_1,
		text='3',
		font=('Arial', 22),
		border = 0,
		relief = GROOVE,
		bg = '#2E2E2B',
		fg = 'white',
		command = lambda: display(3)
		)

	key_3.pack(expand=True, fill=BOTH, side=LEFT)

	key_add = Button(
		frame_1,
		text='+',
		font=('Arial', 22),
		border = 0,
		relief = GROOVE,
		bg = '#2E2E2B',
		fg = 'white',
		command = lambda: display('+')
		)

	key_add.pack(expand=True, fill=BOTH, side=LEFT)

	key_4 = Button(
		frame_2,
		text='4',
		font=('Arial', 22),
		border = 0,
		relief = GROOVE,
		bg = '#2E2E2B',
		fg = 'white',
		command = lambda: display(4)
		)

	key_4.pack(expand=True, fill=BOTH, side=LEFT)

	key_5 = Button(
		frame_2,
		text='5',
		font=('Arial', 22),
		border = 0,
		relief = GROOVE,
		bg = '#2E2E2B',
		fg = 'white',
		command = lambda: display(5)
		)

	key_5.pack(expand=True, fill=BOTH, side=LEFT)

	key_6 = Button(
		frame_2,
		text='6',
		font=('Arial', 22),
		border = 0,
		relief = GROOVE,
		bg = '#2E2E2B',
		fg = 'white',
		command = lambda: display(6)
		)

	key_6.pack(expand=True, fill=BOTH, side=LEFT)

	key_sub = Button(
		frame_2,
		text='-',
		font=('Arial', 22),
		border = 0,
		relief = GROOVE,
		bg = '#2E2E2B',
		fg = 'white',
		command = lambda: display('-')
		)

	key_sub.pack(expand=True, fill=BOTH, side=LEFT)

	key_7 = Button(
		frame_3,
		text='7',
		font=('Arial', 22),
		border = 0,
		relief = GROOVE,
		bg = '#2E2E2B',
		fg = 'white',
		command = lambda: display(7)
		)

	key_7.pack(expand=True, fill=BOTH, side=LEFT)

	key_8 = Button(
		frame_3,
		text='8',
		font=('Arial', 22),
		border = 0,
		relief = GROOVE,
		bg = '#2E2E2B',
		fg = 'white',
		command = lambda: display(8)
		)

	key_8.pack(expand=True, fill=BOTH, side=LEFT)

	key_9 = Button(
		frame_3,
		text='9',
		font=('Arial', 22),
		border = 0,
		relief = GROOVE,
		bg = '#2E2E2B',
		fg = 'white',
		command = lambda: display(9)
		)

	key_9.pack(expand=True, fill=BOTH, side=LEFT)

	key_mul = Button(
		frame_3,
		text='*',
		font=('Arial', 22),
		border = 0,
		relief = GROOVE,
		bg = '#2E2E2B',
		fg = 'white',
		command = lambda: display('*')
		)

	key_mul.pack(expand=True, fill=BOTH, side=LEFT)


	key_clr = Button(
		frame_4,
		text='C',
		font=('Arial', 22),
		border = 0,
		relief = GROOVE,
		bg = '#2E2E2B',
		fg = 'white',
		command = clear_scr 
		)

	key_clr.pack(expand=True, fill=BOTH, side=LEFT)

	key_0 = Button(
		frame_4,
		text='0',
		font=('Arial', 22),
		border = 0,
		relief = GROOVE,
		bg = '#2E2E2B',
		fg = 'white',
		command = lambda: display(0)
		)

	key_0.pack(expand=True, fill=BOTH, side=LEFT)

	key_res = Button(
		frame_4,
		text='=',
		font=('Arial', 22),
		border = 0,
		relief = GROOVE,
		bg = '#2E2E2B',
		fg = 'white',
		command = equal_btn
		)

	key_res.pack(expand=True, fill=BOTH, side=LEFT)

	key_div = Button(
		frame_4,
		text='/',
		font=('Arial', 22),
		border = 0,
		relief = GROOVE,
		bg = '#2E2E2B',
		fg = 'white',
		command = lambda: display('/')
		)

	key_div.pack(expand=True, fill=BOTH, side=LEFT)

# tedit app
def tedit_app():
	global tedit_win, toolbar, toolbartext

	# Return a frame window
	tedit_win = Frame(bd=0, bg='white')
	tedit_win.pack(padx=37, pady=37, fill='both', expand=1)

	# Toolbar
	toolbar = Frame(tedit_win, bg='#2259E1', bd=0)
	toolbar.pack(side='top', fill='x')

	# Exit button
	exit_btn = Button(toolbar, bd=0, text=' ✕ ', fg='white', bg='#FF4900', font=("ubuntu", 10), activebackground='#FF4900', activeforeground='white', command=tedit_exit)
	exit_btn.pack(side='right')

	# Toolbar text
	toolbartext = Label(toolbar, bd=0, text='TextEditor XP', font=('ubuntu', 12), bg='#2259E1', fg='white')
	toolbartext.pack(ipady=1)

	# TLFrm
	TLB = Frame(tedit_win, bg='#2259E1', bd=0)
	TLB.pack(side='top', fill='x')

	# New file
	def newfile():
		my_text.delete("1.0", END)

	# TLB BTN NEW
	newbtn = Button(TLB, bd=0, text='New File', bg='#2259E1', font=('ubuntu', 13), activebackground='#2259E2', fg='white', activeforeground='lightgrey', command=newfile)
	newbtn.pack(fill='x', side='left', ipadx=5)

	# Open file
	def open_file():
		global text_file, trext_file
		my_text.delete("1.0", END)
		trext_file = filedialog.askopenfilename(title="Open file", filetypes=(("Text Files", "*txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
		text_file = open(trext_file, 'r')
		stuff = text_file.read()
		my_text.insert(END, stuff)
		text_file.close()
		
		toolbartext.config(text=f'TextEditor XP - Opened file')

	# TLB BTN
	openbtn = Button(TLB, bd=0, text='Open File', bg='#2259E1', font=('ubuntu', 13), activebackground='#2259E2', fg='white', activeforeground='lightgrey', command=open_file)
	openbtn.pack(fill='x', side='left', ipadx=5)

	def save_file():
		try:
			# Get text and filename
			global content_str
			content_str = my_text.get(1.0, END)

			# Write to filename
			open_filename = open(trext_file, mode='w', encoding='utf8')
			open_filename.write(content_str)
			open_filename.close()

			messagebox_info('Saved file', 'We sucsessfully saved your file, or atleast we think we did?', root)

		except NameError as errraa:
			messagebox_error('Error', 'Please open a file before saving it', root)
		except Exception as exceptiontk:
			messagebox_error('Error', f"We ran into the following error:\n{exceptiontk}", root)

	# TLB BTN SAVE
	save_btn = Button(TLB, bd=0, text='Save File', bg='#2259E1', font=('ubuntu', 13), activebackground='#2259E2', fg='white', activeforeground='lightgrey', command=save_file)
	save_btn.pack(fill='x', side='left', ipadx=5)

	def save_as_file():
		# Get file name, directory
		savefilemsg = filedialog.asksaveasfilename(title='What should we save as?')
		savefilemsg = ''.join(savefilemsg)

		# Make file
		try:
			if (savefilemsg != ""):
				os.system(f'touch "{savefilemsg}"')

				with open(savefilemsg, 'w') as file:
					# Write to file
					file.write(my_text.get(1.0, END))
					file.close()

		except Exception as err__:
			print(err__)
			messagebox_error("Error", f'The following error occoured in PROCESS_SAVE_AS:\n{err__}', root)

	# tTLB SAVE BUTTON AS button
	save_as_btn = Button(TLB, bd=0, text='Save As', bg='#2259E1', font=('ubuntu', 13), activebackground='#2259E2', fg='white', activeforeground='lightgrey', command=save_as_file)
	save_as_btn.pack(fill='x', side='left', ipadx=5)

	tedit_frame = Frame(tedit_win, bg='white')
	tedit_frame.pack(fill='both', expand=1)

	# Main textbox
	my_text = Text(tedit_win, font=("Arial", 16), selectbackground="Lightgrey", selectforeground="Black", undo=True, bd=0)
	my_text.pack(expand=1, fill='both')

	def readtexts():
		engine = pyttsx3.init()
		engine.say(my_text.get(1.0, END))

		engine.runAndWait()
		return

	# A read file
	read_btn = Button(TLB, bd=0, text='Read Text', bg='#2259E1', font=('ubuntu', 13), activebackground='#2259E2', fg='white', activeforeground='lightgrey', command=readtexts)
	read_btn.pack(fill='x', side='left', ipadx=5)

	# Context menu
	tedit_root = Menu(root)

	tedit_root = Menu(tedit_root, tearoff=0, activebackground='lightblue', activeforeground='black')
	tedit_root.add_command(label="Clear text", command=newfile)
	tedit_root.add_command(label="Open file", command=open_file)
	tedit_root.add_command(label="Save file", command=save_file)
	tedit_root.add_command(label="Save as file", command=save_as_file)
	tedit_root.add_command(label="Read Text", command=readtexts)

	def do_pap(event):
		try: tedit_root.tk_popup(event.x_root, event.y_root)
		finally: tedit_root.grab_release()

	my_text.bind("<Button-3>", do_pap)

# About workspace
def about_workspace():
	global about_win
	# Return a frame window
	about_win = Frame()
	about_win.pack(pady=(37, 37))

	# Toolbar
	toolbar = Frame(about_win, bg='#2259E1', bd=0)
	toolbar.pack(side='top', fill='x')

	# Exit button
	exit_btn = Button(toolbar, bd=0, text=' ✕ ', fg='white', bg='#FF4900', font=("ubuntu", 12), activebackground='#FF4900', activeforeground='white', command=about_exit)
	exit_btn.pack(side='right')

	# Toolbar text
	toolbartext = Label(toolbar, bd=0, text='About Workspace (Version Info)', font=('ubuntu', 12), bg='#2259E1', fg='white')
	toolbartext.pack(ipady=1)

	about_label = Text(about_win, font=('Monospace', 13), selectbackground='#f0f0f0', selectforeground='black', bd=0, wrap=WORD, bg='#f0f0f0')
	about_label.insert('1.0', about_txt)
	about_label.pack(expand=1, fill='both', pady=2, padx=2)
	about_label.config(state="disabled")

	# Tag
	about_label.tag_add("start", "2.0", "2.30")
	about_label.tag_config("start", font=('ubuntu', 20), justify='center', foreground='#0077c8')

# Start menu
def startmenu():
	global start_frame, viewbtn

	start_frame = Frame(bg='white', bd=0)
	start_frame.pack(side='left', anchor='s', ipady=100)

	# Top bar
	textlbl = Label(start_frame, bg='#2E77C6', font=("ubuntu", 14), fg='white', text=' Workspace User                                           ')
	textlbl.pack(side='top', ipady=2)

	# Bottom bar
	bottombar = Frame(start_frame, bg='#2E77C6', bd=0)
	bottombar.pack(side='bottom', ipady=2, fill='x')

	# One side bar (#D0E6FD)
	one_sidebar = Frame(start_frame, bg='#D0E6FD')
	one_sidebar.pack(side='right', fill='y')

	# Sidebar text
	mydocs = Button(one_sidebar, bg='#D0E6FD', activebackground='#D0E6FD', text='Kontact Developer', font=("ubuntu", 12), fg='black', bd=0, command=lambda:webbrowser.open("mailto:pycodes.10@gmail.com"))
	mydocs.grid(row=0, column=0, ipadx=3)

	myhelp = Button(one_sidebar, bg='#D0E6FD', activebackground='#D0E6FD', text='About workspace', font=("ubuntu", 12), fg='black', bd=0, command=about_workspace)
	myhelp.grid(row=1, column=0, ipadx=3)

	# Left side bar
	left_sidebar = Frame(start_frame, bg='white')
	left_sidebar.pack(side='left', fill='y')

	mymail = Button(left_sidebar, bg='white', activebackground='white', text='TextEditor', font=("ubuntu", 12), fg='black', bd=0, command=tedit_app)
	mymail.grid(row=1, column=0, ipadx=0)

	rpc_btn = Button(left_sidebar, bg='white', activebackground='white', text='RPCGame', font=("ubuntu", 12), fg='black', bd=0, command=tmrf)
	rpc_btn.grid(row=2, column=0, ipadx=0)

	clc_btn = Button(left_sidebar, bg='white', activebackground='white', text='Calculator', font=("ubuntu", 12), fg='black', bd=0, command=calcs)
	clc_btn.grid(row=3, column=0, ipadx=0)

	ttcbtn = Button(left_sidebar, bg='white', activebackground='white', text='Tic Tac Toe', font=("ubuntu", 12), fg='black', bd=0, command=ttc)
	ttcbtn.grid(row=4, column=0, ipadx=0)

	viewbtn = Button(bottombar, bg='#E68E00', font=('Ubtunu', 10), fg='white', text='FullScreen', bd=0, command=lambda:full_view(viewbtn))
	viewbtn.config(activebackground='#E68E00', fg='white')
	viewbtn.pack(side='right', pady=3, padx=3)

	about_btn = Button(bottombar, bg='#E68E00', font=('Ubtunu', 10), fg='white', text='About WXP', bd=0, command=about_workspace)
	about_btn.config(activebackground='#E68E00', fg='white')
	about_btn.pack(side='right', pady=3, padx=3)

	# Logoff
	shutbtn = Button(bottombar, bg='#FF4D00', font=('Ubtunu', 10), fg='white', text='Shut down', bd=0, command=workspace_exit)
	shutbtn.config(activebackground='#FF4D00', fg='white')
	shutbtn.pack(side='right', pady=3, padx=3)

	start.config(comman=lambda:startoof(start_frame))


# Background image
SPECM = PhotoImage(file=r"Images/windows_xp.png")

background_label = Label(root, image=SPECM)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# TEditor icon
txp_icon = Image.open(r"Icons\texteditor.png")
txp_icon = txp_icon.resize((27, 27))
txp_icon = ImageTk.PhotoImage(txp_icon)

tict_icon = Image.open(r"Icons\tic-tac-toe.png")
tict_icon = tict_icon.resize((27, 27))
tict_icon = ImageTk.PhotoImage(tict_icon)

calc_icon = Image.open(r"Icons\calc.png")
calc_icon = calc_icon.resize((27, 27))
calc_icon = ImageTk.PhotoImage(calc_icon)

tmr_icn = Image.open(r"Icons\terminal.png")
tmr_icn = tmr_icn.resize((27, 27))
tmr_icn = ImageTk.PhotoImage(tmr_icn)

# Taskbar
taskbar = Frame(root, bg='#2E77C6')
taskbar.pack(fill='x', side='bottom')

# Start menu
start = Button(taskbar, bg='#4EC050', text='Workspace', bd=0, font=("ubuntu", 14), fg='white', command=lambda:startmenu())
start.config(activebackground='#52d154', activeforeground='white')
start.pack(side='left', ipady=2, ipadx=2)

# Taskbar icon
txp_btn = Button(taskbar, image=txp_icon, bd=0, activebackground='#2E77C6', bg='#2E77C6', command=tedit_app)
txp_btn.pack(side='left', ipady=5, ipadx=7)

tmr_btn = Button(taskbar, image=tmr_icn, bd=0, activebackground='#2E77C6', bg='#2E77C6', command=tmrf)
tmr_btn.pack(side='left', ipady=5, ipadx=7)

calcs_btn = Button(taskbar, image=calc_icon, bd=0, activebackground='#2E77C6', bg='#2E77C6', command=calcs)
calcs_btn.pack(side='left', ipady=5, ipadx=7)

tic_btn = Button(taskbar, image=tict_icon, bd=0, activebackground='#2E77C6', bg='#2E77C6', command=ttc)
tic_btn.pack(side='left', ipady=5, ipadx=7)

# Time
times = time.strftime("%H:%M:%S")

def timechan():
	global hms
	hms = time.strftime("%X")
	time_lbl.config(text=hms)
	root.after(500, timechan)


def batterchan():
	global percent
	battery = psutil.sensors_battery()
	plugged = battery.power_plugged
	percent = str(battery.percent)
	percent = f'{percent}%'

	battery_lbl.config(text=percent)

	root.after(1000, batterchan)

time_lbl = Label(taskbar, bg='#008EFF', text='', fg='white', font=('Ubuntu', 14))
time_lbl.pack(side='right', ipady=5, ipadx=1)

timechan()

# Battery
battery_lbl = Label(taskbar, bg='#008EFF', text='', fg='white', font=('Ubuntu', 14))
battery_lbl.pack(side='right', ipady=5, ipadx=3)
batterchan()

# Extra icon
extr_icon = Image.open(r"Icons\more.png")
extr_icon = extr_icon.resize((27, 27))
extr_icon = ImageTk.PhotoImage(extr_icon)

# Context menu
context_root = Menu(root)

context_menu = Menu(context_root, tearoff=0, activebackground='lightblue', activeforeground='black')
context_menu.add_command(label="Shut down", command=workspace_exit)
context_menu.add_command(label="Version info", command=about_workspace)
context_menu.add_separator()
context_menu.add_command(label="Full Screen", command=lambda:root.attributes('-fullscreen', True))
context_menu.add_command(label="Exit Full Screen", command=lambda:root.attributes('-fullscreen', False))

def do_popup(event):
	try: context_menu.tk_popup(event.x_root, event.y_root)
	finally: context_menu.grab_release()

# Extra button
extr_btn = Button(taskbar, image=extr_icon, bd=0, activebackground='#008EFF', bg='#008EFF')
extr_btn.bind("<Button-1>", do_popup)
extr_btn.pack(side='right', ipady=5, ipadx=3)

# Execute code
if __name__ == '__main__':

	# Context menu
	text_root = Menu(root)

	text_root = Menu(text_root, tearoff=0, activebackground='lightblue', activeforeground='black')
	text_root.add_command(label="Text Editor XP", command=tedit_app)
	text_root.add_command(label="Rock Paper Scissors", command=tmrf)
	text_root.add_separator()
	text_root.add_command(label="Shut down", command=workspace_exit)
	text_root.add_command(label="About Workspace", command=about_workspace)
	text_root.add_separator()
	text_root.add_command(label="Full Screen", command=lambda:root.attributes('-fullscreen', True))
	text_root.add_command(label="Exit Full Screen", command=lambda:root.attributes('-fullscreen', False))

	def do_poop(event):
		try: text_root.tk_popup(event.x_root, event.y_root)
		finally: text_root.grab_release()

	root.bind("<Button-3>", do_poop)

	# Plugged
	battery = psutil.sensors_battery()
	pluggede = battery.power_plugged

	if pluggede == 1:
		messagebox_info('Plugged in', 'You are plugged in to power', root)
	elif pluggede == 0:
		messagebox_warning("Not Plugged In", "You are not plugged in", root)

	# Mainloop
	root.mainloop()
