text = open("text.txt", "w", encoding="utf-8")
text.write("стол\n")
text.write("экран\n")
text.write("дом\n")
text.write("замок\n")
text.write("закон\n")
text.write("земля\n")
text.write("камаз\n")
text.close()

text = open("text.txt", "r", encoding="utf-8")
words = text.read()
text.close()

# letter = "з"

result = words.replace("з", "***")

# print(result)

file = open("output1.txt", "w", encoding="utf-8")
file.write(result)