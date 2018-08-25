"""
Author: Kyle J. LaFollette
Department of Psychiatry, University of Arizona
Correspondance: kjlafoll@psychiatry.arizona.edu

This script runs Chiu et al.'s 2015 experiment investigating the effect 
of peer influence, or 'other-conferred utility', on lottery 
choice decision-making.

Code has been adapted from that utilized by the original authors to 
operate standalone in Python, using PsychoPy for stimulus presentation, 
and pynput for event monitoring.
"""

from pynput import keyboard
from psychopy.visual import *
from psychopy import monitors
from psychopy import core
from random import *
from time import *
import os
import pickle

#===================================================================================================
# CONSTANTS
#===================================================================================================

# 8 payoff value vectors
PAYOFF_BANK = [["$33.2", "$23.1", "$56.8", "$1.7"], ["$20.8", "$15.2", "$37.4", "$1.1"], ["$19.6", "$18.0", "$38.6", "$0.9"], ["$25.5", "$24.9", "$50.8", "$1.3"], ["$24.4", "$23.0", "$51.1", "$1.2"], ["$26.7", "$21.4", "$51.6", "$1.4"], ["$26.5", "$25.2", "$55.3", "$1.3"], ["$28.3", "$26.6", "$55.5", "$1.6"]]
PROB_BANK = [4, 5, 6, 7, 8, 9]

# COLOR CODE: REB, GREEN, BLUE
COLOR_WHITE = [255, 255, 255]
COLOR_RED = [255, 0, 0]
COLOR_BLACK = [0, 0, 0]

MONITOR_WIDTH = 50
MONITOR_DIST = 55
MONITOR_SIZE = [1280,800]
MONITOR_UNITS = 'pix'
WINDOW_SIZE = (1200,900)

# STIMULUS POSITIONS
PARTNER_TEXT = (-150,300)
YOU_TEXT = (150,300)
PARTNER_CIRCLE = (-150,150)
YOU_CIRCLE = (150,150)
GAMBLE_L_CIRCLE = (-150,-150) 
GAMBLE_R_CIRCLE = (150,-150)
LINE_POS = [(-300,0), (300,0)]
REVEALPOS_POS = (0, -150)

NEWROUND_SIZE = 100
TEXT_SIZE = 40
CIRCLE_SIZE = 250

ROUND_COUNT = 96

DATA_FOLDER = 'PInfMain_Files/data/'
SAVE_NAME = 'PREEMPT1_%s-PeerInfluenceData.txt'

#===================================================================================================
# TASK CLASSES
#===================================================================================================

