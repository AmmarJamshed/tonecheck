#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import language_tool_python
import nltk
from textblob import TextBlob

# Load the NLP tool
nltk.download('punkt')

# Initialize LanguageTool for English
tool = language_tool_python.LanguageToolPublicAPI('en-US')

def analyze_text(text):
    # Checking grammatical errors
    matches = tool.check(text)
    corrections = [
        {'Error': match.ruleId, 'Suggestion': match.replacements} for match in matches
    ]
    
    # Sentiment Analysis
    sentiment = TextBlob(text).sentiment
    
    return corrections, sentiment

# Streamlit UI
st.title("NLP-Based Article Improvement Tool")
st.write("Upload an article to analyze tone and language improvements.")

# Text input
uploaded_text = st.text_area("Paste your article here:")

if st.button("Analyze Text"):
    if uploaded_text:
        corrections, sentiment = analyze_text(uploaded_text)
        
        # Display grammar suggestions
        st.subheader("Grammar & Style Suggestions:")
        if corrections:
            for correction in corrections:
                st.write(f"**Error:** {correction['Error']}")
                st.write(f"**Suggestion:** {', '.join(correction['Suggestion'])}")
                st.write("---")
        else:
            st.write("No grammatical issues found!")
        
        # Display sentiment analysis
        st.subheader("Sentiment Analysis:")
        st.write(f"Polarity: {sentiment.polarity} (Negative: -1, Neutral: 0, Positive: 1)")
        st.write(f"Subjectivity: {sentiment.subjectivity} (Objective: 0, Subjective: 1)")
    else:
        st.warning("Please enter text before analyzing.")

