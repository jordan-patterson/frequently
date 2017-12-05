#!/usr/bin/env python3

import os

def main():
	directory=os.getcwd()
	subcommand="./freq"
	alias="freq"
	command= "cd {} && {}".format(directory,subcommand)
	main="alias {}='{}'".format(alias,command)
	os.system("echo \"{}\" >> ~/.bashrc".format(main))
	print(main)

if __name__=="__main__":
	main()
