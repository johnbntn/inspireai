import random
import markov as m
import ui
import time
def main():

    status = True
    ui.intro()

    with open('trainingData.txt', 'r', encoding='utf-8') as file:
        text = file.readlines()

    while status == True:

        wordCount = random.randint(5, 15)
        quote = "\"" + m.Markov().buildChain(wordCount, text) + "\""
        print(quote)

        time.sleep(2)
        print("\nI:Hope that helped, would you like to see another? (yes,no)")
        
        response = input()
        if response == "no" or response == "No":
            status = False

main()