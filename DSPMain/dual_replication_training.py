# DSP.py
# -------------------------
# A DSP Task

import random, pygame, sys, os, time, collections
import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from pygame.locals import *
from collections import deque
from datetime import datetime

# Colors
#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
BLUE      = (  0,   0, 255)
YELLOW    = (255, 255,   0)
BGCOLOR = BLACK

pygame.init()
info = pygame.display.Info()
screen_width,screen_height = info.current_w,info.current_h

# Constants for display
WINDOWWIDTH = screen_width
WINDOWHEIGHT = screen_height
CELLSIZE = 2
RESPONSEKEYFONT = 50
BLOCKFONTSIZE = 75
SQUARESIZE = 25*CELLSIZE
SEQ_SQUARE_SIZE = 50*CELLSIZE
INSTRUCTFONT = 20
FIXATION = '+'
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)
HALFHEIGHT = WINDOWHEIGHT/2 - SQUARESIZE
HALFWIDTH = WINDOWWIDTH/2
POS_ONE = HALFWIDTH-(1.5*SQUARESIZE)-(3*SQUARESIZE)-SQUARESIZE
POS_TWO = HALFWIDTH-(1.5*SQUARESIZE)-SQUARESIZE
POS_THREE = HALFWIDTH+(1.5*SQUARESIZE)-SQUARESIZE
POS_FOUR = HALFWIDTH+(1.5*SQUARESIZE)+(3*SQUARESIZE)-SQUARESIZE

# instructions (duh)
INSTRUCTIONS = ["PUT INSTRUCTIONS HERE"]
TRIALS_PER_BLOCK = 40
root = os.path.join(os.environ['USERPROFILE'])+"/Desktop/PREEMPT2/DSPMain/DSPexp/"
imgRoot = root+"RES_DSPexp/"

if not os.path.exists(root+"Data_DSPexp/"):
    os.mkdir(root+"Data_DSPexp/")

imgBank_instruct = []
for x in range(1,5):
    imgBank_instruct.append("Slide" + str(x) + ".jpg")

# get subject data from user
SUB_NUM = input("Please enter your subject number:  ")

ALL_SEQ = deque([[3,2,4,1,2,4,3,1],[1,4,2,3,1,3,4,2],[2,1,4,2,3,1,4,3],[4,3,1,4,2,3,1,2]])
ALL_SEQ.rotate(int(SUB_NUM) %4)
	
# Sequence dictionaries
# Each has a sequence, it's associated color for explicit cueing, a label,
# and the number of repetitions per block
TEST_SEQ = [3,2,1,4,1,2,3,4,1,2]
SEQ_A = {'seq':ALL_SEQ[0], 'color':BLUE, 'label':'A', 'reps':int(round(.6*TRIALS_PER_BLOCK))}
SEQ_B = {'seq':ALL_SEQ[1], 'color':RED, 'label':'B','reps':int(round(.3*TRIALS_PER_BLOCK))}
SEQ_C = {'seq':ALL_SEQ[2], 'color':DARKGRAY, 'label':'C','reps':int(round(.1*TRIALS_PER_BLOCK))}
#SEQ_D = {'seq':ALL_SEQ[3], 'color':DARKGRAY, 'label':'D','reps':int(round(.1*TRIALS_PER_BLOCK))}
SEQ_RAND = {'seq':[1,2,3,4], 'color':DARKGRAY, 'label':'random','reps':int(round(.2*TRIALS_PER_BLOCK))}

ONE_BLOCK = [SEQ_A]*SEQ_A['reps']+[SEQ_B]*SEQ_B['reps']+[SEQ_C]*SEQ_C['reps']
NUM_BLOCKS = 8


