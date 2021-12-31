"""
Write

Programmed by: Paramon Yevstigneyev
Programmed in: Python 3.8.10 (64-Bit)

Description:
Writes the generated information into a .txt file,
if the user wishes it to be saved.
"""

def gen_info(info):
    """
    Writes the generated info into a .txt file
    """
    
    # Opens a file stream
    file = open("Generated Info.txt", "w")
    
    # Writes the info into the file
    file.write(info)

    # Closes the file stream
    file.close()
