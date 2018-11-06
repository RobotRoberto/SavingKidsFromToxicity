import markovify
import pandas as pd

df = pd.read_csv('dataset/train.csv')

text=dict()
text['identity_hate'] = ""
text['toxic'] = ""
text['severe_toxic'] = ""
text['obscene'] = ""
text['threat'] = ""
text['insult'] = ""

for index, row in df.iterrows():
	if row['identity_hate'] == 1:
		text['identity_hate'] += row['comment_text']
		text['identity_hate'] += "\n"
	if row['toxic'] == 1:
		text['toxic'] += row['comment_text']
		text['toxic'] += "\n"
	if row['severe_toxic']==1:
		text['severe_toxic'] += row['comment_text']
		text['severe_toxic'] += "\n"
	if row['obscene'] == 1:
		text['obscene'] += row['comment_text']
		text['obscene'] += '\n'
	if row['threat'] == 1:
		text['threat'] += row['comment_text']
		text['threat'] += '\n'
	if row['insult'] ==1:
		text['insult']+= row['comment_text']
		text['insult']+='\n'
	# if index == 100:
	# 	break
output = open("generated_phrases.txt", "a")

for key,value in text.items():
	text_model = markovify.NewlineText(value)

	output.write(key)
	output.write("\n")
	for i in range(10):
		sentence = text_model.make_sentence()
		if sentence is None:
			sentence = "lick my balls"
		print(sentence)
		output.write(sentence)
		output.write("\n")
output.close()