# Indian Budget Chatbot

Simple chatbot to answer questions related to annual budget speeches delivered by Indian Finance Ministers over the years.

This chat bot is based on a Jupyter notebook put together for me by @radoshi 

For this chatbot:

1. I downloaded all the pdf files of the speeches from https://www.indiabudget.gov.in/bspeech.php
, and stored them in the "data" directory.

2. From these documents, I built a VectorStoreIndex using LlamaIndex and persisted it in the "storage" directory. The program create_index.py can be used for regenerating the VectorStoreIndex.

3. The actual chatbot, run_query.py, loads the VectorStoreIndex and uses it as a context to send the query to OpenAI and prints the response. The responses are logged into the chat-log.txt file.

## Installation

Requires `poetry`. If you don't have it, install it using `brew` or `pip`.

```bash
brew install poetry
```

```bash
poetry install
```

## Usage

First, copy the openai api key in a file named **openai-api-key**, then run:

```bash
poetry run python3 run_query.py
```

## To rebuild index

First, copy the openai api key in a file named **openai-api-key**, then run:

```bash
rm -rf storage
poetry run python3 create_index.py
```

# To re-download budget speeches

https://www.indiabudget.gov.in/bspeech.php

```bash
rm -rf data
mkdir data
cd data
wget -r -nd -nc -A.pdf -l 1 -e robots=off https://www.indiabudget.gov.in/bspeech.php
```


