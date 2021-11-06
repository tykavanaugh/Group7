from wonderwords import RandomSentence

encription = {
    
}
def random_sentence(phrase):
    s = RandomSentence()
    for key in encription:
        if key == phrase:
            return encription.get(phrase)
    
    
    new_sentence = s.sentence()
    encription.update({phrase: new_sentence})
    return encription
   
    
    
    
    
    
print(random_sentence('We are all in big trouble'), "\n")
print(random_sentence('Big Trouble in Little China'), "\n")
print(random_sentence('Fantastic voyage of the Enterprise'), "\n")
print(random_sentence('Big Trouble in Little China'), "\n")

    
    