from pynput import keyboard
from psychopy.visual import *
from psychopy import monitors
from psychopy import core
from psychopy.sound import Sound
from psychopy import event
from random import *
from time import *
from datetime import datetime
import os
import pickle

TB = [[90, 45], [60, 60], [60, 90], [90, 45], [60, 0]]
timeorder = [[0,1,2,3,4], [1,0,3,2,4], [2,3,0,1,4], [3,2,1,0,4], [1,0,3,2,4]]
countorder = [[14,19], [17,22], [13,18], [16,21], [15,20]]
subtractionorder = [17,29,13,23,19]

MONITOR_WIDTH = 50
MONITOR_DIST = 55
MONITOR_SIZE = [1280,800]
MONITOR_UNITS = 'pix'
WINDOW_SIZE = (1200,900)

FIXATION_SIZE = 75

COLOR_BLACK = [0,0,0]
COLOR_WHITE = [255, 255, 255]

resourceRoot = os.path.join(os.environ['USERPROFILE'])+"/Desktop/MASTMain/MASTexp/RES_MASTexp/"
soundfile = "ELPHR.wav"

DATA_FOLDER = os.path.join(os.environ['USERPROFILE'])+"/Desktop/MASTMain/MASTexp/Data_MASTexp/"
SAVE_NAME = 'PREEMPT2_%s-MAST%sData.txt'

class LocalGame:

	action = None
	sound = None
	slidenum = None
	slideons = None

	def __init__(self):
		self.immerseT = []
		self.countT = []
		self.imgBank_instruct = []
		self.imgBank_proc = []
		self.slidenum = 0
		self.slideons = None
		self.localGraphics = GameGraphics()
		self.state = Interact()
		self.action = None
		self.sound = Sound(resourceRoot+soundfile)
		self.saveLoc = DATA_FOLDER+"PREEMPT2_%s/"+SAVE_NAME
		self.start()

	def start(self):
		self.generateTimeBank()
		self.generateImgBank()

	def generateTimeBank(self):
		times = timeorder[cycle-1]
		for x in times:
			self.immerseT.append(TB[x][0])
			self.countT.append(TB[x][1])
		self.countT = self.countT[:-1]

	def generateImgBank(self):
		self.imgBank_proc = ["Slide11.jpg", "Slide12.jpg"]
		for x in range(1,11):
			self.imgBank_instruct.append("Slide" + str(x) + ".jpg")
		countorder[cycle-1].extend((23,24))
		for x in countorder[cycle-1]:
			self.imgBank_proc.append("Slide" + str(x) + ".jpg")			

	def runInstructions(self):
		for x in self.imgBank_instruct:
			self.slidenum +=1
			self.localGraphics.baseScreen(x)
			self.slideons = str(datetime.now())
			self.action = self.state.actionCont()
			self.state.saveDataInst()
		self.slidenum = 0
		return

	def runFInstructions(self):
		self.localGraphics.baseScreen("Slide25.jpg")
		self.action = self.state.actionCont()

	def runMast(self):
		retcount = 0
		self.localGraphics.baseScreen(self.imgBank_proc[0])
		self.action = self.state.sleeper(3)
		for x in range(0,5):
			self.slidenum += 1
			self.localGraphics.baseScreen(self.imgBank_proc[1])
			self.sound.play()
			self.state.saveDataMast(self.immerseT[x], 'Immersion')
			self.action = self.state.sleeper(self.immerseT[x])
			if x > 0:
				retcount = 1
			if x < 4:
				self.slidenum += 1
				self.localGraphics.baseScreen(self.imgBank_proc[2+retcount])
				self.sound.play()
				self.state.saveDataMast(self.countT[x], 'Subtraction')
				self.action = self.state.sleeper(self.countT[x])
		self.sound.play()
		self.localGraphics.baseScreen(self.imgBank_proc[4])
		self.action = self.state.sleeper(90)
		self.localGraphics.baseScreen(self.imgBank_proc[5])
		self.action = self.state.actionCont()
		return

	def fixation(self, time):
		self.localGraphics.fixationScreen()
		self.action = self.state.sleeper(time)

