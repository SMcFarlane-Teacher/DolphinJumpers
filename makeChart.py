# Import all modules to be utilised

import pandas as pd 
import plotly.graph_objects as go
import plotly.express as px

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('changed_data_set.csv')
    
def makeThePie():
    # Extract the columns
    labels = df['Volunteering Activities']
    values = df['VALUE']
    # Create the pie chart
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    # Add title
    fig.update_layout(title="All Genders: Percentage of Volunteering Types")
    # Show the pie chart
    fig.show()

makeThePie()

def makeLongFormData():

    # Create a bar chart plot
    fig = px.bar(df, x="Volunteering Activities", y="VALUE", color="Sex", barmode="stack", title="Male verses Female Participation Rates")
    # Show the plot
    fig.show()
    
makeLongFormData()

def makeScatter():

    fig = px.scatter(df, x="Volunteering Activities", y="VALUE", color="Sex", size="VALUE", 
                     hover_name="Sex", title="Male verses Female Participation Rates (Scatter Plot)")
    # Show the plot
    fig.show()
    
makeScatter()
