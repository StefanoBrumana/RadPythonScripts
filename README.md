# RadPythonScripts
Python scripts for RAD devices

All scripts contain commments to maximize understanding and customization

RadMultiTelnet.py: interactive script to telnet multiple Rad devices ( listed in ip.txt file that must be manually created in the same folder of this script ) all with same username and password, enter commands ( listed in commands.txt file that must be manually created in the same folder of this script ) and save the entire log into a .txt file whose name is made by IP address of target device + date/time

RadMultiSsh.py: interactive script to ssh multiple Rad devices ( listed in ip.txt file that must be manually created in the same folder of this script ) all with same username and password, enter commands ( listed in commands.txt file that must be manually created in the same folder of this script ) and save the entire log into a .txt file whose name is made by IP address of target device + date/time

RadMultiTftpUploadTelnet.py: interactive script to access via telnet to a list of Rad devices ( listed in ip.txt file that must be manually created in the same folder of this script ) all with same username and password, export their configuration to the root folder of a TFTP server ( all these activities are logged in a .txt file created in the same folder of the script )

RadMultiTftpUploadSsh.py: interactive script to access via ssh to a list of Rad devices ( listed in ip.txt file that must be manually created in the same folder of this script ) all with same username and password, export their configuration to the root folder of a TFTP server ( all these activities are logged in a .txt file created in the same folder of the script )

If log file has empty lines they can be removed by Notepad++ ( my favourite free app to consult log files: it also has a compare plug-in to quickly locate differences )


- How to run the script ( in Windows command prompt )

Open a DOS prompt and go to folder containing the .py script + ip.txt and commands.txt files that you have downloaded from here

Launch the script ( assuming that python was added to the system path of Windows during its installation on your PC to run it from any folder ) and answer to the questions appearing on screen

Example: C:\Temp> python RadMultiTelnet.py

If upon launching the script you get the error "ModuleNotFoundError: No module named 'paramiko'", you must install this library with the command "pip install paramiko"
Next re-launch the script as explained in the above example
