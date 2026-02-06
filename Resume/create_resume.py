from bs4 import BeautifulSoup
from data_conversion import to_json, to_txt

#===========================================================================================================================================================
#=========================================================Read html and convert to soup=====================================================================
#===========================================================================================================================================================
with open(r"..\index.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

#===========================================================================================================================================================
#==============================================================Send HTML to a json==========================================================================
#===========================================================================================================================================================
converted_html = to_json(soup)

#===========================================================================================================================================================
#=====================================================Ask user to select the sections they want=============================================================
#===========================================================================================================================================================

# Step 1: Show the sections
print("Select what sections you want to include:")
keys = list(converted_html.keys())
for i, key in enumerate(keys, start=1):
    print(f"{i}) {key}")

# Step 2: Ask user to input their choices (comma-separated) with error handling
while True:
    try:
        selected_indices = input("Enter the numbers of the sections you want (e.g., 1,3): ").strip()
        if not selected_indices:
            raise ValueError("No input provided.")
        
        # Convert input to integers
        selected_indices = [int(x.strip()) for x in selected_indices.split(",")]

        # Check if numbers are valid indices
        if any(i < 1 or i > len(keys) for i in selected_indices):
            raise ValueError("One or more numbers are out of range.")

        break  # Input is valid, exit loop

    except ValueError as e:
        print(f"Invalid input: {e}. Please try again.")

# Step 3: Get the corresponding keys
selected_sections = [keys[i-1] for i in selected_indices]

print("\nYou selected the following section(s):")
for section in selected_sections:
    print(section)

# Step 4: Build a new JSON with only selected sections
filtered_converted_html = {section: converted_html[section] for section in selected_sections}

#===========================================================================================================================================================
#====================================================Ask the user to select the format they want============================================================
#===========================================================================================================================================================
print("\nSelect what format you want:")
print("1) Text")
user_input = str(input("Format: "))
correct_input = '0'
while correct_input == '0':
    if user_input == '1':
        to_txt(filtered_converted_html)
        correct_input = '1'
    else:
        print("Please select from the formats displayed above")
        correct_input = '0'
