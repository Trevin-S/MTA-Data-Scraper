import time, requests, keyboard, mechanize
from lxml import html
from bs4 import BeautifulSoup
from tkinter import Tk

import user, agent_data, title_agencies
 
User = user.User()
Title_Agencies = title_agencies.Title_Agencies()
Agent = agent_data.Agent_Data()
 
def getAgencies():

    agencyList = []

    # Browser Objects
    driggs = mechanize.Browser()
 
    print(' Requesting Driggs Title Data \n')
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
            TitleAgencies.add_short_agency(currentAgency[:4].lower())
 
def getData():
 
    NONE = []
    titleNamesHTML = []
    url = ''
 
    NONE.clear()
    time.sleep(0.02)
 
    # Select URL
    keyboard.press_and_release('ctrl+l')
    time.sleep(0.02)
 
    # Copy URL
    keyboard.press_and_release('ctrl+c')
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
 
        titleNames.append('none')
        listingSide.append('1')
        MS1.append('1')
        buySide.append('1')
        MS2.append('1')
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
 
    if keyboard.is_pressed('left arrow'):
 
        print('\n Data Copy Started, Please Wait.')
        getData()
 
 
def pasteData():
 
        # Repeat as many times as there is deals
        for Agent.paste_iteration in range(Agent.get_paste_iteration(), Agent.deal_count()):
            
            matchFound = True
            arrowKeyCount = 0
            shortDuplicate = 0
            fullDuplicate = 0 
            occurences = 0
            nameLength = 17
 
            for i in range(TitleAgencies.agency_count()):
 
                if Agent.title_name(Agent.get_paste_iteration(), 0, 4) in TitleAgencies.short_agency(i):
 
                    occurences += 1
 
            if occurences > 1:
 
                matchFound = False
 
                for i in range(TitleAgencies.agency_count()):
 
                    if Agent.title_name(Agent.get_paste_iteration(), 0, 4) in titleAgencies.short_agency(i) and Agent.title_name(Agent.paste_iteration(), 0, 3) in TitleAgencies.short_agency(i, 0, 4):
 
                        shortDuplicate = i
                        break
 
                for i in range(10):
 
                    for i in range(TitleAgencies.agency_count()):
 
                        if Agent.title_name(Agent.paste_iteration()) in TitleAgencies.long_agency(i) and Agent.title_name(Agent.paste_iteration(), 0, 4) in TitleAgencies.long_agency(i, 0, 4):
 
                            fullDuplicate = i
                            matchFound = True
                            break
 
                    if nameLength > 7 and matchFound == False:
 
                        nameLength -= 1
                        Agent.update_title_name(Agent.paste_iteration(), Agent.title_name(Agent.paste_iteration(), 0, nameLength))
 
            if occurences == 0 or matchFound == False:
 
                Agent.update_title_name(Agent.paste_iteration(), 'othe')
                shortDuplicate = 0
                fullDuplicate = 0
    
            arrowKeyCount = shortDuplicate - fullDuplicate
 
            keyboard.write(Agent.title_name(Agent.paste_iteration(), 0, 4), 0.01)
            time.sleep(0.01)
 
            for i in range(abs(arrowKeyCount)):
 
                keyboard.press_and_release('down arrow')
                time.sleep(0.01)
 
            keyboard.press_and_release('tab')
            time.sleep(0.01)
            keyboard.write(Agent.listing_side(Agent.paste_iteration()), 0.01)
            time.sleep(0.01)
            keyboard.press_and_release('tab')
            time.sleep(0.01)
            keyboard.write(Agent.ms1(Agent.paste_iteration()), 0.01)
            time.sleep(0.01)
            keyboard.press_and_release('tab')
            time.sleep(0.01)
            keyboard.write(Agent.buy_side(Agent.paste_iteration()), 0.01)
            time.sleep(0.01)
            keyboard.press_and_release('tab')
            time.sleep(0.01)
            keyboard.write(Agent.ms2(Agent.paste_iteration()), 0.01)
            time.sleep(0.01)
            keyboard.press_and_release('tab')
            time.sleep(0.01)
 
            if (Agent.paste_iteration() + 1) % 30 != 0:
 
                User.set_full(False)
 
            else: 
 
                User.set_full(True)
                print('\n Table Full, Paste Paused. Submit and resume paste on next open line. \n')
                break
 
        if User.is_full() == False:
 
            print('\n \n Paste Finished. \n')
            Agent.set_paste_iteration(0)
 
    time.sleep(0.2)
 
 
def clearPaste():
 
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


getAgencies() 

while User.is_running() == True:
    
    if User.is_paused() == False:
 
        if keyboard.is_pressed('left arrow'):
            print('\n Data Copy Started, Please Wait.')
            getData()

        if keyboard.is_pressed('right arrow'):
            pasteData()

        if keyboard.is_pressed('-'):
            clearPaste()

    if keyboard.is_pressed('+') and User.get_last_state() == False:
 
        User.pause(not User.is_paused())
        User.last_state(True)
 
        if User.is_paused() == True:
 
            print('\n Program Paused.')
 
        else: 
 
            print('\n Program Resumed.')
 
    elif not keyboard.is_pressed('+'):
 
        User.last_state(False)

    if keyboard.is_pressed('esc'):
        User.stop_running()

    time.sleep(.01)