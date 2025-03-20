from django.shortcuts import render
from datetime import date
my_blogs = [
    {
        "slug" : "hike-in-the-mountain",
        "image" : "mountains.jpg",
        "author" : "Harsh Soni",
        "date" : date(2021,7,21),
        "title" : "Mountain Hiking",
        "excert" : "There's nothing like the views you get when hiking in the mountains!And I wasn't even perpared for what happened whilst I was enjoing the view.",
        "content" : """
            Lorem ipsum dolor sit, amet consectetur adipisicing elit. At vel, quidem officiis rem similique aut, cum quam laboriosam consequatur aperiam ullam delectus consequuntur vero natus accusamus exercitationem impedit excepturi sapiente?
            Lorem ipsum dolor sit, amet consectetur adipisicing elit. At vel, quidem officiis rem similique aut, cum quam laboriosam consequatur aperiam ullam delectus consequuntur vero natus accusamus exercitationem impedit excepturi sapiente?
            Lorem ipsum dolor sit, amet consectetur adipisicing elit. At vel, quidem officiis rem similique aut, cum quam laboriosam consequatur aperiam ullam delectus consequuntur vero natus accusamus exercitationem impedit excepturi sapiente?
            Lorem ipsum dolor sit, amet consectetur adipisicing elit. At vel, quidem officiis rem similique aut, cum quam laboriosam consequatur aperiam ullam delectus consequuntur vero natus accusamus exercitationem impedit excepturi sapiente?       
        """
    },
    {
        "slug" : "progarmming-is-fun",
        "image" : "coding.jpg",
        "author" : "Harsh Soni",
        "date" : date(2022,3,10),
        "title" : "Programming is Great",
        "excert" : "Discover the joy of coding and unlock a world of creativity and problem-solving. In this article, we'll explore what makes programming so great, from the thrill of building something from scratch to the satisfaction of overcoming complex challenges.",
        "content" : """
            Lorem ipsum dolor sit, amet consectetur adipisicing elit. At vel, quidem officiis rem similique aut, cum quam laboriosam consequatur aperiam ullam delectus consequuntur vero natus accusamus exercitationem impedit excepturi sapiente?
            Lorem ipsum dolor sit, amet consectetur adipisicing elit. At vel, quidem officiis rem similique aut, cum quam laboriosam consequatur aperiam ullam delectus consequuntur vero natus accusamus exercitationem impedit excepturi sapiente?
            Lorem ipsum dolor sit, amet consectetur adipisicing elit. At vel, quidem officiis rem similique aut, cum quam laboriosam consequatur aperiam ullam delectus consequuntur vero natus accusamus exercitationem impedit excepturi sapiente?
            Lorem ipsum dolor sit, amet consectetur adipisicing elit. At vel, quidem officiis rem similique aut, cum quam laboriosam consequatur aperiam ullam delectus consequuntur vero natus accusamus exercitationem impedit excepturi sapiente?       
        """
    },
    {
        "slug" : "into-the-woods",
        "image" : "woods.jpg",
        "author" : "Harsh Soni",
        "date" : date(2020,8,5),
        "title" : "Programming is Great",
        "excert" : "Take a journey with us into the heart of the woods, where nature's beauty and wonder await. In this article, we'll explore the magic of the forest, from the towering trees to the creatures that call it home.",
        "content" : """
            Lorem ipsum dolor sit, amet consectetur adipisicing elit. At vel, quidem officiis rem similique aut, cum quam laboriosam consequatur aperiam ullam delectus consequuntur vero natus accusamus exercitationem impedit excepturi sapiente?
            Lorem ipsum dolor sit, amet consectetur adipisicing elit. At vel, quidem officiis rem similique aut, cum quam laboriosam consequatur aperiam ullam delectus consequuntur vero natus accusamus exercitationem impedit excepturi sapiente?
            Lorem ipsum dolor sit, amet consectetur adipisicing elit. At vel, quidem officiis rem similique aut, cum quam laboriosam consequatur aperiam ullam delectus consequuntur vero natus accusamus exercitationem impedit excepturi sapiente?
            Lorem ipsum dolor sit, amet consectetur adipisicing elit. At vel, quidem officiis rem similique aut, cum quam laboriosam consequatur aperiam ullam delectus consequuntur vero natus accusamus exercitationem impedit excepturi sapiente?       
        """
    },
]

# Create your views here.
def index(request):
    return render(request, "blog/index.html")

def posts(request):    
    return render(request, "blog/all-posts.html")

def post_detail(request, slug):
    
    slug = slug
    request_data = slug
    
    return render(request, "blog/post-detail.html", {"request_data" : request_data})