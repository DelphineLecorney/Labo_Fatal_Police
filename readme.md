 ![](Images%5CUs_States.jpg/200x150 "Us States")

# <center>\*\*\*\* 👮‍  **US POLICE SHOOTING**  👮‍ \*\*\*\*</center>

# <p style="color:#139C77">Theme</p>

The U.S. Department of Justice is asking you to help them understand the problems
they are currently experiencing with law enforcement agencies in the country.

# <p style="color:#139C77">Context</p>

Following the recent events, the American police are accused of discriminating
during their discrimination during its various interventions.
Indeed, the trend of fatal shootings by police in the United States seems to be
increase, with an average of 1,000 fatal shootings by the police.
Moreover, this rate appears to be much higher for Black Americans than for any other ethnicity.
The FBI has announced plans to review the way it tracks confrontations
with police.

# <p style="color:#139C77">Objective</p>

Implementation of a data analysis solution:
Construction of a Data Warehouse according to a multi-dimensional model.
Implementation of an ETL that will allow the addition of new data in the future
data as it is added.
Exploit the new model and its data to develop reports to answer the questions
to answer the questions asked in the next slide.
These reports can be built using tools such as Power BI, Qlik, Sense, Tableau, or Python
Creation of an AI to predict potential new cases.

# <p style="color:#139C77"> Requirements</p>

To help understand the global situation of fatal police shootings in the
police shootings in the United States.
To help understand if there is discrimination of a certain ethnicity among
others.
To help understand if there are differences in different regions of the
United States.
To help understand if there is a change over time.
To help understand if there are police blunders in the United States.

# <center>\*\*\*\* <p style="color:#D06AB9">My Analys</p> \*\*\*\*</center>

First, I import the modules that I think are necessary for the analysis of the files, it's always possible to import others afterwards.

Then, I import the files with pd.read (pandas) that I want to analyze, I will first read them with the Sweetviz module which gives me a first overview on the data like missing data for example or distinct, nulls....

I'm doing a little info point to get my data type and target the nulls if that's the case. I get the number of columns and the number of entries.

I repeat the operation for the 3 files.

I then switch to SQL Server Management Studio to create my database which will contain my 3 files.
Once my database is done, I create a project on Visual Studio to store the raw data from my 3 files.
From my 3 files, I build 3 tables of the same type that I put in my database.
At the same time, I'm correcting various data types, like the county_fips_all column to text stream instead of Unicode.

I now create a SQL connection to display the database in my jupyter Notebook.
Once the connection is established, I do a .head() and an .info() to check the data, their numbers...

<br><br>

| <center>Logiciels Utilisés</center> | <center>Langages Utilisés</center> |
|----|----|
| <center>Jupyter Notebook</center> | <center>Python - SQL</center> |
| <center>SQL Management Studio</center> | <center>SQL</center> |
| <center>Visual Studio</center> | <center> MSBuild </center> |

<br><br><br>
<u>Thanks for reading</u> !