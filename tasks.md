# Task - 12

1. deploy it live

# Task 11

1. Done - Set up stripe
2. Done - install stripe
3. Done - run the stripe cli
4. Done - create api functions for stripe
5. Done - update the plan page view
6. Done - create the thank-you page
7. Done - show current plan on team page
8. Done - make it possible to cancel a plan
9. script for checking active subscriptions

``` 
stripe listen --forward-to localhost:8000/dashboard/myaccount/teams/api/stripe_webhooks/

```

# Task 10

1. Done - Create new model for plans and update the team model
2. Done - Create new page for showing plans
3. Done - Add plans to database
4. Done - Change project.html file to implement limits
5. Done - Change projects.html file to implement limits
6. Done - Change invite.html file to implement limits

# Task 9

1. Done - Make a globally available active entry function
2. Done - Add buttons in the menu for tracking time
3. Done - Create api functions for starting, stopping and discarding time
4. Done - Create Vue functionality for starting and stopping time
5. Done - Add modal for choosing what to do
6. Show untracked entries on dashboard
7. Make it possible to delete untracked entries
8. Make it possible to track untracked entries

# Task 8

1. Done - Add avatars to users
2. Done - create new view and template for showing a user
3. Done - Show what a user has done a certain time
4. Done - Show what a user has done a certain month

# Task 7

1. Done - Create new module for invites
2. Done - Get credentials for sendgrid (or a smtp server)
3. Done - Create helper functions for sending emails
4. Done - Set up email templates
5. Done - Create view and template for sending invites
6. Done - show list of invited members
7. Done - check for invitation when you sign up
8. View and template for accepting invite
9. Show your invitations on your account page

## details

```
EMAIL_HOST='smpt.sendgrid.net'
EMAIL_HOST_USER='apikey'
EMAIL_HOST_PASSWORD=''
EMAIL_PORT=587
EMAIL_USE_TLS=true
DEFAULT_EMAIL_FROM='Minutos <admin@example.com>'
ACCEPTATION_URL='http://localhsot:8000/signup'
```

# Task 6

1. Done - Create a new app for dashboard
2. Done - Create a new url file for dashboard
    1. Done - Include the files for user profile, project and team here
3. Done - Show what I have done today and make it possible to go back in time
4. Done - Show what I have done this month and make it possible to go back in time
5. Done - Show what my team has done this month and make it possible to go back in time
6. Done - format minutes
7. Done - Show the newest project at the bottom

# Task 5

1. Done - Add status to tasks
2. Done - show the status together with the task title
3. Done - fix typos
4. Done - show numbers of tasks in project
5. Done - create a new model for entries
6. Done - make it possible to register entries on task
7. Done - fix the registers time function son project and task
8. Done - show entries on a task
9. Done - show total time on the task list
10. Done - Make it possible to edit an entry
11. Make it possible to delete an entry
12. Import font awesome and add icons

# Task 4

1. Fix small things
    1. Done - Add color to navigation bar
    2. Done - Show user profile in admin area
2. Done - Create new app, models for projects
3. Done - Show a list of projects (Model for adding projects)
4. Done - Show detail view of a project
5. Done - Make it possible to edit projects
6. Done - Create models for tasks
7. Done - Show a list of Tasks
8. Done - Make it possible to add tasks
9. Done - Show detail view of a task
10. Done - Make it possible to edit tasks

# Tasks 3

1. Fix small changes from previous tasks
    1. Done - Move sign up view to core app
    2. Done - move templates to the core app (update urls.py)
    3. Done - Add the links/info below signup and login form
    4. Done - Show username in my account button
    5. Done - Hide the plans link in the menu
2. Done - Create a new django app for teams
3. Done - Create a view and template for adding teams
4. Done - Show your teams on account page
5. Done - Make it possible to view a team
6. Done - Make it possible to edit a team

# Tasks 2

1. Done - Create a new django app for user profiles
2. Done - Create view and template for sign up page
3. Done - create template for login
4. Done - create a simple my account page
5. Done - make it possible to logout
6. Done - make it possible to edit user profile

# Tasks 1

1. Done - Create a venv and activate it.
2. Done - Install django and create an empty project
3. Done - Initialize the database and create superuser
4. Done - start dev server and test. also, login to admin
5. Done - create a django app for core views (front page, privacy policy, etc)
6. Done - Create base template files
7. Done - Create the front page
8. Done - create a simple privacy policy and toc
9. Done - create a page to show different pricing plans
