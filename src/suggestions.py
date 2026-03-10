def improve_code(code):
    tips = []

    if "for i in range(len(" in code:
        tips.append("Use direct iteration instead of range(len()).")

    if "==" in code and "None" in code:
        tips.append("Use 'is None' instead of '== None'.")

    if "print(" in code:
        tips.append("Avoid debug print statements in production code.")

    return tips
