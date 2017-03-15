import os.path
import sys
import argparse
import logging

class wc:
	def __init__(self, args):
		self.lineCount = {}
		self.wordCount = {}
		self.charCount = {}

		self.args = args

		self.files = []
		for fileName in self.args.input:
			if os.path.isfile(fileName):
				print "Input file:", fileName, "valid"
				f = open(fileName, 'r')
				self.files.append(f)
			else:
				print "Non-existing file provided as input, exiting now!"
				sys.exit(0)
		print "\n"

	def countLines(self):
		for filePointer in self.files:
			filePointer.seek(0)
			self.lineCount[filePointer.name] = 0
			self.countLinesPerFile(filePointer)

	def countLinesPerFile(self, filePointer):
		for line in filePointer:
			self.lineCount[filePointer.name] += 1
		return self.lineCount[filePointer.name]

	def countWords(self):
		for filePointer in self.files:
			filePointer.seek(0)
			self.wordCount[filePointer.name] = 0
			self.countWordsPerFile(filePointer)

	def countWordsPerFile(self, filePointer):
		for line in filePointer:
			for word in line.split():
				self.wordCount[filePointer.name] += 1
		return self.wordCount[filePointer.name]

	def countChars(self):
		for filePointer in self.files:
			filePointer.seek(0)
			self.charCount[filePointer.name] = 0
			self.countCharsPerFile(filePointer)

	def countCharsPerFile(self, filePointer):
		for line in filePointer:
			self.charCount[filePointer.name] += len(line)
		return self.charCount[filePointer.name]

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("input", nargs = "+", help="name of input file")
	parser.add_argument("-c", "--chars", help="count characters (bytes)", action = "store_true")
	parser.add_argument("-l", "--lines", help="count lines", action = "store_true")
	parser.add_argument("-w", "--words", help="count words", action = "store_true")
	args = parser.parse_args()

	wcInstance = wc(args)

	if args.lines:
		wcInstance.countLines()
	if args.words:
		wcInstance.countWords()
	if args.chars:
		wcInstance.countChars()

	for fileName in args.input:
		output = ""
		if args.lines:
			output += "\t"+str(wcInstance.lineCount[fileName])
		if args.words:
			output += "\t"+str(wcInstance.wordCount[fileName])
		if args.chars:
			output += "\t"+str(wcInstance.charCount[fileName])
		print output+"\t"+fileName

	output = ""
	if args.lines:
		output += "\t"+str(sum(wcInstance.lineCount.values()))
	if args.words:
		output += "\t"+str(sum(wcInstance.wordCount.values()))
	if args.chars:
		output += "\t"+str(sum(wcInstance.charCount.values()))
	print output+"\ttotal"

if __name__ == '__main__':
	main()
