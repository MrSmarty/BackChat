import random


class censor():
    # 0 is no censor
    # 1 is replace only vowels
    # 2 is replace entire word
    level = 1

    chars = "!@#$%&*"

    # list of banned words
    banned = {"shit", "ass", "fuck", "bitch", "crap", "dick", "cunt"}

    vowels = {"a", "e", "i", "o", "u"}

    def Censor(word):
        if any(sample in word.lower() for sample in censor.banned) and censor.level != 0:
            out = ""

            if censor.level == 1:
                # replace vowels with random from chars
                for char in word:
                    # print("test")
                    if char.lower() in censor.vowels:
                        out += str(random.sample(censor.chars, 1))[2:-2]
                    else:
                        out += char

            elif censor.level == 2:
                # replace all characters with new character
                out = str(random.sample(censor.chars, len(word)))[2:-2]
                out = out.replace("', \'", "")

            return out

        else:
            return word


print(censor.Censor("shitass"))
