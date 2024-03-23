# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 20:27:52 2024

@author: scott
"""

import os
current_directory = os.getcwd()
files_in_directory = os.listdir(current_directory)

# Print the list of files
print("Files in the current working directory:")
for file in files_in_directory:
    print(file)

print(current_directory)

#1a Find all pa�ents with Diabetes using the codes above by lis�ng their pa�ent IDs.
covid_diabetes=pd.read_csv('DW3_set_exercise.csv')
print(covid_diabetes.head(10))
# Codes to check for
icd10_diabetes_codes = ['E08', 'E09', 'E10', 'E11', 'E13']

# new dataframe with only the diabetes codes
diabetes_diagnosis = covid_diabetes[covid_diabetes['Diagnosis Code'].isin(icd10_diabetes_codes)]

patients_with_diabetes = diabetes_diagnosis['Patient ID']
print(patients_with_diabetes)
print(len(patients_with_diabetes))

#1b Find the cardinality of the Diabetes set. 
cardinality = len(patients_with_diabetes.drop_duplicates())
print(cardinality)

#2a Find all pa�ents with COVID using the codes above by lis�ng their pa�ent IDs.
#icd10 Covid codes to check
icd10_covid_codes = ['U07.1','J12.82']

# new dataframe with only the covid codes
covid_diagnosis = covid_diabetes[covid_diabetes['Diagnosis Code'].isin(icd10_covid_codes)]

patients_with_covid = covid_diagnosis['Patient ID']
print(patients_with_covid)
print(len(patients_with_covid))

#2b Find the cardinality of the COVID set.
cardinality_covid=len(patients_with_covid.drop_duplicates())
print(cardinality_covid)

#3a Find all patients with Diabetes and COVID using the codes above by listing their patient IDs. 
covid_diabetes_intersect = pd.merge(diabetes_diagnosis, covid_diagnosis, on='Patient ID', how='inner')

#3b Find the cardinality of the Intersection set. 
print(len(covid_diabetes_intersect))

#4a Find all patients with Diabetes or COVID using the codes above by listing their patient IDs. 
covid_diabetes_union = pd.merge(diabetes_diagnosis, covid_diagnosis, on='Patient ID', how='outer')
 
#4b Find the cardinality of the Intersection set. 
print(len(covid_diabetes_union))

#5 Draw a Venn diagram showing the Diabetes, COVID, Intersection and Union sets.
pip install matplotlib_venn matplotlib seaborn
from matplotlib_venn import venn2
import matplotlib.pyplot as plt

print(diabetes_diagnosis.columns)
diabetes_diagnosis_set=set(diabetes_diagnosis['Patient ID'])
covid_diagnosis_set=set(covid_diagnosis['Patient ID'])
venn2([diabetes_diagnosis_set, covid_diagnosis_set], ('Diabetes Patients', 'Covid Patients'))
plt.show()

#6a Now including the date of diagnosis, find all patients with Diabetes only after they had 
# COVID by listing their patient IDs.
print(covid_diabetes_intersect)
print(covid_diabetes_intersect.columns)
diabetes_after_covid=covid_diabetes_intersect[covid_diabetes_intersect['Date_x'] > covid_diabetes_intersect['Date_y']]
print(diabetes_after_covid)
patients_with_diabetes_after_covid=diabetes_after_covid['Patient ID']
print(patients_with_diabetes_after_covid)

#6b Find the cardinality of the Diabetes only after COVID set. 
cardinality_diab_after_covid=len(patients_with_diabetes_after_covid.drop_duplicates())
print(cardinality_diab_after_covid)

#6c Provide a count breakdown for each of the diabetes codes listed above occurring only 
# after COVID. 
covid_diabetes_by_type=diabetes_after_covid.groupby('Diagnosis Code_x')['Patient ID'].count()
print(covid_diabetes_by_type)
