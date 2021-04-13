

import json

from collections import defaultdict


class SentenceReadingAgent:
    def __init__(self):

        pass

    def solve(self, sentence, question):

        ans = ''

        # d = defaultdict(list)
        # with open('dictionary.json') as f:
        #   d = json.load(f)
        d = {"PROPN": ["Serena", "Ada","Irene","Red", "Andrew", "Bobbie", "Cason", "David", "Farzana", "Frank", "Hannah", "Ida", "Irene", "Jim", "Jose", "Keith", "Laura", "Red", "Lucy", "Meredith", "Nick", "Ada", "Yeeling", "Yan"], "DET": ["the", "a", "this", "some", "all", "an", "each", "which", "these", "no", "any", "every", "those", "all" "both"], "ADP": ["of", "to", "for", "with", "as", "at", "from", "by", "up", "like", "over", "after", "under", "through", "before", "between", "next", "until", "above", "during", "toward", "against", "behind", "among"], "CCONJ": ["and", "or", "but"], "NOUN": ["morning", "car", "adults", "island," "room", "men", "women", "children" "word", "time", "make", "thing", "day", "sound", "number", "water", "people", "side", "work", "part", "place", "man", "year", "name", "think", "line", "turn", "mean", "move", "sentence", "set", "air", "end", "hand", "port", "spell", "land", "follow", "act", "men", "kind", "house", "picture", "animal", "point", "mother", "world", "self", "earth", "father", "head", "page", "country", "answer", "school", "grow", "study", "plant", "food", "sun", "eye", "door", "city", "tree", "cross", "start", "story", "sea", "draw", "run", "press", "night", "life", "children", "example", "ease", "paper","play", "mark", "book", "letter", "river", "car", "feet", "group", "carry", "rain", "eat", "room", "friend", "idea", "fish", "mountain", "north", "base", "horse", "watch", "color", "wood", "girl", "list", "talk", "bird", "body", "dog", "family", "pose", "song", "measure", "state", "product", "class", "wind", "question", "ship", "area", "rock", "order", "fire", "problem", "piece", "farm", "king", "size", "hour", "step", "ground", "interest", "listen", "table", "travel", "morning", "vowel", "war", "pattern", "center", "love", "person", "money", "road", "map", "science", "rule", "govern", "notice", "voice", "power", "town", "fly", "unit", "machine", "note", "plan", "figure", "star", "box", "noun", "field", "noun" "rest", "pound", "beauty", "drive", "front", "teach", "week", "sleep", "minute", "mind", "tail", "fact", "street", "inch", "lot", "course", "wheel", "force", "object", "surface", "moon", "island", "foot", "test", "record", "boat", "gold", "plane", "age", "wonder", "laugh", "check", "game", "shape", "miss", "heat", "snow", "bed","weight", "language"], "AUX": [
            "is", "was", "are", "can", "were", "do", "will", "would", "has", "could", "may", "been", "does", "must", "should", "might"], "ARTICLES": ["The", "the", "an", "a"], "PRON": ["it", "She","He","you", "he", "I", "his", "they", "What", "what", "we", "your", "she", "their", "them", "her", "him", "my", "who", "Who","me", "our", "us", "nothing"], "SCONJ": ["that", "if", "than", "near", "since", "while"], "ADV": ["on", "there", "out", "when", "how", "about", "then", "so", "down", "now", "where", "back", "very", "just", "much", "too", "well", "also", "home", "even", "here", "why", "off", "again", "still", "never", "together", "often", "always", "once", "ever", "though", "soon", "better", "early", "fast", "yet", "ago", "perhaps"], "VERB": ["be", "written","sings", "sound", "run", "is", "wrote", "walk", "are", "bring", "give", "brought", "have", "had", "use", "said", "way", "write", "see", "look", "go", "come", "did", "know", "call", "find", "take", "get", "made", "came", "show", "bring","brough","give", "form", "say", "help", "cause", "differ", "tell", "play", "put", "read", "add", "big", "run", "ask", "change", "went", "need", "try", "build", "stand", "found", "learn", "cover", "thought", "let", "keep", "saw", "Give","left", "stop", "seem", "begin", "got", "music", "care", "took", "began", "hear", "cut", "face", "feel", "leave", "happen", "told", "knew", "pass", "heard", "am", "remember", "hold", "reach", "sing", "lay", "serve", "appear", "pull", "fall", "lead", "cry", "wait", "done", "stood", "contain", "gave", "develop", "produce", "stay", "decide", "ran", "brought", "bring", "sit", "fill"], "NUM": ["one hundred" "two", "three", "four", "hundred", "five", "six", "ten", "thousand"], "ADJ": ["hot", "busy", "other", "many", "long", "cool", "more", "most", "first", "new", "live", "little", "only", "round", "good", "great", "low", "same", "right", "old", "want", "small", "large", "high", "such", "light", "own", "last", "hard", "far", "late", "close", "real", "few", "open", "white", "second", "sure", "main", "enough", "plain", "usual", "young", "ready", "red", "direct", "black", "short", "numeral", "complete", "half", "south", "top", "whole", "best", "true", "west", "less", "simple", "several", "slow", "cold", "fine", "certain", "dark", "correct", "able", "final", "green", "quick", "warm", "free", "strong", "special", "clear", "full", "blue", "deep", "busy", "common", "possible", "dry"], "INTJ": ["boy", "oh", "yes", "cool"], "PART": ["n\u2019t"]}

        nouns = [i for i in d["NOUN"]]
        verbs = [i for i in d["VERB"]]
        names = [i for i in d["PROPN"]]
        numbers = [i for i in d["NUM"]]
        adjective = [i for i in d["ADJ"]]
        adverb = [i for i in d["ADV"]]
        articles = [i for i in d["ARTICLES"]]
        det = [i for i in d["DET"]]
        aux = [i for i in d["AUX"]]
        adp = [i for i in d["ADP"]]
        pron = [i for i in d["PRON"]]


        measurements = ['mile', 'half-mile',
                        'kilometer', 'long', 'short', 'big', 'small', 'long', 'one mile', 'mile']

        colors = ['blue', 'green', 'red', 'white', 'orange', 'black']

        times = ['later', 'soon', 'in a bit',
                 'tomorrow', 'now', 'morning', 'night']

        quants = ['all', 'some', 'a few', 'many']

        directions = ['north', 'south', 'east', 'west']

        sentence_dictionary = {}
        sentence = sentence.replace('.', '')
        sentence = sentence.split()
        question = question.replace('?', '')
        question = question.split()

        for i in sentence:
            if i in nouns:
                sentence_dictionary[i] = "NOUN"
            elif i in verbs:
                sentence_dictionary[i] = "VERB"
            elif i in names:
                sentence_dictionary[i] = "NAME"
            elif i in numbers:
                sentence_dictionary[i] = "NUMBER"
            elif i in adjective:
                sentence_dictionary[i] = "ADJECTIVE"
            elif i in adverb:
                sentence_dictionary[i] = "ADVERB"
            elif i in articles:
                sentence_dictionary[i] = "ARTICLE"
            elif i in colors:
                sentence_dictionary[i] = "COLOR"
            elif 'AM' in i or 'PM' in i:
                sentence_dictionary[i] = "TIME"
            elif i in times:
                sentence_dictionary[i] = "TIMEWORDS"
            elif i in measurements:
                sentence_dictionary[i] = "MEASURE"
            elif i in quants:
                sentence_dictionary[i] = "QUANTITY"
            elif i in directions:
                sentence_dictionary[i] = "DIRS"
            elif i in det:
                sentence_dictionary[i] = "DET"
            elif i in aux:
                sentence_dictionary[i] = "AUX"
            elif i in adp:
                sentence_dictionary[i] = "ADP"
            elif i in pron:
                sentence_dictionary[i] = "PRON"
    

            sentence_dict = {}
            for key, value in sentence_dictionary.items():
                if value not in sentence_dict:
                    sentence_dict[value] = [key]
                else:
                    sentence_dict[value].append(key)

        print(sentence_dict)

        
        print(question)

        # if 'At' in question[0]:
        #     return sentence_dict.get("TIME")[0]

        # if 'What' in question[0]:

        #     if question[-1] in colors:
        #         print('here')
        #         if sentence[1] in colors:
        #             print('hereeeee')
        #             return sentence_dict.get("NOUN")[0] if sentence_dict.get("NOUN") else 'none'
        #         if sentence [-1] in colors:
        #             return sentence_dict.get("NOUN")[0] if sentence_dict.get("NOUN") else 'none'
        #         else:
        #             return sentence_dict.get("NOUN")[0] if sentence_dict.get("NOUN") else 'none'

                

        #     if question[1] in aux and question[2] in colors:
        #         return sentence_dict.get("COLOR")[0] if sentence_dict.get("COLOR") else 'none'

        #     if question[1] in aux and question[2] in names and question[3] in verbs:
        #         return sentence_dict.get("VERB")[0] if sentence_dict.get("VERB") else 'none'




        #     if question[1] in colors and question[-1] in nouns:
        #         return sentence_dict.get("COLOR")[0] if sentence_dict.get("COLOR") else 'none'

        #     if question[1] == 'color' and question[-1] in nouns:
        #         return sentence_dict.get("COLOR")[0] if sentence_dict.get("COLOR")[0] else 'none'

        #     if question[1] in verbs and question[2] in aux and sentence[3] in verbs:
        #         return sentence_dict.get("NOUN")[0] if sentence_dict.get("NOUN") else 'none'


        #     if question[1] in verbs and question[2] in pron and question[3] in verbs:
        #         print('')
        #         return sentence_dict.get("NOUN")[-1] if sentence_dict.get("NOUN") else 'none'


        #     if question[1] in verbs and question[2] in aux and sentence[3] in colors:
        #         return sentence_dict.get("COLOR")[0] if sentence_dict.get("COLOR") else 'none'

        #     if question[1] in verbs and question[2] in verbs and sentence[3] in pron:
        #         return sentence_dict.get("NOUN")[-1] if sentence_dict.get("NOUN") else 'none'

        #     if question[1] in verbs and question[2] in adjective:
        #         return sentence_dict.get("NOUN")[0] if sentence_dict.get("NOUN") else 'none'




        #     # if 'color' in question:
        #     #     return sentence_dict.get("COLOR")[0] if sentence_dict.get("COLOR") else 'none'

        #     # if any(x in colors for x in question):
        #     #     return sentence_dict.get("COLOR")[0] if sentence_dict.get("COLOR") else 'none'


        #     # if question[1] in aux and question [3] in pron:
        #     #     print('here')
        #     #     return sentence_dict.get("PRON")[0] if sentence_dict.get("PRON") else 'none'

        #     if question[1] in verbs and question[-1] in nouns:
        #         print('here')
        #         if question[1] in sentence and question[2] in pron:
        #             print('2nd')
        #             return sentence_dict.get("NAME")[0] if sentence_dict.get("NAME") else 'none'
        #         if question[1] in sentence:
        #             print('hehehehehe')
        #             return sentence_dict.get("NOUN")[0] if sentence_dict.get("NOUN") else 'none'
        #         else:
        #             return sentence_dict.get("NOUN")[0] if sentence_dict.get("NOUN") else 'none'


        #         if question[1] in aux and question[2] in names and question[-1] in verbs:
        #             print('hehehe')

        #             return sentence_dict.get("NOUN")[-1] if sentence_dict.get("NOUN") else 'none'


        #     if question[1] in aux and question[2] in pron and question[-1] in pron:
        #         print('here')
        #         return sentence_dict.get("NOUN")[-1] if sentence_dict.get("NOUN")[0] else 'none'

        #     if question[-1] in verbs:
        #         print('here')
        #         if question[1] in aux:
        #             return sentence_dict.get("ADJECTIVE")[0] if sentence_dict.get("ADJECTIVE") else 'none'
        #         elif question[-1] == sentence [-1]:
        #             return sentence_dict.get("NOUN")[0] if sentence_dict.get("NOUN") else 'non'
        #         else:
        #             return sentence_dict.get("NOUN")[0] if sentence_dict.get("NOUN") else 'none'



        #     if question[1] in aux and question[2] in verbs:
        #         print('here')
        #         if question[-1] in sentence:
        #             return sentence_dict.get("NOUN")[0] if sentence_dict.get("NOUN") else 'none'
        #         else:

        #             return sentence_dict.get("VERB")[0] if sentence_dict.get("VERB") else 'none'


        #     if question[1] in aux and question[-1] in nouns:
        #         print('here')  
        #         if sentence[0] in verbs:
        #             return sentence_dict.get("NOUN")[0] if sentence_dict.get("NOUN") else 'none'
        #         else:
        #             return sentence_dict.get("NOUN")[-1] if sentence_dict.get("NOUN") else 'none'



        #     if question[1] in aux and question[-1] in verbs:
        #         return sentence_dict.get("VERB")[0] if sentence_dict.get("VERB") else 'none'

        #     if question[-1] in adp:
        #         return sentence_dict.get("NOUN")[1] if sentence_dict.get("NOUN") else 'none'

        #     if question[1] in verbs and question[-1] in adverb: 
        #         return sentence_dictionary.get("NOUN")[0] if sentence_dict.get("NOUN") else 'none'

        #     if question[1] in aux and question[-1] in nouns:
        #         if 'of' in sentence:
        #             return sentence_dict.get("NOUN")[1] if sentence_dict.get("NOUN") else 'none'
        #         if question[2] == sentence[2]:
        #             return sentence_dict.get("VERB")[0] if sentence_dict.get("VERB") else 'none'
        #         else:
        #             return sentence_dict.get("NAME")[0] if sentence_dict.get("NOUN") else 'none'

        #     if question[1] in aux and question[-1] in pron:
        #         if 'of' in sentence:
        #             return sentence_dict.get("NOUN")[-1] if sentence_dict.get("NOUN") else 'none'
        #         else:
        #             return sentence_dict.get("NAME")[0] if sentence_dict.get("NAME") else 'none'

        #     if question[1] in nouns and question[-1] in colors:
        #         return sentence_dict.get("COLOR")[0] if sentence_dict.get("COLOR") else 'none'

        #     if 'be' in question:
        #         return sentence_dict.get("ADJECTIVE")[0] if sentence_dict.get("ADJECTIVE") else 'none'

        #     if question[1] in nouns and question[-1] in names:
        #         return sentence_dict.get("NOUN")[0] if sentence_dict.get("NOUN") else 'none'

        #     if question[1] in nouns and question[-1] in nouns:
        #         return sentence_dict.get("NOUN")[1] if sentence_dict.get("NOUN") else 'none'

        #     if question[1] in pron and question[-1] in verb:
        #         return sentence_dict.get("VERB")[0] if sentence_dict.get("VERB") else 'none'


        #     if question[1] in pron and question[-1] in pron:
        #         return sentence_dict.get("NOUN")[0] if sentence_dict.get("NOUN") else 'none'

        #     if question[1] in aux and question[1] in aux:
        #         return sentence_dict.get("VERB")[0] if sentence_dict.get("VERB") else 'none'

        #     if question[1] in aux and question [-1] in verbs:
        #         print('here')
        #         return sentence_dict.get("NOUN")[-1] if sentence_dict.get("NOUN") else 'none'

        #     if question[1] in aux and question [-1] in nouns:
        #         print('here')
        #         return sentence_dict.get("NOUN")[0] if sentence_dict.get("NOUN") else 'none'


        #     if question[1] in aux and question [-1] in adjective:
        #         return sentence_dict.get("NOUN")[-1] if sentence_dict.get("NOUN") else 'none'

        #     if question[1] in aux and question[2] in verbs:
        #         print('here')
        #         if question[-1] == sentence[-1]:
        #             return sentence_dict.get("VERB")[0] if sentence_dict.get("VERB") else 'none'







        if 'Who' in question[0]:
            # print(sentence[sentence_dict.get("NAME")[0]])
            
            if question[1] in verbs:
                if sentence[0] in names:
                    return sentence_dict.get("NAME")[0]

            # if question[-1] == 'with':
            #     if sentence_dict.get("NAME")[0] == question[-1]:
            #         return sentence_dict.get("NAME")[1] if sentence_dict.get("NAME") else 'none'
            #     else:
            #         return sentence_dict.get("NAME")[0] if sentence_dict.get("NAME") else 'none'


            # # if question[1] == 'with':
            # #     return sentence_dict.get("NAME")[0] if sentence_dict.get("NAME") else 'none'

            # if question[1] in verbs:
            #     print("HERHERE")
            #     # if question [2] in verbs:
            #     if sentence_dict.get("NAME"):
            #         if question[-1] == sentence[-1]:
            #             return sentence_dict.get("NAME")[0]  if sentence_dict.get("NAME") else 'none'
 
                #     else:
                #         return sentence_dict.get("NAME")[-1]  if sentence_dict.get("NAME") else 'none'
                # if question[2] == sentence[1]:
                #     return sentence[-1]
                # if question[2] in names:
                #     print('here really')
                #     return sentence_dict.get("NAME")[0] if sentence_dict.get("NAME") else 'none'
                # elif sentence_dict.get("PRON"):
                #     print('here now')
                #     return sentence_dict.get("PRON")[0] if sentence_dict.get("PRON") else 'none'

        #     if question[1] in verbs and question[-1] in nouns:
        #         print('here')
        #         if sentence_dict.get("NAME"):
        #             return sentence.get("NAME")[0] if sentence_dict.get("NAME") else 'none'
        #         if sentence_dict.get("PRON"):
        #             return sentence_dict.get("PRON")[0] if sentence_dict.get("PRON") else 'none'
        #         if sentence_dict.get("NOUN"):
        #             return sentence_dict.get("NOUN")[0] if sentence_dict.get("NOUN") else 'none'
        #         else:
        #             return 'none'

        #     if question[1] in aux:
        #         print('here')
        #         if question[-1] in names:
        #             return sentence_dict.get("NAME")[0] if sentence_dict.get("NAME") else 'none'
        #         if question[2] in verbs and sentence[0] in names:
        #             return sentence_dict.get("NAME")[0] if sentence_dict.get("NAME") else 'none'
        #         elif question[2] in verbs:
        #             return sentence_dict.get("NOUN")[0] if sentence_dict.get("NOUN") else 'none'




        #     if question[1] in aux:
        #         print('here')
        #         if sentence[-1] =='to' or any(x in det for x in sentence):
        #             return sentence_dict.get("PRON")[0] if sentence_dict.get("PRON") else 'none'
        #         if sentence[1] in names:
        #             return sentence_dict.get("NAME")[1] if sentence_dict.get("NAME") else 'none'
        #         if sentence[-1] in names:
        #             return sentence_dict.get("NAME")[0] if sentence_dict.get("NAME") else 'none'

        #     if question[1] in pron and 'in' in question:
        #         return sentence.get("NOUN")[-1] if sentence_dict.get("NOUN") else 'none'

        #     # if question[1] in verbs and sentence_dict.get("NAME"): 
        #     #     return sentence_dict.get("NAME")[0] if sentence_dict.get("NAME") else 'none'






        #     # if question[1] in verbs:
        #     #   if any(x in names for x in question) == any(x in names for x in sentence):
        #     #       return sentence_dict.get("NAME")[1] if sentence_dict.get("NAME") else 'none'




        # if 'How' in question[0]:

        #     if question[1] in verbs:
        #         if question[1] in sentence:
        #             return sentence_dict.get("VERB")[0] if sentence_dict.get("VERB") else 'none'
        #         else:
        #             return sentence_dict.get("VERB")[1] if sentence_dict.get("VERB") else 'none'

        #     if question[1] == 'many' or question[1] == 'long' or question[1] == 'big' or \
        #     question[1] == 'much':
        #         if any(x in numbers for x in sentence):
        #             return sentence_dict.get("NUMBER")[0] if sentence_dict.get("NUMBER") else 'none'
        #         elif any(x in measurements for x in sentence):
        #             return sentence_dict.get("MEASURE")[0]
        #         elif any(x in quants for x in sentence):
        #             return sentence_dict.get("QUANTITY")[0] if sentence_dict.get("QUANTITY") else 'none'
        #         else:
        #             return sentence_dict.get("DET")[0] if sentence_dict.get("DET") else 'none'

        #     if question[1] == 'far':
        #         if sentence_dict.get("NUMBER"):
        #             return sentence_dict.get("NUMBER")[0] if sentence_dict.get("NUMBER") else 'none'
        #         else:
        #             return sentence_dict.get("MEASURE")[0] if sentence_dict.get("MEASURE") else 'none'


        #     if 'to' in question:
        #         return sentence_dict.get("VERB")[0] if sentence_dict.get("VERB") else 'none'

        #     if 'much' in question:
        #         if sentence_dict.get("DET"): 
        #             [0]
        #             return sentence_dict.get("DET")[0] if sentence_dict.get("DET") else 'none'
        #         else:
        #             return sentence_dict.get("NUMBER")[0] if sentence_dict.get("NUMBER") else 'none'



        # if 'Where' in question[0]:

        #     if question[1] in verbs and any(x in directions for x in sentence) == False:
        #         if question[1] in sentence:
        #             return sentence_dict.get("NOUN")[-1] if sentence_dict.get("NOUN") else 'none'
        #         else:
        #             return sentence_dict.get("NOUN")[1] if sentence_dict.get("NOUN") else 'none'
                

        #     if question[-1] in verbs:

        #         if sentence_dict.get("NOUN")[0] == question[-1]:
        #             return sentence_dict.get("NOUN")[1] if sentence_dict.get("NOUN") else 'none'
        #         if question[1] in verbs:
        #             return sentence_dict.get("NOUN")[0] or sentence_dict.get("VERB")[0] \
        #             if sentence_dict.get("NOUN") else 'none'
        #         else:
        #             return sentence_dict.get("NOUN")[0] if sentence_dict.get("NOUN") else 'none'

        #     if question[1] in verbs and any(x in directions for x in sentence):
        #         return sentence_dict.get("DIRS")[0] if sentence_dict.get("DIRS") else 'none'


        #     if question[1] in adverb and any(x in directions for x in sentence):
        #         return sentence_dict.get("DIRS")[0] if sentence_dict.get("DIRS") else 'none'

        #     if question[1] in aux and any(x in directions for x in sentence):
        #         return sentence_dict.get("DIRS")[0] if sentence_dict.get("DIRS") else 'none'

        #     if question[1] in verbs and question[-1] in verbs:
        #         return sentence_dict.get("NOUN")[0] if sentence_dict.get("NOUN") else 'none'

        # if 'When' in question[0]:

        #     if question[1] in aux and question[2] in names and question[3] in adjective:
        #         print('here')
        #         return sentence_dict.get("ADJECTIVE")[1] + ' ' + sentence_dict.get("NOUN")[0] \
        #          if sentence_dict.get("NOUN") else 'none'

        #     if any(x in times for x in sentence):
        #         return sentence_dict.get("TIME")[0] if sentence_dict.get("TIME") else 'none'

        #     if any(x in det for x in sentence):
        #         return sentence_dict.get("DET")[0] if sentence_dict.get("DET") else 'none'

        #     if question[1] in aux and question[2] in names:
        #         return sentence_dict.get("NOUN")[0] if sentence_dict.get("NOUN") else 'none'






        #     else:
        #         return sentence_dict.get("ADV")[0] if sentence_dict.get("ADV") else 'none'

        #     # if question[1] in aux ""



test_agent = SentenceReadingAgent()
# # # Sentence: The water is blue.
# # # Question: What color is the water?

s = "Ada brought a short note to Irene."
q ="Who brought the note?"

# # s = "David and Lucy walk one mile to go to school every day at 8:00AM when there is no snow."
# # q = "Who does Lucy go to school with?"

print(test_agent.solve(s, q))  # "8:00AM"