class LocalGame:

	# image banks
	imgBank_inactive = []
	imgBank_cue = []
	imgBank_active = []
	imgBank_control = []

	# variables
	round = None
	subID = None
	control_bank = None
	localGraphics = None
	state = None
	crtIndex = None
	crtChoice = None
	saveFrame = None
	saveLoc = None

	def __init__(self):
		self.round = 0
		self.saveLoc = DATA_FOLDER+SAVE_NAME
		self.subID = input('Please enter 4-digit subject identifier (i.e., 0999): ')
		while os.path.exists(self.saveLoc % self.subID):
			self.subID = input('Data already exists for subject identifier %s. Please provide another ID: ' % self.subID)
		self.control_bank = None
		self.localGraphics = GameGraphics()
		self.state = Interact()
		self.crtIndex = None
		self.crtChoice = None
		self.saveFrame = []
		self.start()

	def start(self):
		self.generateControlBank()
		shuffle(self.control_bank)
		self.generateImgBanks()

	def generateControlBank(self):
		chosenvectors = list(range(8))
		shuffle(chosenvectors)
		chosenvectors = chosenvectors[:4]
		chosenprobs = list(range(4,10))
		chosenconds = list(range(0,3)) # 0 is solo, 1 is info safe, 2 is info risky
		self.control_bank = []
		for x in chosenvectors:
			for y in chosenprobs:
				for z in chosenconds:
					self.control_bank.append({ 
						"bank" : x,
						"safe_Hpayoff" : PAYOFF_BANK[x][0],
						"safe_Lpayoff" : PAYOFF_BANK[x][1],
						"risky_Hpayoff" : PAYOFF_BANK[x][2],
						"risky_Lpayoff" : PAYOFF_BANK[x][3],
						"p_gamble" : y/10,
						"condition" : z
						})

	def generateImgBanks(self):
		option_order = ["A", "B"]
		vector_order = ["V0", "V1", "V2", "V3", "V4", "V5", "V6", "V7"]
		prob_order = ["19", "28", "37", "46", "55", "64", "73", "82", "91", "10"]
		# define imgBank_active
		for i in option_order:            
			tmp4active2 = []
			for j in vector_order:
				tmp4active1 = []
				for k in prob_order:
					tmp4active1.append("ACTIVE_P" + k + "_" + j + "_" + i + ".jpg")
				tmp4active2.append(tmp4active1)
			self.imgBank_active.append(tmp4active2)

		# define imgBank_inactive & imgBank_cue	
		for i in prob_order:
			self.imgBank_inactive.append("INACTIVE_P" + i + ".jpg")
			self.imgBank_cue.append("CUE_P" + i + ".jpg")
			self.imgBank_control.append("CONTROL_P" + i + ".jpg")	

	def revealPosition(self):
		self.localGraphics.positionScreenTxt(["Position 1", "Position 2"], 0)
		self.localGraphics.positionScreenImg(self.imgBank_inactive[9])
		sleep(6)
		self.localGraphics.positionScreenTxt(["Partner", "You"], 1)
		sleep(4)
		return

	def runStage0(self):
		self.localGraphics.clearDisplay()
		self.localGraphics.newroundScreen()
		self.crtIndex = self.control_bank[self.round]
		sleep(uniform(2, 3))
		return

	def runSingleStage1(self):
		self.localGraphics.clearDisplay()
		partner = self.imgBank_control[int(self.crtIndex['p_gamble']*10-1)]
		target = self.imgBank_inactive[int(self.crtIndex['p_gamble']*10-1)]
		choiceL = self.imgBank_active[0][self.crtIndex['bank']][int(self.crtIndex["p_gamble"]*10-1)]
		choiceR = self.imgBank_active[1][self.crtIndex['bank']][int(self.crtIndex["p_gamble"]*10-1)]
		imglist = [partner, target, choiceL, choiceR]
		self.localGraphics.baseScreen(imglist, 0)
		sleep(6)
		return

	def runSingleStage2(self):
		cue = self.imgBank_cue[int(self.crtIndex['p_gamble']*10-1)]
		self.localGraphics.cueScreen(cue)
		self.crtChoice = self.state.selectChoice()
		return

	def runSingleStage3(self):
		if self.crtChoice == "L":
			decision = self.imgBank_active[0][self.crtIndex['bank']][int(self.crtIndex['p_gamble']*10-1)]
			self.crtIndex['choice'] = 0
		elif self.crtChoice == "R":
			decision = self.imgBank_active[1][self.crtIndex['bank']][int(self.crtIndex['p_gamble']*10-1)]
			self.crtIndex['choice'] = 1
		self.localGraphics.reviewScreen(decision)
		sleep(2)
		return

	def runGroupStage1(self):
		self.localGraphics.clearDisplay()
		partner = self.imgBank_cue[int(self.crtIndex['p_gamble']*10-1)]
		target = self.imgBank_inactive[int(self.crtIndex['p_gamble']*10-1)]
		choiceL = self.imgBank_active[0][self.crtIndex['bank']][int(self.crtIndex["p_gamble"]*10-1)]
		choiceR = self.imgBank_active[1][self.crtIndex['bank']][int(self.crtIndex["p_gamble"]*10-1)]
		imglist = [partner, target, choiceL, choiceR]
		self.localGraphics.baseScreen(imglist, 1)
		sleep(uniform(1.8, 3.8))
		return

	def runGroupStage2(self):
		if self.crtIndex['condition'] == 1: # Partner chose safe (left)
			choiceP = self.imgBank_active[0][self.crtIndex['bank']][int(self.crtIndex["p_gamble"]*10-1)]
		elif self.crtIndex['condition'] == 2: # Partner chose risky (right)
			choiceP = self.imgBank_active[1][self.crtIndex['bank']][int(self.crtIndex["p_gamble"]*10-1)]
		self.localGraphics.partnerreviewScreen(choiceP)
		sleep(2)
		return

	def runGroupStage3(self):
		cue = self.imgBank_cue[int(self.crtIndex['p_gamble']*10-1)]
		self.localGraphics.cueScreen(cue)
		self.crtChoice = self.state.selectChoice()
		return

	def runGroupStage4(self):
		if self.crtChoice == "L":
			decision = self.imgBank_active[0][self.crtIndex['bank']][int(self.crtIndex['p_gamble']*10-1)]
			self.crtIndex['choice'] = 0
		elif self.crtChoice == "R":
			decision = self.imgBank_active[1][self.crtIndex['bank']][int(self.crtIndex['p_gamble']*10-1)]
			self.crtIndex['choice'] = 1
		self.localGraphics.reviewScreen(decision)
		sleep(2)
		return

	def saveData(self):
		saveFrame = []
		titleFrame = []
		self.crtIndex['trial'] = self.round + 1
		self.crtIndex['subID'] = self.subID
		for x in list(self.crtIndex.keys()):
			saveFrame.append(self.crtIndex[x])
			if self.round == 0:
				titleFrame.append(x)
		for i, x in enumerate(saveFrame):
			saveFrame[i] = str(x)
		with open(self.saveLoc % self.subID, 'a') as file:
			if self.round == 0:
				file.write('\t'.join(titleFrame[0:]) + '\n')
			file.write('\t'.join(saveFrame[0:]) + '\n')

