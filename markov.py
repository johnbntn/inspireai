import collections, random, sys, textwrap

class Markov:
    def buildChain(self, outLen, input):
        # Build possibles table indexed by pair of prefix words (w1, w2)
        w1 = w2 = ''
        possibles = collections.defaultdict(list)
        for line in input:
            for word in line.split():
                possibles[w1, w2].append(word)
                w1, w2 = w2, word

        # Avoid empty possibles lists at end of input
        possibles[w1, w2].append('')
        possibles[w2, ''].append('')

        # Generate randomized output (start with a random capitalized prefix)
        w1, w2 = random.choice([k for k in possibles if k[0][:1].isupper()])
        output = [w1, w2]
        for _ in range(outLen):
            word = random.choice(possibles[w1, w2])
            output.append(word)
            w1, w2 = w2, word

        w1, w2 = output[-2], output[-1]

        while w2[-1] != '.':
            word = random.choice(possibles[w1, w2])
            output.append(word)
            w1, w2 = w2, word

        # return output wrapped to 70 columns
        out = ' '.join(output)
        return out