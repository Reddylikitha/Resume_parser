import json
import pandas as pd
from Approach2.cosine_similarity import cosine_similarity
from openai import OpenAI


client = OpenAI(api_key="YOUR OPENAI KEY")

# from sklearn.metrics.pairwise import cosine_similarity
def get_embeddings(text, model="text-embedding-ada-002"):
   return client.embeddings.create(input = [text], model=model,encoding_format="float").data[0].embedding

query = input("Enter the job description: ")
query_embeddings = get_embeddings(query)

df = pd.read_csv('./embeddings.csv')
results = {}

results_keys = list(df['name'])

embeddings = df['embeddings'].apply(lambda x : json.loads(x))

ind = 0
for embedding in embeddings:
    similarity = cosine_similarity(list(embedding),query_embeddings)
    results[results_keys[ind]]= similarity
    ind+=1

print("****************** Results ******************")
print(dict(sorted(results.items(),key=lambda x :x[1], reverse=True )))


