"""
Generate

Programmed by: Paramon Yevstigneyev
Programmed in: Python 3.8.10 (64-Bit)

Description:
This is a custom-made python library that generates fake information such as:
- Name
- Phone Number
- Date of birth
- Social Security Number
- Credit or Debit Card
- Bank
- Experation date
"""

# Used for generating names
import names

# Used for generating a fake credit/debit card experation date
from time import strftime as time

# Used for generating a fake social security number, card number, and cvv number
from random import randint as rand

# Used for randomly picking a bank, gender, 
from random import choice as choose

def name():
    """
    Generates a name
    """

    # list of genders
    genders = ["male", "female"]

    # Randomly picks a gender
    gender = choose(genders)

    # Generates a first name
    first_name = names.get_first_name(gender)

    # Generates a last name
    last_name = names.get_last_name()

    # Stores the generated first and last name as one string
    name = f"{first_name}, {last_name}"

    # Returns the generated name and gender
    return name, gender

def phone_number():
    """
    Generates a random phone number
    """

    phone_num = f"+{rand(0,300)} ({rand(1,9)}{rand(0,9)}{rand(0,9)}) {rand(1,9)}{rand(0,9)}{rand(0,9)} {rand(1,9)}{rand(0,9)}{rand(0,9)}{rand(0,9)}"
    # Returns the randomly generated phone number
    return phone_num

def date_of_birth():
    """
    Generates a fake Date of Birth
    """

    # Generates random birth year
    year = rand(1950,2010)

    # Generates random birth month
    month = rand(1,12)

    # If the month generated is less than nine, then it will add a zero to it
    if month <= 9:
        month = "0" + str(month)

    # If the month generated is more than nine, then it will pass
    else:
        pass

    day = rand(1,31)

    # If the day genertaed is less than nine, then it will add a zero to it
    if day <= 9:
        day = "0" + str(day)

    # If the day generated is more than nine, then it will pass
    else:
        pass
    
    # Returns the generated date of birth
    return f"{month}/{day}/{year}"

def card():
    """
    Generates a fake credit or debit card
    """

    # Generates a random card number
    card_num = f"{rand(0,9)}{rand(0,9)}{rand(0,9)}{rand(0,9)} {rand(0,9)}{rand(0,9)}{rand(0,9)}{rand(0,9)} {rand(0,9)}{rand(0,9)}{rand(0,9)}{rand(0,9)} {rand(0,9)}{rand(0,9)}{rand(0,9)}{rand(0,9)}"
    
    # list of card types
    card_types = ["Debit", "Credit"]

    # list of Card Brands
    card_brand_type = ["Visa", "Mastercard", "Discover", "American Express"]

    # list of banks
    banks = ["Bank of America", "Chase", "US Bank","Wells Fargo", "Key Bank", "Citi Bank", "Capital One"]

    # Picks a random bank
    bank = choose(banks)

    # generates a random experation month
    experation_month = rand(1,12)

    # If the generated experation month is less than nine, then it will add a zero to it
    if experation_month <= 9:
        experation_month = "0" + str(experation_month)

    # If the generated experation month is more than nine, then it will pass
    else:
        pass

    # Generates a random experation year
    experation_year = int(time('%Y')) + rand(1,10)

    # Stores the experation date as a single string
    experation_date = f"{experation_month}/{experation_year}"


    # Randomly picks a card brand
    card_brand = choose(card_brand_type)

    # Randomly picks a card type
    card_type = choose(card_types)
    
    # If the card brand generated is either 'Visa' or 'Mastercard', then it will generate a 3 digit CVV number
    if card_brand == card_brand_type[0] or card_brand == card_brand_type[1]:
        cvv_num = f"{rand(0,9)}{rand(0,9)}{rand(0,9)}"

    # if the card brand generated is either 'Discover' or 'American Express', then it will generate a 4 digit CVV number
    elif card_brand == card_brand_type[2] or card_brand == card_brand_type[3]:
        cvv_num = f"{rand(0,9)}{rand(0,9)}{rand(0,9)}{rand(0,9)}"
    
    else:
        pass

    # Returns the generatd card number, brand, type, cvv number, experation date, and bank.
    return card_num, card_brand, card_type, cvv_num, experation_date, bank

def social_security():
    """
    Generates a fake Social Security Number
    """

    # Generates a nne digit social security number
    ss_num = f"{rand(0,9)}{rand(0,9)}{rand(0,9)} {rand(0,9)}{rand(0,9)}{rand(0,9)} {rand(0,9)}{rand(0,9)}{rand(0,9)}"
    
    # Returns the generated social security number
    return ss_num
