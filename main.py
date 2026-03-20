from langchain_helper import get_few_shot_db_chain

import streamlit as st

st.title("T shirts: Database Q&A 👕")

question = st.text_input("Question: ")

if question:
    chain = get_few_shot_db_chain()
    ans = chain.run(question)
    final_answer = ans.split("Answer:")[-1].strip()

    st.header("Answer:")
    st.write(final_answer)
