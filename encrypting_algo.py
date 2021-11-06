from wonderwords import RandomSentence
import csv

def random_sentence(phrase):
    
    encryption = {}
    
    with open('encrypting_algo.csv', mode='r') as r:
        reader = csv.reader(r)
        encryption.update({rows[0]:rows[1] for rows in reader})
    
    s = RandomSentence()
    for key in encryption:
        if key == phrase:
            return encryption.get(phrase)
    
    new_sentence = s.sentence()
    encryption.update({phrase: new_sentence})
    
    with open('encrypting_algo.csv', 'w') as f:
        for key in encryption.keys():
            f.write("%s,%s\n"%(key,encryption[key]))
    print("File Saved\n")
    return new_sentence
   
    




    

  
    