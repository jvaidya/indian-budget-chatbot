import os
import openai

if os.path.exists("openai-api-key"):
    openai.api_key = open("openai-api-key").read().strip()
else:
    print("\nERROR: Store openai key in a file named openai-api-key and rerun.\n")
    exit(1)

if not os.path.exists("data"):
    print('''
ERROR: Did not find "data" directory.

Run the following commands to populate the data directory with budget data:
    mkdir data
    cd data
    wget -r -nd -nc -A.pdf -l 1 -e robots=off https://www.indiabudget.gov.in/bspeech.php

''')
    exit(1)

if not os.path.exists("./storage"):
    os.mkdir("./storage")
else:
    print('''
ERROR: The ./storge directory already exists.
If you want to regenerate the index, remove or rename this directory and rerun.
''')
    exit(1)

from llama_index import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader('data').load_data()

index = VectorStoreIndex.from_documents(documents)
    
index.storage_context.persist("./storage")

print("Index created in ./storage\n")