def main():
    global BASICFONT, DISPLAYSURF

    # SET EMPTY LISTS FOR DATA COLLECTION
    # ---------------------------
    accuracies = []
    training_IKIs = []
    training_RTs = []
    training_MTs = []
    sequence_labels = []
    block_nums = []
    pressed_keys =[]
    sequence_keys = []

    # for each item in each sequence
    One_IKIs = []
    Two_IKIs = []
    Three_IKIs = []
    Four_IKIs = []
    Five_IKIs = []
    Six_IKIs = []
    Seven_IKIs = []
    Eight_IKIs  = []
    One_RTs = []
    Two_RTs = []
    Three_RTs = []
    Four_RTs = []
    Five_RTs = []
    Six_RTs = []
    Seven_RTs = []
    Eight_RTs  = []
    # ------------------------    

    # create block sequences
    all_seq = []
    if SUB_NUM != '0':
        for b in np.arange(NUM_BLOCKS):
            a = list(ONE_BLOCK)
            random.shuffle(a)
            all_seq = all_seq + a
    else:
        all_seq = [SEQ_A, SEQ_B, SEQ_RAND, SEQ_RAND, SEQ_A,SEQ_B, SEQ_RAND]

    # Do all the training trials
    pygame.init()
    info = pygame.display.Info()
    screen_width,screen_height = info.current_w,info.current_h
    os.environ['SDL_VIDEO_WINDOW_POS'] = str(0) + "," + str(0)
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    #DISPLAYSURF = pygame.display.set_mode((screen_width, screen_height), FULLSCREEN)
    pygame.mouse.set_visible(False)
    pygame.display.flip()
    Instructions()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    doTraining()
    for sind,seq in enumerate(all_seq):
        if sind% TRIALS_PER_BLOCK==0:
            waitForNextBlock(sind/TRIALS_PER_BLOCK+1)
        DISPLAYSURF.fill(BGCOLOR)
        drawMessage("Sequence:", RESPONSEKEYFONT)
        drawSquare(HALFWIDTH-SEQ_SQUARE_SIZE, HALFHEIGHT, SEQ_SQUARE_SIZE, seq['color'])
        pygame.display.update()  
        pygame.time.wait(1000)
        drawBackSquares()
        pygame.display.update()
        pygame.time.wait(1000)
        if checkForKeyPress(): # clear event queue
            pygame.event.get()
        if seq['label']=='random':
            seq = makeRandomSeq(seq)
        acc, IKIs, RTs, MT, pressed = runSequence(seq['seq'])

        # Fill in data for saving
        # ----------------------------
        sequence_labels.append(seq['label'])
        accuracies.append(acc)
        training_IKIs.append(IKIs)
        training_RTs.append(RTs)
        training_MTs.append(MT)
        One_IKIs.append(IKIs[0])
        Two_IKIs.append(IKIs[1])
        Three_IKIs.append(IKIs[2])
        Four_IKIs.append(IKIs[3])
        Five_IKIs.append(IKIs[4])
        Six_IKIs.append(IKIs[5])
        Seven_IKIs.append(IKIs[6])
        Eight_IKIs.append(IKIs[7])
        One_RTs.append(RTs[0])
        Two_RTs.append(RTs[1])
        Three_RTs.append(RTs[2])
        Four_RTs.append(RTs[3])
        Five_RTs.append(RTs[4])
        Six_RTs.append(RTs[5])
        Seven_RTs.append(RTs[6])
        Eight_RTs.append(RTs[7])
        block_nums.append(sind/TRIALS_PER_BLOCK+1)
        pressed_keys.append(pressed)
        sequence_keys.append(seq['seq'])
        
        # ---------------------------------------

        # create a list with the subject number as long as the number of trials completed
        sub_nums = [SUB_NUM]*len(accuracies) 
        # write temporary output in case something crashes . . .
        data = {'subject': sub_nums, 'sequence': sequence_labels, 'accuracy': accuracies,
                'movement_time': training_MTs, 'one_IKI':One_IKIs, 'two_IKI':Two_IKIs,
                'three_IKI':Three_IKIs, 'four_IKI':Four_IKIs, 'five_IKI':Five_IKIs,
                'six_IKI':Six_IKIs, 'seven_IKI':Seven_IKIs, 'eight_IKI':Eight_IKIs,
                'one_RT':One_RTs, 'two_RT':Two_RTs,'three_RT':Three_RTs,
                'four_RT':Four_RTs, 'five_RT':Five_RTs, 'six_RT':Six_RTs,
                'seven_RT':Seven_RTs, 'eight_RT':Eight_RTs, 'block':block_nums,
                'pressed':pressed_keys, 'seq_keys':sequence_keys}
        frame = DataFrame(data)
        if not os.path.exists(root+"Data_DSPexp/PREEMPT2_%s/" % SUB_NUM):
            os.mkdir(root+"Data_DSPexp/PREEMPT2_%s/" % SUB_NUM)
        if not os.path.exists(root+"Data_DSPexp/PREEMPT2_%s/temp_output_files/" % SUB_NUM):
            os.mkdir(root+"Data_DSPexp/PREEMPT2_%s/temp_output_files/" % SUB_NUM)
        tempfolder = root+"Data_DSPexp/PREEMPT2_%s/temp_output_files/" % SUB_NUM
        frame.to_csv(tempfolder+'PREEMPT2_%s_temp_training_output.csv' % (SUB_NUM), sep= '\t')
        
    # save output
    if not os.path.exists(root+"Data_DSPexp/PREEMPT2_%s/output_files/" % SUB_NUM):
        os.mkdir(root+"Data_DSPexp/PREEMPT2_%s/output_files/" % SUB_NUM)
    folder = root+"Data_DSPexp/PREEMPT2_%s/output_files/" % SUB_NUM
    frame.to_csv(folder+'PREEMPT2_%s_training_output.csv' % (SUB_NUM), sep= '\t')    
    terminate()

