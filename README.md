# MonthEndClose

## Prerequisites
1. python 3+
1. git
1. pip
    1. django
    1. crispy forms
    1. django rest
    ```

    pip install --upgrade django-crispy-forms pandas djangorestframework markdown django notifications
    pip install django-notifications-hq
    ```

## Windows setup
1. Install git - https://gitforwindows.org/

1. Open a windows command prompt (tip: search for CMD in windows search)

1. Utilize the "cd" command to navigate to where you want to download (i.e.: clone) the project/code to. 
    ```
    (i.e.: type the following into the command prompt "cd C:\Users\Dylan\CloneTest\").
    ```

Note: cd brings the command prompt to the directory specified

1. Type the following into the command prompt 
    ```
    git clone https://gitlab.com/dylan1218/monthendclose.git
    ```

Note: You may receive a popup requesting you log into gitlab.

Note2: Once this is completed you will have downloaded the project to the directory specified in (3)

1. perform another cd into the monthendclose folder (i.e.: type the following into the command prompt 
    ```
    cd C:\<path to clone dir>\monthendclose
    ```

1. Type the following into the command prompt 
    ```
    python manage.py runserver
    ```

Note: you'll need to have python installed for this step

## Accessing the site once the server is running

1. Open a web broswer and go to "http://127.0.0.1:8000/ClosePortal/Task_Checklist/"

note: refer to the admin panel at http://127.0.0.1:8000/admin

login: admin_brian

password: password

1. added permission test user 

login: noperm
password: N0Perm1234