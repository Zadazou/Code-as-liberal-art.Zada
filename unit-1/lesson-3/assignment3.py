import sys
word_list = [ "astonishing", "rehabilitation", "understanding", "mathematics", "liability", "obligation", "fashionable", "organisation", "evolution", "excavation", "constitution", "invisible", "implication", "academy", "appreciate", "aquarium", "generation", "reproduction", "accessible", "commemorate", "violation", "integration", "combination", "definition", "emergency", "deprivation", "vegetarian", "photocopy", "radiation", "admiration", "laboratory", "helicopter", "embarrassment", "experience", "hierarchy", "hospitality", "conventional", "deviation", "regulation", "indication", "acquisition", "ambiguous", "civilization", "exaggerate", "intermediate", "recommendation", "casualty", "motivation", "manufacture", "deteriorate" ]
word_list.sort()
word_list = sys.argv
word_list.pop(0)
index = int(sys.argv[1])
print( word_list[index] )