# Run one sequence of the DSP.  If training is set to True, display the keys associated with each
# position on the screen.  Return the accuracy of the trial, a list of the IKIs, a list of the RTs
# and the total movement time.
def runSequence(sequence, training = False):
    
    # create an array of -1's for the time between key presses
    interkey_times = [None] * len(sequence) # np.ones(len(sequence)) * -1 # to be filled with actual responses later
    RTs = [None] * len(sequence)
    accuracy = 0 # initialize accuracy to 'wrong' until sequence is completed
    MT = None # initialize movement time to nothing
    pressed = []
    for pind, pos in enumerate(sequence):
        no_user_resp = True # has the user responded yet?
        key = 'null'
        drawBackSquares()
        colorSquare(pos, WHITE)
        if training == True:
            drawTrainingCues()
        pygame.display.update()
        color_disp_time = pygame.time.get_ticks() # when the square is initially displayed  
        if pind ==0:
            seq_start_time = color_disp_time # get the start of the entire sequence display
        while no_user_resp: # game loop
            currtime = pygame.time.get_ticks()-seq_start_time
            # check to see if 8s has elapsed
            if currtime > 8000:
                displayError(timeout=True)
                return accuracy, interkey_times, RTs, MT, pressed
            for event in pygame.event.get(): # event handling loop
                if event.type == QUIT:
                    terminate()
                elif event.type == KEYDOWN:
                    key = checkKeyPress(event.key)
                if key == 1 or key ==2 or key ==3 or key ==4:
                    pos_RT = pygame.time.get_ticks() - color_disp_time # get the reaction time for this key press
                    RTs[pind] = pos_RT # record the RT for this item
                    if pind == 0:
                        move_start_time = pygame.time.get_ticks() # get the start time of the movement
                    MT = pygame.time.get_ticks() - move_start_time # update the movement time for the sequence
                    pressed.append(key)
                    if key != pos: # if error is made
                        colorSquare(key,RED)
                        pygame.display.update()
                        displayError()
                        return accuracy, interkey_times, RTs, MT, pressed
                    else:
                        no_user_resp = False
                        key_press_time = pygame.time.get_ticks() # record the clock for this button press
                        if pind ==0: # for the first item in the sequence
                            interkey_times[pind] = pos_RT # set the IKI to the RT for the first button press
                            last_key_time = key_press_time # record the time of the first button press
                        else:
                            interkey_times[pind] = key_press_time - last_key_time # record the IKI
                            last_key_time = key_press_time
    accuracy = 1 # set to correct if sequence was completed                    
    return accuracy, interkey_times, RTs, MT, pressed

# Have the participant do two different sequences with the keys printed on the screen
# to familiarize them with the task
def doTraining():
    training_sequence = [1,2,3,4,4,3,2,1]
    harder_sequence = [2,1,4,2,3,1,4,3] # so it's not in order
    accuracy = 0
    while accuracy ==0:
        accuracy,IKI,RTs,MT, pressed =runSequence(training_sequence,True)
        if accuracy ==0:
            drawBackSquares()
            drawMessage("Try again please.", RESPONSEKEYFONT)
            pygame.time.wait(1000)
    drawMessage("Good!", RESPONSEKEYFONT)
    pygame.time.wait(1000)
    accuracy = 0
    while accuracy ==0:
        accuracy,IKI,RTs,MT, pressed =runSequence(harder_sequence,True)
        if accuracy ==0:
            drawBackSquares()
            drawMessage("Try again please.", RESPONSEKEYFONT)
            pygame.time.wait(1000)
    drawMessage("Good!", RESPONSEKEYFONT)
    pygame.time.wait(1000)

