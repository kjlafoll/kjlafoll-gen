# DSP.py
# -------------------------
# A DSP Task

import random, pygame, sys, os, time, collections, os.path
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
REWARDFONTSIZE = 300
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
TRIALS_PER_BLOCK = 27
ITI_LENGTH = 1000
ABORT_TIME = 4000
root = os.path.join(os.environ['USERPROFILE'])+"/Desktop/PREEMPT2/DSPMain/DSPexp/"
imgRoot = root+"RES_DSPexp/"

if not os.path.exists(root+"Data_DSPexp/"):
    os.mkdir(root+"Data_DSPexp/")

imgBank_instruct = []
imgBank_instruct.append("Slide" + str(1) + ".jpg")
imgBank_instruct.append("Slide" + str(5) + ".jpg")
imgBank_instruct.append("Slide" + str(6) + ".jpg")


# get subject data from user
SUB_NUM = input("Please enter your subject number:  ")
CYCLE_NUM = input("Please enter cycle #:  ")
TRAINING_FILE = root+"Data_DSPexp/PREEMPT2_%s/output_files/PREEMPT2_%s_training_output.csv" % (SUB_NUM, SUB_NUM)
REWARD_FILE = root+'Reward_Schedules/test_rewards_and_sequences.csv'

# Sequence dictionaries
# Each has a sequence, it's associated color for explicit cueing, a label,
# and the number of repetitions per block

ALL_SEQ = deque([[3,2,4,1,2,4,3,1],[1,4,2,3,1,3,4,2],[2,1,4,2,3,1,4,3],[4,3,1,4,2,3,1,2]])
ALL_SEQ.rotate(int(SUB_NUM) %4)

TEST_SEQ = [3,2,1,4,1,2,3,4,1,2]
SEQ_A = {'seq':ALL_SEQ[0], 'color':BLUE, 'label':'A', 'reps':int(round(.333*TRIALS_PER_BLOCK))}
SEQ_B = {'seq':ALL_SEQ[1], 'color':RED, 'label':'B','reps':int(round(.333*TRIALS_PER_BLOCK))}
SEQ_C = {'seq':ALL_SEQ[2], 'color':DARKGRAY, 'label':'C','reps':int(round(.333*TRIALS_PER_BLOCK))}
SEQ_D = {'seq':ALL_SEQ[3], 'color':DARKGRAY, 'label':'D','reps':int(round(.1*TRIALS_PER_BLOCK))}
SEQ_RAND = {'seq':[1,2,3,4], 'color':DARKGRAY, 'label':'random','reps':int(round(.2*TRIALS_PER_BLOCK))}

NUM_TRIALS_FOR_MT = 8 # number of trials from the end of training to calculate max movement time
MT_PERCENTILE = .25 # what percentile to use from training to calculate max movement time (.5 = median)



if os.path.isfile(TRAINING_FILE)==False:
	print("Cannot find training file for subject %s" % SUB_NUM)

