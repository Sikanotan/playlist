import os
import argparse
import re


cwd_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(cwd_directory)


# Arguments
parser = argparse.ArgumentParser(prog="Illu",
                        description="Process the given email, or the given file.\
                        Accepted(xlsx)")

parser.add_argument('email', nargs='*', default='None')

if __name__ == "__main__":

	"""
		The purpose of this script is to extract mail address and test with an
		STMP validation if the email seems to exist.
	"""

def isanemail(address): -> bool
	"""
		Check if the given string is an email following RFC 822.
		https://www.w3.org/Protocols/rfc822/

		local-part@domain
	"""
	# The special char are unauthorized execept .
	address_validity = False
	error_message = ""
	specials   = ["(", ")", "<", ">", "@", ",", ";", ":", "\\", "<", ">", ".",\
	"[","]", "\""]
	# And the range bellow 38
	ascii_unauthorized = [127, 177]

	addr_spec = str(address).split("@")

	if addr_spec == 2:
		
		local_part, domain = addr_spec

		mail = local_part + domain
		dot_found = False

		for each in mail:

			if each in specials:

				if each == ".":
					if dot_found == True:
						error_message = "The given address is not valid."
						break
					else:
						dot_found = True
				else:
					error_message = "The given address is not valid."
					break
			else:
				dot_found = False

			ascii_value = ord(each)

			if ascii_value in ascii_unauthorized:

				error_message = "The given address is not valid."
				break
			elif ascii_value < 38:
				error_message = "The given address is not valid."
				break
			else:
				char_valid = True

		address_validity = True

	else:

		error_message = "The given address is not valid."

	print(error_message)

	return address_validity