class GameGraphics:

	monitor = None
	win = None
	imgRoot = None

	def __init__(self):
		self.monitor = monitors.Monitor('expMonitor', width = MONITOR_WIDTH, distance = MONITOR_DIST)
		self.monitor.setSizePix(MONITOR_SIZE)
		self.monitor.saveMon()
		self.win = Window(size = WINDOW_SIZE, fullscr=True, screen=0, allowGUI=False, allowStencil=False, monitor='expMonitor', color=COLOR_BLACK, colorSpace='rgb255', blendMode='avg', useFBO=True, units=MONITOR_UNITS)
		self.imgRoot = resourceRoot

	def baseScreen(self, img):
		bStim = ImageStim(self.win, image="%s%s" % (self.imgRoot, img))
		bStim.draw()
		self.win.update()

	def fixationScreen(self):
		fStim = TextStim(self.win, text="+", height=FIXATION_SIZE, color=COLOR_WHITE, colorSpace='rgb255')
		fStim.draw()
		self.win.update()

class Interact:

	choice = None
	exit_flag = False

	def __init__(self):
		self.choice = None
		self.exit_flag = False

	def actionCont(self):

		def keyPress(key):
			try:
				if key == keyboard.Key.space:
					self.choice = "Next"
					listener.stop()
			except:
				pass
			if key == keyboard.Key.esc:
				self.exit_flag = True
				listener.stop()

		with keyboard.Listener(on_release=keyPress) as listener:
			listener.join()
		if self.exit_flag == True:
			mast.localGraphics.win.close()
			sys.exit()
		return(self.choice)

	def sleeper(self, counter):

		event.clearEvents()
		exit_flag = event.waitKeys(maxWait=counter, keyList=['escape'])
		if exit_flag == ['escape']:
			mast.localGraphics.win.close()
			sys.exit()

	def saveDataInst(self):
		saveFrame = [ptp, cycle, mast.slidenum, mast.slideons]
		titleFrame = ['subID', 'cycle', 'slidenum', 'onstimestamp']
		for i, x in enumerate(saveFrame):
			saveFrame[i] = str(x)
		with open(mast.saveLoc % (ptp, ptp, 'Inst'), 'a') as file:
			if os.stat(mast.saveLoc % (ptp, ptp, 'Inst')).st_size == 0:
				file.write('\t'.join(titleFrame[0:]) + '\n')
			file.write('\t'.join(saveFrame[0:]) + '\n')

	def saveDataMast(self, ctTime, ctType):
		if ctType == 'Subtraction':
			subtrahend = subtractionorder[cycle-1]
		else:
			subtrahend = 'NA'
		saveFrame = [ptp, cycle, mast.slidenum, ctType, ctTime, subtrahend, mast.slideons]
		titleFrame = ['subID', 'cycle', 'slidenum', 'stimtype', 'timespent', 'subtrahend', 'onstimestamp']
		for i, x in enumerate(saveFrame):
			saveFrame[i] = str(x)
		with open(mast.saveLoc % (ptp, ptp, 'Stim'), 'a') as file:
			if os.stat(mast.saveLoc % (ptp, ptp, 'Stim')).st_size == 0:
				file.write('\t'.join(titleFrame[0:]) + '\n')
			file.write('\t'.join(saveFrame[0:]) + '\n')

if __name__ == "__main__":
	print("[1] Baseline Fixation"+"\n"+"[2] MAST")
	version = int(input("Please enter version (1 or 2):  "))
	ptp = input("Participant ID:   ")
	cycle = int(input("Cycle #:   "))
	if not os.path.exists(resourceRoot):
		print('Resource folder not found. Should be: %s' % resourceRoot)
		input('Press ENTER to exit')
		sys.exit()
	if not os.path.exists(DATA_FOLDER):
		os.mkdir(DATA_FOLDER)
	if not os.path.exists(DATA_FOLDER+"PREEMPT2_%s/" % ptp):
		os.mkdir(DATA_FOLDER+"PREEMPT2_%s/" % ptp)
	while cycle not in [1,2,3,4,5]:
		cycle = input("Not a number between 1 and 5. Try again. Cycle #:   ")
	mast = LocalGame()
	mast.runFInstructions()
	if version == 2:
		mast.fixation(90)
		mast.runInstructions()
		mast.runMast()
	elif version == 1:
		mast.fixation(300)
	mast.localGraphics.win.close()
	sys.exit()