text = ""
stopword = ""
while True:
    line = input()
    if line.strip() == stopword:
        break
    text += "%s ],[" % line


print(text)

