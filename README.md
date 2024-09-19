Welcome to this repository! Here, you will find the code to analyse the data from the APS experiment performed at LaPsyDÉ. 

In summary, APS (Auditory Perception Simulation) is a reading strategy in which readers imagine an external narrator's voice (hence *simulating* it) while performing a silent reading task reading in their heads). In [Zhou and Christianson's 2016 eyetracking study]([https://www.semanticscholar.org/paper/Auditory-perceptual-simulation%3A-Simulating-speech-Zhou-Christianson/e79a7561b51894c93ba518adf893ed86e1aa1010]), APS was found to help readers achieve a higher understanding of complex sentences. Our experiment aimed to reproduce theirs on a population of French speaking adults. We ended up doing the experiment in three different formats:

  1. In-lab, on a population of native french speakers. We also recorded eye-tracking data for this one;
  2. Online, on a population of native french speakers;
  3. Online, on a population of native english speakers.

## 1. Preparation 
Before doing anything, make sure you must have:
  - for online data: downloaded online datafiles from Gorilla in the .csv format, with ',' delimiter **and** named the files containing the response data as *list1, list2, list3, ...*;
  - for lab data: put all data in aps/ and control/ directories (simpler if all excluded recording sessions are in a separate folder).
  - **make sure you have python, jupyter and R installed on your computer**

Now we can start playing with the data!

## 2. Transform the raw data into exploitable data (all in the Data/Processed Data/. folder):
     
For the online experiments, you must use
   - `Data/ParticipantLogCreation_online.ipynb` to create a participant log file (and remove participants that do not match criteria)
   - `Data/OnlineData_DataSetBuilding.ipynb` to create a .csv file that matches the format of the eyetracking (in-lab) data
  outputs: `{english}_online_{aps}Data.csv` in the {English}Lab subdirectory (Note: english <-> french and aps <-> silent)
        
  For the eyetracking experiment, you must use
    - run ` python {...}\APS\analysis\Data\DatasetBuilding.py` (where {} depends on where you put this repo) to navigate to the right directory
  outputs:  `lab_apsData.csv` and `lab_silentData.csv` in the subdirectory `FrenchLab/`

## 3. Clean the data
In your terminal: 
  1. navigate to the directory:
    `cd {your path to this repo}\APS\analysis\Data`
  2. `python ..\Code\DataCleaning.py`    
  3. enter `Processed data/FrenchOnline/{french or english}_online_{aps or silent}Data_formatted.csv` for online data or `only_{aps or silent}_data.csv` for lab data
  4. `python ..\Code\DescriptiveStats.py`   
  5. enter `CLEAN_{}` <-- {} = whatever file was in 3
  6. for online data: if you want the table with all the summary means run `python ..\Code\TableOnline.py`  and pick the function for control or aps  
    for lab data: run `ComparingGroups.py`

Now you have all the data in the same format and therefore can use any of the files in the next steps, depending on what you want to analyse.

## 4. Perform some preliminary stats and analyses (LMMs)
-
-

Furthermore, following Zhou and Christianson's analysis, we have added two additional analyses, namely a attractivness survey and eyetracking analysis for the lab data.

## 5. Attractivness Survey
Note that attractivness surveys were only administered to the french lab and english online participants.
  1. Put the attractiveness survey data in `{}APS/analysis/Data/Raw data/Attractiveness_{lab or online}.csv` ; 
  2.  Run `python wilcoxon_for_{lab or online}.py`. 

## 6. Eyetracking 
The eyetracking data file must be in ____. This data was extracted following these steps in DataViewer:

add steps

One 

1. Then you can use the R notebook: `C:/Users/anaho/Desktop/research/Language/APS/analysis/Code/Eyetracking/DescriptiveStats_ET.R` to reproduce Table _ of the paper. This code also plots the results from the table and stores them in the same directory (Analysis/Eyetracking/.) as the proportions table and the R file. 
2. Add here the file for LMMs
  


  





























