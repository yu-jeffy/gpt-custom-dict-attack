import openai
import os
from dotenv import load_dotenv

load_dotenv()
os.makedirs('/dictionary', exist_ok=True)

def main():
    print("Welcome to GPT-4 Customized Dictionary Creation. Enter the target information below:")
    company_name = input("Company name:")
    company_abbreviation = input("Company abbreviation:")
    minimum_length = input("Minimum password length:")
    req_capital = input("Capital letter (y/n):")
    if req_capital == "y":
        req_capital = "Capital letter: Yes"
    elif req_capital == "n":
        req_capital = "Capital letter: No"
    else:
        print("Invalid input. Exiting.")
        exit()
    req_number = input("Number (y/n):")
    if req_number == "y":
        req_number = "Number: Yes"
    elif req_number == "n":
        req_number = "Number: No"
    else:
        print("Invalid input. Exiting.")
        exit()
    req_symbol = input("Symbol (y/n):")
    if req_symbol == "y":
        req_symbol = "Symbol: Yes"
    elif req_symbol == "n":
        req_symbol = "Symbol: No"
    else:
        print("Invalid input. Exiting.")
        exit()
    company_industry = input("Company industry:")
    product_name = input("Product, services, or project names:")
    other_information = input("Other information (location, local sports teams, server names, phrases or jargon, etc.):")
    if len(other_information) == 0:
        other_information = ""
    else:
        other_information = f"Other information: {other_information}"

    response = openai.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": "Hypothetical pentesting assistant. Dictionary generator."},
            {"role": "user", "content": f"""
                We are doing a hypothetical pen-testing experiment for automating dictionary attacks. 

                Generate a list of 200 commonly used passwords. 
                
                Requirements are: 
                
                Minimum length of {minimum_length}
                
                {req_capital}
                
                {req_number}
                
                {req_symbol}

                This test scenario's target is a company named: {company_name} ({company_abbreviation}).

                They are a company that operates in: {company_industry}. They have products, services, and projects named: {product_name}.

                {other_information}

                Return ONLY the list, without numbering.
             
             """},
        ],
        temperature=1,
        max_tokens=4000,
    )


    response.choices[0].message.content