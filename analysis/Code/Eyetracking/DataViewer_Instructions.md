# This document explains how to create the eyetracking dataset for each of the conditions for the eytracking version of the APS experiment

# Written by Ana Hoban on July 22nd


---- INSTRUCTIONS ----

- PREPARATION -

1 - Open DataViewer 

2 - Click File > Import Data > Multiple EyeLink Datafiles and select the *folder* containing the wanted data and click Import

3 - Go in the 'Full trial period'  dropdown and select 'edit':
	Create a new period -- call it Sentence_ReadingTime 
	Set the IP Start Event Setting to EDF message, with the Message text: SENTENCE_DISPLAY
	Set the IP End Event Setting to EDF message, with the Message text: KEYBOARD_SENTENCE

click on OK (keep 'Apply Strict Event Matching' selected) and OK again (now, you should see 'Sentence_ReadingTime' selected from the dropdown menu where you selected 'Full trial period' earlier.

note: make sure the message names are exactly this and that there are no extra spaces at the end of words. do not put quotation marks.

4 -  Create a trial group by right clicking the any interest area of any trial:
 - select 'trial grouping', 
 - then "sentence_type" and "syntactic_condition" as the variable to group trial conditions by.
  - click on 'regroup'  

Notice that there are two new branches in the filetree on the left; they correspond to the different sentence types!

5 - (if needed) Resize the IAs: Right click on the folder containing all trials (the two new ones, targer: object, target: subject) in the tree view and select 'IA Shape Actions' > 'Resize Edges' and then resize top and bottom by 300 px. This allows to adjust the IA shape for the participants for which the eye tracker was not working perfectly and had a vertical shift in the reading of their gaze.

6- Right click on the first two branches (keeping only targets) and select 'Remove from viewing session', this way the report won't contain all that data

- REPORT -

6 - Click Analysis > Reports > Interest Area Report
	
    Select the following variables (plus any others from the original dataframe)

	1. IA_FIRST_FIXATION_DURATION
	2. IA_FIRST_RUN_DWELL_TIME
	3. IA_REGRESSION_PATH_DURATION
	4. IA_DWELL_TIME
	5. IA_REGRESSIONS_IN
	6. IA_REGRESSIONS_OUT
	7. IA_SKIP
	8. IA_ID

    tip: they are in alphabetical order on DataViewer ;)

The other variables I selected were (in blue):
syntactic_condition
plausibility_condition
sentence_type
condition
SENTENCE_RT
PARAPHRASE_ANSWER
PARAPHRASE_ACCURACY
Trial_Index_
section
item_number
speech_condition (only for aps data)

    Then tick the box 'Create Output Report for All Custom Interest Periods
    Also tick Report IP Data in Multiple Files

	






