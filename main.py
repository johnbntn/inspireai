import collections, random, sys, textwrap
import markov as m
def main():

    wordCount = random.randint(10, 15)
    #Create chain
    markov = m.Markov().buildChain(wordCount, sys.stdin)

    #Call intro thing

    print(markov)