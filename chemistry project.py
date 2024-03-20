from element_info import elements
 
def get_element_by_name(name):
    name = name.lower()
    for atomic_number, data in elements.items():
        if data["name"].lower() == name:
            return atomic_number, data

    return None

def get_element_by_number(number):
    number = int(number)
    for atomic_number,data in elements.items():
        if number == atomic_number:
            return atomic_number, data
        
    return None

def molar_mass(chem_name):
   symbol = symbol.upper
   for atomic_number,data in elements.items():
      if data["symbol"] == symbol:
         return atomic_number, data
      

def calculate_molar_mass(formula):
    molar_mass = 0
    chem_name = chem_name
    for atomic_weight, data in elements.items():
     if data["symbol"] == chem_name:
      return atomic_weight,data
   

ans = input("what would you like to do?")
if ans == "find element":
 chemical_name = input("name of element")
 atomic_number, element_data = get_element_by_name(chemical_name)
 if element_data:
    # Print all data associated with the element
    print(f"Atomic Number: {atomic_number}")
    print(f"Symbol: {element_data['symbol']}")
    print(f"Name: {element_data['name']}")
    print(f"Atomic Weight: {element_data['atomic_weight']}")
 else:
    print("Element not found.")

elif ans == "find element by number":
 chemical_number = input("Enter the atomic number of element: ")
 atomic_number, element_data = get_element_by_number(chemical_number)
 if element_data:
    # Print all data associated with the element
    print(f"Atomic Number: {atomic_number}")
    print(f"Symbol: {element_data['symbol']}")
    print(f"Name: {element_data['name']}")
    print(f"Atomic Weight: {element_data['atomic_weight']}")
 else:
    print("Element not found.")

if ans == "molar mass":
   chem_name = input("enter chamical formula:")
   chem_form = list(chem_name)
   ans = calculate_molar_mass(chem_name)
   for i in chem_form:
     if i == 
   if chem_name.isalpa:
    print()







