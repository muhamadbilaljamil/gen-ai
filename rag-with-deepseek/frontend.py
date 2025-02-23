from rag_pipeline import answer_query, retrieve_docs, llm_model

# Step1 : Setup upload PDF functionality
import streamlit as st

upload_file = st.file_uploader("Upload PDF", type="pdf", accept_multiple_files=False )

# Step2 : Chatbot skeleton (Question & Answer)

user_query = st.text_area("Enter you question here", height=100, placeholder="Ask me anything")

ask_question = st.button("Ask AI Lawyer")

if ask_question:
    
    if upload_file:
        
        st.chat_message("user").write(user_query)
    
        # RAG Pipeline
    
        # fixed_response = "Hi, this is a fixed response!"

        retrieved_docs = retrieve_docs(user_query)
        response = answer_query(documents=retrieved_docs, model=llm_model, query=user_query)
    
        st.chat_message("AI Lawyer: I'm here to help. What's your question?").write(response)
        
    else:
        
        st.error("Please upload a valid PDF file first.")
    
