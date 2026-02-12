
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

try:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found.")
        exit(1)

    client = genai.Client(api_key=api_key)
    
    print("Listing models...")
    # The new SDK might allow iterating over models
    # Check if client.models.list() exists or similar
    try:
        # Pager object
        pager = client.models.list() 
        with open("models.txt", "w") as f:
            for model in pager:
                if "gemini" in model.name:
                    f.write(f"{model.name}\n")
        print("Models written to models.txt")



    except Exception as e:
         print(f"Error listing models: {e}")

except Exception as e:
    print(f"General Error: {e}")
