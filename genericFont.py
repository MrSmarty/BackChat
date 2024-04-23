class genericFont():

    uppercase = {"A": " ### \n#   #\n#   #\n#   #\n#####\n#   #\n#   #\n#   #\n", "B": "#### \n#   #\n#   #\n#### \n#   #\n#   #\n#   #\n#### \n", "C": " ### \n#   #\n#    \n#    \n#    \n#    \n#   #\n ### \n",
                 "D": "#### \n#   #\n#   #\n#   #\n#   #\n#   #\n#   #\n#### \n", "E": "#####\n#    \n#    \n#### \n#    \n#    \n#    \n#####\n", "F": "#####\n#    \n#    \n#### \n#    \n#    \n#    \n#    \n",
                 "G": " ### \n#   #\n#    \n# ###\n#   #\n#   #\n#   #\n ### \n", "H": "#   #\n#   #\n#   #\n#####\n#   #\n#   #\n#   #\n#   #\n", "I": "###\n # \n # \n # \n # \n # \n # \n###\n", "J": " ###\n   #\n   #\n   #\n   #\n   #\n#  #\n ## \n",
                 "K": "#   #\n#  # \n# #  \n##   \n# #  \n#  # \n#   #\n#   #\n", "L": "#   \n#   \n#   \n#   \n#   \n#   \n#   \n####\n", "M": "#     #\n##   ##\n# # # #\n#  #  #\n#     #\n#     #\n#     #\n#     #\n",
                 "N": "#   #\n##  #\n##  #\n# # #\n# # #\n#  ##\n#  ##\n#   #\n", "O": " #### \n#    #\n#    #\n#    #\n#    #\n#    #\n#    #\n #### \n", "P": "#### \n#   #\n#   #\n#### \n#    \n#    \n#    \n#    \n",
                 "Q": " #### \n#    #\n#    #\n#    #\n#    #\n#    #\n#  # #\n #### \n    # \n", "R": "#### \n#   #\n#   #\n#### \n# #  \n#  # \n#   #\n#   #\n", "S": " ####\n#    \n#    \n ### \n    #\n    #\n    #\n#### \n",
                 "T": "#####\n  #  \n  #  \n  #  \n  #  \n  #  \n  #  \n  #  \n", "U": "#   #\n#   #\n#   #\n#   #\n#   #\n#   #\n#   #\n ### \n", "V": "#   #\n#   #\n#   #\n#   #\n#   #\n#   #\n #  # \n  #  \n",
                 "W": "#       #\n#       #\n#   #   #\n #  #  # \n # # # # \n # # # # \n  #   #  \n  #   #  \n", "X": "#   #\n#   #\n # # \n  #  \n  #  \n # # \n#   #\n#   #\n", "Y": "#   #\n#   #\n#   #\n # # \n  #  \n  #  \n  #  \n  #  \n",
                 "Z": "######\n     #\n    # \n   #  \n  #   \n #    \n#     \n######\n"}
    lowercase = {}

    numbers = {"0": " ### \n#  ##\n#  ##\n# # #\n# # #\n##  #\n##  #\n ### \n",
               "1": " # \n## \n # \n # \n # \n # \n # \n###\n"}

    symbols = {".": " \n \n \n \n \n \n \n#\n", ",": "  \n  \n  \n  \n  \n #\n #\n# \n",
               ";": "  \n  \n  \n #\n  \n #\n #\n# \n", ":": "  \n  \n  \n #\n  \n  \n #\n  \n", "$": "  #  \n ####\n# #  \n ### \n  # #\n  # #\n#### \n  #  \n"}

    space = "  \n  \n  \n  \n  \n  \n  \n  \n"

    notFound = "#####\n##  #\n##  #\n# # #\n# # #\n#  ##\n#  ##\n#####\n"


def getSymbol(symbol):
    if symbol in genericFont.uppercase:
        return genericFont.uppercase[symbol]
    elif symbol in genericFont.lowercase:
        return genericFont.lowercase[symbol]
    elif symbol in genericFont.numbers:
        return genericFont.numbers[symbol]
    elif symbol in genericFont.symbols:
        return genericFont.symbols[symbol]
    elif symbol == " ":
        return genericFont.space
    else:
        return genericFont.notFound

# print(genericFont.numbers["1"])
