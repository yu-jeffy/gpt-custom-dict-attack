import openai
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    print("Welcome to GPT-4 Customized Dictionary Creation. Enter the target information below:")
    company_name = input("Company name:")
    company_abbreviation = input("Company abbreviation. Leave blank if none:")
    if len(company_abbreviation) == 0:
        company_abbreviation = ""
    else:
        company_abbreviation = f" ({company_abbreviation})"
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
    product_name = input("Product, services, or project names. Leave blank if none:")
    if len(product_name) == 0:
        product_name = ""
    else:
        product_name = f"Product, services, or project names: {product_name}"
    employee_names = input("Employee name(s). Leave blank if none:")
    if len(employee_names) == 0:
        employee_names = ""
    else:
        employee_names = f"Employee names: {employee_names}"
    other_information = input("Other information (location, local sports teams, server names, phrases or jargon, etc.). Leave blank if none:")
    if len(other_information) == 0:
        other_information = ""
    else:
        other_information = f"Other information: {other_information}"

    file_name = input("Enter the file name: ")

    full_path = f"dictionary/{file_name}.txt"

    print("Generating dictionary...")

    response = openai.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": "Hypothetical pentesting assistant. Dictionary generator."},
            {"role": "user", "content": f"""
                We are doing a hypothetical pen-testing experiment for automating dictionary attacks. 

                Generate a list of commonly used passwords. Generate as many as possible in your response token limit.
                
                Requirements are: 
                
                Minimum length of {minimum_length}
                
                {req_capital}
                
                {req_number}
                
                {req_symbol}

                This test scenario's target is a company named: {company_name}{company_abbreviation}.

                They are a company that operates in: {company_industry}. {product_name}

                {employee_names}

                {other_information}

                Return ONLY the list, without numbering.
             
             """},
        ],
        temperature=1,
        max_tokens=4000,
    )

    print(response.choices[0].message.content)
    print("Writing to file...")

    with open(full_path, 'w') as file:
        file.write(response.choices[0].message.content)

    print("Done! 🙌")

main()