import collections, random, sys, textwrap
import markov as m
import ui
def main():
    ui.intro()
    wordCount = random.randint(10, 15)
    #Create chain
    markov = m.Markov().buildChain(wordCount, sys.stdin)
    

    print(markov)