class symbolify():
    d = {"hashtag ": "#", "hash tag ": "#", "hash-tag ": "#",
         " period period": ".", " comma": ",", }

    def Symbolify(string):
        for entry in symbolify.d.keys():
            print(entry)
            string = string.replace(entry, symbolify.d.get(entry))
        return string


print(symbolify.Symbolify("hashtag I like apples"))
