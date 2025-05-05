import google.generativeai as genai

# Configure API Key
genai.configure(api_key="")

# Load the Gemini Pro model
model = genai.GenerativeModel("gemini-2.0-flash")

def ask_gemini(
    question,
    instructions,
    content=None,
):
    prompet = f"""response instruction:{" ".join(instructions)} \n {content}"""
    response = model.generate_content(

    )
    print(" ".join(instructions))

    return response.text


