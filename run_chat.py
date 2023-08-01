import os
import openai

# Query examples:
#   What is a high level trend in the latest budget?
#   Can you compare the latest budget with the previous budget specifically on anti-poverty programs?

if os.path.exists("openai-api-key"):
    openai.api_key = open("openai-api-key").read().strip()
else:
    print("\nERROR: Store openai key in a file named openai-api-key and rerun.\n")
    exit(1)

from llama_index import StorageContext, load_index_from_storage
from llama_index.memory import ChatMemoryBuffer

storage_context = StorageContext.from_defaults(persist_dir="./storage")

index = load_index_from_storage(storage_context)

# query_engine = index.as_query_engine()
memory = ChatMemoryBuffer.from_defaults(token_limit=256000)
chat_engine = index.as_chat_engine(chat_mode="context",
                                   memory=memory,
                                   system_prompt="You are a chatbot, able to have normal interactions, as well as talk about Indian Budget Speeches",
)

print("\nThis program can chat about the Indian Budget speeches delivered by the Finance Minister.\n")

output = ""

while True:
    try:
        query = input("Ask away (Ctrl-D to exit): ")
        response = chat_engine.chat(query)
        print(response)
        print("\n")
        output = output + "Q: " + query + "\nA: " + response.response.lstrip() + "\n\n"
    except EOFError:
        logfile = "chat-log.txt"
        if os.path.exists(logfile):
            f = open(logfile, 'a')
        else:
            f = open(logfile, 'w')
        f.write(output)
        f.close()
        print("\nLog in " + logfile + ". Goodbye!\n")
        break





