import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyBOgx6_jTZIZIsaE-Ol_awnKnyneHCtmSs")  # Replace with your actual API key

# Create a model object
model = genai.GenerativeModel("gemini-1.5-flash")  # Ensure the model name is correct

def generate_content(prompt):
    try:
        # Generate content with the model
        response = model.generate_content(prompt)
        print("Generated Response:", response.text)
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
generate_content("Explain how ML works")

