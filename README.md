# Anomaly Detection Project
by: Morgan Cross

This project is designed to answer specific questions from the curriculum log data sent over by a fictional supervisor.  

-----
## Project Overview:

#### Objectives:
- Document code, process (data acquistion, preparation, and exploratory data analysis), findings, and key takeaways in a Jupyter Notebook Final Report.
- Create modules (wrangle.py) that make the process repeateable and the report (notebook) easier to read and follow.
- Answer the questions using data exploratory to support your findings.
- Refine work into an email, including a jupyter notebook and one-slider executive summary, that you will walk through explaining the work you did, why, goals, what you found, and your conclusions.

#### Audience:
- Immediate supervisor prepping for a board meeting

#### Project Deliverables:
- this README.md walking through the project details
- email answering the questions
- one-slider executive summary
- final_report.ipynb displaying the process, findings, key takeaways, recommendation and conclusion
- wrangle.py with all acquire and prepare functions
- working_report.ipynb showing all work throughout the pipeline

-----
## Executive Summary:
Goals
 - Answer direct questions provided
 - Locate and interperate any anomaly occurance in the logs
 
Key Findings
 - Data Science alumni often come back for the fundamentals lesson, insinuating this information needs more review prior to graduation
 - The 2019 shut down of program cross-curriculum-access did not take effect. A data science student was able to access web development curriculum in May 2020
 
Takeaways
 - Students and Alumni can still access other programs information and this needs to be addressed
 - Programs are consistent cohort to cohort on their lessons with very few significant variations
 - Site visits are trending up
 
Recommendations
- Add extra emphasis and focus on spring content for web development students
- Adding in a fundamentals review towards the end of the data science program may mitigate knowledge lost after graduation
- Develop dashboard to update live data to visually display how current cohorts are interacting with the curriculum
- Ensure the server resources can handle added demand as programs continue to grow

-----
## Data Dictionary:
| Feature Name | Type | Description |
| ---- | ---- | ---- |
| page | str | pathway to page |
| user | int | student's user number |
| cohort | int | cohort id number |
| ip | str | ip address |
| name | str | name of cohort |
| start_date | datetime | start date of cohort |
| end_date | datetime | end date of cohort |
| program | str | which program the cohort teaches. Data Science is 3 and the Web Development is split into 1 for PHP, 2 for Java, and 4 for Front End |

-----
## Planning
 - Create deliverables:
     - email
     - final_report.ipynb
     - one-slide executive summary
 - Bring over functional wrangle.py and explore.py files
 - Acquire the data from the local CSV's via the acquire function
 - Prepare the data via the prepare function
 - Explore the data and answer the questions. 
 - Document findings and takeaways.
 - Develop and document all findings, takeaways, recommendations and next steps.

-----
## Data Aquisition and Preparation
Files used:
 - wrangle.py

Steps taken:
In this step, I call my aquire function from my wrangle.py. This function:
- grabs the data from the locally saved CSVs 
- combines them into one dataframe

Next, I called my prepare function from my wrangle.py. This function:
- splits out and renames columns to be human readable
- moves erroneous ip addresses to the correct column
- handes nulls in cohort data
- merges the log and cohort dataframes
- creates a datetime index using the log entry dates
- feature engineers 'lesson' with the root of the page pathway
- renames lesson names with near-duplicates
- saves a clean version of the CSV locally

Takeaways:
- The data brings in 900,000 log records and data on 53 cohorts across 5 features.
- This step is lengthy due to the number of erroneous ip address entries. By saving the clean CSV locally, this will expidite beginning any future exploration.
-----
## Data Exploration
Files used:
- explore.py

