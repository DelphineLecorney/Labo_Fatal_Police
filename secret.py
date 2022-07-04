import pyodbc


server = 'FORMA1305\TFTIC' 
database = 'Fatal_Police' 
username = 'sa' 
password = 'tftic@2012' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)