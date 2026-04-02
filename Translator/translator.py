from googletrans import Translator, LANGUAGES

translator = Translator()

print("Available languages and their codes:")
for code, name in LANGUAGES.items():
    print(f"{code} = {name}")

target_lang = input("\nType the code of the language you want to translate to: ").lower()

print("\nType anything in English to translate (type 'exit' to quit):")

while True:
    text = input("English: ")
    if text.lower() == "exit":
        break
    print("Translation:", translator.translate(text, dest=target_lang).text, "\n")