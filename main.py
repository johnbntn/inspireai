import random
import markov as m
def main():

    wordCount = random.randint(5, 15)
    #Create chain
    with open('trainingData.txt', 'r', encoding='utf-8') as file:
        text = file.readlines()
    markov = m.Markov().buildChain(wordCount, text)

    #Call intro thing

    print(markov)

main()