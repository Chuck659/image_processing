
from PIL import Image
from io import BytesIO
import datetime
import requests
import os

baseAddress = "http://192.168.1.203"
capture = "/capture"
submit = "/submit"

# Display a title bar.
print("**********************************************")
print("ContrastLightLevels:   Resolutions:")
print(" 0 = 0                 0 = 160x120")
print(" 1 = +1                1 = 176x144")
print(" 2 = +2                2 = 320x240")
print(" 3 = -1                3 = 352x288")
print(" 4 = -2                4 = 640x480")
print("                       5 = 800x600")
print("                       6 = 1024x768")
print("                       7 = 1280x1024")
print("                       8 = 1600x1200")
print("")
print("Type a command to execute")
print("")
print("COMMANDS - use the integer values inside the <>")
print("")
print(" SET <lightLevel> <resolution>")
print(" CAPTURE")
print(" EXIT")
print("")

dir_path = os.path.dirname(os.path.realpath(__file__)) + "\\"

command = [""]
while command[0] != "exit":
    command = input("Input: ").lower().split()

    try:

        if command[0] == "capture":
            fileName = dir_path + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S.jpg")
            response = requests.get(baseAddress + capture)
            image_bytes = BytesIO(response.content)
            image = Image.open(image_bytes)
            image.save(str(fileName))
            print("Saved to " + fileName)
            img = Image.open(fileName)
            img.show()

        if command[0] == "set":
            response = requests.post(baseAddress + submit, data={"rez": command[2], "light": command[1]})

    except:
        print("There was an error. Make sure the ESP is on and connected to the wifi and try again. ")
        exit()

