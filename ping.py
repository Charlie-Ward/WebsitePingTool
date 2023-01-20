import requests
import time
from datetime import datetime

responseCode = ""
responseTime = ""

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

FileTitle = f"{current_time}.txt"

File = open(FileTitle, "a")
File.truncate(0)
File.close()

def fileNewLine(FileToEdit):
	File = FileToEdit
	File.write("\n")

def pingSuccessFileWrite(FileToEdit, currentTime, pingedWebsite,  responseCode, responseTime):
	File = FileToEdit
	File.write("Ping at: ")
	File.write(currentTime)
	File.write(" to: ")
	File.write(pingedWebsite)
	File.write(" {")
	fileNewLine(File)
	File.write("\tStatus Code: ")
	File.write(str(responseCode))
	fileNewLine(File)
	File.write("\tResponse Time: ")
	File.write(str(responseTime))
	fileNewLine(File)
	File.write("}")
	fileNewLine(File)

def ping(url):
	try:
		response = requests.get(url)
		print(f"Status Code: {response.status_code}")
		print(f"Response Time: {response.elapsed.total_seconds()} seconds")
		responseCode = response.status_code
		responseTime = response.elapsed.total_seconds()
		File = open(FileTitle, "a")
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		pingSuccessFileWrite(File, current_time, url, responseCode, responseTime)
		File.close()
	except requests.exceptions.RequestException as e:
		print(f"Request failed: {e}")
		File = open(FileTitle, "a")
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		ResponseText = (f"Request failed: {e}")
		File.write(str(ResponseText))
		fileNewLine(File)
		File.close()

print("INITAL SETUP")

print("Please input a website to ping")
websiteToPingBeforePrefix = input("www.")
print("Please enter how frequently you want to ping the website. If you want it to only happen once please input 0")
timeBetween = int(input())

websiteToPingWithFilePrefix = f'www.{websiteToPingBeforePrefix}'
websiteToPingWithCodePrefix = f'http://{websiteToPingBeforePrefix}'

File = open(FileTitle, "a")
File.write("Pinging Website:")
fileNewLine(File)
File.write(websiteToPingWithFilePrefix)
for i in range(3):
	fileNewLine(File)
File.close()

print("STARTING PINGS")

if timeBetween == 0:
	ping(websiteToPingWithCodePrefix)
else:
	while True:
		ping(websiteToPingWithFilePrefix)
		time.sleep(timeBetween)