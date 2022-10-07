# standard ds imports
import numpy as np
import pandas as pd

# for visualization
import matplotlib.pyplot as plt
import seaborn as sns


def q1(df):
    lessons = pd.DataFrame(df[df.program_id == 3].groupby(['lesson']).page.count().reset_index())
    ds = lessons.sort_values('page', ascending=False).head(5)
    
    lessons = pd.DataFrame(df[df.program_id != 3].groupby(['lesson']).page.count().reset_index())
    wd = lessons.sort_values('page', ascending=False).head(5)
    
    return ds, wd

def q2(df):
    hold = df[df.program_id == 3].groupby(['cohort', 'lesson']).lesson.count()
    gloss = pd.DataFrame(data=hold, index=hold.index).rename(columns=({'lesson':'count'})).reset_index()
    
    plt.figure(figsize=(12,8))
    sns.barplot(data=gloss[gloss.lesson == 'classification'], x='cohort', y='count')
    plt.ylabel('lesson visits')
    plt.title('Data Science cohort 59 visits classification significantly more')
    plt.show()
    
    hold = df[df.program_id != 3].groupby(['cohort', 'lesson']).lesson.count()
    gloss = pd.DataFrame(data=hold, index=hold.index).rename(columns=({'lesson':'count'})).reset_index()

    fig,axes = plt.subplots(1,2, sharey=True,  figsize=(15,8))
    fig.suptitle('Cohort 28 visits the lessons significantly more often because they are staff')

    sns.barplot(ax=axes[1], data=gloss[gloss.lesson == 'html-css'], x='cohort', y='count')
    axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=90)
    axes[1].set_title('Web Development cohort 33 visited html-css significantly more than other cohorts')

    sns.barplot(ax=axes[0], data=gloss[gloss.lesson == 'spring'], x='cohort', y='count')
    axes[0].set_ylabel('lesson visits')
    axes[0].set_xticklabels(axes[0].get_xticklabels(), rotation=90)
    axes[0].set_title('Web Development staff dug into the spring lesson')
    
    
    plt.show()
    
    
def q5(df):
    return df[(df.cohort == 55)&(df.lesson == 'java-ii')]

def q6(df):
    ds_cohorts = df[df.program_id == 3].cohort.unique().tolist()
    wd_cohorts = df[df.program_id == 2].cohort.unique().tolist()
    wd_cohorts.remove(28)
    
    a = df[df.cohort== ds_cohorts[0]].end_date.max()
    total = pd.DataFrame(df[df.cohort == ds_cohorts[0]].loc[a:].groupby('lesson').page.count().sort_values().reset_index())

    for c in ds_cohorts[1:]:
        d = df[df.cohort== c].end_date.max()
        new = pd.DataFrame(df[df.cohort == c].loc[d:].groupby('lesson').page.count().sort_values().reset_index())
        pd.concat([new, total])
        
    ds = pd.DataFrame(total.groupby('lesson').page.sum().sort_values(ascending=False)).reset_index().rename(columns=({'page':'visit_count'})).head()
    
    a = df[df.cohort== wd_cohorts[0]].end_date.max()
    total = pd.DataFrame(df[df.cohort == wd_cohorts[0]].loc[a:].groupby('lesson').page.count().sort_values().reset_index())

    for c in wd_cohorts[1:]:
        d = df[df.cohort== c].end_date.max()
        new = pd.DataFrame(df[df.cohort == c].loc[d:].groupby('lesson').page.count().sort_values().reset_index())
        pd.concat([new, total])
        
    wd = pd.DataFrame(total.groupby('lesson').page.sum().sort_values(ascending=False)).reset_index().rename(columns=({'page':'visit_count'})).head()
    
    return ds, wd

def q7(df):
    ds = df[df.program_id == 3].groupby(['lesson']).lesson.count().sort_values(ascending=False).head(15)
    ds = pd.DataFrame(ds).rename(columns={'lesson':'visit_count'}).reset_index()

    wd = df[df.program_id == 2].groupby(['lesson']).lesson.count().sort_values(ascending=False).head(9)
    wd = pd.DataFrame(wd).rename(columns={'lesson':'visit_count'}).reset_index()  
      
    return ds, wd

def q8(df):
    ds = df[df.program_id == 3][['page']].resample('W').count()
    php = df[df.program_id == 1][['page']].resample('W').count()
    java = df[df.program_id == 2][['page']].resample('W').count()
    fe = df[df.program_id == 4][['page']].resample('W').count()
    
    plt.figure(figsize=(12,8))
    sns.lineplot(data=ds, x=ds.index, y='page', label='ds')
    sns.lineplot(data=php, x=php.index, y='page', label='php')
    sns.lineplot(data=java, x=java.index, y='page', label='java')
    sns.lineplot(data=fe, x=fe.index, y='page', label='fe')
    plt.title('Page visits by program over time')
    plt.legend()
    plt.show()