# Draw the key that corresponds to each square on the screen
def drawTrainingCues():
    drawMessage("H", RESPONSEKEYFONT, SQUARESIZE*5, POS_ONE-HALFWIDTH+SQUARESIZE)
    drawMessage("J", RESPONSEKEYFONT, SQUARESIZE*5, POS_TWO-HALFWIDTH+SQUARESIZE)
    drawMessage("K", RESPONSEKEYFONT, SQUARESIZE*5, POS_THREE-HALFWIDTH+SQUARESIZE)
    drawMessage("L", RESPONSEKEYFONT, SQUARESIZE*5, POS_FOUR-HALFWIDTH+SQUARESIZE)

# display an error message above the squares on the screen
def displayError(timeout=False):
    if timeout:
        drawMessage("Too slow!", RESPONSEKEYFONT)
    else:
        drawMessage("Error!", RESPONSEKEYFONT)
    pygame.display.update()
    pygame.time.wait(1000)
    
# Light up the square at a given position
def colorSquare(position, color):
    if position == 1:
        screen_pos = POS_ONE
    elif position == 2:
        screen_pos =POS_TWO
    elif position == 3:
        screen_pos = POS_THREE
    elif position ==4:
        screen_pos = POS_FOUR
    else:
        screen_pos = 0
    drawSquare(screen_pos, HALFHEIGHT, SQUARESIZE, color)
    
# draw four gray squares in the background
def drawBackSquares():
    DISPLAYSURF.fill(BGCOLOR)
    drawSquare(POS_ONE, HALFHEIGHT, SQUARESIZE, DARKGRAY)
    drawSquare(POS_TWO, HALFHEIGHT, SQUARESIZE, DARKGRAY)
    drawSquare(POS_THREE, HALFHEIGHT, SQUARESIZE, DARKGRAY)
    drawSquare(POS_FOUR, HALFHEIGHT, SQUARESIZE, DARKGRAY)
    pygame.display.update()
    
def checkKeyPress(key):
    #keytype = 'error'
    if key == K_h: 
        return 1
    elif key == K_j:
        return 2
    elif key == K_k:
        return 3
    elif key == K_l:
        return 4
    elif key == K_ESCAPE:
        terminate()
    else:
        return 0

def waitForUser():
    DISPLAYSURF.fill(BGCOLOR)
    pressKeyFont = pygame.font.Font('freesansbold.ttf', CONFONT)
    pressKeySurf = pressKeyFont.render('Press any button to continue', True, WHITE)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.midtop = (WINDOWWIDTH / 2, WINDOWHEIGHT /3)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)
    pygame.display.update()
    while True:
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                else: return event.key
               
def terminate():
    pygame.quit()
    sys.exit()
    
def actionCont():

    while True:
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                else: return event.key

def Instructions():
    slidenum = 0
    for x in imgBank_instruct:
        slidenum +=1
        bStim = pygame.image.load("%s%s" % (imgRoot, x))
        DISPLAYSURF.blit(bStim, bStim.get_rect(center = DISPLAYSURF.get_rect().center))
        pygame.display.flip()
        slideons = str(datetime.now())
        action = actionCont()
        #state.saveDataInst()
        slidenum = 0
                
def drawSquare(x, y, size, color):
    Square = pygame.Rect(x, y, CELLSIZE*size, CELLSIZE*size)
    pygame.draw.rect(DISPLAYSURF, color, Square)

def drawMessage(value, fontSize, y_offset = 0, x_offset = 0):
    rewardFont = pygame.font.Font('freesansbold.ttf', fontSize)
    rewardSurf = rewardFont.render(value, True, WHITE)
    rewardRect = rewardSurf.get_rect()
    rewardRect.midtop = (WINDOWWIDTH / 2 +x_offset, WINDOWHEIGHT / 3+ y_offset)
    DISPLAYSURF.blit(rewardSurf, rewardRect)
    pygame.display.update()

def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()
    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key

def waitForNextBlock(blockNum):
    if checkForKeyPress(): # clear event queue
        pygame.event.get()
    DISPLAYSURF.fill(BGCOLOR)
    drawMessage('Block # %i' % (blockNum), BLOCKFONTSIZE)
    drawMessage('Press any key to continue', RESPONSEKEYFONT, BLOCKFONTSIZE*2)
    pygame.display.update()
    while True:
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                else:
                    return
					
def makeRandomSeq(seq):
	fragment = seq['seq']
	first = random.sample(fragment, len(fragment))
	second = random.sample(fragment, len(fragment))
	while first[-1]==second[0]:
		second = random.sample(fragment, len(fragment))
	new_seq = first+second
	new_seq_dict = seq.copy()
	new_seq_dict['seq']=new_seq
	return new_seq_dict 
                
if __name__ == '__main__':
    main()
