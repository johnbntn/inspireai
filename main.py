import random
import markov as m
def main():
    
    #Create chain
    with open('trainingData.txt', 'r', encoding='utf-8') as file:
        text = file.readlines()
    markov = m.Markov().buildChain(text)

    #Call intro thing

    print(markov)

main()