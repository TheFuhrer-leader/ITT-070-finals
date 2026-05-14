# Final Project Reflection

 What part of the project was hardest?
The hardest part was connecting all five files together properly. Making sure that `main.py` could successfully import functions from other files and that objects could be saved and loaded correctly using JSON was challenging at first. I also struggled with planning the structure before writing code.

 What bug took the longest to solve?
The longest bug was the "ModuleNotFoundError" when trying to import `inventory_manager`. It took me a while to realize all files must be in the exact same folder and that file names must match exactly (no extra spaces or wrong capitalization). Another difficult bug was when receiving a shipment — the inventory quantity was not updating until I fixed the reference to the product object.

 How did you organize your code across multiple files?
I followed the assignment requirements:
- `models.py` contains only classes
- `file_manager.py` handles all save and load operations
- `inventory_manager.py` contains core logic (add, search, sort, receive)
- `reports.py` contains all reporting functions
- `main.py` only handles the menus and program flow

This separation made the code much cleaner and easier to maintain.

## How does your save/load system work?
The `file_manager.py` has two main functions: `save_data()` and `load_data()`. When saving, each object is converted to a dictionary using the `to_dict()` method. When loading, the dictionaries are turned back into class objects. This allows the data to persist even after the program is closed.

## What would you improve if you had another week?
If I had more time, I would:
1. Add a full vendor management menu with add/edit/search
2. Create a transaction history log for every stock change
3. Add password protection for the system
4. Export reports to text or CSV files
5. Improve the user interface with better formatting and colors

Overall, this project helped me understand how real applications are structured with multiple files and classes. I learned a lot about modular programming, error handling, and data persistence. I'm proud that the program runs smoothly and meets all the requirements.
