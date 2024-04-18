import os
name = input("enter name of component >>> ")

list_of_components = [name + ".js", name + ".css", "index.js"]

print(f"names is saved: {list_of_components}")

os.makedirs(os.path.dirname(f"./{name}/"), exist_ok=True)

for component in list_of_components:
    file_path = f"./{name}/{component}"
    
    with open(file_path, "w") as file:
        pass

    print(f"{file_path} file is created")