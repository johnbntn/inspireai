import random
art= """
  _____ _   _  _____ _____ _____ _____  ______ 
 |_   _| \ | |/ ____|  __ \_   _|  __ \|  ____|
   | | |  \| | (___ | |__) || | | |__) | |__   
   | | | . ` |\___ \|  ___/ | | |  _  /|  __|  
  _| |_| |\  |____) | |    _| |_| | \ \| |____ 
 |_____|_| \_|_____/|_|   |_____|_|  \_\______|
                                                                                            
"""

print (art)
introduction = ["Hello, how are you feeling today?", "How do you do?", "Hi! How are you?", "Greetings! What's your mood like?", "Howdy! How ya doing?"]
response = [" Well, if that's the case, I think you'd like this quote I made...", "Oh, wow. I think you'll like my quote then...", "I feel you! You'd like my quote then...", "We've all been there. Here's some food for thought...", "Your feelings are valid. Consider this quote I made..."]
def intro(): 
    print ("I:" + random.choice(introduction))
    x = input()
    print ("I:" + random.choice(response))

intro()