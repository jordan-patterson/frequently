#!/usr/bin/python3

import os
import webbrowser
from clmenu import getch,Menu,printLogo
import yaml
import argparse
import subprocess as sub

getch=getch()

def getDict(filename):
	with open(filename,"r") as file:
		data=yaml.load(file)
	return data

def addSite():
	try:
		sites=getDict("sites.yaml")
	except:
		#file not found, create new dict
		sites={}
	printLogo("logo.txt")
	name=input("\n\n\t\t\tName of website: ")
	url=input("\n\n\t\t\tAddress of website: ")
	sites[name]=url
	update("sites.yaml",sites)

def openSite():
	try:
		sites=getDict("sites.yaml")
	except:
		printLogo("logo.txt")
		print("\n\t\t\t\tError: There were no sites found.")
		getch()
		return None
	options=list(sites.keys())
	options.append("GO BACK")
	instructions="\t\t  What should I open?"
	menu=Menu(options,instructions,"logo.txt")
	temp=0
	while(temp!=len(options)-1):
		temp=menu.prompt()
		if(temp!=len(options)-1):
			webbrowser.open_new_tab("https://"+sites[options[temp]])

def addNewStartSite():
	try:
		sites=getDict("sitesOnStartUp.yaml")
	except:
		sites={}
	printLogo("logo.txt")
	name=input("\n\n\n\t\t\tName of website: ")
	url=input("\n\n\t\t\tAddress of website (www.example.com): ")
	sites[name]=url
	update("sitesOnStartUp.yaml",sites)

def addExistingStartSite():
	try:
		sites=getDict("sites.yaml")
	except:
		printLogo("logo.txt")
		print("\n\n\t\t\t\tError: No websites were found")
		getch()
		return None
	options=list(sites.keys())
	options.append("GO BACK")
	instructions="\n\t\t\t\tWhat website should I add?"
	menu=Menu(options,instructions,"logo.txt")
	temp=menu.prompt()
	if(temp!=len(options)-1):
		try:
			startupSites=getDict("sitesOnStartUp.yaml")
		except:
			startupSites={}
		finally:
			startupSites[options[temp]]=sites[options[temp]]
			update("sitesOnStartUp.yaml",startupSites)

def addStartUpWebsite():
	options=["NEW","EXISTING","GO BACK"]
	instructions="Select the type"
	menu=Menu(options,instructions,"logo.txt")
	temp=9
	while(temp!=len(options)-1):
		temp=menu.prompt()
		if(temp==0):
			addNewStartSite()
		elif(temp==1):
			addExistingStartSite()

def update(filename,dictionary):
	with open(filename,'w') as file:
		yaml.dump(dictionary,file)

def removeSite(filename):
	try:
		sites=getDict(filename)
	except:
		printLogo("logo.txt")
		print("\n\n\t\t\t\tError: There are no sites to remove")
		getch()
		return None
	options=list(sites.keys())
	options.append("GO BACK")
	instructions="\n\n\t\t\t\tWhat should I remove?"
	menu=Menu(options,instructions,"logo.txt")
	temp=menu.prompt()
	if(temp!=len(options)-1):
		del sites[options[temp]]
		update(filename,sites)

def website():
	options=["OPEN WEBSITE","ADD WEBSITE","REMOVE WEBSITE","ADD WEBSITE ON STARTUP","REMOVE WEBSITE FROM STARTUP","GO BACK"]
	instructions="\tWhat action should I take?"
	menu=Menu(options,instructions,"logo.txt")
	temp=0
	while(temp!=len(options)-1):
		temp=menu.prompt()
		if(temp==0):
			openSite()
		elif(temp==1):
			addSite()
		elif(temp==2):
			removeSite("sites.yaml")
		elif(temp==3):
			addStartUpWebsite()
		elif(temp==4):
			removeSite("sitesOnStartUp.yaml")

def openTextEditor():
	if(not os.path.exists("config.yml")):
		printLogo("logo.txt")
		editor=input("\n\n\t\t\t\tName of text editor: ")
		with open("config.yml","a") as file:
			yaml.dump({"editor":editor},file)
	with open("config.yml","r") as file:
		data=yaml.load(file)
	editor=data["editor"]
	os.system(editor)

def addScript():
	try:
		scripts=getDict("scripts.yml")
	except:
		scripts={}
	printLogo("logo.txt")
	name=input("\n\n\n\t\t\tEnter the name of the script: ")
	path=''
	while(not os.path.exists(path)):
		path=input("\n\n\t\t\tEnter a valid path to where the script is located:")
	scripts[name]=path
	update("scripts.yml",scripts)

