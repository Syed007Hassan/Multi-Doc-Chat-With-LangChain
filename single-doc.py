import requests
import os
from dotenv import load_dotenv
from langchain_community.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain_community.document_loaders import PyPDFLoader
from constant import jobDescription

load_dotenv('.env')

# URL of the PDF
url = "https://syncflow-bucket.s3.amazonaws.com/resume/Ehtesham-Zafar-CV.pdf"

# Send GET request
response = requests.get(url)

# Ensure the request was successful
response.raise_for_status()

# Write the content of the request to a file
with open("temp.pdf", "wb") as f:
    f.write(response.content)

pdf_loader = PyPDFLoader('temp.pdf')
documents = pdf_loader.load()

chain = load_qa_chain(llm=OpenAI())
query = 'How much does the resume of the candidate match the job description?'
response = chain.run(input_documents=documents,
                     question=jobDescription + query)
print(response)

# Remember to remove the file after you're done to clean up
os.remove("temp.pdf")
