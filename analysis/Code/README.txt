 * READ ME *
Instructions on how to transform the raw data into analyzable data for LMMs and perform descriptive stats

Written by Ana Hoban
Last update: 08/2024

----------------------------------------------------- ONLINE DATA PREP -------------------------------------------------------------

(When downloading files from the gorilla website:

1. import as comma delimited csv file
2. name the files with the response data as list1, list2.. etc)

3. use the Data/ParticipantLogCreation_online.ipynb notebook to create the participant log and exclude participants
4. Code/OnlineData_DataSetBuilding.ipynb : Follow the directions written in the first cell
                                                 ----------------------------

------------------------------------------------------ LAB DATA PREP ---------------------------------------------------------------

1. Put all data in aps/ and control/ directories (simpler if all excluded recording sessions are in a separate folder)
2. cd C:\Users\anaho\desktop\research\Language\APS\analysis\Data
3. run  ..\Code\DatasetBuilding.py
                                                   --------------------------

# open terminal and run the following:

(1.) cd C:\Users\anaho\desktop\research\Language\APS\analysis\Data
2. python ..\Code\DataCleaning.py    
3. enter: Processed data/FrenchOnline/french_online_apsData_formatted.csv in terminal (or whichever file) or only_aps_data.csv
4. python ..\Code\DescriptiveStats.py   
5. enter: CLEAN_{} <-- {} = wtv was in 3
6. for online data: if you want the table with all the summary means run python ..\Code\TableOnline.py  and pick the function for control or aps  
    for lab data: run ComparingGroups.py