Questions Addressed:
1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
2. Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?
3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?
4. Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses?
5. At some point in 2019, the ability for students and alumni to access both curriculums (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before?
6. What topics are grads continuing to reference after graduation and into their jobs (for each program)?
7. Which lessons are least accessed? 
8. Anything else I should be aware of?

### Takeaways from exploration:
 - Data Science:
     - visits the fundamentals lesson pages the most
     - Darden cohort (59) had 3,000 more visits in the classification lesson than the other cohorts
     - Alumni reference the fundamentals lesson the most
     - visits the advanced topics and distributed-ml lessons the least with about 1,500-2,000 less visits than the next least visited lesson
 
 - Web Development:
     - visits the javascript-i lesson pages the most
     - Ceres cohort (33) had higher visit counts to html-css lesson, but the following cohorts also held higher visits to this lesson
     - Alumni reference the spring lesson the most
     - visits javascript-ii and java-i the least at about 12,000 less visits than the next least visited lesson
     
 - Access to both sets of lessons was not turned off in 2019. The last finiding of a program student accessing the other program material was in May of 2020.

### Email response
The answers to most of your questions are below, and the requested slide is attached. I was unable to answer your questions refering to suspicious activity and students with low page visit counts due to the tight deadline. With more time, I would love to look into these for you still. 

1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
- Fundamentals for data science
- Javascript-i for web dev

2. Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?
-  The Darden data science cohort had 3,000 more visits to the classification lesson than other cohorts did. This is almost twice as much as other cohorts.
- The web dev lessons were much more consistent across cohort with a small exception for Ceres visiting the html-css lesson more. This could simply be due to cohorts having different needs, and this cohort happended to have a steeper learning curve in html-css. 

5. At some point in 2019, the ability for students and alumni to access both curriculums (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before?
- There is no evidence of this shutdown happening in 2019, nor earlier. There last crossover visit I could find was a data science student visiting the web dev curriculum in May of 2020.

6. What topics are grads continuing to reference after graduation and into their jobs (for each program)?
- Alumni are coming back for the fundamentals in data science and spring in web dev. This could be a sign of possible gaps in the curriculum or shifts in industry needs.

7. Which lessons are least accessed?
- Data science students are accessing the advanced topics and distributed-ml lessons the least. They have about 1500-2000 less visits than the next least visited lesson. This could easily be due to these skills are late in the curriculum and not used in as many project over the time in the program. 
- Web dev students have javascript-ii and java-i as the least accessed; about 12000 less visits than the next least visited. With javascript-i being the most visited at over 4x the page visit count, this could be a sign the curriculum is split too heavily into the javascript-i page.

8. Anything else I should be aware of?
- I did a pull to see how site visits are trending overall by program and found there is a strong positive trend. If left unaddressed, server capabilites could be maxed out as these programs continue to grow. 

Moving forward, I believe keeping a finger on the pulse here is key. As a dynamic tech organization, we know we need to stay on top of the industry needs as they continue to progress and develop. Looking further into alumni trends could guide curriculum changes to match industry needs. Additionally, developing a dashboard to analyse live trends in student interactions with the curriculum can help us identify (and give us a timely heads-up) to address any gaps in lesson coverage or required review. 


-----
## Conclusion
The programs are highly consistent with what material is covered, and this is true very few significant variations. There is value in looking into what our alumni come back to visit, as this could be an indicator of changes in the industry. Similarly, the pages least visited might also be an indicator of contant losing relevancy in the industry.  

### Recommendations
- Adding in more time during the web development program to review spring. With it being the most referenced after graduation, it can be assumed this skill needs more dedicated time or depth in the curriculum
- Adding in a fundamentals review towards the end of the data science program may mitigate knowledge lost after graduation
- Double check that programs are officially shut down from accessing other program's pages. It does not appear the 2019 shut down occured
- Develop dashboard to update live data to visually display how current cohorts are interacting with the curriculum

### Next Steps:
- With more time, I would dig into the other vital questions asked reguarding students who rarely access the curriculum and identifying any potential threats to the online property. 
- Look into server limits as program attendance and cohort timeline overlap continues to trend upwards
- Add page classifiers such as program name or informational page in order to ease future exploration of this data

-----