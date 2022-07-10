import pyodbc
import sqlalchemy
import urllib


server = 'FORMA1305\TFTIC' 
database = 'Fatal_Police' 
username = 'sa' 
password = 'tftic@2012' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERver='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)


server = 'FORMA1305\TFTIC' 
database = 'DW_Fatal_Police' 
username = 'sa' 
password = 'tftic@2012' 
cndw = sqlalchemy.create_engine(
               "mssql+pyodbc:///?odbc_connect={}".format(urllib.parse.quote_plus("DRIVER=ODBC Driver 17 for SQL Server;SERVER={0};PORT=1433;DATABASE={1};UID={2};PWD={3};TDS_Version=8.0;".format(server, database, username, password))),
               echo=False)