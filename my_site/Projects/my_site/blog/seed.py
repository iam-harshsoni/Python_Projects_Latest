
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
            random_author = random.choice(author_obj)
            
            tag_obj = list(Tag.objects.all())
            random_tag = random.choice(tag_obj)
            
            author = random_author
            title = fake.sentence(nb_words=3)
            tags = tag_obj
            excert = fake.sentence(nb_words=20)
            image_name = random.choice(images)
            date = fake.date()
            content = fake.sentence(nb_words=100)
            
            Post.objects.create(
                author = author,
                title = title,
                tags = tag_obj,
                excert = excert,
                image_name = image_name,
                date = date,
                content = content,
            )
        
    except Exception as e:
        print(e)
        
def update_post():
    try:
        tag_obj = list(Tag.objects.all())
        random_tag = random.choice(tag_obj)
        
        posts = list(Post.objects.all())
        
        for post in posts:
            post.tags.set([random_tag])
            
            post.save()
            
    except Exception as e:
        print(e)