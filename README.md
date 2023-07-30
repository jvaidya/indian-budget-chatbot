# Indian Budget Chatbot

Simple chatbot to answer questions related to annual budget speeches delivered by Indian Finance Ministers over the years.

This OpenAI-powered chatbot is based on a Jupyter notebook put together for me by [@radoshi](https://github.com/radoshi) 

For this chatbot:

1. I downloaded all the pdf files of the speeches from https://www.indiabudget.gov.in/bspeech.php, and stored them in the "data" directory.

2. From these documents, I built a VectorStoreIndex using LlamaIndex and persisted it in the "storage" directory. The program *create_index.py* can be used for regenerating the VectorStoreIndex.

3. The actual chatbot, *run_query.py*, loads the VectorStoreIndex and uses it as a context to send the query to OpenAI and prints the response. The responses are logged into the chat-log.txt file.

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

## To re-download budget speeches

https://www.indiabudget.gov.in/bspeech.php

```bash
rm -rf data
mkdir data
cd data
wget -r -nd -nc -A.pdf -l 1 -e robots=off https://www.indiabudget.gov.in/bspeech.php
```
## Sample queries and responses (also see chat-log.txt)

Q: What is the earliest budget you know about?

A: The earliest budget mentioned in the context information is the Budget for the Year 1950-51 presented by Shri John Mathai, Minister of Finance.

Q: What were the highlights of the 1971 budget?

A: The 1971 budget highlighted a significant increase in outlays on development and social welfare, a promising picture of the economy, a satisfactory rate of food grains production, import substitution efforts, recovery from recession in the middle 1960s, a spurt in exports, cost reduction and improvement in efficiency, and the search for high-yielding varieties of paddy.

Q: What are the prominent trends over the last ten years?

A: The prominent trends over the last ten years include an increase in food grain production from 213 million tonnes to 263 million tonnes, an increase in installed power capacity from 112,700 MW to 234,600 MW, an increase in coal production from 361 million tonnes to 554 million tonnes, an increase in rural roads under PMGSY from 51,511 km to 389,578 km, an increase in Central Government expenditure on education from `10,145 crore to `79,451 crore, and an increase in Central Government expenditure on health from `7,248 crore to `36,322 crore. Additionally, the trend growth rate of the Indian economy has been 6.2 percent over the last 33 years, with average annual GDP growth of 5.9 percent during the period 1999-2004, 8.4 percent during the period 2004-2009, and 6.6 percent during the period 2009-2014.

Q: What were the highlights of the 2020 budget?

A: The highlights of the 2020 budget included the Pradhan Mantri Garib Kalyan Yojana, valued at `2.76 lakh crores, which provided free food grain to 800 million people, free cooking gas for 80 million families for months, and cash directly to over 400 million farmers, women, elderly, the poor and the needy.

Q: Can you compare the latest budget with the previous budget specifically on anti-poverty programs?

A: Yes, it is possible to compare the latest budget with the previous budget specifically on anti-poverty programs. The latest budget has increased outlays for major anti-poverty programmes by nearly 65 per cent, while the previous budget provided an increase in the Plan by 20.5 per cent. Additionally, the latest budget has introduced new schemes for the benefit of rickshaw pullers, cobblers, sweepers, porters and other urban disadvantaged groups, while the previous budget provided tax relief to the fixed income groups and incentives for import substitution and export promotion.

Q: Summerize the 2022 budget speech.

A: In the 2022 budget speech, Nirmala Sitharaman, the Minister of Finance, expressed her empathy for those affected by the pandemic and highlighted the strong resilience of India's economy. She also discussed the vision for India@100 and the goals to be achieved during the Amrit Kaal, a 25-year-long leadup to India@100. Additionally, she acknowledged the unprecedented circumstances of the 2021 budget and the Pradhan Mantri Garib Kalyan Yojana, which provided free food grain, cooking gas, and cash to millions of people.

Q: How have the agricultural subsidies changed over the last ten years?

A: Over the last ten years, the agricultural subsidies have decreased significantly. The Central Government has reduced and eliminated subsidies for foodgrains, and the State Governments have been asked to subsidize foodgrains on their own resources. Additionally, the price of fertilizers has not been increased since 1981, and the export subsidies have been reduced from Rs.4200 crores to Rs.1224 crores.