def addNewStartupScript():
	try:
		scripts=getDict("startupScripts.yml")
	except:
		scripts={}
	printLogo("logo.txt")
	name=input("\n\n\t\t\t Enter the name you wish to call the executable: ")
	path=''
	while(not os.path.exists(path)):
		path=input("\n\n\t\t\t Enter a valid path to where the exec is located: ")
	scripts[name]=path
	update("startupScripts.yml",scripts)

def addExistingStartupScript():
	try:
		existing_scripts=getDict("scripts.yml")
	except:
		printLogo("logo.txt")
		print("\n\n\t\t\t\tError: No scripts were found")
		getch()
		return None
	options=list(existing_scripts.keys())
	options.append("GO BACK")
	instructions="\tWhat executable should I add?"
	menu=Menu(options,instructions,"logo.txt")
	temp=menu.prompt()
	if(temp!=len(options)-1):
		try:
			scripts=getDict("startupScripts.yml")
		except:
			scripts={}
		finally:
			scripts[options[temp]]=existing_scripts[options[temp]]
			update("startupScripts.yml",scripts)

def addScriptOnStartup():
	options=["NEW","EXISTING","GO BACK"]
	instructions="\t   Select the type"
	menu=Menu(options,instructions,"logo.txt")
	temp=9
	while(temp!=len(options)-1):
		temp=menu.prompt()
		if(temp==0):
			addNewStartupScript()
		elif(temp==1):
			addExistingStartupScript()

def removeScript(filename):
	try:
		scripts=getDict(filename)
	except:
		printLogo("logo.txt")
		print("\n\n\t\t\tError: There are no scripts to remove")
		getch()
		return None
	options=list(scripts.keys())
	options.append("GO BACK")
	instructions="\t  What should I remove?"
	menu=Menu(options,instructions,"logo.txt")
	temp=menu.prompt()
	if(temp!=len(options)-1):
		del scripts[options[temp]]
		update(filename,scripts)

def run(path):
	maindir=os.getcwd()
	executable=path.split('/')[-1]
	path=path.strip(executable)
	os.chdir(path)#go to directory where executable is located
	os.system("gnome-terminal -e './"+executable+"'")
	os.chdir(maindir)#come back to program's directory

def runScript():
	try:
		scripts=getDict("scripts.yml")
	except:
		printLogo("logo.txt")
		print("\n\n\t\t\t\tError: There were no executables found")
		getch()
		return None
	options=list(scripts.keys())
	options.append("GO BACK")
	instructions="\t  Select the executable you want to run"
	menu=Menu(options,instructions,"logo.txt")
	temp=0
	while(temp!=len(options)-1):
		temp=menu.prompt()
		if(temp!=len(options)-1):
			run(scripts[options[temp]])

def scripts():
	options=["RUN EXECUTABLE","ADD EXECUTABLE","REMOVE","ADD ON STARTUP","REMOVE ON STARTUP","GO BACK"]
	instructions="\t What action should I take?"
	menu=Menu(options,instructions,"logo.txt")
	temp=0
	while(temp!=len(options)-1):
		temp=menu.prompt()
		if(temp==0):
			runScript()
		elif(temp==1):
			addScript()
		elif(temp==2):
			removeScript("scripts.yml")
		elif(temp==3):
			addScriptOnStartup()
		elif(temp==4):
			removeScript("startupScripts.yml")

def openTerminal():
	terminal_commands=["konsole","xterm","gnome-terminal"]
	for i in range(len(terminal_commands)):
		try:
			sub.Popen([terminal_commands[i]],stdout=sub.PIPE,stderr=sub.PIPE)
			break
		except:
			continue

def main():
	options=["WEBSITE","EXECUTABLE","TERMINAL","TEXT EDITOR","EXIT"]
	instructions=" "
	menu=Menu(options,instructions,"logo.txt")
	temp=9
	while(temp!=len(options)-1):
		temp=menu.prompt()
		if(temp==0):
			website()
		elif(temp==1):
			scripts()
		elif(temp==2):
			openTerminal()
		elif(temp==3):
			openTextEditor()

def startallWebsites():
	try:
		sites=getDict("sitesOnStartUp.yaml")
	except:
		return None
	for site in sites.items():
		webbrowser.open_new_tab("https://"+site[1])

def startAllScripts():
	try:
		scripts=getDict("startupScripts.yml")
	except:
		return None
	for script in scripts.items():
		run(script[1])

if __name__=="__main__":
	parser=argparse.ArgumentParser(prog="Frequently")
	parser.add_argument('-a','--all',help="Starts all listed scripts and websites on start",action="store_true")
	parser.add_argument('-w','--web',help="Starts all listed websites on start",action="store_true")
	parser.add_argument('-e','--ex',help="Starts all listed executables on start",action="store_true")
	args=parser.parse_args()
	if(args.all):
		startallWebsites()
		startAllScripts()
	elif(args.web):
		startallWebsites()
	elif(args.ex):
		startAllScripts()
	main()
	#website()