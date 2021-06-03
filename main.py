import time
import requests
import keyboard
import random
from lxml import html
from bs4 import BeautifulSoup
from tkinter import Tk
from mechanize import Browser
import classes
 
User = classes.user()
TitleAgencies = classes.titleAgencies()
Agent = classes.agent()
 
x = 0
 
def programStartup():
 
	print(' Trevin Small, 02/14/2019.')
	print('\n Program: MTA Data Scraper')
	print(' Version 1.6 \n \n')
 
	getAgencies()
 
	print(' Data Recieved! \n \n')
	print(' Program Ready to Use. \n')
	print(' Left Arrow Key Copies from MyMTA Market Share Reports.')
	print(' Right Arrow Key Pastes into Reports.')
	print(' Minus Sign clears an MTA Report to fix mistakes.')
	print(' Esc Key closes the program.\n')
	print(' (Make sure to click onto a seperate program, the program')
	print(' will not work correctly if it is the active window)')
 
 
def getAgencies():
 
	agencyList = []
 
	# Browser Objects
	driggs = Browser()
	driggs.set_handle_robots(False)
 
	print(' Requesting Data \n')
	driggs.open('https://www.driggstitle.com/beta/')
	driggs.forms()
	driggs.select_form(nr = 0)

	# User credentials
	driggs.form['name'] = User.get_username()
	driggs.form['password'] = User.get_password()
	driggs.submit()
	html = driggs.open('https://rightdata.driggstitle.com/prv/mta_dta.title_comps')
 
	print(' Requesting Data from Driggs Title, please wait... \n')
	soup = BeautifulSoup(html, 'lxml')
	agencyList = soup.find('table')
	agencyList = agencyList.find_all('input', {'size':'100'})
 
	for i in range(len(agencyList)):
 
		currentAgency = agencyList[i]['value']
 
		if '\xa0' in currentAgency or 'value="293"' in currentAgency or "'" in currentAgency:
 
			currentAgency = currentAgency.replace(u'\xa0', u' ')
			currentAgency = currentAgency.replace(u'value="293">', u'')
			currentAgency = currentAgency.replace(u"'", u'')
 
		if currentAgency != '':
 
			TitleAgencies.add_long_agency(currentAgency.lower())
			TitleAgencies.add_short_agency(currentAgency[:5].lower())
 
	print(TitleAgencies.get_title_agencies())

def getData():
 
	NONE = []
	titleNamesHTML = []
	url = ''
 
	NONE.clear()
	time.sleep(0.02)
 
	# Select URL
	keyboard.press_and_release('cmd+l')
	time.sleep(0.02)
 
	# Copy URL
	keyboard.press_and_release('cmd+c')
	time.sleep(0.02)
 
	try:
 
		# Pull URL from clipboard
		url = Tk().clipboard_get()
 
		# Pull HTML from URL
		r = requests.get(url)
		soup = BeautifulSoup(r.text, 'lxml')
 
	except:
 
		print(' No URL found! Try reselecting web page before copying data. \n')
		return
 
	# Store data on Agent Deals as lists
	titleNamesHTML = soup.find_all('div', attrs={'class':'a78'})
	listingSideHTML = soup.find_all('div', attrs={'class':'a119'})
	MS1HTML = soup.find_all('div', attrs={'class':'a127'})
	buySideHTML = soup.find_all('div', attrs={'class':'a135'})
	MS2HTML = soup.find_all('div', attrs={'class':'a143'})
	doubleDipHTML = soup.find_all('div', attrs={'class':'a151'})
	MS3HTML = soup.find_all('div', attrs={'class':'a159'})
	NONE = str(soup.find_all('a', href = True)) 
 
	# Set count equal to the length of the list 
	count = len(titleNamesHTML)
 
	if '<a href="mailto:info@mymta.com">info@mymta.com</a>' in NONE:
 
		Agent.add_deal('none', 1, 1, 1, 1)
		count = 1
	
	elif count == 0:
	
		print(" We couldn't find any data, are you sure you are copying a MyMTA Market Share Report?")
 
	else:
 
		if count > 0:
 
			for i in range(count):
 
				currentTitleName = str(titleNamesHTML[i])
				currentTitleName = currentTitleName[17:-6]
 
				currentListingSideSTR = str(listingSideHTML[i])
				currentListingSideSTR = currentListingSideSTR[19:-6]
 
				currentMS1STR = str(MS1HTML[i])
				currentMS1STR = currentMS1STR[18:-6]
 
				currentBuySideSTR = str(buySideHTML[i])
				currentBuySideSTR = currentBuySideSTR[19:-6]
 
				currentMS2STR = str(MS2HTML[i])
				currentMS2STR = currentMS2STR[18:-6]
 
				currentDoubleDipSTR = str(doubleDipHTML[i])
				currentDoubleDipSTR = currentDoubleDipSTR[19:-6]
 
				currentMS3STR = str(MS3HTML[i])
				currentMS3STR = currentMS3STR[18:-6]
 
				currentListingSideSTR = currentListingSideSTR.replace(',' , '')
				currentBuySideSTR = currentBuySideSTR.replace(',' , '')
				currentDoubleDipSTR = currentDoubleDipSTR.replace(',' , '')
 
				currentListingSide = int(currentListingSideSTR)
				currentMS1 = int(currentMS1STR)
				currentBuySide = int(currentBuySideSTR)
				currentMS2 = int(currentMS2STR)
				currentDoubleDip = int(currentDoubleDipSTR)
				currentMS3 = int(currentMS3STR)
 
				currentMS1 += currentMS3
				currentMS1STR = str(currentMS1)
 
				currentMS2 += currentMS3
				currentMS2STR = str(currentMS2)
 
				if currentDoubleDip > 0 and currentListingSide == 0:
 
					currentListingSide = currentDoubleDip
					currentListingSideSTR = str(currentListingSide)
 
				if currentDoubleDip > 0 and currentBuySide == 0:
 
					currentBuySide = currentDoubleDip
					currentBuySideSTR = str(currentBuySide)
 
				Agent.add_deal(currentTitleName[0:17].lower(), currentListingSideSTR.lower(), currentMS1STR.lower(), currentBuySideSTR.lower(), currentMS2STR.lower())
				time.sleep(0.01)
 
	print(f"Done, Deal Count: {Agent.deal_count()}")
 
 
