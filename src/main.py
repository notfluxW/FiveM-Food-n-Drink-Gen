import os
import tkinter as tk
from tkinter import filedialog
import shutil
import datetime

current_time = datetime.datetime.now()
timestamp_format = "%Y-%m-%d %H_%M_%S"
timestamp = current_time.strftime(timestamp_format)
output_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "output")
timestamped_folder = os.path.join(output_folder, timestamp)
lua_file_path = os.path.join(timestamped_folder, "generated.lua")
sql_file_path = os.path.join(timestamped_folder, "generated.sql")

def generate_lua_file(image_names):
    print("\n\n>>> Lua Generation <<<\n")
    isFood = input("Food or Liquid (F / L): ")
    if isFood != "F" and isFood != "L":
        isFood = input("Food or Liquid (F / L): ")
    isFood = (isFood == "F")
    percentage = float(input("Enter amount it should fill up (%): "))
    lua_array = "{"
    index = 0
    for item in image_names:
        index += 1
        if index < len(image_names):
            lua_array = lua_array + "'" + item + "'" + ', '
        else:
            lua_array = lua_array + "'" + item + "'" + '}'

    if isFood:
        lua_code = f"""for _,item in pairs({lua_array}) do
    ESX.RegisterUsableItem(item, function(source)
        local xPlayer = ESX.GetPlayerFromId(source)

        xPlayer.removeInventoryItem(item, 1)

        TriggerClientEvent('esx_status:add', source, 'hunger', {percentage}*10000)
        TriggerClientEvent('esx_basicneeds:onEat', source)
    end)
end"""
    else:
        lua_code = f"""for _,item in pairs({lua_array}) do
    ESX.RegisterUsableItem(item, function(source)
        local xPlayer = ESX.GetPlayerFromId(source)

        xPlayer.removeInventoryItem(item, 1)

        TriggerClientEvent('esx_status:add', source, 'thirst', {percentage}*10000)
        TriggerClientEvent('esx_basicneeds:onDrink', source)
    end)
end"""
    
    os.makedirs(timestamped_folder, exist_ok=True)
    print("Lua file generated successfully!")
    with open(lua_file_path, "w") as lua_file:
        lua_file.write(lua_code)
    Choice = input("Would you like to generate SQL too? (Y / N): ")
    while Choice != "Y" and Choice != "N":
        Choice = input("Can remove (Y / N): ")
    if Choice == "Y":
        generate_sql_file(image_names)


def generate_sql_file(python_array):
    print("\n\n>>> SQL Generation <<<\n")
    Label = str(input("Give your items a global label: "))
    Limit = int(input("Give your items a global limit: "))
    Can_Remove = input("Can remove (Y / N): ")
    while Can_Remove != "Y" and Can_Remove != "N":
        Can_Remove = input("Can remove (Y / N): ")
    if Can_Remove == "Y":
        Can_Remove = 1
    else:
        Can_Remove = 0
    
    sql_code = "INSERT INTO `items` (`name`, `label`, `limit`, `rare`, `can_remove`) VALUES"
    for item in python_array:
        sql_code = sql_code + f"\n    ('{item}', '{Label}', {Limit}, 0, {Can_Remove}),"
    with open(sql_file_path, "w") as sql_file:
        sql_file.write(sql_code)
    print("SQL file generated successfully!")

def copy_images(source_directory, destination_directory, image_files):
    try:
        for filename in image_files:
            source_path = os.path.join(source_directory, filename)
            destination_path = os.path.join(destination_directory, filename)
            if os.path.exists(destination_path):
                continue  # Skip if the file already exists in the destination
            shutil.copy(source_path, destination_path)
        return True
    except Exception as e:
        print(f"An error occurred while copying images: {e}")
        return False

def main():
    root = tk.Tk()
    root.withdraw()
    print(">>> Directory Selection <<<\n")
    print("Select a directory . . . ")
    directory = filedialog.askdirectory(title="Select a directory containing images")

    if not directory:
        print("No directory selected.")
        return
    image_extensions = [".png", ".jpg", ".webp"]
    image_names = []
    for filename in os.listdir(directory):
        if any(filename.lower().endswith(ext) for ext in image_extensions):
            image_names.append(os.path.splitext(filename)[0])
    

    generate_lua_file(image_names)
    print("\n\n>>> Additional Question <<<\n")
    response = input("Would you like to copy your images to another directory? (Y / N): ")
    while response != "Y" and response != "N":
        response = input("Would you like to copy your images to another directory? (Y / N): ")
    if response == "Y":
        response = "yes"
    else:
        response = "no"

    if response == "yes":
        image_files = []

        for filename in os.listdir(directory):
            if any(filename.lower().endswith(ext) for ext in image_extensions):
                image_files.append(filename)

        destination_directory = filedialog.askdirectory(title="Select a destination directory")

        if not destination_directory:
            print("No destination directory selected.")
            return

        success = copy_images(directory, destination_directory, image_files)

        if success:
            print("Image files copied successfully!")
        else:
            print("Error occurred while copying image files.")

if __name__ == "__main__":
    main()