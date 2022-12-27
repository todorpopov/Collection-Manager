A collection management application, built in Python, using the Tkinter GUI framework.

The application uses the Pandas library. It can be installed either 
throught the "requirements.txt", or separately, using pip.


How to use:

    - Open "main.py"

    - Upon starting, the user can select a collection throught the
buttons in the upper left corner of the window("Books" will load by default).

    - Items, already saved in the files, will load automatically in the 
list box on the right.

    - To create a new item, the user has to enter the necessary information
in the input fields, located under the three buttons mentioned earlier.
After that, the user has to press the "Create" button. This will save the information 
to the correct file and update the list box.

    - The "Show All" button shows all of the items that have already been saved to 
the current, working file.

    - The "Edit" button works as follows. First, the user choses the item they want 
to edit, by clicking on it in the list box. Afterwards, the input fields will update 
with the saved information about the selected item. The user can now change some 
or all of the information in the input fields. To save, the user clicks on the "Edit" button.
This will save the newly entered information and update the list box.

    - The "Delete" button will delete the selected item, in the list box, form the working file.

    - The Search function finds exact matches of an entered keyword and the items in the working file.
Above the list box, the user can find the search bar. It works as follows. The user enters the 
exact text they are looking for, than press the "Search" button. The list box will update with the matches.
      To see all of the items again, press the "Show All" button.
