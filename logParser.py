import os, sys
import subprocess
import argparse
import numpy as np
import matplotlib.pyplot as plt

class logParser:
	def __init__(self, args):
		self.purities = {};
		self.efficiencies = {};
		self.labels = {};

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

	def parse(self):
		for filePointer in self.files:
			bashCommand = "grep PrChecker.Downs "+filePointer.name
			output = subprocess.check_output(bashCommand.split())
			outputList = output.split()

			self.purities[filePointer.name] = [float(outputList[i+1]) for i,x in enumerate(outputList) if x == "purity:"]
			self.efficiencies[filePointer.name] = [float(outputList[i+1]) for i,x in enumerate(outputList) if x == "hitEff:"]
			self.labels[filePointer.name] = [outputList[i] for i,x in enumerate(outputList) if "UT" in x]

	def plotData(self):
		for filePointer in self.files:
			ax = plt.subplot(111)
			colors = ["#ff0000","#ff4e00","#ff9c00","#ffeb00","#c4ff00","#75ff00","#27ff00","#00ff27","#00ff75","#00ffc4","#00ebff","#009cff","#004eff","#0000ff"]
			for i in range(14):
				plt.scatter(self.efficiencies[filePointer.name][i], self.purities[filePointer.name][i], s = 25, c = colors[i], label = self.labels[filePointer.name][i])
			plt.xlabel("Hit efficiency [%]")
			plt.ylabel("Purity [%]")
			plt.legend(loc = 'lower right', scatterpoints = 1, prop={'size':6})
			plt.savefig(filePointer.name[5:-4] + ".pdf")
			plt.clf()


def main():
	argparser = argparse.ArgumentParser()
	argparser.add_argument("input", nargs = "+", help="name of input file")
	args = argparser.parse_args()

	lpInstance = logParser(args)

	lpInstance.parse()
	lpInstance.plotData()


if __name__ == '__main__':
	main()
