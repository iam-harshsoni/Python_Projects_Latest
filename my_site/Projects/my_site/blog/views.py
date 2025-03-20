from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "climbing-new-heights",
        "image": "mountains.jpg",
        "author": "Harsh Soni",
        "date": date(2024,1,8),
        "title": "Climbing New Heights",
        "excert": "A journey of perseverance and determination while scaling new peaks.",
        "content": "Mountain climbing is not just about reaching the summit; it's about the journey, the struggles, and the mindset required to overcome obstacles. Recently, I embarked on a trekking adventure to the Himalayas, and the experience was beyond words. The thin air made every step a challenge, but with every altitude gain, the breathtaking views made it all worthwhile. Standing at the peak, I realized that every challenge in life can be conquered with persistence and the right strategy. If you ever get a chance, climb a mountain—not just to reach the top, but to discover yourself along the way."
    },
    {
        "slug": "code-and-coffee",
        "image": "coding.jpg",
        "author": "Harsh Soni",
        "date": date(2024,2,20),
        "title": "Code and Coffee",
        "excert": "How coffee fuels programmers and enhances productivity.",
        "content": "For many developers, coffee is not just a beverage; it's a ritual. The moment you take that first sip, the caffeine kickstarts your brain, making coding sessions more productive. I remember working on a complex backend system at 2 AM, with only a cup of espresso keeping me company. Studies have shown that moderate caffeine consumption enhances focus and alertness, making it a great companion for programmers. However, balance is key—too much caffeine can lead to crashes. So, the next time you're stuck on a bug, take a sip, take a break, and let the solution come to you naturally."
    },
    {
        "slug": "nature-walk",
        "image": "woods.jpg",
        "author": "Harsh Soni",
        "date": date(2024,3,5),
        "title": "Nature Walk",
        "excert": "The rejuvenating experience of walking through a quiet forest.",
        "content": "Walking through a dense forest early in the morning is a surreal experience. The chirping of birds, the scent of fresh earth, and the sight of dew-covered leaves create a sense of peace rarely found in urban life. Recently, I took a short trip to a nearby forest reserve, and for the first time in a long while, I disconnected from technology and just observed nature. Studies suggest that spending time in nature reduces stress and improves mental clarity. If you're feeling overwhelmed, take a break, step outside, and let nature heal you."
    },
    {
        "slug": "coding-marathon",
        "image": "coding.jpg",
        "author": "Harsh Soni",
        "date": date(2023,6,3),
        "title": "Coding Marathon",
        "excert": "A deep dive into the world of coding marathons and their impact on developers.",
        "content": "Hackathons and coding marathons push developers beyond their limits. Recently, I participated in a 48-hour coding marathon, and the experience was exhilarating. The pressure to build a working prototype within a strict deadline forces creativity and teamwork. While caffeine and adrenaline kept us awake, it was the passion for coding that drove us to the finish line. If you're a developer, I highly recommend participating in hackathons—it not only sharpens your skills but also introduces you to amazing like-minded people."
    },
    {
        "slug": "summit-success",
        "image": "mountains.jpg",
        "author": "Harsh Soni",
        "date": date(2024,3,18),
        "title": "Summit Success",
        "excert": "Reaching the summit and reflecting on the journey of challenges and growth.",
        "content": "Every summit conquered is a personal victory. A few months ago, I decided to challenge myself with a solo trek to a peak I had never attempted before. The climb was physically exhausting, and at times, I questioned whether I should turn back. But the moment I reached the top, all the struggles felt worth it. The journey reminded me that success is not about taking shortcuts; it's about resilience, effort, and enjoying the climb. Whether it's a career goal or a life goal, keep climbing—success is waiting for you at the top."
    }
]

#helper function to get the date
def get_date(post):
    print(f"Calling get_date with: {post}") 
    return post['date']

# Create your views here.

def index(request):
    
    sorted_post = sorted(all_posts, key=get_date)
    latest_post = sorted_post[-3:]

    return render(request, "blog/index.html", {"posts": latest_post})


def posts(request):
   
    return render(request, "blog/all-posts.html", {"all_posts" : all_posts})


def post_detail(request, slug):

    for post in all_posts:
        if post['slug'] == slug:
            request_data = post
            
    # ********** OR *************
    """ More efficient than For loop above as 
        Forloop: ( Disadvantages )
            - Inefficient because it keeps looping even after finding a match.
            - if post is not found, request_data might be undefined, causing issues.
        
        next(): (Advantages ✅)
            - More efficient since it stops searching after finding the first match.
            - Shorter and cleaner code.
    
    """

    # Raises StopIteration error if no match is found (unless a default value is provided).
    # Safer to provide defaul value as 'None' at the end to This prevents errors by returning None if no matching post is found.
    
    request_data = next((post for post in all_posts if post["slug"] == slug), None)

    return render(request, "blog/post-detail.html", {"post": request_data})