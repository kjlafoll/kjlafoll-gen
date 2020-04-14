"""
Author: Kyle J. LaFollette
Department of Psychiatry, University of Arizona
Correspondance: kjlafoll@psychiatry.arizona.edu

This script runs the Active Maintenance Offloading Task investigating
the combined effect of peer influence and visual working memory
capacity on delayed visual discrimination.
"""

from psychopy.visual import *
from psychopy.event import *
from psychopy import monitors
from psychopy import core
import pygame
from pygame.locals import *
from pyglet.window import key
from random import *
from time import *
from datetime import datetime
import os, sys
import pickle

#===================================================================================================
# CONSTANTS
#===================================================================================================

# 8 payoff value vectors
REWARD_BANK = ['$5', '$15', '$40']
ORI_BANK = [45, 90, 135, 180]
DEVIATION_BANK = ['C', 'CC']
PEER_BANK = ['Y', 'N']
HEMI_BANK = ['L', 'R']

# COLOR CODE: REB, GREEN, BLUE
COLOR_WHITE = [255, 255, 255]
COLOR_RED = [255, 0, 0]
COLOR_BLACK = [0, 0, 0]
COLOR_BLUE = [0, 0, 255]
COLOR_YELLOW = [255, 255, 0]

MONITOR_WIDTH = 50
MONITOR_DIST = 55
MONITOR_SIZE = [1280,800]
MONITOR_UNITS = 'pix'
WINDOW_SIZE = (1200,900)

GRATING_DIST = 600
GRATING_SIZE = 400
GRATING_SF = .05
GRATING_MASK = 'gauss'
OPACITIES = 0.5

FIXATION_SIZE = 75
TEXT_SIZE = 75
NEWROUND_SIZE = 100

ROUND_COUNT = 144
BLOCK_SIZE = 24
MAX_ERROR = 45
ORI_JITTER = 45/2
PEER_JITTER = 60/2
LINE_WIDTH = 6

NEWROUND_TIME = .5
REWARD_TIME = 2
FIXATION_TIME = 1
PRIME_TIME = 1.5
MASK_TIME = .5
CUEDELAY_TIME = 7.5
PROBE_TIME = 3
REVIEW_TIME = 2

DATA_FOLDER = "AMOexp/Data_AMOexp/"
IMG_FOLDER = "AMOexp/RES_AMOexp/"
SAVE_NAME = 'PREEMPT1_%s-AMOData.txt'
INSTRUCT_SAVE_NAME = 'PREEMPT1_%s-AMOInstructData.txt'
QUIZ_SAVE_NAME = 'PREEMPT1_%s-AMOQuizData.txt'

#===================================================================================================
# TASK CLASSES
#===================================================================================================

