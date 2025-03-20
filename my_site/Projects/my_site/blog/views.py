from django.shortcuts import render

my_blogs = {
    
    "blog1" : {
            "img" : "",
            "title" : "",
            "body" : ""
        },
    "blog2" : {
            "img" : "",
            "title" : "",
            "body" : ""
        },
}

# Create your views here.
def index(request):
    return render(request, "blog/index.html")

def posts(request):    
    return render(request, "blog/all-posts.html")

def post_detail(request, slug):
    
    slug = ""
    request_data = ""
    
    return render(request, "", {"request_data" : request_data})