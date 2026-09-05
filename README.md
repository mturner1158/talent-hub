# Project 3: Talent Hub
Talent Hub is a web application which allows a company to create a profile to uplaod job applications and applications to browse and apply for the uploaded jobs. 

## Table of Contents

TBC

## Project Goals 
This web application will allow users to upload or view job applications that are posted to the site. A user can sign up as a company or a candidate and then use the features. 

### User Goals
Users have the following goals: 
* Browse uploaded jobs 
* Upload a new job
* Submit an application 
* View the applications 

### Site Goals
Site managers have the following goals: 
* View which jobs are being posted 
* Maintain a database of companies 

## User Experience
This section shows the considerations for each type of user that would use the website and the experiences they would have.

### Target Audience 
The target audience is a user which would like to apply for a job in technology consulting or a user which would like to upload a job for the technology consultnacy. 

### Expectations 
Users of the site can expect:
* Easy to use navigation
* Clear layout
* Links to everything described
* Responsiveness to view the site on any device

### User Stories
The following users and their user stories have been considered: 

|User ID|User|Goal|Stories|
|:-----|:-------|:-------------|:-------|
|User 1|Visitor|Browse uploaded jobs anonymously|<ul><li>As a visitor, I want to see a list of active job postings so I can decide whether to register.</li><li>As a visitor, I want to view full details of a single job so I understand what's required before signing up.</li><li>As a visitor, I want to register as either a Company or a Candidate so I can access the right dashboard.</li><li>As a visitor, I want to be redirected sensibly (not a broken page) if I try to access a protected page.</li></ul>|
|User 2|Candidate|Register to the site and submit applications|<ul><li>As a candidate, I want to create a profile with my name, skills, and a short CV summary so companies can understand my background.</li><li>As a candidate, I want to edit my profile so I can keep it up to date.</li><li>As a candidate, I want to search/filter jobs by keyword, location, or job type so I can find relevant roles quickly.</li><li>As a candidate, I want to apply to a job with a short cover note so I can express my interest.</li><li>As a candidate, I want to be prevented from applying to the same job twice so my application list stays clean.</li><li>As a candidate, I want to see a list of jobs I've applied to and their current status so I can track my progress.</li><li>As a candidate, I want to withdraw an application I no longer want to pursue.</li><li>As a candidate, I want clear confirmation when my application is submitted so I know it worked.</li></ul>|
|User 3|Company|Register to the site and post jobs|<ul><li>As a company, I want to create a company profile (name, description, website) so candidates know who's hiring.</li><li>As a company, I want to post a new job listing with title, description, location, salary range, and type so candidates can evaluate it.</li><li>As a company, I want to edit or deactivate my own job listings so I can keep them current.</li><li>As a company, I want to be prevented from editing or deleting another company's job listing, for obvious data-integrity/security reasons.</li><li>As a company, I want to view all applicants for a specific job so I can review candidates.</li><li>As a company, I want to update an applicant's status (e.g. Received → Shortlisted → Rejected/Hired) so candidates know where they stand.</li><li>As a company, I want confirmation and feedback whenever I post, edit, or delete a job.</li> </ul>|
|User 4|Admin|Manage the site|<ul><li>As an admin, I want to manage all users, companies, jobs, and applications via the Django admin so I can moderate the platform if needed.</li></ul>|

## Design
This section shows the design choices I made as part of the design of this website, alongside wireframes to show the rough layout of each page before construction of the website. Through all these choices, I have considered the 5 planes of user experience to ensure a smooth and enjoyable experience for all users of the site.

### Fonts, Colours and Structure
The colour theme of this site is as follows:

|Colour|Hex Code|Description   |
|:-----|:-------|:-------------|
|Off-white|#FAF9F6|Primary Background Colour|
|Talent Hub Red|#C00000|Primary Colour|
|Muted Grey|#D9D9D9|Secondary Colour|
|Teal|#009098|Primary Accent Colour|
|Pastel Teal|#99D3D6|Secondary Accent Colour|
|Pastel Talent Hub Red|#FFD5D5|Selection Colour|
|Charcoal|#3D3D3C|Primary Text Colour|
|Grey|#8D8D8B|Border Colour|

Using this [contrast evaluator](https://coolors.co/contrast-checker/3d3d3c-faf9f6), the background colour and text colour have a contrast score of 10.33 which is rated very good, and the background colour and primary colour have a contrast score of 6.15 which is acceptible due to this being used graphically rather than for text. 

There are two fonts used through this site:

1. Hanken Grotesk will be used for headers and key text. 
2. Inter will be used for blocks of text and information.

The site will have the following pages: 

1. Job Listing page which has a paginated overview of all roles and the option to filter your search. 
2. A job details page which will show all information available and that role 
3. A company dashboard which will show you applications for a role you have posted 
4. An applicant dashboard which will allow users to see how their application is progressing (DO I NEED THIS OR SHOULD I JUST USE EMAIL)
5. A log in and account registration page to allow users to sign up in either role

### Wireframes

#### One per page TBC

## Frameworks & Languages

## Data Model
In this project, my application will utilise a PostgreSQL data base provided by the Code Instutute. I have created the following tables and provided a graphical representation of how they are connected. 

### Table 1: Users
The Users table will contain user information be created through Django authentication. 

|Data Type|Field|Key|
|:------|:-----------|:------|
|Int|id|Parent Key|
|String|username||
|String|email||
|String|password||

### Table 2: Companies
The Companies table will contain information related to the company that can be viewed by the applicants.

|Data Type|Field|Key|
|:------|:-----------|:------|
|Int|id|Parent Key|
|Int|user_id|Foreign Key|
|String|company_name||
|String|description||
|String|website||
|Image|logo||
|String|sectors||
|Date Time|created_on||

### Table 3: Jobs
The Jobs table will contain information related to each job a company has posted that can be viewed by the applicants.

|Data Type|Field|Key|
|:------|:-----------|:------|
|Int|id|Primary Key|
|Int|company_id|Foreign Key|
|String|title||
|String|description||
|String|requirements||
|String|location||
|Integer|salary_min||
|Integer|salary_max||
|Choice|job_type||
|Boolean|is_active||
|Date Time|created_on||
|Date Time|updated_on||

### Table 4: Candidates
The Candidates table will contain information related to each candidate that would apply to the job application.

|Data Type|Field|Key|
|:------|:-----------|:------|
|Int|id|Primary Key|
|Int|user_id|Foreign Key|
|String|first_name||
|String|last_name||
|String|personal_statement||
|String|skills||
|String|experience||
|Date Time|created_on||
|Date Time|updated_on||

### Table 5: Applications
The Applications table will contain information for which candidate has applied to which opportunity. 

|Data Type|Field|Key|
|:------|:-----------|:------|
|Int|id|Primary Key|
|Int|job_id|Foreign Key|
|Int|candidate_id|Foreign Key|
|String|cover_note||
|Choice|uk_working_status||
|Choice|application_status||
|Date Time|applied_on||
|Date Time|updated_on||

### Relationships
create and add the image plus a relationships table



## Features 

### Common Features 

#### One per Item TBC

### Each Page Feature 

## Testing 

### User Story Testing 

### Lighthouse Testing 

### HTML

### CSS

### JavaScript

### Django TestCase 

## Bugs
The following bugs occured during the design of this site: 

|ID|Bug|Fix   |
|:-----|:-------|:-------------|

## Deployment 

## Code from External Sources 
add packages used here 

## Credits and Disclaimer 