def main():
    global BASICFONT, DISPLAYSURF

    # SET EMPTY LISTS FOR DATA COLLECTION
    accuracies = []
    training_IKIs = []
    training_RTs = []
    training_MTs = []
    sequence_labels = []
    sequence_keys = []
    block_nums = []
    rewards=[]
    max_time_list = []
    too_slows = []
    pressed_keys =[]
    key_errors = []

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
    
    

    # create block sequences
    if SUB_NUM == 'test':
        max_times = {'A':3000, 'B':3000, 'C':3000} # ms
    else:
        training_data = pd.read_table(TRAINING_FILE)
        print(training_data)
        max_times = getMedianTimes(training_data)
    # load reward_file
    if os.path.isfile(REWARD_FILE)==False:
        print("Cannot find reward file for subject %s" % SUB_NUM)
    reward_table = pd.read_table(REWARD_FILE)
    #initialize pygame
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
    for sind,seq_label in enumerate(reward_table.sequences):
        
        seq = selectSeq(seq_label)
        if seq == SEQ_D:
            continue
        if seq == SEQ_RAND:
            continue
        if sind% TRIALS_PER_BLOCK==0:
            waitForNextBlock(sind/TRIALS_PER_BLOCK+1)
        DISPLAYSURF.fill(BGCOLOR)
        displayReward(reward_table.reward[sind],seq)
        pygame.display.update()  
        pygame.time.wait(2000)

        drawBackSquares()
        pygame.display.update()
        pygame.time.wait(1000)
        if checkForKeyPress(): # clear event queue
            pygame.event.get()
        acc, IKIs, RTs, MT, slow, pressed, key_error = runSequence(seq['seq'],max_times[seq['label']])

        # ITI
        DISPLAYSURF.fill(BGCOLOR)
        drawMessage(FIXATION, REWARDFONTSIZE)
        pygame.display.update()
        pygame.time.wait(ITI_LENGTH)

        # Fill in data for saving
        sequence_labels.append(seq['label'])
        accuracies.append(acc)
        training_IKIs.append(IKIs)
        training_RTs.append(RTs)
        training_MTs.append(MT)
        One_RTs.append(RTs[0])
        Two_RTs.append(RTs[1])
        Three_RTs.append(RTs[2])
        Four_RTs.append(RTs[3])
        Five_RTs.append(RTs[4])
        Six_RTs.append(RTs[5])
        Seven_RTs.append(RTs[6])
        Eight_RTs.append(RTs[7])
        block_nums.append(sind/TRIALS_PER_BLOCK+1)
        rewards.append(reward_table.reward[sind])
        too_slows.append(slow)
        max_time_list.append(max_times[seq['label']])
        pressed_keys.append(pressed)
        sequence_keys.append(seq['seq'])
        key_errors.append(key_error)
        # create a list with the subject number as long as the number of trials completed
        sub_nums = [SUB_NUM]*len(accuracies)
        # write temporary output in case something crashes . . .
        data = {'subject': sub_nums, 'sequence': sequence_labels, 'accuracy': accuracies,
                'movement_time': training_MTs,
                'one_RT':One_RTs, 'two_RT':Two_RTs,'three_RT':Three_RTs,
                'four_RT':Four_RTs, 'five_RT':Five_RTs, 'six_RT':Six_RTs,
                'seven_RT':Seven_RTs, 'eight_RT':Eight_RTs, 'block':block_nums,
                'reward': rewards, 'max_time':max_time_list, 'too_slow': too_slows,
                'pressed':pressed_keys, 'seq_keys':sequence_keys, 'key_error': key_errors}
        frame = DataFrame(data)
        tempfolder = root+"Data_DSPexp/PREEMPT2_%s/temp_output_files/" % SUB_NUM
        frame.to_csv(tempfolder+'PREEMPT2_%s_rep_temp_reward_output_cycle%s.csv' % (SUB_NUM, CYCLE_NUM), sep= '\t')
        
    # save output
    folder = root+"Data_DSPexp/PREEMPT2_%s/output_files/" % SUB_NUM
    frame.to_csv(folder+'PREEMPT2_%s_rep_reward_output_cycle%s.csv' % (SUB_NUM, CYCLE_NUM), sep= '\t')    
    terminate()

# Run one sequence of the DSP.  If training is set to True, display the keys associated with each
# position on the screen.  Return the accuracy of the trial, a list of the IKIs, a list of the RTs
# and the total movement time.
def runSequence(sequence, max_time,training = False):
    
    # create an array of -1's for the time between key presses
    interkey_times = [None] * len(sequence) # np.ones(len(sequence)) * -1 # to be filled with actual responses later
    RTs = [None] * len(sequence)
    accuracy = 0 # initialize accuracy to 'wrong' until sequence is completed
    too_slow = 0 # value to return denoting whether participant completed the seq in time
    key_error = 0 # initialize to 'false' unless the participant makes a key press error
    MT = None # initialize movement time to nothing
    pressed=[]
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
            if currtime > ABORT_TIME:
                drawBackSquares()
                colorSquare(1, RED)
                colorSquare(2, RED)
                colorSquare(3, RED)
                colorSquare(4, RED)
                displayError(timeout=True)
                too_slow = 1
                return accuracy, interkey_times, RTs, MT, too_slow, pressed, key_error
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
                        key_error = 1
                        return accuracy, interkey_times, RTs, MT, too_slow, pressed, key_error
                    else:
                        no_user_resp = False
                        key_press_time = pygame.time.get_ticks() # record the clock for this button press
                        if pind ==0: # for the first item in the sequence
                            interkey_times[pind] = pos_RT # set the IKI to the RT for the first button press
                            last_key_time = key_press_time # record the time of the first button press
                        else:
                            interkey_times[pind] = key_press_time - last_key_time # record the IKI
                            last_key_time = key_press_time
                            
    if currtime > max_time:
        drawBackSquares()
        colorSquare(1, RED)
        colorSquare(2, RED)
        colorSquare(3, RED)
        colorSquare(4, RED)
        displayError(timeout=True)
        too_slow = 1
        return accuracy, interkey_times, RTs, MT, too_slow, pressed, key_error
    accuracy = 1 # set to correct if sequence was completed                    
    return accuracy, interkey_times, RTs, MT, too_slow, pressed, key_error


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

# draw text on the screen with the given fontSize in the center of the screen
# move the text from the center with the given x and y offsets
def drawMessage(value, fontSize, y_offset = 0, x_offset = 0):
    rewardFont = pygame.font.Font('freesansbold.ttf', int(fontSize))
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

# function that returns the median time of the last NUM_TRIALS_FOR_MT for each sequence during training
# currently returns the MT_PERCENTILE instead of actual median
def getMedianTimes(trainingFrame):
    a_frame = trainingFrame[trainingFrame.sequence=='A']
    b_frame = trainingFrame[trainingFrame.sequence=='B']
    c_frame = trainingFrame[trainingFrame.sequence=='C']
