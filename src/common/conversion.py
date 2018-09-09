import argparse

TRUE_LIST = ["yes",
			 "true",
			 "y",
			 "t",
			 "1"
			 ]

FALSE_LIST = ["no",
			  "false",
			  "n",
			  "f",
			  "0"
			  ]

def str2bool(value):
	if value.lower() in TRUE_LIST:
		return True
	elif value.lower() in FALSE_LIST:
		return False
	else:
		raise argparse.ArgumentTypeError('Boolean value expected.')