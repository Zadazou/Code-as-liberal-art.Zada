import markovify
# # look at documentation for markofivy here: https://github.com/jsvine/markovify

text = open("cookingsteps.txt").read()

generator = markovify.Text(text) 

paragraph = ""

for i in range(10):
    paragraph += str(generator.make_short_sentence(150))
    paragraph += " "

print("\n\n\n")
print(paragraph)
print("\n\n\n")

# with open("ingredient.txt") as f:
#        text = f.read()
# text_model = markovify.NewlineText(text)
# for key in text_model.chain.model.keys():
#        if "___BEGIN__" in key:
#            print(key)