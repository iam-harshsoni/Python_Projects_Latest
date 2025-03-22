import random
from faker import Faker
from .models import Author, Post, Tag

fake = Faker()  # Initialize Faker for generating fake data

def generate_author(n=1):
    """
    Function to generate and create 'n' random authors.

    - Uses Faker to generate a random first name, last name, and email.
    - Saves the generated author to the database.
    - Handles exceptions and prints errors if any occur.
    """
    try:
        for _ in range(n):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()

            Author.objects.create(
                first_name=first_name,
                last_name=last_name,
                email_address=email
            )

    except Exception as e:
        print(e)  # Print error for debugging


def generate_post(n=1):
    """
    Function to generate and create 'n' random blog posts.

    - Selects a random author from the database.
    - Selects random tags from the Tag model.
    - Generates fake title, excerpt, content, and date using Faker.
    - Randomly assigns an image from a predefined list.
    - Saves the post to the database.
    - Handles exceptions and prints errors if any occur.
    """
    try:
        for _ in range(n):        
            images = ["mountains.jpg", "woods.jpg", "coding.jpg"]  # Predefined image list
            
            # Select a random author from existing authors
            author_obj = list(Author.objects.all())
            random_author = random.choice(author_obj)
            
            # Select random tags from existing tags
            tag_obj = list(Tag.objects.all())
            random_tag = random.choice(tag_obj)
            
            title = fake.sentence(nb_words=3)  # Generate a random title
            excert = fake.sentence(nb_words=20)  # Generate a random excerpt
            image_name = random.choice(images)  # Choose a random image
            date = fake.date()  # Generate a random date
            content = fake.sentence(nb_words=100)  # Generate random content
            
            # Create and save the post
            post = Post.objects.create(
                author=random_author,
                title=title,
                excert=excert,
                image_name=image_name,
                date=date,
                content=content,
            )

            # Set tags for the post after creation (Many-to-Many relationship)
            post.tags.set(tag_obj)

    except Exception as e:
        print(e)  # Print error for debugging


def update_post():
    """
    Function to update all posts by assigning a random tag.

    - Fetches all available tags and selects one randomly.
    - Assigns the selected tag to all posts using the `set()` method.
    - Saves the updated post data.
    - Handles exceptions and prints errors if any occur.
    """
    try:
        tag_obj = list(Tag.objects.all())  # Fetch all tags
        random_tag = random.choice(tag_obj)  # Select a random tag
        
        posts = list(Post.objects.all())  # Fetch all posts
        
        for post in posts:
            post.tags.set([random_tag])  # Assign the selected tag to the post
            post.save()  # Save the updated post

    except Exception as e:
        print(e)  # Print error for debugging