class LocalGame:

	# image banks
	imgBank_instruct = []
	imgBank_quiz = []

	# variables
	round = None
	subID = None
	localGraphics = None
	state = None
	control_bank = None
	crtIndex = None
	crtChoice = None
	saveFrame = None
	saveLoc = None

	def __init__(self):
		self.round = 0
		self.saveLoc = DATA_FOLDER+SAVE_NAME
		self.subID = input('Please enter 4-digit subject identifier (i.e., 0999):   ')
		self.cycle = int(input('Please enter Day #:   '))
		while os.path.exists(self.saveLoc % self.subID):
			self.subID = input('Data already exists for subject identifier %s. Please provide another ID: ' % self.subID)
		self.control_bank = None
		self.localGraphics = GameGraphics()
		self.state = Interact()
		self.crtIndex = None
		self.jitter = None
		self.crtChoice = None
		self.saveFrame = []
		self.start()

	def start(self):
		self.generateControlBank()
		shuffle(self.control_bank)
		self.generateBlockBank()
		self.generateImgBanks()

	def generateControlBank(self):
		self.control_bank = []
		for v in REWARD_BANK:
			for w in ORI_BANK:
				for x in list(set(ORI_BANK) - set([w])):
					for y in DEVIATION_BANK:
						if y == "C":
							dev = randint(45, 90)
						elif y == "CC":
							dev = randint(-90, -45)
						jitter = uniform(-ORI_JITTER, ORI_JITTER)
						peerjitter = uniform(-PEER_JITTER, PEER_JITTER)
						for z in PEER_BANK:
							self.control_bank.append({
								"reward" : v,
								"cueprime_Ori" : w,
								"noncueprime_Ori" : x,
								"deviation" : dev,
								"probe_Ori" : w + dev,
								"peer_Inf" : z,
								"cueprime_Hemi" : choice(HEMI_BANK),
								"jitter" : jitter,
								"peer_Jitter" : peerjitter
								})

	def generateBlockBank(self):
		self.block_bank = [0]
		block = BLOCK_SIZE
		while block < ROUND_COUNT:
			self.block_bank.append(block)
			block += block

	def generateImgBanks(self):
		# define imgBank_instruct & imgBank_quiz
		for x in range(1,13):
			self.imgBank_instruct.append("Slide" + str(x) + ".JPG")
		# for x in range(12,23):
		# 	self.imgBank_quiz.append("Slide" + str(x) + ".jpg")

	def runInstructions(self):
		self.slidenum = 0
		for x in self.imgBank_instruct:
			self.slidenum +=1
			self.localGraphics.instructScreen(x)
			self.slideons = str(datetime.now())
			self.action = self.state.actionCont()
			self.state.saveDataInst()
		self.slidenum = 0
		return

	# def runQuiz(self):
	# 	self.slidenum = 0
	# 	self.answers = ['2', '3', '2', '4', '1', '2', '2', '1', '1', '2', '3']
	# 	for i, x in enumerate(self.imgBank_quiz):
	# 		self.slidenum +=1
	# 		self.localGraphics.instructScreen(x)
	# 		self.slideons = str(datetime.now())
	# 		self.action = self.state.actionQuiz()
	# 		if self.action == self.answers[i]:
	# 			self.accuracy = 1
	# 		else:
	# 			self.accuracy = 0
	# 		self.state.saveDataQuiz()
	# 	self.slidenum = 0
	# 	return

	def runStage0(self): #NEW ROUND
		self.localGraphics.clearDisplay()
		text = "NEW ROUND"
		for i, x in enumerate(self.block_bank):
			if self.round == x:
				text = "BLOCK %s : NEW ROUND" % str(i+1)
		self.localGraphics.textScreen(text)
		self.crtIndex = self.control_bank[self.round]
		self.jitter = self.crtIndex['jitter']
		self.peerjitter = self.crtIndex['peer_Jitter']
		self.state.actionWait(NEWROUND_TIME)
		return

	def runStage1(self): #REWARD
		self.localGraphics.clearDisplay()
		self.localGraphics.textScreen(self.crtIndex['reward'])
		self.state.actionWait(REWARD_TIME)
		return

	def runStage2(self): #FIXATION
		self.localGraphics.clearDisplay()
		fixation = '+'
		color = COLOR_WHITE
		imglist = [fixation, color]
		self.localGraphics.fixationScreen(imglist)
		self.state.actionWait(FIXATION_TIME)
		return

	def runStage3(self): #PRIMES
		self.localGraphics.clearDisplay()
		fixation = '+'
		color = COLOR_WHITE
		self.crtIndex['cueprime_jOri'] = int(self.crtIndex['cueprime_Ori']) + self.jitter
		self.crtIndex['noncueprime_jOri'] = int(self.crtIndex['noncueprime_Ori']) + self.jitter

		if self.crtIndex['cueprime_jOri'] < 0:
			self.crtIndex['cueprime_jOri'] = self.crtIndex['cueprime_jOri'] + 180
		elif self.crtIndex['cueprime_jOri'] > 180:
			self.crtIndex['cueprime_jOri'] = self.crtIndex['cueprime_jOri'] - 180

		if self.crtIndex['noncueprime_jOri'] < 0:
			self.crtIndex['noncueprime_jOri'] = self.crtIndex['noncueprime_jOri'] + 180
		elif self.crtIndex['noncueprime_jOri'] > 180:
			self.crtIndex['noncueprime_jOri'] = self.crtIndex['noncueprime_jOri'] - 180

		if self.crtIndex['cueprime_Hemi'] == 'L':
			leftPrime = self.crtIndex['cueprime_jOri']
			rightPrime = self.crtIndex['noncueprime_jOri']
		elif self.crtIndex['cueprime_Hemi'] == 'R':
			leftPrime = self.crtIndex['noncueprime_jOri']
			rightPrime = self.crtIndex['cueprime_jOri']
		imglist = [fixation, color, leftPrime, rightPrime]
		self.localGraphics.primeScreen(imglist)
		self.state.actionWait(PRIME_TIME)
		return

	def runStage4(self): #MASKS
		self.localGraphics.clearDisplay()
		fixation = '+'
		color = COLOR_WHITE
		imglist = [fixation, color]
		self.localGraphics.maskScreen(imglist)
		self.state.actionWait(MASK_TIME)
		return

	def runStage5(self): #CUE/DELAY
		self.localGraphics.clearDisplay()
		if self.crtIndex['cueprime_Hemi'] == 'L':
			fixation = '<'
		elif self.crtIndex['cueprime_Hemi'] == 'R':
			fixation = '>'
		color = COLOR_RED
		imglist = [fixation, color]
		self.localGraphics.fixationScreen(imglist)
		self.state.actionWait(CUEDELAY_TIME)
		return

	def runStage6(self): #PROBE
		self.localGraphics.clearDisplay()
		pygame.event.clear()
		if self.crtIndex['cueprime_Hemi'] == 'L':
			fixation = '<'
			probePos = -1
		elif self.crtIndex['cueprime_Hemi'] == 'R':
			fixation = '>'
			probePos = 1
		color = COLOR_RED
		self.crtIndex['probe_jOri'] = int(self.crtIndex['probe_Ori']) + self.jitter
		self.crtIndex['peer_Ori'] = int(self.crtIndex['cueprime_jOri']) + self.peerjitter
		self.crtRotate = 0
		probe = int(self.crtIndex['probe_Ori']) + self.jitter
		imglist = [fixation, color, probe, probePos]
		self.localGraphics.probeScreen(imglist)
		self.state.actionRotateClear()
		then = datetime.now(); now = datetime.now(); diff = now-then
		while diff.total_seconds() < PROBE_TIME:
			sleep(.0001)
			now = datetime.now()
			diff = now-then
			self.crtRotate += self.state.actionRotate()
			game.localGraphics.staticStim[0]["probe"].ori = int(self.crtIndex['probe_Ori']) + self.jitter + self.crtRotate
			if game.localGraphics.staticStim[0]["probe"].ori < 0:
				game.localGraphics.staticStim[0]["probe"].ori = game.localGraphics.staticStim[0]["probe"].ori + 180
			elif game.localGraphics.staticStim[0]["probe"].ori > 180:
				game.localGraphics.staticStim[0]["probe"].ori = game.localGraphics.staticStim[0]["probe"].ori - 180
			game.localGraphics.win.update()
		self.crtIndex['final_Ori'] = game.localGraphics.staticStim[0]["probe"].ori
		if self.crtRotate > 0:
			self.crtIndex['rotation_Dir'] = 'Clockwise'
		elif self.crtRotate < 0:
			self.crtIndex['rotation_Dir'] = 'Counterclockwise'
		elif self.crtRotate == 0:
			self.crtIndex['rotation_Dir'] = 'NA'
		for x in list(game.localGraphics.staticStim[0].keys()):
			game.localGraphics.staticStim[0][x].setAutoDraw(False)
		game.localGraphics.win.update()
		game.localGraphics.staticStim = []
		return

	def runStage7(self): #REVIEW
		self.localGraphics.clearDisplay()
		if self.crtIndex['cueprime_Hemi'] == 'L':
			fixation = '<'
			probePos = -1
		elif self.crtIndex['cueprime_Hemi'] == 'R':
			fixation = '>'
			probePos = 1
		color = COLOR_RED
		imglist = [fixation, color, probePos]
		self.localGraphics.reviewScreen(imglist)
		self.state.actionWait(REVIEW_TIME)
		return

	def saveData(self):
		saveFrame = []
		titleFrame = []
		self.crtIndex['trial'] = self.round + 1
		self.crtIndex['subID'] = self.subID
		self.crtIndex['day'] = self.cycle
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

	def __init__(self):
		self.monitor = monitors.Monitor('expMonitor', width = MONITOR_WIDTH, distance = MONITOR_DIST)
		self.monitor.setSizePix(MONITOR_SIZE)
		self.monitor.saveMon()
		self.win = Window(winType='pygame', size=WINDOW_SIZE, fullscr=True, screen=0, allowGUI=True, allowStencil=False, monitor='expMonitor', color=COLOR_BLACK, colorSpace='rgb255', blendMode='avg', useFBO=True, units=MONITOR_UNITS, mouseVisible=False)
		self.win.mouseVisible = False
		self.staticStim = []

	def instructScreen(self, img):
		bStim = ImageStim(self.win, image="%s%s" % (IMG_FOLDER, img))
		bStim.draw()
		self.win.update()

	def textScreen(self, text):
		text = TextStim(self.win, text=text, pos=(0, 0), height=NEWROUND_SIZE, color=COLOR_WHITE, colorSpace='rgb255')
		text.draw()
		self.win.update()

	def primeScreen(self, imglist):
		primeStim = {
		"fixation" : TextStim(self.win, text=imglist[0], height=FIXATION_SIZE, color=imglist[1], colorSpace='rgb255'),
		"leftPrime" : GratingStim(self.win, sf=GRATING_SF, ori=imglist[2], pos=(-GRATING_DIST/2, 0), size=GRATING_SIZE, mask=GRATING_MASK),
		"rightPrime" : GratingStim(self.win, sf=GRATING_SF, ori=imglist[3], pos=(GRATING_DIST/2, 0), size=GRATING_SIZE, mask=GRATING_MASK)
		}
		for x in list(primeStim.keys()):
			primeStim[x].draw()
		self.win.update()

	def fixationScreen(self, imglist):
		fixationStim = {
		"fixation": TextStim(self.win, text=imglist[0], height=FIXATION_SIZE, color=imglist[1], colorSpace='rgb255')
		}
		# if imglist[0] == '>':
		# 	fixationStim['highlight'] = psychopy.visual.Rect(self.win, pos=(GRATING_DIST/2, 0), height=GRATING_SIZE, width=GRATING_SIZE, fillColor=None, lineWidth=LINE_WIDTH, lineColor=COLOR_RED, lineColorSpace='rgb255')
		# elif imglist[0] == '<':
		# 	fixationStim['highlight'] = psychopy.visual.Rect(self.win, pos=(-GRATING_DIST/2, 0), height=GRATING_SIZE, width=GRATING_SIZE, fillColor=None, lineWidth=LINE_WIDTH, lineColor=COLOR_RED, lineColorSpace='rgb255')
		for x in list(fixationStim.keys()):
			fixationStim[x].draw()
		self.win.update()

	def maskScreen(self, imglist):
		maskStim = {
		"fixation": TextStim(self.win, text=imglist[0], height=FIXATION_SIZE, color=imglist[1], colorSpace='rgb255'),
		"mask1" : GratingStim(self.win, sf=GRATING_SF, ori=0, pos=(-GRATING_DIST/2, 0), mask=GRATING_MASK, size=GRATING_SIZE),
		"mask2" : GratingStim(self.win, sf=GRATING_SF, ori=90, pos=(-GRATING_DIST/2, 0), mask=GRATING_MASK, size=GRATING_SIZE, opacity=OPACITIES),
		"mask3" : GratingStim(self.win, sf=GRATING_SF, ori=0, pos=(GRATING_DIST/2, 0), mask=GRATING_MASK, size=GRATING_SIZE),
		"mask4" : GratingStim(self.win, sf=GRATING_SF, ori=90, pos=(GRATING_DIST/2, 0), mask=GRATING_MASK, size=GRATING_SIZE, opacity=OPACITIES)
		}
		for x in list(maskStim.keys()):
			maskStim[x].draw()
		self.win.update()

	def probeScreen(self, imglist):
		probeStim = {
		"fixation" : TextStim(self.win, text=imglist[0], height=FIXATION_SIZE, color=imglist[1], colorSpace='rgb255'),
		"probe" : GratingStim(self.win, sf=GRATING_SF, ori=imglist[2], pos=(imglist[3]*GRATING_DIST/2, 0), size=GRATING_SIZE, mask=GRATING_MASK),
		}
		if game.crtIndex['peer_Inf'] == 'Y':
			probeStim["peerLine"] = Line(self.win, pos=(imglist[3]*GRATING_DIST/2, 0), start=(0,-GRATING_SIZE/2), end=(0,GRATING_SIZE/2), ori=game.crtIndex['peer_Ori'], opacity=OPACITIES, lineWidth=LINE_WIDTH, lineColor=COLOR_RED, lineColorSpace='rgb255')
			probeStim["peerText"] = TextStim(self.win, pos=(imglist[3]*GRATING_DIST/2, 300), text='Partner', height=TEXT_SIZE, color=COLOR_RED, colorSpace='rgb255')
		self.staticStim.append(probeStim)
		for x in list(probeStim.keys()):
			self.staticStim[0][x].setAutoDraw(True)
		self.win.update()

	def reviewScreen(self, imglist):
		reviewStim = {
		"fixation" : TextStim(self.win, text=imglist[0], height=FIXATION_SIZE, color=imglist[1], colorSpace='rgb255'),
		"finalLine" : Line(self.win, pos=(imglist[2]*GRATING_DIST/2, 0), start=(0,-GRATING_SIZE/2), end=(0,GRATING_SIZE/2), ori=game.crtIndex['final_Ori'], opacity=OPACITIES, lineWidth=LINE_WIDTH, lineColor=COLOR_BLUE, lineColorSpace='rgb255'),
		"trueLine" : Line(self.win, pos=(imglist[2]*GRATING_DIST/2, 0), start=(0,-GRATING_SIZE/2), end=(0,GRATING_SIZE/2), ori=game.crtIndex['cueprime_jOri'], opacity=OPACITIES, lineWidth=LINE_WIDTH, lineColor=COLOR_YELLOW, lineColorSpace='rgb255'),
		"finalText" : TextStim(self.win, pos=(imglist[2]*GRATING_DIST/2, 350), text='You', height=TEXT_SIZE, color=COLOR_BLUE, colorSpace='rgb255'),
		"trueText" : TextStim(self.win, pos=(imglist[2]*GRATING_DIST/2, 300), text='Actual', height=TEXT_SIZE, color=COLOR_YELLOW, colorSpace='rgb255')
		}
		if game.crtIndex['peer_Inf'] == 'Y':
			reviewStim["peerLine"] = Line(self.win, pos=(imglist[2]*GRATING_DIST/2, 0), start=(0,-GRATING_SIZE/2), end=(0,GRATING_SIZE/2), ori=game.crtIndex['peer_Ori'], opacity=OPACITIES, lineWidth=LINE_WIDTH, lineColor=COLOR_RED, lineColorSpace='rgb255')
			reviewStim["peerText"] = TextStim(self.win, pos=(imglist[2]*GRATING_DIST/2, 400), text='Partner', height=TEXT_SIZE, color=COLOR_RED, colorSpace='rgb255')
		for x in list(reviewStim.keys()):
			reviewStim[x].draw()
		self.win.update()

	def clearDisplay(self):
		self.win.flip()

