# standard ds imports
import numpy as np
import pandas as pd

# for visualization
import matplotlib.pyplot as plt
import seaborn as sns


def q1(df):
    '''
    This function returns the results for q1 of the anomaly detection project.
    The first dataframe is the data science results. The second is the web dev
    results.
    '''
    # create dataframe showing page counts for each data science lesson
    lessons = pd.DataFrame(df[df.program_id == 3].groupby(['lesson']).page.count().reset_index())
    # sort and save the lessons with the top 5 visit counts
    ds = lessons.sort_values('page', ascending=False).head(5)
    # create dataframe showing page counts for each web dev lesson
    lessons = pd.DataFrame(df[df.program_id != 3].groupby(['lesson']).page.count().reset_index())
    # sort and save the lessons with the top 5 visit counts
    wd = lessons.sort_values('page', ascending=False).head(5)
    # return results
    return ds, wd

def q2(df):
    '''
    This function returns the visualization for q2 of the anomaly detection project.
    '''
    # show visit counts for each lesson by data science cohort
    hold = df[df.program_id == 3].groupby(['cohort', 'lesson']).lesson.count()
    # make it its own dataframe
    gloss = pd.DataFrame(data=hold, index=hold.index).rename(columns=({'lesson':'count'})).reset_index()
    
    # plot how many visits each data science cohort had for the classification lesson
    plt.figure(figsize=(12,8))
    sns.barplot(data=gloss[gloss.lesson == 'classification'], x='cohort', y='count')
    plt.ylabel('lesson visits')
    plt.title('Data Science Darden, cohort 59, visits classification significantly more')
    plt.show()
    
    # show visit counts for each lesson by web dev cohort
    hold = df[df.program_id != 3].groupby(['cohort', 'lesson']).lesson.count()
    # make it its own dataframe
    gloss = pd.DataFrame(data=hold, index=hold.index).rename(columns=({'lesson':'count'})).reset_index()

    # build the frame for the plots
    fig,axes = plt.subplots(1,2, sharey=True,  figsize=(15,8))
    # give it a title
    fig.suptitle('Staff, cohort 28, visits the lessons significantly more often')

    # plot how many visits each web dev cohort had for the html-css lesson
    sns.barplot(ax=axes[1], data=gloss[gloss.lesson == 'html-css'], x='cohort', y='count')
    axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=90)
    axes[1].set_title('Web Development Ceres, cohort 33, visited html-css significantly more than other cohorts')

    # plot how many visits each web dev cohort had for the spring lesson
    sns.barplot(ax=axes[0], data=gloss[gloss.lesson == 'spring'], x='cohort', y='count')
    axes[0].set_ylabel('lesson visits')
    axes[0].set_xticklabels(axes[0].get_xticklabels(), rotation=90)
    axes[0].set_title('Web Development staff, cohort 28, dug into the spring lesson')
    
    # show it all!
    plt.show()
    
    
def q5(df):
    '''
    This function returns the results for q5 of the anomaly detection project
    in a dataframe.
    '''
    # return the row where the data science student from cohort 55 visited the java-ii lesson
    return df[(df.cohort == 55)&(df.lesson == 'java-ii')]

def q6(df):
    '''
    This function returns the results for q6 of the anomaly detection project.
    The first dataframe is the data science results. The second is the web dev
    results.
    '''
    # create lists of the data science and web dev cohort ids
    ds_cohorts = df[df.program_id == 3].cohort.unique().tolist()
    wd_cohorts = df[df.program_id == 2].cohort.unique().tolist()
    # remove the staff cohort id from web dev list
    wd_cohorts.remove(28)
    
    # save the end date of the first cohort in the list
    a = df[df.cohort== ds_cohorts[0]].end_date.max()
    # make a dataframe with a count of how many times each lesson was visited by that cohort, while active
    total = pd.DataFrame(df[df.cohort == ds_cohorts[0]].loc[a:].groupby('lesson').page.count().sort_values().reset_index())
    # do the same thing for each additional cohort in the list, add it to the dataframe
    for c in ds_cohorts[1:]:
        d = df[df.cohort== c].end_date.max()
        new = pd.DataFrame(df[df.cohort == c].loc[d:].groupby('lesson').page.count().sort_values().reset_index())
        total = pd.concat([new, total])
    # save top 5 resutls from the above for loop in its own dataframe
    ds = pd.DataFrame(total.groupby('lesson').page.sum().sort_values(ascending=False)).reset_index().rename(columns=({'page':'visit_count'})).head()
    
    # save the end date of the first cohort in the list
    a = df[df.cohort== wd_cohorts[0]].end_date.max()
    # make a dataframe with a count of how many times each lesson was visited by that cohort, while active
    total = pd.DataFrame(df[df.cohort == wd_cohorts[0]].loc[a:].groupby('lesson').page.count().sort_values().reset_index())
    # do the same thing for each additional cohort in the list, add it to the dataframe
    for c in wd_cohorts[1:]:
        d = df[df.cohort== c].end_date.max()
        new = pd.DataFrame(df[df.cohort == c].loc[d:].groupby('lesson').page.count().sort_values().reset_index())
        total = pd.concat([new, total])
    # save the top 5 results from the above for loop in its own dataframe
    wd = pd.DataFrame(total.groupby('lesson').page.sum().sort_values(ascending=False)).reset_index().rename(columns=({'page':'visit_count'})).head()
    
    # return both dataframes with results
    return ds, wd

def q7(df):
    '''
    This function returns the results for q7 of the anomaly detection project.
    The first dataframe is the data science results. The second is the web dev
    results.
    '''
    # select top 16 data science lessons with the highest visit count
    ds = df[df.program_id == 3].groupby(['lesson']).lesson.count().sort_values(ascending=False).head(16)
    # save it in its own dataframe
    ds = pd.DataFrame(ds).rename(columns={'lesson':'visit_count'}).reset_index()
    
    # select top 9 web dev lessons with the highest visit count
    wd = df[df.program_id == 2].groupby(['lesson']).lesson.count().sort_values(ascending=False).head(9)
    # save it in its own dataframe
    wd = pd.DataFrame(wd).rename(columns={'lesson':'visit_count'}).reset_index()  
    
    # return both dataframes with results
    return ds, wd

def q8(df):
    '''
    This function returns the visualization for q8 of the anomaly detection project.
    '''
    # create weekly page visit counts for each program
    ds = df[df.program_id == 3][['page']].resample('W').count()
    php = df[df.program_id == 1][['page']].resample('W').count()
    java = df[df.program_id == 2][['page']].resample('W').count()
    fe = df[df.program_id == 4][['page']].resample('W').count()
    
    # plot the programs over time to compare them to each other
    plt.figure(figsize=(12,8))
    sns.lineplot(data=ds, x=ds.index, y='page', label='ds')
    sns.lineplot(data=php, x=php.index, y='page', label='php')
    sns.lineplot(data=java, x=java.index, y='page', label='java')
    sns.lineplot(data=fe, x=fe.index, y='page', label='fe')
    plt.title('Page visits by program over time')
    plt.legend()
    plt.show()