#    d_frame = trainingFrame[trainingFrame.sequence=='D']
#    rand_frame = trainingFrame[trainingFrame.sequence=='random']
    a_frame = a_frame[a_frame.accuracy == 1]
    b_frame = b_frame[b_frame.accuracy == 1] 
    c_frame = c_frame[c_frame.accuracy == 1]
#    d_frame = d_frame[d_frame.accuracy == 1]
#    rand_frame = rand_frame[rand_frame.accuracy == 1]
    a_MTs = a_frame[-NUM_TRIALS_FOR_MT:].movement_time
    b_MTs = b_frame[-NUM_TRIALS_FOR_MT:].movement_time
    c_MTs = c_frame[-NUM_TRIALS_FOR_MT:].movement_time
#    d_MTs = d_frame[-NUM_TRIALS_FOR_MT:].movement_time
#    rand_MTs = rand_frame[-NUM_TRIALS_FOR_MT:].movement_time
    
    a_RTs = a_frame[-NUM_TRIALS_FOR_MT:].one_RT
    b_RTs = b_frame[-NUM_TRIALS_FOR_MT:].one_RT
    c_RTs = c_frame[-NUM_TRIALS_FOR_MT:].one_RT
#    d_RTs = d_frame[-NUM_TRIALS_FOR_MT:].one_RT
#    rand_RTs = rand_frame[-NUM_TRIALS_FOR_MT:].one_RT

    a_MT_sort = sorted(a_MTs, reverse=True)
    b_MT_sort = sorted(b_MTs, reverse=True)
    c_MT_sort = sorted(c_MTs, reverse=True)
#    d_MT_sort = sorted(d_MTs, reverse=True)
#    rand_MT_sort = sorted(rand_MTs, reverse=True)
    
    a_RT_sort = sorted(a_RTs, reverse=True)
    b_RT_sort = sorted(b_RTs, reverse=True)
    c_RT_sort = sorted(c_RTs, reverse=True)
#    d_RT_sort = sorted(d_RTs, reverse=True)
#    rand_RT_sort = sorted(rand_RTs, reverse=True)

    a_time = a_MT_sort[int(NUM_TRIALS_FOR_MT*MT_PERCENTILE)]+ a_RT_sort[int(NUM_TRIALS_FOR_MT*MT_PERCENTILE)]
    b_time = b_MT_sort[int(NUM_TRIALS_FOR_MT*MT_PERCENTILE)]+ b_RT_sort[int(NUM_TRIALS_FOR_MT*MT_PERCENTILE)]
    c_time = c_MT_sort[int(NUM_TRIALS_FOR_MT*MT_PERCENTILE)]+ c_RT_sort[int(NUM_TRIALS_FOR_MT*MT_PERCENTILE)]
    print(a_time)
    print(b_time)
    print(c_time)
#    d_time = d_MT_sort[int(NUM_TRIALS_FOR_MT*MT_PERCENTILE)]+ d_RT_sort[int(NUM_TRIALS_FOR_MT*MT_PERCENTILE)]
#    rand_time = rand_MT_sort[int(NUM_TRIALS_FOR_MT*MT_PERCENTILE)]+ rand_RT_sort[int(NUM_TRIALS_FOR_MT*MT_PERCENTILE)]
    # get median times
    #a_time = np.median(a_frame[-NUM_TRIALS_FOR_MT:].movement_time)+np.median(a_frame[-NUM_TRIALS_FOR_MT:].one_RT)
    #b_time = np.median(b_frame[-NUM_TRIALS_FOR_MT:].movement_time)+np.median(b_frame[-NUM_TRIALS_FOR_MT:].one_RT)
    #c_time = np.median(c_frame[-NUM_TRIALS_FOR_MT:].movement_time)+np.median(c_frame[-NUM_TRIALS_FOR_MT:].one_RT)
    # print(a_time)
    # print(b_time)
    # print(c_time)
    return {'A':a_time, 'B':b_time, 'C':c_time}

def displayReward(rewardVal, seq = None):
    if seq == None:
        drawMessage('$' + str(rewardVal), REWARDFONTSIZE)
    else:
        drawMessage("Sequence:", RESPONSEKEYFONT, x_offset = -HALFWIDTH/4)
        drawSquare(HALFWIDTH/1.5, HALFHEIGHT, SEQ_SQUARE_SIZE, seq['color'])
        drawMessage('$' + str(rewardVal), REWARDFONTSIZE*3/4, x_offset = HALFWIDTH/4)

def selectSeq(label):
    if label == 'A':
        return SEQ_A
    elif label == 'B':
        return SEQ_B
    elif label == 'C':
        return SEQ_C
    elif label == 'D':
        return SEQ_D
    elif label == 'random':
        return makeRandomSeq(SEQ_RAND)
    else:
        print('something wrong with rewards and sequences file')
        terminate()
        
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
