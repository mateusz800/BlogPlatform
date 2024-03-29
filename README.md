[![BCH compliance](https://bettercodehub.com/edge/badge/mateusz800/stories?branch=master)](https://bettercodehub.com/)
<br/><br/>
A website that allows registered user to create stories and make them visible to everyone.
<div style="display:flex;">
<img style='float:left align-self:flex-start' width='49%' src='https://user-images.githubusercontent.com/44299056/78504852-d6f9ed00-776f-11ea-9dbb-c55a5bd4423e.png'/>
<img style='float:left' width='49%' src='https://user-images.githubusercontent.com/44299056/78504894-2809e100-7770-11ea-917a-8647536f634a.png'/>
</div>
 <img src='https://user-images.githubusercontent.com/44299056/78504800-94381500-776f-11ea-9ab3-ead3481b34aa.png'/>

### Documentation
Frontend:
 https://mateusz800.github.io/stories/

### Running project
1. Clonning project ```git clone https://github.com/mateusz800/blog```
2. ``` cd ``` into project folder
3. Creating virtual environment ```python -m venv venv```
4. Activating venv ```source venv/bin/activate```
5. Installing dependencies ``` pip install -r requirements.txt ```
6. Changing settings.py (email server credentials)
7. Migrating the database 

```bash
python manage.py makemigrations
python manage.py migrate
```
8. Starting server ```python manage.py runserver```

**or by docker**
1. Update settings.py (email server credentials)
2. ```docker-compose up -d```


The application will run on ```127.0.0.1:80000```


Steps that you have to follow if you want to edit frontend
1. cd frontend
2. yarn install
3. npm run dev
