# Create and Load Data
A small project to demonstrate skills in the Python Basics section of the python training program

## Description
This is a small script with the aim of generating fake data for fictional people and load them into a database using the Faker library and sqlite3.

## Getting Started
### Dependencies
Please ensure that you have Python version 3 installed on your computer.

Ypu can find the latest version of Python available using this link: https://www.python.org/downloads/

### Installing
* Open your preferred terminal (command prompt, windows powershell etc.) in the directory where this README.md file is located
* Activate the virtual environment by writing: ``` source .venv/bin/activate ```
* Now you should have the required libraries to run the project

### Executing the program
* To create fake data and load this data into a database, write the following command in the terminal: ``` python3 create_and_load_data.py ```
* To verify that fake data has been created and loaded into a database, write ``` python3 ``` in the terminal.
* At this point, you will now be in the Python console. Here you can write the following statements:
* ``` import sqlite3 ```
* ``` con = sqlite3.connect("fake_people.db") ```
* ``` cur = con.cursor() ```
* ``` list_people = [row for row in cur.execute("SELECT * FROM people")] ```
* ``` list_people[7] # Returning the fake person in the 7th row of the database ```

#### Other comments
* The program can take quite a while to run as it is creating 1000 fake people. Hopefully as I improve with Python, I can learn some techniques to improve how long the program takes to run. (For the time being, you can change 1000 to 100 on line 16 of the create_and_load_data.py file)
* Feel free to navigate to the tests directory (ensuring that you are still within the virtual environment) and writing ``` pytest ``` in the terminal.

### Author
Nathan Lutala, nlutala

## Version History
* 0.1 - First release

## Acknowledgements
Inspiration for writing this readme file
* https://github.com/nlutala/tic-tac-toe-ml/
