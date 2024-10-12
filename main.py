import random
import markov as m
import ui
def main():
    ui.intro()
    wordCount = random.randint(5, 15)
    #Create chain
    with open('trainingData.txt', 'r', encoding='utf-8') as file:
        text = file.readlines()
    markov = m.Markov().buildChain(wordCount, text)
    markov = "\"" + markov + "\""
    print(markov)

main()