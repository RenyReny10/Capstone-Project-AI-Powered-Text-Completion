import openai
import os

# Asegúrate de tener tu API key como variable de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    print("Welcome to the AI Text Completion App!")
    while True:
        prompt = input("\nEnter a prompt (or type 'exit' to quit): ")
        if prompt.lower() == "exit":
            print("Goodbye!")
            break
        try:
            temp_input = input("Set temperature (0.0 - 1.0, default 0.7): ")
            temperature = float(temp_input) if temp_input else 0.7

            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=temperature,
                max_tokens=150
            )

            print("\nAI Response:\n")
            print(response.choices[0].message.content)

        except Exception as e:
            print("\nError:\n", e)

if __name__ == "__main__":
    main()
