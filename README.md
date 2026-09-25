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
|User 3|Company|Register to the site and post jobs|<ul><li>As a company, I want to create a company profile (name, description, website) so candidates know who's hiring.</li><li>As a company, I want to post a new job listing with title, description, location, salary range, and type so candidates can evaluate it.</li><li>As a company, I want to edit or deactivate my own job listings so I can keep them current.</li><li>As a company, I want to be prevented from editing or deleting another company's job listing</li><li>As a company, I want to view all applicants for a specific job so I can review candidates.</li><li>As a company, I want to update an applicant's status so candidates know where they stand.</li><li>As a company, I want confirmation and feedback whenever I post, edit, or delete a job.</li> </ul>|
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
This section shows the wireframes for each page created in this web application across mobile, tablet and desktop screens. 

#### Home Page 
This page shows all job listings and is accessible without a log in. 

<img src="wireframes/home.png">

#### Job Listing 
This page shows all the details of a selected job and is accessible without a log in. 

<img src="wireframes/job-listings.png">

To select apply you will be prompted to log in if not already. When logged in, a model will auto-populate with candidate information from their profile and additional questions to fill out set by the company. 

#### Company Dashboard
This page shows all job listings for a company and applicants which have applied. 

<img src="wireframes/company-page.png">

#### Applications for a specific role 
This page shows applicants for a specific role. 

#### Candidate Dashboard 
This page shows all the roles a candidate has applied for, the status and the option to withdraw. 

<img src="wireframes/candidate-page.png">

## Frameworks & Languages
This section highlights all the languages and frameworks used in this project. 

The following languages are used in this project: 

* HTML
* CSS
* Python
* Javascript

The following frameworks are used in this project: 

* Django 6.1.1
* Bootstrap v5.3.8
* Github
* Google Fonts 
* Font Awesome 

The following packages have been used in this project, and are also listed in requirements.txt: 

* asgiref 3.12.1
* bleach 6.4.0
* dj-database-url 3.1.2
* Django 6.1.1
* django-allauth 65.19.2
* django-environ 0.14.0
* django-summernote 0.8.20.0
* gunicorn 26.2.0
* psycopg2-binary 2.9.12
* sqlparse 0.6.0
* tzdata 2026.3
* webencodings 0.6.1
* whitenoise 6.12.0

The application is deployed using Heroku. 

## Data Model
In this project, my application will utilise a PostgreSQL data base provided by the Code Instutute. I have created the following tables and provided a graphical representation of how they are connected. 

<img src="./wireframes/data-model.png">

|Table|Description|
|:------|:-----------|
|Users|The Users table will contain user information be created through Django authentication. |
|Candidates|The Candidates table will contain information related to each candidate that would apply to the job application.|
|Applications|The Applications table will contain information for which candidate has applied to which opportunity. |
|Jobs|The Jobs table will contain information related to each job a company has posted that can be viewed by the applicants.|
|Companies|The Companies table will contain information related to the company that can be viewed by the applicants.|

Relationships are shown by the lines joining the tables, with a 1 on each end meaining a one-to-one connection and a 1 and a cross on the end meaning a one-to-many connection.

## Features 
This section outlines key features on each page. 

### Common Features 
Common features appear across all pages. 

#### Navigation Bar
The navigation bar is featured on all pages and aims to apply consistant styling and positon for all users, built with responsive design. The navigation bar displays different options based on a users authentication. 

* For no authentication, users will see one option to see available jobs and the option to log in or register
* For candidates who are authenticated, they can view the job list, their applications and edit their profile. They also have the option to log out.
* For companies, they can view the available jobs and their job dashboard. They also have the option to log out.

<img src="./wireframes/nav-bar.png">

#### Footer

The footer features links to key social media sites. 

<img src="./wireframes/footer.png">

### Job List
The home page features a header with some information, followed by multiple search fields which can filter the job cards below. Each card holds key information about a role, including title, company, location and maximum salary. There is an arrow link to see more details. 

<img src="./wireframes/home-page.png">

### Job Details
Once a user has selected a job card, they will be taken to a page showing the full job listing. Each job listing has a back button to take users back to the home page, the role title, key information displayed at the top and then the full job desription. Further down the page is information about the hiring company, and where provided a link to the companies website. 

The user will also have different options available depending on their authentication and role. 

* If a user is not authenticated, there will be no options to go any further in the application. 
* If a user is authenticated as a candidate, there will be the 'Apply' button. Selecting this button will bring up a modal which will allow the user to write a cover note, select their working status and submit their application. 
* If a user is authenticated as the company which owns the job listing, they will have the option to edit the role or view applications to the role
* If a user is authenticated as a company which does not own the job listing, they will not see any buttons. 

<img src="./wireframes/job-detail-1.png">
<img src="./wireframes/job-detail-2.png">

### Company Dashboard 
The company dashboard is only available to users which are classfied as a company. The user has access to the following features: 

* A count of active jobs 
* The number of applications to their roles 
* The option to post a new job listing 
* Tiles for each role with the view to edit the role or view the applications to the role

<img src="./wireframes/company-dashboard.png">

### Job Listing Application List
The application list for a role is only available to users which are classified as a company. The user has access to the following features: 

* A list of applicants to the role 
* Further details such as their working status and the date they applied on
* A status field which is a drop down that updates the status of the application 
* A see more button per applicant which displays their full application in a modal

<img src="./wireframes/applicant-table.png">

### Applicant Dashboard 
The applicant dashboard is only availablto users which are classified as a candidate. The user has access to the following features: 

* A view of all roles the user has applied to
* The status of the users application 
* The date the user applied to the job listing 
* A link to view the job listing 
* The option to withdraw their application

<img src="./wireframes/candidate-dashbaord.png">

### Edit Forms
All edit forms across the project follow a similar format, with summernote used for rich text inputs. 

* Candidate users will be able to access the edit profile form to update their skills
* Company users will be able to access the edit profile form and the edit / post a job form

<img src="./wireframes/edit-form.png">

### Authentication 
Modifying allauth's base templates, there are signup, sign in and log out pages matching the style of this web application.

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

* auth additional question was not working and adding data to the database. Needed to update logic and fix a typo in the model
* back button pathing from job page erroring. All urls needed distinct names
* could not submit a job application. Set account as a forein key rather than a one to one field to ensure django expects a unique value

## Deployment 

## Code from External Sources 
add packages used here 

## Credits and Disclaimer 
