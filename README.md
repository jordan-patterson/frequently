# frequently
## Small tool to make your life easier in the terminal

### - Open websites that you frequently visit

### - Run scripts or executables without having to constantly change directories

### - Specify what executables, commands you want to run or websites you want to open whenever you start the script

##Installation
```bash
$ #clone the repository
$ git clone https://github.com/jordan-patterson/frequently.git
$
$ #create virtual environment
$ virtualenv env -p python3
$ source env/bin/activate
$
$ #install requirements
$ pip3 install -r requirements.txt
$ ./install.py
```


## Usage
```bash
$ freq -a #run all scripts,commands and websites that you specify 
$ freq -w #open all specified websites on start
$ freq -e #run all specified scripts on start
$ freq -c #run all specified commands on start
$ freq #does not perform any action
```
