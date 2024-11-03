!pip install -q cassio datasets langchain openai tiktoken
!pip install openai==0.28
!pip install -U langchain-community
!pip install PyPDF2

# LangChain components to use
from langchain.vectorstores.cassandra import Cassandra
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings

# Support for dataset retrieval with Hugging Face
from datasets import load_dataset

# With CassIO, the engine powering the Astra DB integration in LangChain,
# you will also initialize the DB connection:
import cassio
from PyPDF2 import PdfReader


ASTRA_DB_APPLICATION_TOKEN = "AstraCS:tRaQATgwZpLriOJMWlakfYbX:de56e2dc16bf17a8eb9101fe3f088568438c617bd2ad17ee9b2a13796b03dcf2"

#enter your Database ID : 9198a15d-1168-48a6-b4d3-4ddcb209573b
ASTRA_DB_ID = "9198a15d-1168-48a6-b4d3-4ddcb209573b"
# enter your OpenAI key
OPENAI_API_KEY = "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" 

# provide the path of  pdf file/files.
pdfreader = PdfReader('https://drive.google.com/file/d/1tiUQ4fSmQrYQxDjFn8N2hufWB0dBSAaM/view?usp=drive_link')

from typing_extensions import Concatenate
# read text from pdf
raw_text = ''
for i, page in enumerate(pdfreader.pages):
    content = page.extract_text()
    if content:
        raw_text += content

raw_text

cassio.init(token=ASTRA_DB_APPLICATION_TOKEN, database_id=ASTRA_DB_ID)

#Create your LangChain Vector Store
astra_vector_store = Cassandra(
    embedding=embedding,
    table_name="qa_mini_demo",
    session=None,
    keyspace=None,
)

from langchain.text_splitter import CharacterTextSplitter
# We need to split the text using Character Text Split such that it sshould not increse token size
text_splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 800,
    chunk_overlap  = 200,
    length_function = len,
)
texts = text_splitter.split_text(raw_text)

texts[:50]

astra_vector_store.add_texts(texts[:50])
print("Inserted %i headlines." % len(texts[:50]))
astra_vector_index = VectorStoreIndexWrapper(vectorstore=astra_vector_store)

first_question = True
while True:
    if first_question:
        query_text = input("\nEnter your question (or type 'quit' to exit): ").strip()
    else:
        query_text = input("\nWhat's your next question (or type 'quit' to exit): ").strip()

    if query_text.lower() == "quit":
        break

    if query_text == "":
        continue

    first_question = False

    print("\nQUESTION: \"%s\"" % query_text)
    answer = astra_vector_index.query(query_text, llm=llm).strip()
    print("ANSWER: \"%s\"\n" % answer)


    print("FIRST DOCUMENTS BY RELEVANCE:")
    for doc, score in astra_vector_store.similarity_search_with_score(query_text, k=4):
        print("    [%0.4f] \"%s ...\"" % (score, doc.page_content[:84]))
