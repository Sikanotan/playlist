import os
import argparse


cwd_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(cwd_directory)


# Arguments
parser = argparse.ArgumentParser(prog="Illu",
                        description="Process the given email, or the given file.\
                        Accepted(xlsx)")

parser.add_argument('', nargs='*', default='all')

if __name__ == "__main__":

	"""
		The purpose of this script is to extract mail address and test with an
		STMP validation if the email seems to exist.
		The script will accept as argument an email address or a file where 
		email address are stored
	"""