class GameGraphics:

	monitor = None
	win = None
	imgRoot = None
	staticStim = None

	def __init__(self):
		self.monitor = monitors.Monitor('expMonitor', width = MONITOR_WIDTH, distance = MONITOR_DIST)
		self.monitor.setSizePix(MONITOR_SIZE)
		self.monitor.saveMon()
		self.win = Window(size = WINDOW_SIZE, fullscr=False, screen=0, allowGUI=False, allowStencil=False, monitor='expMonitor', color=COLOR_BLACK, colorSpace='rgb255', blendMode='avg', useFBO=True, units=MONITOR_UNITS)
		self.imgRoot = "PInfMain_Files/ImgSource/"
		self.staticStim = []

	def newroundScreen(self):
		text = TextStim(self.win, text="New Round", pos=(0, 0), height=NEWROUND_SIZE, color=COLOR_WHITE, colorSpace='rgb255')
		text.draw()
		if len(self.staticStim) > 0:
			for x in range(len(self.staticStim)):
				for y in list(self.staticStim[x].keys()):
					self.staticStim[x][y].setAutoDraw(False)
			self.staticStim = []
		self.win.update()

	def positionScreenImg(self, img):
		img_pStim = {
		"img_p1" : ImageStim(self.win, image="%s%s" % (self.imgRoot, img), pos=PARTNER_CIRCLE, size=CIRCLE_SIZE),
		"img_p2" : ImageStim(self.win, image="%s%s" % (self.imgRoot, img), pos=YOU_CIRCLE, size=CIRCLE_SIZE)
		}
		self.staticStim.append(img_pStim)
		for x in list(self.staticStim[0].keys()):
			self.staticStim[0][x].setAutoDraw(True)
		self.win.update()

	def positionScreenTxt(self, titlelist, timepoint):
		if timepoint == 0:
			p2color = COLOR_WHITE
		else:
			p2color = COLOR_RED
		txt_pStim = {
		"txt_p1" : TextStim(self.win, text=titlelist[0], pos=PARTNER_TEXT, height=TEXT_SIZE, color=COLOR_WHITE, colorSpace='rgb255'),
		"txt_p2" : TextStim(self.win, text=titlelist[1], pos=YOU_TEXT, height=TEXT_SIZE, color=p2color, colorSpace='rgb255'),
		"txt_bottom" : TextStim(self.win, text="Choosing order...", pos=REVEALPOS_POS, height=TEXT_SIZE, color=COLOR_WHITE, colorSpace='rgb255')
		}
		if timepoint != 0:
			txt_pStim["txt_bottom"].text = "You will be POSITION 2"
		for x in list(txt_pStim.keys()):
			txt_pStim[x].draw()
		if timepoint != 0:
			self.win.update()

	def baseScreen(self, imglist, isGroup):
		bStim = {
		"txt_partner" : TextStim(self.win, text="Partner", pos=PARTNER_TEXT, height=TEXT_SIZE, color=COLOR_WHITE, colorSpace='rgb255'),
		"txt_you" : TextStim(self.win, text="You", pos=YOU_TEXT, height=TEXT_SIZE, color=COLOR_WHITE, colorSpace='rgb255'),
		"img_partner" : ImageStim(self.win, image="%s%s" % (self.imgRoot, imglist[0]), pos=PARTNER_CIRCLE, size=CIRCLE_SIZE),
		"img_you" : ImageStim(self.win, image="%s%s" % (self.imgRoot, imglist[1]), pos=YOU_CIRCLE, size=CIRCLE_SIZE),
		"line" : Line(self.win, start=LINE_POS[0], end=LINE_POS[1], lineColor=COLOR_WHITE),
		"img_choiceL" : ImageStim(self.win, image="%s%s" % (self.imgRoot, imglist[2]), pos=GAMBLE_L_CIRCLE, size=CIRCLE_SIZE),
		"img_choiceR" : ImageStim(self.win, image="%s%s" % (self.imgRoot, imglist[3]), pos=GAMBLE_R_CIRCLE, size=CIRCLE_SIZE)
		}
		if isGroup == 0:
			bStim["txt_partner"].text = "------"
		self.staticStim.append(bStim)
		for x in list(self.staticStim[0].keys()):
			self.staticStim[0][x].setAutoDraw(True)
		self.win.update()
		if isGroup == 0:
			self.staticStim[0]['img_you'].setAutoDraw(False)
		elif isGroup == 1:
			self.staticStim[0]['img_partner'].setAutoDraw(False)

	def cueScreen(self, img):
		cStim = {
		"img_cue" : ImageStim(self.win, image="%s%s" % (self.imgRoot, img), pos=YOU_CIRCLE, size=CIRCLE_SIZE),
		"txt_cue" : TextStim(self.win, text="You", pos=YOU_TEXT, height=TEXT_SIZE, color=COLOR_RED, colorSpace='rgb255')
		}
		for x in list(cStim.keys()):
			cStim[x].draw()
		self.win.update()

	def reviewScreen(self, img):
		rStim = {
		"img_choice" : ImageStim(self.win, image="%s%s" % (self.imgRoot, img), pos=YOU_CIRCLE, size=CIRCLE_SIZE),
		"txt_you" : TextStim(self.win, text="You", pos=YOU_TEXT, height=TEXT_SIZE, color=COLOR_WHITE, colorSpace='rgb255')
		}
		for x in list(rStim.keys()):
			rStim[x].draw()
		self.win.update()

	def partnerreviewScreen(self, img):
		prStim = {
		"img_pchoice" : ImageStim(self.win, image="%s%s" % (self.imgRoot, img), pos=PARTNER_CIRCLE, size=CIRCLE_SIZE),
		"txt_partner" : TextStim(self.win, text="Partner", pos=PARTNER_TEXT, height=TEXT_SIZE, color=COLOR_WHITE, colorSpace='rgb255')
		}
		self.staticStim.append(prStim)
		for x in list(self.staticStim[1].keys()):
			self.staticStim[1][x].setAutoDraw(True)
		self.win.update()
		self.staticStim[0]['img_you'].setAutoDraw(False)

	def clearDisplay(self):
		self.win.flip()

class Interact:

	choice = None

	def __init__(self):
		self.choice = None

	def selectChoice(self):
		def keyPress(key):
			try:
				if key.char == '1':
					print("Left Choice!")
					self.choice = "L"
					listener.stop()
				elif key.char == '0':
					print("Right Choice!")
					self.choice = "R"
					listener.stop()
			except:
				pass
			if key == keyboard.Key.esc:
				listener.stop()
				Window.close()
				core.quit()
		with keyboard.Listener(on_press=keyPress) as listener:
			listener.join()
		return(self.choice)

def runRound(game):
	game.runStage0()
	if game.crtIndex['condition'] == 0:
		game.runSingleStage1()
		game.runSingleStage2()
		game.runSingleStage3()
	else:
		game.runGroupStage1()
		game.runGroupStage2()
		game.runGroupStage3()
		game.runGroupStage4()
	game.saveData()
	game.round += 1

if __name__ == "__main__":
	if not os.path.exists(DATA_FOLDER):
		os.mkdir(DATA_FOLDER)
	game = LocalGame()
	game.revealPosition()
	for x in range(ROUND_COUNT):
		runRound(game)