class Interact:

	def __init__(self):
		pygame.init()
		self.rotate = 0

	def actionCont(self):
		self.choice = psychopy.event.waitKeys(keyList = ['space', 'escape'])
		if self.choice[0] == 'escape':
			game.localGraphics.win.close()
			core.quit()
		return(self.choice[0])

	def actionWait(self, time):
		then = datetime.now(); now = datetime.now(); diff = now-then
		while diff.total_seconds() < time:
			now = datetime.now()
			diff = now-then
			for event in pygame.event.get():
				if event.type == QUIT:
					game.localGraphics.win.close()
					core.quit()
				elif event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						game.localGraphics.win.close()
						core.quit()

	def actionRotate(self):
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					self.rotate = -1
				elif event.key == pygame.K_0:
					self.rotate = 1
				elif event.key == K_ESCAPE:
					game.localGraphics.win.close()
					core.quit()
			if event.type == pygame.KEYUP:
				self.rotate = 0
		return(self.rotate)

	def actionRotateClear(self):
		self.rotate = 0

# 	def actionQuiz(self):
# 		if game.slidenum <= 4:
# 			self.choice = psychopy.event.waitKeys(keyList = ['1', '2', '3', '4'])
# 		elif game.slidenum >= 5 and game.slidenum <= 8:
# 			self.choice = psychopy.event.waitKeys(keyList = ['1', '2'])
# 		elif game.slidenum >= 9:
# 			self.choice = psychopy.event.waitKeys(keyList = ['1', '2', '3'])
# 		return(self.choice[0])

	def saveDataInst(self):
		saveFrame = [game.subID, game.cycle, game.slidenum, game.slideons]
		titleFrame = ['subID', 'day', 'slidenum', 'onstimestamp']
		for i, x in enumerate(saveFrame):
			saveFrame[i] = str(x)
		with open(DATA_FOLDER+INSTRUCT_SAVE_NAME % (game.subID), 'a') as file:
			if os.stat(DATA_FOLDER+INSTRUCT_SAVE_NAME % (game.subID)).st_size == 0:
				file.write('\t'.join(titleFrame[0:]) + '\n')
			file.write('\t'.join(saveFrame[0:]) + '\n')

# 	def saveDataQuiz(self):
# 		saveFrame = [game.subID, game.cycle, game.slidenum, game.slideons, game.accuracy]
# 		titleFrame = ['subID', 'day', 'slidenum', 'onstimestamp', 'accuracy']
# 		for i, x in enumerate(saveFrame):
# 			saveFrame[i] = str(x)
# 		with open(DATA_FOLDER+QUIZ_SAVE_NAME % (game.subID), 'a') as file:
# 			if os.stat(DATA_FOLDER+QUIZ_SAVE_NAME % (game.subID)).st_size == 0:
# 				file.write('\t'.join(titleFrame[0:]) + '\n')
# 			file.write('\t'.join(saveFrame[0:]) + '\n')

def runRound(game):
	game.runStage0()
	game.runStage1()
	game.runStage2()
	game.runStage3()
	game.runStage4()
	game.runStage5()
	game.runStage6()
	game.runStage7()
	game.saveData()
	#game.saveData()
	game.round += 1

if __name__ == "__main__":
	if not os.path.exists(DATA_FOLDER):
		os.mkdir(DATA_FOLDER)
	game = LocalGame()
	game.runInstructions()
	#game.runQuiz()
	for x in range(ROUND_COUNT):
		runRound(game)