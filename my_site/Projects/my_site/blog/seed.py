
from faker import Faker
from .models import Author,Tag,Post
import random

fake = Faker()

def generate_author(n=1):
    try:
        for _ in range(n):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()
            
            Author.objects.create(
                first_name = first_name,
                last_name = last_name,
                email_address= email 
            )
               
    except Exception as e:
        print(e)

def generate_post(n=1):
        
    try:   
        for _ in range(n):        
            images = ["mountains.jpg","woods.jpg","coding.jpg"]
            
            author_obj = list(Author.objects.all())
            # random_author = author_obj[random.randint(0,len(author_obj)-1)]
            random_author = random.choice(author_obj)
            
            author = random_author
            title = fake.sentence(nb_words=3)
            excert = fake.sentence(nb_words=20)
            image_name = random.choice(images)
            date = fake.date()
            content = fake.sentence(nb_words=100)
            
            Post.objects.create(
                author = author,
                title = title,
                excert = excert,
                image_name = image_name,
                date = date,
                content = content,
            )
        
    except Exception as e:
        print(e)