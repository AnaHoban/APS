Welcome to this repository that aims to analyse the data from the APS experiment performed at LaPsyDÉ. In summary, APS (Auditory Perception Simulation) is a reading strategy in which readers imagine an external
narrator's voice (hence *simulating* it) while performing a silent reading task (reading in their heads). In Zhou and Christianson's 2016 eyetracking study**, APS was found to help readers achieve a higher understanding of complex sentences. Our experiment aimed to reproduce theirs on a population of French speaking adults. We ended up doing the experiment in three different formats:

  1. In-lab, on a population of native french speakers. We also recorded eye-tracking data for this one.
  2. Online, on a population of native french speakers.
  3. Online, on a population of native english speakers.

You will therefore find here all the files needed to:
  ## 1. Transform the raw data into exploitable data (all in the Data/Processed Data/. folder):
     
       For the online experiments, you must use
      - *Data/ParticipantLogCreation_online.ipynb* to remove participants 
      - *Data/OnlineData_DataSetBuilding.ipynb* to create a .csv file that matches the format of the eyetracking (in-lab) data
        output: *{english}_online_{aps}Data.csv* in the {English}Lab subdirectory (Note: english <-> french and aps <-> silent)
        
     For the eyetracking experiment, you must use
       - *Data/DatasetBuilding.py*
         output:  *lab_apsData.csv* and *lab_silentData.csv* in the subdirectory FrenchLab

   -> All these files will produce outputs
         
  ## 2. Perform analyses




























**https://www.semanticscholar.org/paper/Auditory-perceptual-simulation%3A-Simulating-speech-Zhou-Christianson/e79a7561b51894c93ba518adf893ed86e1aa1010 
