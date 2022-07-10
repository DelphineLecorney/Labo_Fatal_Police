<center>\*\*\*\* 👮 US POLICE SHOOTING 👮 \*\*\*\*</center>

<p style="color:#139C77">Subject</p>

The U.S. Department of Justice is asking you to help them understand the problems
they are currently experiencing with law enforcement across the country.

<p style="color:#139C77">Context</p>

In the wake of recent events, police officers in the United States have been accused of discriminating
when they discriminate against them in their various interventions.
Indeed, the trend of police officer deaths in the United States appears to be in
increasing, with an average of 1,000 fatal shootings by police.
Moreover, this rate seems to be much higher for Black Americans than for any other ethnicity.
The FBI has announced plans to review the way it tracks confrontations
with police.

<p style="color:#139C77">Objective</p>

Implement a data analytics solution:
Build a data warehouse based on a multidimensional model.
Set up an ETL that will allow new data to be added as it arrives.
Adding data as it arrives.
Leverage the new model and its data to develop reports to answer the questions
to answer the questions posed in the next slide.
These reports can be developed using tools such as Power BI, Qlik, Sense, Tableau or Python.
Create an AI to predict potential new cases.

<p style="color:#139C77">Quests</p>

Help understand the big picture of fatal police shootings in
Police shootings in the United States.
To help understand if there is discrimination of a certain ethnicity among
others.
To help understand if there are differences in different regions of the
regions of the United States.
To help understand if there is a change over time.
Help understand if there are police blunders in the United States.

<center>\*\*\*\* <p style="color:#D06AB9">My Analysis</p> \*\*\*\*</center>

To begin, I create a database in SQL Management Studio named Fatal_Police.

I import the files fatal-police-shootings-data.csv, uscities.csv and Ethnicity Data USA.xlsx into SSIS, I create the necessary tables for these 3 files that I will send to my database.

Once my database is filled, I create a notebook on Visual Studio Code to analyze and clean the files.

I import all the modules that I think are necessary for the analysis, it is always possible to import others later.

Then, with pd.excel (pandas) I get the files I want to analyze.

<u>Lethal Shot File</u>:

I look at the types, shape, columns and nulls.

I decide to remove the "is_geocoding_exact" column as well as the "body-camera" column, the former won't tell me anything important, the latter is not really reliable in my opinion.

I realize that there are nulls, I replace the blanks in the numeric columns with 0's (I'll have to remember to ignore them in the statistics) and I replace the blanks in the strings with "undetermined".

<u>Us city file</u>:

I also take a look at the composition of the file, look for nulls and replace them if they are.

I delete some columns that I don't need for my analysis.

<u>Ethnicity file</u>:

I also look at the information in this file and I see that the id column is empty, I decide to auto-increment it when building the tables to build the star.

The 3 files are composed of usable data, I make a to.SQL connection to rework them on SSIS to build my star.

At the same time, I make a query to build the 5 useful tables for the star on SQL.

On SSIS, I import the tables into a cube to connect it all together, link keys from the fact table to the other tables and make the connection to get my final star.

<br><br>

<u>Used software</u> :
Visual Studio -
SQL Management Studio -
SQL SERVER

<u>Used languages</u> :
Jupyter Notebook -
Python - SQL -
MSBuild

<br><br><br>
<u>Thanks for reading</u> !