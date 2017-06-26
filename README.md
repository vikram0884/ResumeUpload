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

    1. Go to the project path, use the below command:

       usrname@My-PC:~/ResumeUpload$ python set_env.py
       ...
       ...
       ...

       [Will ask for user details for user creation]

       Performing system checks...

       System check identified no issues (0 silenced).
       June 19, 2017 - 03:02:49
       Django version 1.10.5, using settings 'FileUploads.settings'
       Starting development server at http://127.0.0.1:8000/
       Quit the server with CONTROL-C.

    2. Open Browser as applicant using http://localhost:8000/upload/ and upload the application as you please.

    3. Open Browser as ADMIN using http://localhost:8000/su/login/
       After successfull login, ADMIN is taken to list page where he/she can do all of their tasks appropriately.






