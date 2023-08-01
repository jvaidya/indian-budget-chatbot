# Indian Budget Chatbot

Simple chatbots to answer questions related to annual budget speeches delivered by Indian Finance Ministers over the years.

These programs are based on a Jupyter notebook put together for me by [@radoshi](https://github.com/radoshi) 

Here is what I did:

1. I downloaded all the pdf files of the speeches from https://www.indiabudget.gov.in/bspeech.php, and stored them in the "data" directory.

2. From these documents, I built a VectorStoreIndex using LlamaIndex and persisted it in the "storage" directory. The program *create_index.py* can be used for regenerating the VectorStoreIndex.

3. The actual chatbots, *run_query.py* and *run_chat.py* load the VectorStoreIndex and use it as a context to send the query to OpenAI using **query_engine.query** and **chat_engine.chat** API calls respectively and print the response. The chat_engine.chat call maintains and uses the context from previous questions in the chat. The responses are logged into the query-log.txt and chat-log.txt files.

## Installation

Requires `poetry`. If you don't have it, install it using `brew` or `pip`.

```bash
brew install poetry
```

```bash
poetry install
```

## Usage

First, copy the openai api key in a file named **openai-api-key**, then:

To run the chat program, which keeps context across the questions:

```bash
poetry run python3 run_chat.py
```

To run the query program:

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

The speeches live at: https://www.indiabudget.gov.in/bspeech.php

```bash
rm -rf data
mkdir data
cd data
wget -r -nd -nc -A.pdf -l 1 -e robots=off https://www.indiabudget.gov.in/bspeech.php
```

## Sample queries and responses from run_query.py (also see query-log.txt)

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

## Sample of a chat session from run_chat.py (also see chat-log.txt)

Q: which years does your knowledge of budgets span?
A: My knowledge of Indian budget speeches spans from 1956-57 to 2014-15.

Q: what were the major changes from 56 to 66
A: The major changes from 1956-57 to 1966-67 include an increase in government expenditure, a decrease in non-food imports, an increase in food imports, a decrease in foreign exchange reserves, and an increase in foreign aid. Additionally, the budget deficit increased significantly during this period.

Q: could you give me numbers?
A: Sure. Government expenditure increased from Rs. 2,845 crore in 1956-57 to Rs. 5,845 crore in 1966-67. Non-food imports decreased from Rs. 1,845 crore to Rs. 1,345 crore during this period. Food imports increased from Rs. 1,095 crore to Rs. 1,495 crore. Foreign exchange reserves decreased from Rs. 1,095 crore to Rs. 845 crore. Foreign aid increased from Rs. 545 crore to Rs. 1,095 crore. The budget deficit increased from Rs. 345 crore to Rs. 1,845 crore.

Q: do you have budget speechees from 2014 to 2022?
A: Yes, I have budget speeches from 2014-15 to 2021-22.

Q: which years does your knowledge of budgets span?
A: My knowledge of Indian budget speeches spans from 1956-57 to 2021-22.

Q: what were the major changes from 2014 to 2022
A: The major changes from 2014-15 to 2021-22 include an increase in government expenditure, an increase in foreign aid, an increase in foreign direct investment, an increase in digital infrastructure, an increase in the number of patents issued, an increase in the GDP growth rate, and an increase in the number of social and economic indicators. Additionally, the government has implemented a number of game-changing reforms, such as the Goods and Services Tax (GST) and the JAM Trinity (Jan Dhan, Aadhar and Mobile).

Q: could you give me numbers?
A: Sure. Government expenditure increased from Rs. 17,94,892 crore in 2014-15 to Rs. 30,42,230 crore in 2021-22. Foreign aid increased from Rs. 67,876 crore to Rs. 1,19,955 crore during this period. Foreign direct investment increased from Rs. 1,45,814 crore to Rs. 3,05,814 crore. Digital infrastructure increased from Rs. 1,13,000 crore to Rs. 3,00,000 crore. The number of patents issued increased from 8,945 to 11,945. The GDP growth rate increased from 6.9% to 7.4%. The number of social and economic indicators increased from 8 to 12.

