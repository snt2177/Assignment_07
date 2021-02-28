#------------------------------------------#
# Title: CDInventory.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# STimchenko, 2021-Feb-20, Incorporated file's TODO
# STimchenko, 2021-Feb 27, Added structured error handling, modified data storage to use binary data
#------------------------------------------#

# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # dictionary of data row
strFileName = 'CDInventory.dat'  # data storage file
objFile = None  # file object


# -- PROCESSING -- #
class DataProcessor:
    """Processing CD inventory modyfication"""
    
    @staticmethod
    def add_entry(cd_id, cd_title, cd_artist, table):
        """Function to manage the addition of entries to the existing table
       
        Adds entries to the existing table after the user uses the 'a' functionality
        built into the script.
       
        Args:
            None.
           
        Returns:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime
        """
        intID = int(cd_id)
        dicRow = {'ID': intID, 'Title': cd_title, 'Artist': cd_artist}
        lstTbl.append(dicRow)
        
    @staticmethod
    def del_cd(table):
    # 3.5.2 search thru table and delete CD
        """ Function searches thru the table and deletes CD
        
        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime
   
        Returns:
            New table (list of dict) with removed CD line.
        """
        intRowNr = -1
        blnCDRemoved = False
        for row in table:
            intRowNr += 1
            if row['ID'] == intIDDel:
                del table[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')

class FileProcessor:
    """Processing the data to and from text file"""
    
    @staticmethod
    def load_file(file_name, table):
        """Function to load data from pickled file to a list of dictionaries

        Reads the data from the pickled file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from            

        Returns:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.
        """
        with open(strFileName, 'rb') as fileObj:
            table = pickle.load(fileObj)
        return table

    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.
        """
        strYes = IO.load_inventory()
        if strYes == 'yes':
            with open(strFileName, 'rb') as fileObj:
                 table = pickle.load(fileObj)   
            return table
        else:
            input('The file was NOT loaded. Press [ENTER] to return to the menu.')
            return table

    @staticmethod
    def write_file(file_name, table):
        """ Function to write the data into the file using binary data
        Opens file identified by file_name with owerwrite option
        Gets the data from (list of dicts) and writes into the text file.

        Args:
            file_name (string): name of file used to write the data to
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        with open(file_name, 'wb') as fileObj:
            pickle.dump(lstTbl, fileObj)


# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
            
        """
        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')
    @staticmethod
    def new_CD_info():
        """Collects a user input to add a CD to the current inventory table
        Also checks if disk is an integer and CD Title and Artist are not empty
        
        Args:
            User input for disk ID
            User input for CD Title
            Use input for Artist
            
        Returns:
            strID: the integer ID of the CD
            strTitle: the title of the CD
            strArtist: the CD artist's nameNone.
        
        """
        # Checks if CD number is an integer 
        strIDinput =''
        while True:
            strIDinput = input('Enter ID: ').strip()
            try:
                strID = int(strIDinput)
                break
            except ValueError:
                print('Disk ID should be a number')
        # Checks if Title is non empty
        strTitle =''
        while True:
            strTitle = input('What is the CD\'s title? ').strip()
            try:
                if not strTitle:
                    raise ValueError('Empty String')
                break
            except ValueError:
                print('CD Title can not be empty')
        # Checks if Artist is non empty
        strArtist =''
        while True:
            strArtist = input('What is the Artist\'s name? ').strip()
            try:
                if not strArtist:
                    raise ValueError('Empty String')
                break
            except ValueError:
                print('Artist\'s name can not be empty')
        return strID, strTitle, strArtist
     
    @staticmethod
    def save_inventory():
        """Writes the contents of the current inventory to file.
        
        Args:
            None.
            
        Returns:
            strYesNo: the user selection for saving.
        
        """
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        print()
        return strYesNo
        
    @staticmethod
    def load_inventory():
        """Processes the user input when loading a file.
        
        Args:
            None.
        
        Returns:
            table: the data loaded from strFileName
        
        """
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        # Checks for a 'yes' input
        
        strYes= input('Type \'yes\' to continue and reload from file. Otherwise loading will be canceled: ').strip().lower()
        print()
        return strYes


# 1. When program starts, read in the currently saved Inventory
import pickle
lstTbl = FileProcessor.load_file(strFileName, lstTbl)
IO.show_inventory(lstTbl)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        lstTbl = FileProcessor.read_file(strFileName, lstTbl)
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        # 3.3.2 Add item to the table
        strID, strTitle, strArtist = IO.new_CD_info()
        DataProcessor.add_entry(strID, strTitle, strArtist, lstTbl)
        # Display the inventory post-entry addition.
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstTbl)
        # 3.5.1.2 ask user which ID to remove
        intIDDel = int(input('Which ID would you like to delete? ').strip())
        # 3.5.2 search thru table and delete CD
        DataProcessor.del_cd(lstTbl)
        # 3.5.3 display inventory
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileProcessor.write_file(strFileName, lstTbl)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')




