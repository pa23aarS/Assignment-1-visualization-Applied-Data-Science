# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 03:56:36 2023

@author: prave
"""
#importing the neccessary libararies to the required visualisations
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker

file_name = '10_Property_stolen_and_recovered.csv'
data= pd.read_csv(file_name)
print(data)



def recovered_cases_by_year(data):
    # Filter data for Assam and Chandigarh
    assam_data = data[data['Area'] == 'Assam']
    chandigarh_data = data[data['Area'] == 'Chandigarh']
    assam_cases = assam_data.groupby('Year')['Cases_Property_Recovered'].sum()
    chandigarh_cases = chandigarh_data.groupby('Year')['Cases_Property_Recovered'].sum()

    # Plotting the line chart
    plt.plot(assam_cases.index, assam_cases.values, label='Assam')
    plt.plot(chandigarh_cases.index, chandigarh_cases.values, label='Chandigarh')

    # Adding labels and title
    plt.xlabel('Year')
    plt.ylabel('Number of Recovered Cases')
    plt.title('Recovered Cases by Year in Assam and Chandigarh')

    # Adding legend
    plt.legend()

    # Displaying the chart
    plt.show()
recovered_cases_by_year(data)

def stolen_property_comparison(data):
    # Filter data for Bihar and Delhi
    bihar_data = data[data['Area'] == 'Bihar']
    delhi_data = data[data['Area'] == 'Delhi']

    #Calculation of Total Cases
    bihar_stolen = bihar_data['Cases_Property_Stolen'].sum()
    delhi_stolen = delhi_data['Cases_Property_Stolen'].sum()

    # Creating bar chart
    fig, ax = plt.subplots()
    ax.bar(['Bihar', 'Delhi'], [bihar_stolen, delhi_stolen])

  
    plt.xlabel('State')
    plt.ylabel('Total Number of Cases of Property Stolen')
    plt.title('Property Stolen Cases in Bihar and Delhi')

    # Displaying the chart
    plt.show()
stolen_property_comparison(data)




def top_group_names(data):
    group_data = data.groupby('Group_Name')['Value_of_Property_Stolen'].sum()
    sorted_groups = group_data.sort_values(ascending=False)
    top5_groups = sorted_groups.head(5)
    fig, ax = plt.subplots()
    ax.pie(top5_groups, labels=top5_groups.index, autopct='%1.1f%%')

    # Adding title
    plt.title('Top 5 Group Names by Value of Property Stolen')
    plt.show()
top_group_names(data)













