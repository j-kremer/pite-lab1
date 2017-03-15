import os, sys
import subprocess
import argparse

class logParser:
	def __init__(self, args):
		self.args = args

		self.files = []
		for fileName in self.args.input:
			if os.path.isfile(fileName):
				print "Input file:", fileName, "valid\n"
				f = open(fileName, 'r')
				self.files.append(f)
			else:
				print "Non-existing file:", fileName, "provided as input, exiting now!"
				sys.exit(0)

		for filePointer in self.files:
			bashCommand = "grep PrChecker.Downs "+filePointer.name
			output = subprocess.check_output(bashCommand.split())
			print output


def main():
	argparser = argparse.ArgumentParser()
	argparser.add_argument("input", nargs = "+", help="name of input file")
	args = argparser.parse_args()

	lpInstance = logParser(args)


if __name__ == '__main__':
	main()
