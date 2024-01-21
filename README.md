# Multi Document Reader and Chatbot using LangChain and OpenAI

## Summary
Provided here are a few python scripts to help get started with building your own multi document reader and chatbot.
The scripts increase in complexity and features, as follows:

`single-doc.py` Can handle interacting with a single pdf. Sends the entire document content to the LLM prompt.

`single-long-doc.py` Can handle interacting with a long single pdf. Uses embeddings and a vector store to handle
sending only relevant information to the LLM prompts.

`multi-doc-chatbot.py` Can handle interacting with multiple different documents and document types (.pdf, .dox, .txt), 
and remembers the chat history and recent conversations.
It uses embeddings and vector stores to send the relevant information to the LLM prompt. Also provides a chat interface
via the terminal using stdin and stdout. Press `q` to escape the chat window.


## Getting started


Clone the repository, set up the virtual environment, and install the required packages. Use Python 3.11.5 to avoid any breaking changes for LangChain

```
git clone https://github.com/Syed007Hassan/Multi-Doc-Chat-With-LangChain.git
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

## Store your OpenAI API key
Copy the example env file

`cp .env.example .env`

Now copy your OpenAI API key into the `.env` file, and save the file. It should send up looking something like

`OPENAI_API_KEY=sk-`

## Start chatting
Kick off the **multi-doc-chatbot.py**, and start interacting with your files. Place any files you would like to
interact with inside the `/docs` folder. Enter `q` to exit the prompt at any time.

```python
python3 multi-doc-chatbot.py
```

![image](https://github.com/Syed007Hassan/Multi-Doc-Chat-With-LangChain/assets/104893311/be60c727-ff22-48ae-b996-c500a2c79aa9)

![image](https://github.com/Syed007Hassan/Multi-Doc-Chat-With-LangChain/assets/104893311/7d2f4d91-4963-4683-b766-a30e8e2a100d)

![image](https://github.com/Syed007Hassan/Multi-Doc-Chat-With-LangChain/assets/104893311/e854eaab-32b2-4ed4-9369-084be67e2d59)

![image](https://github.com/Syed007Hassan/Multi-Doc-Chat-With-LangChain/assets/104893311/64c8a342-8fcb-4b20-abe6-3dc13e533ec5)

![image](https://github.com/Syed007Hassan/Multi-Doc-Chat-With-LangChain/assets/104893311/53f4254d-1d9a-401f-b4d6-729bce013bcd)


It's not perfect, and it does give strange answers sometimes, but it does get a basic setup running. It does show 
that getting a basic Q&A chain working is not enough to create a really good chatbot. To get that working, you will
need to dig deeper and explore the concepts and ideas in more detail. Possibilities could include optimising the prompt
templates, using different LLMs which can accept more tokens and context lengths, creating an agent to refine the results,
and whatever else you can think of 🙂

