"""
Author: Kyle J. LaFollette
Department of Psychiatry, University of Arizona
Correspondance: kjlafoll@psychiatry.arizona.edu
This script searches the PREEMPT shared drive for files matching keyword
specifications. It begins by allowing you to specify the subdirectories 
within PREEMPT that you'd like to narrow your search to, which speeds up
the searching process. Next, you specify keywords to search with. Keywords
are specified in groups, such that all keywords in a group need to be found
in a filename to match. Multiple groups can be specified, and only one group
need be satisfied to match. Lastly, you specify a file extension to include
in your search.
Currently, matched files are copied to a folder written to the local user's
desktop titled SearchTool_Matches.
"""

import os
import sys
import string
from shutil import copyfile

class SearchTool:

	connected = False
	root = None
	newroot = None
	saveDir = None
	fileslist = None
	pathslist = None
	matchlist = None
	finished = None
	tag = None
	cont = True

	def __init__(self):

		self.connected = False
		self.root = None
		self.newroot = None
		self.saveDir = None
		self.fileslist = []
		self.pathslist = []
		self.matchlist = []
		self.finished = None
		self.tag = None
		self.cont = True
		self.start()

	def start(self):

		while self.connected == False:
			for x in list(string.ascii_uppercase):
				if sys.platform == "win32":
					self.root = "%s:\\Killgore_Scan\\UA_SCAN_Shared\\PREEMPT\\" % x
					self.saveDir = "%s\\SearchTool_Matches\\" % os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
					self.tag = "\\"
				elif sys.platform == "darwin":
					self.root = "/Volumes/psy-dfs/Killgore_SCAN/UA_SCAN_Shared/PREEMPT/"
					self.saveDir = "%s/SearchTool_Matches/" % os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
					self.tag = "/"
				if os.path.isdir(self.root):
					self.connected = True
					break
			if self.connected == False:
				check = input("\nNot connected to Killgore_Scan Shared Drive. Please connect and press any key to restart.")

	def specifier(self):

		exkeys = True
		key = []
		ext = []
		crtkey = 0

		while exkeys == True:
			if crtkey == 0:
				key.append([input("\nEnter a keyword to search for. Or enter NONE to collect all files in the search directory: ")])
			else:
				key.append([input("\nEnter another keyword to search for IN SEPARATE FILENAMES. This is useful if you have multiple file types that you are searching for. Or enter NONE to continue: ")])
			if key[crtkey][0] != "NONE":
				while "NEXT" not in [x for x in key[crtkey]]:
					print("\nCurrent keywords to search for: %s" % key)
					key[crtkey].append(input("\nEnter another keyword to search for IN THE SAME FILENAME. Or enter NEXT to continue: "))
				key[crtkey] = key[crtkey][:-1]
			else:
				exkeys = False
			crtkey += 1
		key = key[:-1]

		ext.append(".%s" % input("\nEnter a file extension to search for. Enter only the alphanumeric symbols after the '.' (i.e., 'txt', 'csv'). Or enter ALL to collect all files matching previous specifications: "))
		if ext[0] != ".ALL":
			while "NEXT" not in ext:
				ext.append(input("\nEnter another extension to search for. Collected files will contain EITHER extension. Or enter NEXT to continue: "))
		ext = ext[:-1]

		self.matchlist = []
		count = 0
		cmtp = 0

		for i, x in enumerate(self.fileslist):
			if len(key) > 0:
				for y in key:
					if all(subs in os.path.basename(x) for subs in y):
						if len(ext) > 0:
							if all(subs in os.path.basename(x) for subs in ext):
								self.matchlist.append([i, x])
								break
						else:
							self.matchlist.append([i, x])
							break
			else:
				self.matchlist.append([i, x])
			count += 1
			if count >= 100:
				cmtp += 1
				print("\n%s files checked for match..." % (100*cmtp))
				count = 0

	def director(self):

		self.newroot = None

		while self.newroot != "ALL":
			print("\nSearch tool directed to %s" % self.root)
			subdirs = []
			actualdirs = []
			for s in os.listdir(self.root):
				if os.path.isdir(os.path.join(self.root, s)):
					actualdirs.append(s)
			if len(actualdirs) == 0:
				break
			print("\nSubdirectories listed below:")
			for i, x in enumerate(actualdirs):
				print("%s. %s" % (i+1, x))
				subdirs.append([i+1, x])
			subdirs.append(["ALL", None])

			self.newroot = input("\nEnter the number for the subdirectory you'd like to search. Or enter ALL to search all subdirectories: ")
			while self.newroot not in [str(x[0]) for x in subdirs]:
				print("\nNot a valid input.")
				self.newroot = input("\nEnter the number for the subdirectory you'd like to search. Or enter ALL to search all subdirectories: ")
			if self.newroot in [str(x[0]) for x in subdirs][:-1]:
				self.root = os.path.join(self.root, subdirs[int(self.newroot)-1][1])

		self.pathslist = []
		self.fileslist = []
		count = 0
		cmtp = 0
		for p, s, f in os.walk(self.root):
			for n in f:
				count += 1
				if count >= 100:
					cmtp += 1
					print("\n%s files collected..." % (100*cmtp))
					count = 0
				self.pathslist.append(os.path.join(p, n))
				self.fileslist.append(n)

	def writer(self):

		if len(self.matchlist) > 0:
			copycheck = input("\n%s file(s) found matching specifications. Would you like to copy files? (y/n): " % len(self.matchlist))
			while copycheck not in [x for x in ['y', 'n']]:
				copycheck = input("\nNot a valid input. Would you like to copy files? (y/n): ")
			if copycheck == "y":
				print("\nCurrent saving directory: %s" % self.saveDir)
				doublecheck = input("\nWould you like to save here? (y/n): ")
				while doublecheck not in [x for x in ["y", "n"]]:
					doublecheck = input("\nNot a valid input. Would you like to save to %s? (y/n): " % self.saveDir)
				if doublecheck == "y":
					newFolder = input("\nEnter the name of a new folder to save to (will be created in %s): " % self.saveDir)
					if not os.path.isdir(self.saveDir):
						os.mkdir(self.saveDir)
					if not os.path.isdir(self.saveDir+newFolder+self.tag):
						os.mkdir(self.saveDir+newFolder+self.tag)
					for x in self.matchlist:
						copyfile(self.pathslist[x[0]], "%s%s" % (self.saveDir+newFolder+self.tag, os.path.basename(self.pathslist[x[0]])))
					self.finished = input("\nFiles saved. Task complete. Enter 'r' to restart program, 's' to respecify keywords, 'd' to redirect the search tool, and any other key to exit: ")
				else:
					self.finished = input("\nChange the saving directory in the source code if you'd like to save elsewhere. Task Complete. Enter 'r' to restart program, 's' to respecify keywords, 'd' to redirect the search tool, and any other key to exit: ")
			else:
				self.finished = input("\nGood bye. Enter 'r' to restart program, 's' to respecify keywords, 'd' to redirect the search tool, and any other key to exit: ")
		else:
			self.finished = input("\n0 files found matching specifications. Enter 'r' to restart program, 's' to respecify keywords, 'd' to redirect the search tool, and any other key to exit: ") 

if __name__ == "__main__":

	executor = SearchTool()
	executor.director()
	executor.specifier()
	while executor.cont == True:
		executor.writer()
		if executor.finished == "d":
			executor.connected = False
			executor.start()
			executor.director()
		elif executor.finished == "s":
			executor.specifier()
		elif executor.finished == "r":
			executor.connected = False
			executor.start()
			executor.director()
			executor.specifier()
		else:
			executor.cont = False