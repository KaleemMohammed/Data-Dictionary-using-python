
#====================================================================================================#
#                                   Data Dictionary for Exploratory data analysis                    #
#====================================================================================================#

import pandas as pd
import os

# Set the working directory
os.chdir('F:\\GIT\\Git_KaleemMohammed')

# Load the data
filename = 'Back_pain'
inputdata = pd.read_csv(filename + ".csv", sep=',' , encoding='latin-1')


def get_data_dictionary(df):
    """
    Description:
        
        Prepare data dictionary with below columns
        1.Variable_Name
        2.Format
        3.Levels
        4.No.of Missings
        5. % of Missings
        6.Sample
        
        This code will not give datatime format for date variables when it has loaded it as an object
        
    Args:
        Non-empty data frame

    Returns:
        data dictionary with filenname_data_dictionray name
    """

    if len(df)>0:
        try:
            data = pd.DataFrame()
            data["Variable_Name"] = list(df.columns)
            data["Format"] = list(df.dtypes)
            data["Levels"] = list(df.apply(lambda x: len(x.unique())))
            data["No.of Missings"] = list(df.isnull().sum())
            data[" % of Missings"] = round((data["No.of Missings"]/len(df))*100,2).astype(str)+"%"
            newlist1 = df.head().values.tolist()
            newlist2 = list(zip(*newlist1))
            data["Sample"] = newlist2
            data.to_csv(filename + "_data_dictionary.csv",index=False)
        except Exception as e:
            print("Something went wrong :), Please check using '"+str(e)+"' error")
    else:
        print("Input data is empty")

#Calling the method
get_data_dictionary(inputdata)