def copyData():

	released = True
 
	if keyboard.is_pressed('left arrow') and released == True:
 
		print('\n Data Copy Started, Please Wait.')
		Agent.reset_deal_count()
		getData()
		released = False
	
	elif keyboard.is_pressed('left arrow') == False and released == True:

		released = False

	else: 

		released = True
 
 
def pasteData():
 
	global x
 
	if keyboard.is_pressed('right arrow'):
 
		# Repeat as many times as there is deals
		for x in range(x, Agent.deal_count()):
			
			matchFound = True
			arrowKeyCount = 0
			shortDuplicate = 0
			fullDuplicate = 0 
			occurences = 0
			nameLength = 17
 
			for i in range(TitleAgencies.agency_count()):
 
				if Agent.title_name(x, 0, 5) in TitleAgencies.short_agency(i):
 
					occurences += 1
 
			if occurences > 1:
 
				matchFound = False
 
				for i in range(TitleAgencies.agency_count()):
 
					if Agent.title_name(x, 0, 5) in TitleAgencies.short_agency(i) and Agent.title_name(x, 0, 4) in TitleAgencies.short_agency(i, 0, 5):
 
						shortDuplicate = i
						break
 
				for i in range(10):
 
					for i in range(TitleAgencies.agency_count()):
 
						if Agent.title_name(x) in TitleAgencies.long_agency(i) and Agent.title_name(x, 0, 5) in TitleAgencies.long_agency(i, 0, 5):
 
							fullDuplicate = i
							matchFound = True
							break
 
					if nameLength > 7 and matchFound == False:
 
						nameLength -= 1
						Agent.update_title_name(x, Agent.title_name(x, 0, nameLength))
 
			if occurences == 0 or matchFound == False:
 
				Agent.update_title_name(x, 'othe')
				shortDuplicate = 0
				fullDuplicate = 0
	
			arrowKeyCount = shortDuplicate - fullDuplicate
 
			keyboard.write(Agent.title_name(x, 0, 4), 0.01)
			time.sleep(0.01)
 
			if (abs(arrowKeyCount) > 0):

				keyboard.press_and_release('down arrow')
				time.sleep(0.04)

				for i in range(abs(arrowKeyCount)):
	 
					keyboard.press_and_release('down arrow')
					time.sleep(0.02)

				time.sleep(0.01)
				keyboard.press_and_release('enter')
				time.sleep(0.01)
 
			keyboard.press_and_release('tab')
			time.sleep(0.01)
			keyboard.write(Agent.listing_side(x), 0.01)
			time.sleep(0.01)
			keyboard.press_and_release('tab')
			time.sleep(0.01)
			keyboard.write(Agent.ms1(x), 0.01)
			time.sleep(0.01)
			keyboard.press_and_release('tab')
			time.sleep(0.01)
			keyboard.write(Agent.buy_side(x), 0.01)
			time.sleep(0.01)
			keyboard.press_and_release('tab')
			time.sleep(0.01)
			keyboard.write(Agent.ms2(x), 0.01)
			time.sleep(0.01)
			keyboard.press_and_release('tab')
			time.sleep(0.01)
 
			if (x + 1) % 30 != 0:
 
				Agent.set_full(False)
 
			else: 
 
				Agent.set_full(True)
				print('\n Table Full, Paste Paused. Submit and resume paste on next open line. \n')
				break
 
		if Agent.is_full() == False:
 
			print('\n \n Paste Finished. \n')
			x = 0
 
		time.sleep(0.2)
 
 
def clearPaste():
 
	if keyboard.is_pressed('-'):
 
		for i in range(Agent.deal_count()):
 
			time.sleep(0.01)
			keyboard.write('choo', 0.01)
			time.sleep(0.01)
			keyboard.press_and_release('tab')
			time.sleep(0.01)
			keyboard.press_and_release('0')
			time.sleep(0.01)
			keyboard.press_and_release('tab')
			time.sleep(0.01)
			keyboard.press_and_release('backspace')
			time.sleep(0.01)
			keyboard.press_and_release('tab')
			time.sleep(0.01)
			keyboard.press_and_release('0')
			time.sleep(0.01)
			keyboard.press_and_release('tab')
			time.sleep(0.01)
			keyboard.press_and_release('backspace')
			time.sleep(0.01)
			keyboard.press_and_release('tab')
			time.sleep(0.01)
 
			if (i + 1) % 30 == 0:
				break
 
 
def pauseProgram():
 
	if keyboard.is_pressed('+') and User.get_last_state() == False:
 
		User.pause(not User.is_paused())
		User.last_state(True)
 
		if User.is_paused() == True:
 
			print('\n Program Paused.')
 
		else: 
 
			print('\n Program Resumed.')
 
	elif not keyboard.is_pressed('+'):
 
		User.last_state(False)
 
 
 
def exitProgram():
 
	if keyboard.is_pressed('esc'):
		User.stop_running()
 
programStartup()
 
while User.is_running() == True:
	
	if User.is_paused() == False:
 
		copyData()
		pasteData()
		clearPaste()
 
	pauseProgram()
	exitProgram()
	time.sleep(.01)
