try:
    input_filename = input("Enter the name of the file to read: ")
    
    with open(input_filename, "r") as infile:
        content = infile.read()
    
    modified_content = content.upper()
    
    output_filename = input("Enter the name of the file to save the modified content: ")
    
    with open(output_filename, "w") as outfile:
        outfile.write(modified_content)
    
    
    print(f"Your modified content has been saved to '{output_filename}'!")
    

except FileNotFoundError:
    print("The file you are trying to read does not exist. Please check the name and try again.")

except IOError as e:
    print(f"There was a problem reading or writing the file. Error details: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
