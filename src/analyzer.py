import re

def basic_analysis(code):
    suggestions = []

    if "eval(" in code:
        suggestions.append("Avoid using eval() for security reasons.")

    if "password" in code.lower():
        suggestions.append("Do not hardcode passwords in code.")

    if len(code.split("\n")) > 50:
        suggestions.append("File is large. Consider splitting into smaller functions.")

    return suggestions
