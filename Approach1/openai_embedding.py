import os
from openai import OpenAI
import pandas as pd
client = OpenAI(api_key="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")

csv_schema = {
    'name':str,
    'embeddings':list[float]
}

def get_embeddings(text, model="text-embedding-ada-002"):
   return client.embeddings.create(input = [text], model=model,encoding_format="float").data[0].embedding

def save_embeddings(embeddings,file_path):
    # df['ada_embedding'] = df.combined.apply(lambda x: get_embedding(x, model='text-embedding-3-small'))
    df = pd.DataFrame(columns = csv_schema.keys())
    df = df._append({'name':file_path,'embeddings':embeddings},ignore_index = True)
    # df.to_csv('./embeddings.csv', index=False)
    embeddings_file_path = './embeddings.csv'
    if os.path.exists(embeddings_file_path):
        # If the file exists, open it in append mode
        df.to_csv(embeddings_file_path, mode='a', header=False, index=False)  # Append new data without writing headers
    else:
        # If the file does not exist, write the DataFrame with headers
        df.to_csv(embeddings_file_path, index=False)
