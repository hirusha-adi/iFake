
# Fake Data Generator Readme

This is a Python program that generates fake data for various purposes, such as testing, data entry, and more. The program is designed to be run offline and provides various options for generating different types of fake data.

![image](https://user-images.githubusercontent.com/36286877/121724622-c24c7e00-cb05-11eb-9012-9fa8d61d333a.png)

## Prerequisites

Before using this program, you should have Python installed on your computer. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/)

You will also need to install the following Python packages:

- `Faker`: A library for generating fake data, including names, addresses, and more.
- `termcolor`: A package for adding colored output to the terminal.

You can install these packages using `pip`:

```bash
pip install Faker termcolor
```

## Usage

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt.

3. Navigate to the directory where the script is located.

4. Run the script by executing the following command:

   ```bash
   python fake_data_generator.py
   ```

   This will start the program and display a menu of options.

5. Follow the on-screen menu to select the type of fake data you want to generate. You can choose from options like generating high-information profiles, mid-information profiles, low-information profiles, credit card data, and more.

6. Depending on your choice, the program will generate fake data and save it to text files with appropriate names.

7. You can access the generated data in the same directory where the script is located.

## Available Commands

- `start high`: Generates high-information profiles with options to select the nationality.
- `start mid`: Generates mid-information profiles.
- `start low`: Generates low-information profiles.
- `cc all`: Generates random fake credit card data with all information.
- `cc pr`: Generates a list of credit card providers.
- `cc no`: Generates a list of credit card numbers.
- `cc cvv`: Generates random credit card CVVs (Card Verification Values).
- `cc exp`: Generates random expiry dates for credit cards.
- `cc gene`: Opens an external credit card data generator website.
- `cc check`: Checks the validity of a credit card number using the Luhn algorithm (offline).
- `cc checke`: Opens an external credit card checking website.
- `help`: Displays a help menu with explanations of the available commands.
- `menu`: Returns to the main menu from other pages.

## Credits

This program was created by ZeaCeR#5641. It is intended for educational purposes only. Please use it responsibly and do not use the generated data for illegal activities.

If you encounter any issues or have suggestions for improvements, you can contact the creator on Discord (ID: ZeaCeR#5641).

## Disclaimer

The generated data is entirely fictional and should not be used for any malicious or illegal activities. This program is meant for educational and testing purposes only. Be sure to use the generated data in a legal and ethical manner.

![iFake_icon](https://user-images.githubusercontent.com/36286877/127768584-d94d0a78-15e7-4861-ac60-bd94b9da7608.png)
