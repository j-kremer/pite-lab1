import os.path
import sys
import argparse
import logging

class wc:
	def __init__(self, args):
		self.lineCount = {}
		self.wordCount = {}
		self.charCount = {}

		logFileName = "wc.log"
		if os.path.isfile(logFileName):
			os.remove(logFileName)
		logging.basicConfig(filename = logFileName, level = logging.INFO)

		self.args = args
		self.files = []
		for fileName in self.args.input:
			if os.path.isfile(fileName):
				logging.info("Input file: %s valid\n", fileName)
				f = open(fileName, 'r')
				self.files.append(f)
			else:
				logging.info("Non-existing file: %s provided as input, exiting now!", fileName)
				sys.exit(0)

	def countLines(self):
		for filePointer in self.files:
			filePointer.seek(0)
			self.lineCount[filePointer.name] = 0
			self.countLinesPerFile(filePointer)
		self.totalLineCount = sum(self.lineCount.values())

	def countLinesPerFile(self, filePointer):
		for line in filePointer:
			self.lineCount[filePointer.name] += 1
		return self.lineCount[filePointer.name]

	def countWords(self):
		for filePointer in self.files:
			filePointer.seek(0)
			self.wordCount[filePointer.name] = 0
			self.countWordsPerFile(filePointer)
		self.totalWordCount = sum(self.wordCount.values())

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
		self.totalCharCount = sum(self.charCount.values())

	def countCharsPerFile(self, filePointer):
		for line in filePointer:
			self.charCount[filePointer.name] += len(line)
		return self.charCount[filePointer.name]


	def printLogFile(self):
		if self.args.chars:
			nDigits = str(len(str(self.totalCharCount)))
		elif self.args.words:
			nDigits = str(len(str(self.totalWordCount)))
		elif self.args.lines:
			nDigits = str(len(str(self.totalLineCount)))
		else:
			nDigits = 0
			return

		for filePointer in self.files:
			if self.args.lines:
				if self.args.words:
					if self.args.chars:
						logging.info("%"+nDigits+"d %"+nDigits+"d %"+nDigits+"d %s", self.lineCount[filePointer.name], self.wordCount[filePointer.name], self.charCount[filePointer.name], filePointer.name)
					else:
						logging.info("%"+nDigits+"d %"+nDigits+"d %s", self.lineCount[filePointer.name], self.wordCount[filePointer.name], filePointer.name)
				else:
					if self.args.chars:
						logging.info("%"+nDigits+"d %"+nDigits+"d %s", self.lineCount[filePointer.name], self.charCount[filePointer.name], filePointer.name)
					else:
						logging.info("%"+nDigits+"d %s", self.lineCount[filePointer.name], filePointer.name)
			else:
				if self.args.words:
					if self.args.chars:
						logging.info("%"+nDigits+"d %"+nDigits+"d %s", self.wordCount[filePointer.name], self.charCount[filePointer.name], filePointer.name)
					else:
						logging.info("%"+nDigits+"d %s", self.wordCount[filePointer.name], filePointer.name)
				else:
					if self.args.chars:
						logging.info("%"+nDigits+"d %s", self.charCount[filePointer.name], filePointer.name)

		if self.args.lines:
			if self.args.words:
				if self.args.chars:
					logging.info("%"+nDigits+"d %"+nDigits+"d %"+nDigits+"d total", self.totalLineCount, self.totalWordCount, self.totalCharCount)
				else:
					logging.info("%"+nDigits+"d %"+nDigits+"d total", self.totalLineCount, self.totalWordCount)
			else:
				if self.args.chars:
					logging.info("%"+nDigits+"d %"+nDigits+"d total", self.totalLineCount, self.totalCharCount)
				else:
					logging.info("%"+nDigits+"d total", self.totalLineCount)
		else:
			if self.args.words:
				if self.args.chars:
					logging.info("%"+nDigits+"d %"+nDigits+"d total", self.totalWordCount, self.totalCharCount)
				else:
					logging.info("%"+nDigits+"d total", self.totalWordCount)
			else:
				if self.args.chars:
					logging.info("%"+nDigits+"d total", self.totalCharCount)


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

	wcInstance.printLogFile()


if __name__ == '__main__':
	main()
