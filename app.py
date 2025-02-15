import streamlit as st
from transformers import pipeline

# Load summarization model
summarizer = pipeline("summarization")

# Streamlit UI
st.title("Paragraph Summarization App")
st.write("Enter a paragraph below to generate a summary.")

# Input text box
text = st.text_area("Enter text:", "")

if st.button("Summarize"):
    if text:
        summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
        st.subheader("Summary:")
        st.write(summary[0]['summary_text'])
    else:
        st.warning("Please enter a paragraph to summarize.")
