ResumeUpload
------------

    ResumeUpload allow applicants to submit his/her resume in any valid file format
    which will be proccessed by ADMIN. This project allows the ADMIN to view the resume 
    and to approve or reject the application.

    For Applicant:
       1. Hit upload page(http://localhost:8000/upload) and upload the file.

    For ADMIN:
       1. Hit login page(http://localhost:8000/su/login) after successfull login, it redirects 
          to list page.
       2. In the list page(http://localhost:8000/su/list), the list of applications submitted 
          by the applicants are ready to get VIEWED or APPROVED or REJECTED.
 

Set Env & Deploy:
-----------------

    1. To run for first time, we need to setup the environment and use the below command

       usrname@My-PC:~/ResumeUpload$ python run.py setup_env

           This will accomplish the following:
               1. Dependency checks
               2. Root DB credentials
               3. DB User to create
               4. DB Connection creation
               5. db creation for the app
               6. DB User creation & permissions
               7. DB Config file creation
               8. Create admin user

    2. To run for the first time and to start the site, use the below command

       usrname@My-PC:~/ResumeUpload$ python run.py all

           This will accomplish the following:
               1. Dependency checks
               2. Root DB credentials
               3. DB User to create
               4. DB Connection creation
               5. db creation for the app
               6. DB User creation & permissions
               7. DB Config file creation
               8. Create admin user
               9. Migrate changes and start the site

    3. To start the site, use the below command

       usrname@My-PC:~/ResumeUpload$ python run.py start_app

           Starting the site ... 

           No changes detected
           Operations to perform:
             Apply all migrations: admin, auth, contenttypes, sessions, su
           Running migrations:
             No migrations to apply.
           Performing system checks...

           System check identified no issues (0 silenced).
           June 27, 2017 - 06:45:08
           Django version 1.10.5, using settings 'ResumeUpload.settings'
           Starting development server at http://127.0.0.1:8000/
           Quit the server with CONTROL-C.

    4. Open Browser as applicant using http://localhost:8000/upload/ and upload the application as you please.

    5. Open Browser as ADMIN using http://localhost:8000/su/login/
       After successfull login, ADMIN is taken to list page where he/she can do all of their tasks appropriately.






