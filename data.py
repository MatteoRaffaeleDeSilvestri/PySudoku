import pickle, json, utilities
from tkinter import Tk, filedialog
from os.path import join, expanduser, exists

# SAVE DATA IN PICKLE FILE AND SHOW THEM IN GAME STATISTICS SECTION

def management(data_type, diff_lvl, data_1, data_2):
    
    # Store data into stats 
    if data_type == 'algo':
        load(1, 'pg', diff_lvl)
        load(data_1, 'agt', diff_lvl)
        load(data_2, 'ast', diff_lvl)

    if data_type == 'player':
        load(1, 'gw', diff_lvl)
        load(data_1, None, diff_lvl)

def load(data, info_type, location):

    # Load data into the file

    # Open file and load info    
    file_data = read()
    
    # Update played game (per difficult)
    if type(data) == int:
        file_data[info_type][location] += data
    elif type(data) == float:
        file_data[info_type][location].append(data)
    else:
        file_data['lg'][location] = utilities.longest_game(file_data['lg'][location], data)
        file_data['sg'][location] = utilities.shortest_game(file_data['sg'][location], data)
    
    # Update file
    with open('data.pickle', 'wb') as f:
        pickle.dump(file_data, f) 

def read():
    
    # Read data from the file
    if exists('data.pickle'):
        with open('data.pickle', 'rb') as f:
            data = pickle.load(f)
        return data
    else:
        return reset()

def reset():

    # Reset the data into the file
    default_data = {
        "pg": 
            {
                "e": 0,
                "m": 0,
                "h": 0           
            },
        "lg": 
            {
                "e": "00:00:00",
                "m": "00:00:00",
                "h": "00:00:00"
            },
        "sg":
            {
                "e": "00:00:00",
                "m": "00:00:00",
                "h": "00:00:00"
            },
        "gw": 
            {
                "e": 0,
                "m": 0,
                "h": 0
            },
        "agt": 
            {
                "e": [],
                "m": [],
                "h": []
            },
        "ast":
            {
                "e": [],
                "m": [],
                "h": []
            }
    }
    
    with open('data.pickle', 'wb') as f:
        pickle.dump(default_data, f)
    return read()

def decode_data():

    # Read data from the file
    try:
        default_file_name = 'data.json'
        initial_save_path = join(expanduser('~'), 'Desktop/')

        # Hide Tkinter window
        Tk().withdraw()

        # Open dialog window from Tkinter
        file_info = filedialog.asksaveasfile(initialdir = initial_save_path, initialfile = default_file_name,  title = 'Generate json', defaultextension = '.json', filetypes = [('JSON file', '.json')])    

        with open('data.pickle', 'rb') as f:
            data = pickle.load(f) 
        with open(file_info.name, 'w') as f:
            json.dump(data, f, indent = 4)
            print('Operation successful')
            
    except Exception as error:
        print(error)

# Use the commands below and run this file to generate a json file with statistics
'''
if __name__ == "__main__":
    decode_data()
'''
