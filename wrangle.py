import numpy as np
import pandas as pd

def acquire():
    '''
    This function reads locally saved files for the anonymized curriculum access,
    and the cohort data. It returns both in two separate dataframes.
    '''
    # read the txt file and save it as a dataframe
    df = pd.read_table('anonymized-curriculum-access.txt')
    # read the csv and save it as a dataframe
    cohorts = pd.read_csv('cohorts.csv')
    # return both
    return df, cohorts

    
def prepare(df, cohorts):
    '''
    This function takes in both the curriculum access dataframe and the cohorts
    dataframe and completes the following:
    - splits out the curriculum access data and renames the columns to be human readable
    - moves erroneous ip addresses to the correct column
    - handles nulls in the cohort data
    - merges the curriculum access data with the cohort data
    - creates a datetime index
    - feature engineers 'lesson' with the root of the page pathway
    - renames lesson names with near-duplicates
    - saves a clean version of the data as a CSV locally
    '''
    # splits out the curriculum access data
    df.columns = ['entry']
    df = df.entry.str.split(expand=True)
    df = df.drop(columns=1)
    # make columns human readable
    df.columns = ['date', 'page', 'user', 'cohort', 'ip']
    
    # move erroneous ip addresses to the correct column
    temp = df[df.ip.isnull()].index
    for spot in temp:
        df.ip.iloc[spot] = df.cohort.iloc[spot]
        df.cohort.iloc[spot] = 0
    
    # handles nulls in the cohort data
    t2 = df[((df.user == '88')|(df.user == '247')|(df.user == '103'))& (df.cohort == 'nan')].index
    for spot in t2:
        df.cohort.iloc[spot] = 0
        
    # make numerical columns into integer types
    df.cohort = df.cohort.astype(int)
    df.user = df.user.astype(int)
    
    # merge the dataframes
    df = df.merge(cohorts, how='left', left_on=df.cohort, right_on=cohorts.id)
    # drop extra columns and foreign key
    df = df.drop(columns=['key_0', 'id'])
    
    # set date to datetime type
    df.date = pd.to_datetime(df.date)
    # set date to make a datetime index
    df = df.set_index('date')

    # set start and end dates to datetime types
    df.start_date = pd.to_datetime(df.start_date)
    df.end_date = pd.to_datetime(df.end_date)

    # feature engineer lesson to be the root of the page pathway
    df['lesson'] = df.page.str.split('/',1,True)[0].values
    
    # correct lesson name duplicates
    df.lesson = df.lesson.str.replace('1-fundamentals', 'fundamentals')
    df.lesson = df.lesson.str.replace('2-storytelling', 'storytelling')
    df.lesson = df.lesson.str.replace('3-sql', 'sql')
    df.lesson = df.lesson.str.replace('4-python', 'python')
    df.lesson = df.lesson.str.replace('5-stats', 'stats')
    df.lesson = df.lesson.str.replace('6-regression', 'regression')
    df.lesson = df.lesson.str.replace('7-classification', 'classification')
    df.lesson = df.lesson.str.replace('8-clustering', 'clustering')
    df.lesson = df.lesson.str.replace('9-timeseries', 'timeseries')    
    df.lesson = df.lesson.str.replace('10-anomaly-detection', 'anomaly-detection')
    df.lesson = df.lesson.str.replace('11-nlp', 'nlp')
    df.lesson = df.lesson.str.replace('12-distributed-ml', 'distributed-ml')
    df.lesson = df.lesson.str.replace('13-advanced-topics', 'advanced-topics')

    # save clean version to a local csv
    df.to_csv('prepared_curriculum_access.csv')
    
    # return the final dataframe
    return df



