# Mach3 Controller

ESP32 / ESP8266 based display and controller for Mach3 CNC software from Artsoft.
It relies heavily on Mach3's macropump function to write to a simple text file.
We will read that text file with python and send it over UDP (mostly because it's the only
one that lets me send and receive at the same time). I have examples of receiving coordinates over
Serial, Serial over Bluetooth, Websocket, reading the file over Samba/CIFS (Raspberry Pi or equivalent only sorry)
and lastly UDP, which I like the most. I liked Bluetooth as well, but I couldn't get HID and SPP (or UART) working
at the same time, if you know how in the Arduino IDE, please let me know.

## Getting Started

First you need to replace or copy the macropump.m1s file over to C:\Mach3\macros\Mach3Mill\ (be sure to edit the path to wherever you'd like the text file to be)
Then go to Config -> General Config -> Check MacroPump
Install Python for Windows, be sure to check ADD to PATH at the beginning
After installation, open Command Prompt (Start -> Run -> CMD -> ENTER)
Then run command Pip install keyboard
I suggest you download the python scripts to C:\Python but ultimately doesn't matter
You will need to edit the udpserver.py to match your network setup (meaning 192.168.1.1 or 10.0.0.1 so on and so forth)
I highly suggest you use the broadcast address (ie 192.168.1.255, it's your regular IP address but change the last 3 to 255)
This will broadcast on the whole network so you could have multiple nodes.
You can also edit the receive.py to match whatever keyboard keys you want, please read the Python Keyboard library for more info.
You can just double click a python script to run it or make a batch file to run both.
You need to run at least the udpserver.py script to get coordinates to your display.

You will load the INO files in Arduino IDE and compile it for the ESP32.
I will not go through the steps for that, lots of youtube videos and articles explaining how to get setup.

### Prerequisites

Windows 7 or newer (I have not tested 32 bit if you are running Mach3 on 32 bit windows let me know how this performs)

## Authors

* **Patrick Rankin** - *lead doofus* - [Patrick-E-Rankin](https://github.com/Patrick-E-Rankin/)


## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details

