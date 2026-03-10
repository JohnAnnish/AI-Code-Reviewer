import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.analyzer import basic_analysis
from src.complexity import check_complexity
from src.suggestions import improve_code

st.title("AI Code Reviewer")

code = st.text_area("Paste your code here")

if st.button("Analyze Code"):

    st.subheader("Suggestions")
    suggestions = basic_analysis(code)

    for s in suggestions:
        st.write("- ", s)

    st.subheader("Code Improvements")
    tips = improve_code(code)

    for t in tips:
        st.write("- ", t)

    st.subheader("Complexity Analysis")
    complexity = check_complexity(code)

    for c in complexity:
        st.write(f"Function: {c['name']} | Complexity: {c['complexity']}")

