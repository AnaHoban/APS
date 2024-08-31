#setting the speakers for the online version of the experiment
import pandas as pd
import random
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#import the list
print('Which list do you need to transform?')
list_nb = input()
list_a = pd.read_csv('./english items - list{}a.csv'.format(list_nb), encoding = 'latin1')
list_a_items = list_a[list_a.display == 'Liste'].copy()

#keeping track of the og indices
original_indices = list_a_items.index

list_a_items = list_a_items.sort_values(by=['Structure', 'Plausibility'], ascending=[True, True])

#create speaker lists: the first 48 are for the targets and the next 96 are for the fillers
speakers_a = ['AF.jpg','AF.jpg','WF.jpg','WF.jpg']*12  + ['AF.jpg','WF.jpg']*48  

#assign them to the separate item lists
list_a_items['Photo'] = speakers_a

# reoder the manipulated subset to match og indices
list_a_items = list_a_items.loc[original_indices]

# update the original df with the updated items
list_a.loc[original_indices, list_a_items.columns] = list_a_items

#add the quotation marks
def add_quotes(text):
    return f'"{text}"'

# Apply the function to the specified column
list_a['Phrase'] = list_a['Phrase'].apply(add_quotes)
list_a['Phrase entrainement'] = list_a['Phrase entrainement'].apply(add_quotes)
list_a['Phrase'] = list_a['Phrase'].replace('"nan"', '', regex=True)
list_a['Phrase entrainement'] = list_a['Phrase entrainement'].replace('"nan"', '', regex=True)


#from there, create list b with inverted speakers

def speaker_inverter(speaker):
    inversion_dict = {
        'WF.jpg': 'AF.jpg',
        'AF.jpg': 'WF.jpg',
        'Femme entrainement.png': 'Homme entrainement.png',
        'Homme entrainement.png': 'Femme entrainement.png'
    }
    return inversion_dict.get(speaker, speaker)

def audio_inverter(speaker):
    inversion_dict = {
        'Audio femme entrainement.mp3': 'Audio homme entrainement.mp3',
        'Audio homme entrainement.mp3': 'Audio femme entrainement.mp3'
    }
    return inversion_dict.get(speaker, speaker)


list_b = list_a.copy()

#invert all speakers(including trainings
list_b.Photo = list_b.Photo.apply(speaker_inverter)
list_b.Audio = list_b.Audio.apply(audio_inverter)



#save the lists
list_a.to_csv('C:/Users/anaho/desktop/research/language/aps/MakingStimuli/list{}a.csv'.format(list_nb), header= True, index = False, encoding='latin1')
list_b.to_csv('C:/Users/anaho/desktop/research/language/aps/MakingStimuli/list{}b.csv'.format(list_nb), header= True, index = False, encoding='latin1')