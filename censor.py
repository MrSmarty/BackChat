import random


# 0 is no censor
# 1 is replace only vowels
# 2 is replace entire word
level = 1

chars = "!@#$%&*"

# list of banned words
banned = {"shit", "ass", "fuck", "bitch", "crap", "dick", "cunt", "nigger"}

vowels = {"a", "e", "i", "o", "u"}

def Censor(string):
	out = ""
	for word in string.split(" "):
		if any(sample in word.lower() for sample in banned) and level != 0:
        		#out = ""

			if level == 1:
            			# replace vowels with random from chars
				for char in word:
                			# print("test")
					if char.lower() in vowels:
						out += str(random.sample(chars, 1))[2:-2]
					else:
						out += char
				print("testing")
				out += " "
			elif level == 2:
				# replace all characters with new character
				out += str(random.sample(chars, len(word)))[2:-2] + " "
				out = out.replace("', \'", "")

        	#return out
		else:
        		out += word + " "
	
	return out

#print(Censor("Move over asshole"))
