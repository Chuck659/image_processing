Before you can run the program there are a few things that need to be set up.

Inside ArduCam_ESP8266_FileCapture\libraries folder there is an updated ArduCAM library.
Move the ArduCAM folder to your local Arduino libraries folder.

Replace the ssid and password values in the ArduCam_ESP8266_FileCapture.ino file with your wireless internet credentials.

Upload the code and verify the ESP is connected to your wifi through the serial debuger.

You will notice there is a file off of root that says Start.exe
This is an exacutable that was compiled from the source code.
The source code is also provided in the source folder (source\Start.py).

All you need to do is double click Start.exe and the program will open in a command window.


The program will display this text:

-------------------------------------------------------------------------------------------------------------------------------------
	**********************************************
	ContrastLightLevels:   Resolutions:
	0 = 0                 0 = 160x120
	1 = +1                1 = 176x144
	2 = +2                2 = 320x240
	3 = -1                3 = 352x288
	4 = -2                4 = 640x480
							  5 = 800x600
							  6 = 1024x768
							  7 = 1280x1024
							  8 = 1600x1200
	
	Type a command to execute
	
	COMMANDS - use the integer values inside the <>
	
	SET <lightLevel> <resolution>
	CAPTURE
	EXIT
	
	Input:
-------------------------------------------------------------------------------------------------------------------------------------

**NOTE: the commands are not case sensitive. ie: capture = CAPTURE = cApTuRe

Type "capture" and press enter. A picture will be saved and displayed to you on the screen.
Type "set 2 8" and press enter. The camera will now take pictures with a contrast of -2 and resolution of 1600x1200.
**NOTE: be sure there is only a single space between "set" and "2". And a single space between "2" and "8".

From here you can request more pictures by typing "capture" and try other settings with the "set" command.

When you are finished, either close the command window or type "exit"




