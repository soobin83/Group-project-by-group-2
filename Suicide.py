# Dependencies 
import matplotlib.pyplot as plt
import pandas as pd
import csv
suicide_path ="Data/Suicide.csv"
# Read the suicide_path
suicide = pd.read_csv(suicide_path)
suicide.head()