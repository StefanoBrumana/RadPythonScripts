#python script version 0.3 December 2021 to telnet multiple Rad devices all
#with same username and password 
#enter commands and save the entire log into a .txt file
#whose name is made by IP address of target device + date/time
#tested in python 3.8.5 on windows 7 pro 64 bit + pip version 20.1.1
#ssh libraries: paramiko version 2.7.2, netmiko version 3.3.2
#import required python libraries to execute this script
import getpass
import sys
import telnetlib
import time
import socket
import os
from datetime import datetime

#user is prompted to insert unique username and password of all the target devices
print ("#############################")
print ("Python telnet script for Rad")
print ("##########FaAndàIMan#########")
user=input("Enter Username: ")
password=getpass.getpass()

#open file ip.txt to retrieve addresses of target devices
#this ip.txt file must be in same folder of this python script
iplist=open("ip.txt")

for line in iplist:
 #open file commands.txt to retrieve commands to be executed on target devices
 #this commands.txt file must be in same folder of this python script
 #commands.txt must begin with terminal pagination disable in order to collect
 #entire outputs of certain long show commands
 commands=open("commands.txt")
 Host=line.strip("\n")
 print ("Working on device",Host )

 #telnet performed on default TCP port 23
 try:
  tn = telnetlib.Telnet(Host,23)
  #following line must exactly match the prompt of the target device
  #telnet the target device to verify if its exact prompt is Login:
  #or Username: or user> or something else
  tn.read_until(b"user>", timeout=5)
  tn.write(user.encode("ascii") + b"\n")
  #following line must exactly match the prompt of the target device
  #telnet the target device to verify if its exact prompt is Password:
  #or password: or password> or something else
  tn.read_until(b"Password:", timeout=5)
  tn.write(password.encode("ascii")+ b"\n")
  time.sleep(2)
  print ("Executing and logging these commands:")
  for line in commands:
   tn.write(line.encode("ascii") + b"\n")
   print (line)
   time.sleep(3)
   #each telnet command is executed every 3 seconds: increase it if some output is missing
  #telnet session MUST be closed properly with a logout command otherwise log files will not be 
  #created or the telnet session will not work reliably
  tn.write( b"logout\n")
  str_all = tn.read_all().decode("ascii")
  timestr = datetime.now().strftime("%m%d%Y-%H%M%S")
  log_file = Host + "_" + timestr + ".txt"
  f = open (log_file,"w")
  f.write(str_all)
  emptyline = "\n"
  confirmation = "Log closed on "
  f.writelines(emptyline)
  f.writelines(confirmation)
  f.writelines(timestr)
  print ("End of operations on device",Host)
  print ("All logged into file ", Host, "_", timestr, ".txt", sep="" )
  print ("Wait conclusion of the entire process before opening any log file")
  #all operations are logged in a file with name: IP-address_Date-Time.txt
  #this file is created in the same folder of this script
   
  tn.close()
  commands.close()
 except IOError:
  print ("Unable to reach via telnet device", Host )
  time.sleep(5)
  pass
  
print ("##############################################")
print ("##################FaAndàIMan##################")
print ("##############################################")
print ("All operations logged into your present folder")
iplist.close()

#remove empty lines from log ( file with name: IP-address_Date-Time.txt )
#this file is created in the same folder of this script
filename = log_file
def remove_empty_lines(filename):
    if not os.path.isfile(filename):
        print("{} does not exist ".format(filename))
        return
    with open(filename) as filehandle:
        lines = filehandle.readlines()

    with open(filename, 'w') as filehandle:
        lines = filter(lambda x: x.strip(), lines)
        filehandle.writelines(lines)

remove_empty_lines(filename)
f.close()