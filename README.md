# Mach3 Controller

Android / ESP32 / ESP8266 based display and controller for Mach3 CNC software from Artsoft.<br>
It relies heavily on Mach3's macropump function to write to a simple text file. <br>
We will read that text file with python and send it over UDP (mostly because it's the only<br>
one that lets me send and receive at the same time easily). I have examples of receiving coordinates over<br>
Serial, Serial over Bluetooth, Websocket, reading the file over Samba/CIFS (Raspberry Pi or equivalent only) <br>
and lastly UDP, which I like the most. I liked Bluetooth as well, but I couldn't get HID and SPP (or UART) working <br>
at the same time, if you know how in the Arduino IDE, please let me know. <br>

## Getting Started

First you need to replace or copy the macropump.m1s file over to C:\Mach3\macros\Mach3Mill\ <br>
(be sure to edit the path to wherever you'd like the text file to be) <br>
Then go to Config -> General Config -> Check MacroPump<br>
Install Python for Windows, be sure to check ADD to PATH at the beginning <br>
After installation, open Command Prompt (Start -> Run -> CMD -> ENTER) <br>
Then run command Pip install keyboard <br>
I suggest you download the python scripts to C:\Python but ultimately doesn't matter <br>
You will need to edit the udpserver.py to match your network setup (meaning 192.168.1.1 or 10.0.0.1 so on and so forth) <br>
I highly suggest you use the broadcast address (ie 192.168.1.255, it's your regular IP address but change the last 3 to 255) <br>
This will broadcast on the whole network so you could have multiple nodes. <br>
You can also edit the receive.py to match whatever keyboard keys you want, please read the Python Keyboard library for more info. <br>
You can just double click a python script to run it or make a batch file to run both. <br>
You need to run at least the udpserver.py script to get coordinates to your display. <br><br>

You will load the INO files in Arduino IDE and compile it for the ESP32. <br>
I will not go through the steps for that, lots of youtube videos and articles explaining how to get setup. <br>

## Android

Excited about this new app I made on App Inventor! AIA file is included in the Android folder along with the great UDP library/extension
from <a href="https://ullisroboterseite.de/android-AI2-UDP.html">Ulrich</a>? <br>
Anyway I'm including it in the folder as well.<br>
<img src="https://raw.githubusercontent.com/Patrick-E-Rankin/Mach3Controller/master/Android/AndroidScreenshot.png"></img>

### Prerequisites

Windows 7 or newer (if you are using Windows 7 32bit you will need to use an older version of Python)

## Authors

* **Patrick Rankin** - *lead doofus* - [Patrick-E-Rankin](https://github.com/Patrick-E-Rankin/)


## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details

