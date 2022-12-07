To Start
py manage.py runserver

To Migrate DB
py manage.py migrate

To Migrate Updated DB (For DjangoApp)
py manage.py makemigrations

To Create Directory (DjangoApp)
py manage.py startapp {nama-directory}

To Create Superuser
py manage.py createsuperuser

To Open Interactive Shell
py manage.py shell

To insert data to DB using Shell
#articles-> AppName
#Article-> Model name
from articles.models import Article
#To Check if Article have input
Article.objects.all()
#To insert Data 
article=Article()
#insert Article title
article.title='Hello,World'
#to save
article.save()
#to Check
Article.objects.all()[0].title

Models in py are a class which represent a table in DB
Each Type of data we have is represented by it's own model
Each model maps to a single table in DB

Ex:
Code
class Article():
	title= models.CharField()
	body= models.TextField()

DB Articles
id	| title		| body
1	| blah		| blah blah blah
2	| blah2		| blah blah blah
3	| blah3		| blah blah blah

{%%}-> Template text for python but no output
{{}}-> template for py for output
