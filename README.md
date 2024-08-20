# Blood of Eden Library
### A home of fan stories set in the world of Tamsyn Muir's _The Locked Tomb_ series, made for reading, commenting and rating

Blood of Eden Library is a web app aiming to entertain and inspire fan fiction enthusiasts. The theme of stories is limited to the characters and events based in the world of Tamsyn Muir's award-winning book series _The Locked Tomb_. Blood of Eden Library can be used by casual readers who just want to access the stories, or avid fans who want to create a profile and engage in conversation in the comments or rate the stories.

![Screenshot 2024-08-20 at 10 08 54](https://github.com/user-attachments/assets/c4354d7b-a4c0-4af7-8cf3-0ccad31c907d)

## Contents
- [UX and Design](https://github.com/maria-grozova/blood-of-eden-blog/edit/main/README.md#ux-and-design)
  - [Site goals](https://github.com/maria-grozova/blood-of-eden-blog/edit/main/README.md#site-goals)
  - [Target audience](https://github.com/maria-grozova/blood-of-eden-blog/edit/main/README.md#target-audience)
  - [Direction](https://github.com/maria-grozova/blood-of-eden-blog/edit/main/README.md#direction)
  - [User journeys](https://github.com/maria-grozova/blood-of-eden-blog/edit/main/README.md#user-journeys)
  - [Design choices](https://github.com/maria-grozova/blood-of-eden-blog/edit/main/README.md#site-goals)
  - [User stories](https://github.com/maria-grozova/blood-of-eden-blog/edit/main/README.md#site-goals)
  - [Wireframes](https://github.com/maria-grozova/blood-of-eden-blog/edit/main/README.md#wireframes)
  - [Database structure](https://github.com/maria-grozova/blood-of-eden-blog/edit/main/README.md#database-structure)
- [Features](https://github.com/maria-grozova/blood-of-eden-blog/edit/main/README.md#features)
  - [Existing features](https://github.com/maria-grozova/blood-of-eden-blog/edit/main/README.md#existing-features)
  - [Planned features](https://github.com/maria-grozova/blood-of-eden-blog/edit/main/README.md#planned-features)
- [Testing](https://github.com/maria-grozova/blood-of-eden-blog/edit/main/README.md#testing)
  - [Manual testing](https://github.com/maria-grozova/blood-of-eden-blog/edit/main/README.md#manual-testing)
  - [Validator testing](https://github.com/maria-grozova/blood-of-eden-blog/edit/main/README.md#validator-testing)
- [Deployment](https://github.com/maria-grozova/blood-of-eden-blog/edit/main/README.md#deployment)
  - [Live link](https://github.com/maria-grozova/blood-of-eden-blog/edit/main/README.md#live-link)
- [Resources and credits](https://github.com/maria-grozova/blood-of-eden-blog/edit/main/README.md#resources-and-credits)
  - [Content](https://github.com/maria-grozova/blood-of-eden-blog/edit/main/README.md#content)
  - [Media](https://github.com/maria-grozova/blood-of-eden-blog/edit/main/README.md#media)
  - [Code](https://github.com/maria-grozova/blood-of-eden-blog/edit/main/README.md#code)

## UX and Design
### Site goals
Our web app will let users read and rate fan stories which will affect the fans of The Locked Tomb book series by being able to feel like a part of the community and participate in the fandom. We will measure effectiveness by the user feedback, activity levels and return rates.

### Target audience
Fans of The Locked Tomb books:
- looking to connect with other fans
- looking to read more stories about their favourite characters
- wanting to share fan stories they created
- wanting to share their thoughts on fan stories

### Direction
The principles and needs that were considered.

How might we:
- make it easy for users to pick the stories they would enjoy
- allow users to set up an account
- make it easy to create, edit and delete comments/ratings
- allow users to submit their stories
- make it easy to understand the site's theme and purpose

### User journeys
![image](https://github.com/user-attachments/assets/b608b91c-e780-4eaa-bd7d-e951dfae9e0c)

### Design choices
The aim with the design choices was to slightly evoke the nostalgia feeling of the "old web" fan forums - choosing simple rectangular shapes and buttons, mono typeface and a colour scheme that both meets standards of accessibility and calls to mind that MySpace era. A design moodboard was compiled by me using Mural. In addition to this, the imagery used is both relevant to the macabre visuals of the book series and fits the theme of stories and libraries.

![Design Moodboard](https://github.com/user-attachments/assets/ba2b620c-1677-47c1-bcdb-48f0a5024af9)
![Blood of Eden Blog](https://github.com/user-attachments/assets/9cbe9bb3-9045-4777-a2ff-e08d57903081)

### User stories
I identified 16 user user stories and used the MoSCoW method to prioritise the backlog (as illustrated), ending up with 11 user stories for the MVP.
The project progress was planned and tracked using Agile, as documented here in [GitHub Project](https://github.com/users/maria-grozova/projects/6/views/1)

![Screenshot 2024-08-19 at 08 45 22](https://github.com/user-attachments/assets/cdeb2bcd-b49e-4f67-96a3-3d4fe6853e50)

<img width="1423" alt="Screenshot 2024-08-20 at 14 39 09" src="https://github.com/user-attachments/assets/98ce705b-bb5a-45ff-8a10-f21dc5c3d6fc">

### Wireframes
The wireframes were created in Balsamiq following the ideation and mapping out the user stories.
Mobile first approach was utilised, and layouts for each page were considered.
- Mobile low fidelity wireframes
![image](https://github.com/user-attachments/assets/bacd52bc-13cf-45ad-b689-bbc32fd1f2c2)

- Desktop low fidelity wireframes
![image](https://github.com/user-attachments/assets/168d542d-12b8-4e35-b49e-f72ca88db613)

- Story detail page high fidelity
![image](https://github.com/user-attachments/assets/36f53c5c-9a22-40a3-b294-01557e1eb8de)

### Database structure
The database structure is based on Code Institute's walkthrough project Codestar Blog. Below is an overview of the customisation I implemented and the relational diagram created with Lucidchart.

- User
This is a Django predefined class incorporating an username & password to log in
- Story
This is the main class, I added tags to ensure users have additional information to help them choose what they would like to read
- Comment
Related to the Story class, I added a rating integer field to allow users to rate the stories as well as comment as an additional form of engagement
- About
This class stores the information and image the admin can add and update to give users more background on Blood of Eden

![Screenshot 2024-08-20 at 09 38 08](https://github.com/user-attachments/assets/28e279a9-7b70-41b2-88bf-7ae0f9e3f0c6)

## Features
### Existing features
- Paginated list of stories ([User story](https://github.com/users/maria-grozova/projects/6?pane=issue&itemId=75118168))

A list of each published story, newest to oldest. The stories are limited to 6 per page and display the story title, author, summary, tags and date.

<img width="1418" alt="Screenshot 2024-08-20 at 14 41 18" src="https://github.com/user-attachments/assets/b4b95389-ab8b-4a17-8e2d-4d6ad2e5aed6">

- Story detail view ([User story](https://github.com/users/maria-grozova/projects/6/views/1?pane=issue&itemId=75118234))

A detailed view of the story, showing the full text and the featured image.

<img width="485" alt="Screenshot 2024-08-20 at 14 45 36" src="https://github.com/user-attachments/assets/8a4cb10a-0528-4cb7-b518-7ef5a910b29d">

- Comments and Rating display ([User Story](https://github.com/users/maria-grozova/projects/6/views/1?pane=issue&itemId=75118244))

Below each post, all approved relevant comments and ratings are displayed.

- Comments and Rating form ([User Story](https://github.com/users/maria-grozova/projects/6/views/1?pane=issue&itemId=75118286))

Below the existing comments, users can use a form to leave their comment and rating.

![Screenshot 2024-08-20 at 10 09 52](https://github.com/user-attachments/assets/d7727c74-e15a-48d3-a76e-fc997b03b93d)

- About page ([User Story](https://github.com/users/maria-grozova/projects/6/views/1?pane=issue&itemId=75118322))

A page with information about the theme and aim of the website.

<img width="1417" alt="Screenshot 2024-08-20 at 14 51 36" src="https://github.com/user-attachments/assets/44c331dd-4b07-4b82-831e-f6fc88ad13cb">

For the full list of implemented features, please refer to the [project board](https://github.com/users/maria-grozova/projects/6/views/1)

### Planned features
- [Submit stories](https://github.com/users/maria-grozova/projects/6/views/1?pane=issue&itemId=75118980)
As a Site user I can submit stories so they can be reviewed by the admin
- ["Like" comments](https://github.com/users/maria-grozova/projects/6/views/1?pane=issue&itemId=75118684)
As a Site User I can leave like comments that I agree with
- [Favourite stories](https://github.com/users/maria-grozova/projects/6/views/1?pane=issue&itemId=75118882)
As a Site User I can favourite a story so I can easily find it again
- [Add stories](https://github.com/users/maria-grozova/projects/6/views/1?pane=issue&itemId=75119009)
As a Site user I can create draft stories so that I can finish writing the content later or submit for admin approval
- [Comment chains](https://github.com/users/maria-grozova/projects/6/views/1?pane=issue&itemId=75119051)
As a Site User I can reply to comments on a story so that I can continue the conversation

## Testing
### Manual testing
Manual testing was used to check through each acceptance criteria of the implemented User Stories, and to test the responsiveness of each web app template (using Chrome Devtools). Each of these passed after a round of bug fixing.
 ![Screenshot 2024-08-20 at 15 20 26](https://github.com/user-attachments/assets/da7753f0-0f37-4783-a62f-fad6d14ce41d)

### Validator testing
- HTML
Necessary errors resolved, however there are some error messages remaining due to the content created using Django Summernote editor in the admin panel and AllAuth generating the Registration form.
<img width="783" alt="signup_validation" src="https://github.com/user-attachments/assets/ba1008ca-de7b-4c9e-ae30-93ea39137918">
<img width="1358" alt="Screenshot 2024-08-20 at 15 18 48" src="https://github.com/user-attachments/assets/4e7c36fc-f08b-432e-be3e-f380f5d61bde">

- CSS
No issues found
<img width="671" alt="Screenshot 2024-08-20 at 09 27 56" src="https://github.com/user-attachments/assets/8cf74a04-0237-48de-84a0-7809f447a799">

- JavaScript
All issues and warnings cleared
<img width="1033" alt="Screenshot 2024-08-20 at 09 27 06" src="https://github.com/user-attachments/assets/ccd36b00-3d25-4b41-a278-2d624fb2b060">

- Python
All custom Python files were tested using CI Python Linter.
All errors cleared, except for a handful of errors "Line too long", due to code generated by Django.

- Colour contrast
All text and visual input on the site meets WCAG AA standards.
![Screenshot 2024-08-20 at 13 42 54](https://github.com/user-attachments/assets/bd222056-18f2-4526-88b1-02cd069d9835)

## Deployment
- Repository created in Git
- Deployed to Heroku
- Connected Secret Keys to Config Vars
- Connected Code Institute PostGres Database
- Connected Cloudinary media storage

### Live link
https://blood-of-eden-d0985035c7c3.herokuapp.com/

## Resources and credits
### Content
- To avoid using real fan writers' IP, all currently published stories on Blood of Eden are generated by [Chat GPT](https://chatgpt.com/)

### Media
- Favicon generated using [Favicon.io](https://favicon.io/emoji-favicons/). The emoji graphics are from the open source project Twemoji. The graphics are copyright 2020 Twitter, Inc and other contributors,licensed under CC-BY 4.0.
- Hero and background images on the home page, about page and stories pages are from [Pexels](https://www.pexels.com/collections/blood-of-eden-jvmiwhg/)
- Story featured images have been generated by [Chat GPT](https://chatgpt.com/)
- [Coolors](https://coolors.co/) for generating a cohesive colour scheme
- Design moodboard
  - [Faithsweird](https://federicasasso1995.wixsite.com/faithsweird)
  - [Kelsey Michele](https://kelseymichele.crevado.com/)
  - [LogRocket](https://blog.logrocket.com/20-web-design-relics-of-the-old-internet-eb3df4ac13e7/)
  - [Type 01](https://type-01.com/best-practises-for-designing-a-mono-typeface-with-cotypes-mark-bloom/)
  - [Macmillan Publishers](https://us.macmillan.com/author/tamsynmuir)
 
### Code
- [Django Taggit](https://django-taggit.readthedocs.io/en/latest/) for tag implementation in the Story model
- Icons used from [FontAwesome](https://fontawesome.com/)
- Fonts Cousine and Rubik Mono One imported from [Google Fonts](https://fonts.google.com/)
- [Django documentation](https://docs.djangoproject.com/en/5.1/) for reference
- [W3Schools](https://www.w3schools.com/) for reference
- Code Institute - [Codestar Blog](https://learn.codeinstitute.net/) was used as a base and modified to create this project
- Special thank you to Lewis, David , Mark and Spencer at Code institute for support and tips
