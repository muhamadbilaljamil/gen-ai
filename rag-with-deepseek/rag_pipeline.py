from langchain_groq import ChatGroq
from dotenv import load_dotenv
from vector_database import faiss_db
from langchain_core.prompts import ChatPromptTemplate


# Step 1: Setup LLM (Use DeepSeek R1 with Groq)
load_dotenv()
llm_model = ChatGroq(model="deepseek-r1-distill-llama-70b")

# Step 2: Retrieve Docs

def retrieve_docs(query):
    docs = faiss_db.similarity_search(query)
    return docs

def get_context(documents):
    context = "\n\n".join([doc.page_content for doc in documents])
    return context


# Step 3: Answer Question

custom_prompt_template = """
Use the pieces of information provided in the context to answer user's question.
If you don't know the answer, just say that you don't know. Don't try to make up an answer.
Don't provide any information that is not provided in the context.
Context: {context}
Question: {question}
"""

def answer_query(documents,model, query):
    context = get_context(documents)
    prompt = ChatPromptTemplate.from_template(custom_prompt_template)
    chain = prompt | model
    response = chain.invoke({"context": context, "question": query})
    return response.content


# question = "If a government forbids the right to assemble peacefully which articles are violated and why"
# 
# retrieved_docs = retrieve_docs(question)
# print("AI Lawyer: ", answer_query(documents=retrieved_docs, model=llm_model, query=question))

