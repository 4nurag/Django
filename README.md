### Summary: Creating a Poll App with Django

1. **Setup**:
   - Install Django: `pip install django`.
   - Create a new project: `django-admin startproject pollster_project`.
   - Create a new app: `python manage.py startapp polls`.

2. **Define Models**:
   - In `polls/models.py`, create `Question` and `Choice` models:
     ```python
     class Question(models.Model):
         question_text = models.CharField(max_length=200)
         pub_date = models.DateTimeField('date published')

     class Choice(models.Model):
         question = models.ForeignKey(Question, on_delete=models.CASCADE)
         choice_text = models.CharField(max_length=200)
         votes = models.IntegerField(default=0)
     ```

3. **Database Migration**:
   - Run migrations: 
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

4. **Create Views**:
   - In `polls/views.py`, define views for displaying questions and handling votes.

5. **Setup URLs**:
   - Create `polls/urls.py` to map URLs to views and include it in the main project’s `urls.py`.

6. **Run the App**:
   - Start the development server: `python manage.py runserver`.
   - Access the app at `http://127.0.0.1:8000/polls/`.

This concise guide outlines the essential steps to build a Poll App using Django, from setup to deployment.


![Screenshot from 2024-08-01 11-32-28](https://github.com/user-attachments/assets/4c463c63-af86-4b26-a273-c676dec1c7ff)


![Screenshot from 2024-08-01 11-32-45](https://github.com/user-attachments/assets/7fe48503-fe3f-4a83-857a-4ad467226e2c)

