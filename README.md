# GPT-4 Customized Dictionary Creation

This project is a Python script that uses OpenAI's GPT-4 model to generate a customized dictionary for dictionary attacks. The script prompts the user for various inputs about the target, such as the company name, industry, and specific password requirements. It then uses this information to generate a list of potential passwords.

## Requirements

- Python 3.6 or higher
- OpenAI Python client
- dotenv Python library

## Setup

1. Clone the repository to your local machine.
2. Install the required Python libraries using pip:

```bash
pip install openai python-dotenv
```

3. Create a `.env` file in the root directory of the project and add your OpenAI API key:

## Usage

Run the `generate.py` script:
```python
python generate.py
```

Follow the prompts to enter information about the target. The script will generate a list of potential passwords and save them to a file in the `dictionary` directory.

Happy hunting! 🤠

## Disclaimer
This tool is intended for educational and research purposes only. The authors are not responsible for any misuse or damage caused by this tool. Always obtain proper authorization before conducting penetration testing.