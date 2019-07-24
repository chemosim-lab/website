# website
Database website 



accounts: the folder handle the login logout and registration
 Need to login to create an account for other user.
 Login is required to see the data or upload the data
chemosimdata: URL Configuration and setting
phandlers : all the main function of the website can be found in this folder; 
phandlers/models: the database function  you can modify it to add or delete a column
phandlers/upload: the function to upload the new dataframe file into the database
 The function accept only csv file
 CSV file column must follow the structure of the database: 
 eg. Ligand; the file column name must be  inchikey,name, smiles.


How to run:
Download the files
pip install requirement.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser ## imporant step remember your user name and password
python manage.py runserver 



To do List:
add header menu for recepteur, psychophysiology data, donnee affinite
add search and sort option do the table
