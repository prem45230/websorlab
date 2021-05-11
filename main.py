import rospy
from sensor_msgs.msg import Image
from cefpython3 import cefpython as cef
import codecs
import autopy
#import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import threading
import base64
import tkinter as tk
import sys
from gtts import gTTS
import playsound
run = True



class LoadHandler(object):
	def OnLoadingStateChange(self,browser,is_loading,**_):
		pass

def say(text):
	tts = gTTS(text=text,lang='th')
	tts.save('sound.mp3')
	playsound.playsound('sound.mp3', True)

def command(func):
	a=[]
	b=[]
	x_temp=[]
	for i in range(10):
		b_time=time.time()
		a.append(random.randrange(1, 255))
		b.append(random.randrange(1, 255))
		x_temp.append(int(b_time-a_time))
	y = [a,b,x_temp]
	func.Call(y)

def command(function1,function2):
	global fun1,fun2
	fun1 = function1
	fun2 = function2

def setBindings(browser):
	bindings = cef.JavascriptBindings()
	bindings.SetFunction("setup",command)
	browser.SetJavascriptBindings(bindings)

def move():
	pass

def callback(data):
	print(data.data)
	if not run :
		exit()
	#rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def saveImg():
	bitmap_object = autopy.bitmap.capture_screen()
	bitmap_object.save('img/path.png')
	im = Image.open(r"img/path.png")
	left = 0
	top =  720
	right = 400
	bottom = 1000
	im1 = im.crop((left, top, right, bottom))
	im1.save("pathreal.png")
	try:
		retval, buffer = cv2.imencode('.jpg', cv2.imread("pathreal.png"))
		jpg_as_text = base64.b64encode(buffer)
		global fun2
		fun2.Call("data:image/jpeg;base64,/"+str(jpg_as_text)[3:-1])    
	except:
		pass

def loop_camera():
	global run
	while run:
		saveImg()


def main(frame):
	with codecs.open("joystick.html","r",encoding="utf-8") as file:
		global html_code
		html_code = file.read()
	sys.excepthook = cef.ExceptHook
	window_info = cef.WindowInfo(frame.winfo_id())
	window_info.SetAsChild(frame.winfo_id(),[0,0,1200,900])
	cef.Initialize()
	browser = cef.CreateBrowserSync(
		window_info,
		url=cef.GetDataUrl(html_code))
	browser.SetClientHandler(LoadHandler())
	setBindings(browser)
	cef.MessageLoop()

if __name__ == "__main__":
	say("hello sorlab")
	root = tk.Tk()
	root.title("BUEN AI Cashier")
	root.geometry('1200x900+0+0')
	frame = tk.Frame(root, height=900)
	frame.pack(side='top', fill='x')
	thread = threading.Thread(target=main, args=(frame,))
	thread.start()
	thread_camera = threading.Thread(target=loop_camera)
	thread_camera.start()
	root.mainloop()
	run = False
	#listener()
	"""
	run = False
	process.raise_exception()
	process.join()
	"""
