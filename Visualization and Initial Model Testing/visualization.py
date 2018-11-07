import numpy as np
import pandas as pd
import spacy
from wordcloud import WordCloud

# True if class(ex. toxic) == 1
complete_df = pd.read_csv("../dataset/train.csv")
toxic = complete_df["toxic"] == 1
severe_toxic = complete_df["severe_toxic"] == 1
obscene = complete_df["obscene"] == 1
threat = complete_df["threat"] == 1
insult = complete_df["insult"] == 1
identity_hate = complete_df["identity_hate"] == 1

def generate_word_cloud(text, custom_word_cloud):
    word_cloud = custom_word_cloud.generate(text)
    return word_cloud

def generate_word_clouds_from_dataframe(complete_df):
    complete_body_string = "".join(complete_df["comment_text"])

    word_cloud = WordCloud(width=1000, height=900, max_words=500)
    complete_word_cloud = generate_word_cloud(complete_body_string, word_cloud)
    complete_word_cloud.to_file("../dataset/complete_word_cloud.png")

    class_word_cloud = WordCloud(width=1000, height=900, max_words=100)

    toxic_word_cloud = generate_word_cloud(toxic_string, class_word_cloud)
    toxic_word_cloud.to_file("../dataset/toxic_word_cloud.png")

    severe_toxic_word_cloud = generate_word_cloud(severe_toxic_string, class_word_cloud)
    severe_toxic_word_cloud.to_file("../dataset/severe_toxic_word_cloud.png")

    obscene_word_cloud = generate_word_cloud(obscene_string, class_word_cloud)
    obscene_word_cloud.to_file("../dataset/obscene_word_cloud.png")

    threat_word_cloud = generate_word_cloud(threat_string, class_word_cloud)
    threat_word_cloud.to_file("../dataset/threat_word_cloud.png")

    insult_word_cloud = generate_word_cloud(insult_string, class_word_cloud)
    insult_word_cloud.to_file("../dataset/insult_word_cloud.png")

    identity_hate_word_cloud = generate_word_cloud(identity_hate_string, class_word_cloud)
    identity_hate_word_cloud.to_file("../dataset/identity_hate_word_cloud.png")

complete_df_count = len(complete_df.index)
toxic_count = complete_df[toxic]["toxic"].astype(bool).sum(axis=0)
severe_toxic_count = complete_df[severe_toxic]["severe_toxic"].astype(bool).sum(axis=0)
obscene_count = complete_df[obscene]["obscene"].astype(bool).sum(axis=0)
threat_count = complete_df[threat]["threat"].astype(bool).sum(axis=0)
insult_count = complete_df[insult]["insult"].astype(bool).sum(axis=0)
identity_hate_count = complete_df[identity_hate]["identity_hate"].astype(bool).sum(axis=0)

string = """
            The complete count for total comments: {}
            The count for toxic comments: {}
            The count for severe_toxic comments: {}
            The count for obscene comments: {}
            The count for threat comments: {}
            The count for insult comments: {}
            The count for identity_hate comments: {}
            """.format(complete_df_count, toxic_count, severe_toxic_count,
            obscene_count, threat_count, insult_count, identity_hate_count)

print(string)
