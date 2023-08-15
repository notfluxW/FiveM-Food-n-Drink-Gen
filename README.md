# Food & Drink Generator

The **Food & Drink Generator** is a Python script designed to simplify the process of generating Lua configuration files for the **[esx_basicneeds](https://github.com/mitlight/esx_basicneeds)** resource in the popular FiveM framework. This script takes images as input, creates corresponding in-game food and drink items, and even offers the option to generate SQL files for the items. It's especially useful for creating items with multiple variants, such as various flavors of drinks.

## Table of Contents

- **[Getting Started](#getting-started)**
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- **[Usage](#usage)**
  - [Generating Items](#generating-items)
  - [Generating SQL](#generating-sql)
  - [Copying Images](#copying-images)
- **[Configuration](#configuration)**
- **[Contributing](#contributing)**
- **[License](#license)**

## Getting Started

### Prerequisites

Before using the **Food & Drink Generator**, ensure you have the following:

- Python 3.x installed on your system.
- Images of the food and drink items you want to create.

### Installation

1. Clone this repository to your desired location:

   ```bash
   git clone https://github.com/notfluxW/FiveM-Food-n-Drink-Gen.git
   cd FoodAndDrinkGenerator
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage {#gemerating-items}
1. Place the images of the food and drink items you want to generate in a folder.
2. Run the script using the *run.bat* file or with the following command:
   ```bash
   python food_and_drink_generator.py
   ```
3. The script will prompt you to select the folder containing the images. It will automatically generate Lua configuration files (**`generated.lua`**) based on the selected images. You will also be given the option to generate SQL files and copy images to another directory.

### Generating SQL
If you choose to generate SQL files for the items:

1. The script will prompt you to provide a global label and limit for the items.
2. You will also be asked whether the items can be removed from the inventory.
3. SQL files (**`generated.sql`**) will be generated in the same output folder.

### Copying Images
If you choose to copy the generated item images to another directory:
1. The script will prompt you to select the destination directory.
2. The images will be copied from the source directory to the destination directory.

## Configuration
No direct configuration is required for the script itself. However, you can customize the script's behavior by modifying the settings in **`food_and_drink_generator.py`**.

## Contributing
Contributions are welcome! If you have improvements or new features to add, please fork the repository and submit a pull request.

## License
This project is licensed under the [**MIT License**](https://github.com/notfluxW/FiveM-Food-n-Drink-Gen/blob/main/LICENSE).