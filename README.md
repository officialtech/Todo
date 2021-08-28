# Todo

## This is an ASANA API based Django fully loaded web app, where you can perform CURD operation in ASANA from django webapp.

![OfficialTech](https://user-images.githubusercontent.com/46815338/131124790-d7351745-0913-46eb-b5f7-b5fdfe3acec6.png)


1. clone repository from here [TODO](https://github.com/officialtech/Todo)
2. go inside directory where *manage.py* file is located or inside *TODO*
3. now you can install *requirements.txt*
``` pip install -r requirements.txt ```
4. if you want to create virtualenv you can create that and than pip install requirements, after that activate virtualenv and fire your development server
5. else now going from 3 step you can fire your development server
``` python manage.py runserver ```


## For using ASANA API you have to sign in and get
you can visit here [ASANA](https://app.asana.com)
```
ACCESS_TOKEN
CLIENT_ID
```
and you have to find your workspace gid and assignee, in the way what i worked on it, it will dynamic when there is more than one assignee and workspace
> put all the details in utils.py and settings.py where i mentioned all the above fields because till my * Access token and client id * will may or may not be work


# Proof of concept
https://user-images.githubusercontent.com/46815338/131211203-4c1cdb4e-0c65-4554-b95e-812654f6c7d8.mp4


