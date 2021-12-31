"""
Fake Info Generator

Programmed by: Paramon yevstigneyev
Programmed in: Python 3.8.10 (64-Bit)

Description:
Do you ever encounter a scam, or don't want to give away personal infomation
to anyone suspicous? Well then this is the right python program for you! As this
python program generates fake information such as a phone number, credit/debit card,
social security number, and other personal information that scammers or companies
would ask you for.
"""

# Used for writing the generated info into a .txt file
import write

# Used for generating information
import gen as generate

# Stores the generated name and gender as a string
name, gender = generate.name()

# Store the generated phone number as a string
phone_num = generate.phone_number()

# Stores the generated Date of Birth as a string
date_ob = generate.date_of_birth()

# Stores the generated card information as a string
card_num, card_brand, card_type, cvv_num, exp_date, bank = generate.card()

# Stores the generated Social Security number as a string
ss_num = generate.social_security()

# Stores all the generated info as one string
info = f"""
Generated Information:

--- Personal Information ---
Name: {name}
Gender: {gender}
Date of Birth: {date_ob}
Phone Number: {phone_num}
Social Security Number: {ss_num}

--- Card ---
Card Number: {card_num}
Card Brand: {card_brand}
Card Type: {card_type}
Experation: {exp_date}
CVV Number: {cvv_num}
Bank: {bank}
"""

# Displays the generated info
print(info)

# Infinite while-loop that prompts the user if they want it saved as a .txt file
while True:

    # Prompts the user to enter Y (Yes) or N (No), if they do or don't want it saved as a .txt file
    choice = input("\nWould you like to have this in a .txt file (Y/N)?")

    # If the user enters "Y" or "y", then it will write the generated info into a .txt file
    if choice.upper() == "Y":

        # Writes the generated info
        write.gen_info(info)

        print("File sucessfully saved")

        # Breaks the infinite while-loop, and ends the program
        break
    
    # If the user enters "N" or "n", then it will not save the generated info into a .txt file
    elif choice.upper() == "N":
        
        # Breaks the infinite while-loop, and ends the program
        break
    
    # If the user enters any invalid input, then it will tell the user they enterted something invalid.
    else:
        print("\nInvalid Input!")
        
        # Continues the loop until the user enters valid input
        continue