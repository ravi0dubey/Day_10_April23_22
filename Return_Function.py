def format_name(f_name, l_name):
  if (f_name == "" and l_name==""):
    return("Either of the names are empty")
  
  return (f"Result: {f_name.title()} " + "" + f"{l_name.title()}")


f_name = input("Enter your first_name: ")
l_name = input("Enter your Last_name: ")

print(format_name(f_name,l_name))




  