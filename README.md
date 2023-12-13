# File Sharing Application

File Sharing Application is implemented as the file-sharing system through Python socket (base on TCP/IP protocol).

## Usage
There are three folders in the source code:
### Server
In the server folder, run command below to start the server:
```bash
python .\server.py
```
There are several commands to control the server, which format is command "parameter 1" "parameter2"...:
-  start: start the server
- stop: stop the server
- clear: clear the command-line output
- ping "hostname": check if the host with hostname is online
- discover "hostname": check the local files of host hostname
### Client
### Server
In the client folder, run command below to start the server:
```bash
python .\client.py
```
There are several commands to control the server, which format is command "parameter 1" "parameter2"...:
- start: start the client
- stop: stop the client
- list: list all files in the local repository
- notify: list all notifications from the server
- publish "lname" "fname": a local file (which is stored in the client's file system at "lname") is added to the client's repository as a file named "fname" and this information is conveyed to the server
- describe "fname" "description": add a description to the file "fname" in the local repository
- fetch "file name": fetch some copy of the target file and add it to the local repository
- download "index": download the file with the index <index> return from the fetch command to local repository on your computer
### ClientUI
We also make the UI version for the client. To run it, you must install PySide6 first:
```bash
pip install PySide6
```
The UI is based on 
PyDracula - Modern GUI PySide6 / PyQt6PyDracula - Modern GUI PySide6 / PyQt6, which was contributed by Wanderson-Magalhaes, you can go to see the documentary
[here](https://github.com/Wanderson-Magalhaes/Modern_GUI_PyDracula_PySide6_or_PyQt6)
