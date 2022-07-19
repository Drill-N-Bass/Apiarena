from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	print("args, kwargs: ", args, kwargs) # checking args and kwargs in console
	print("User's name that is log in now is: ", request.user) # checking username that is log in (in console)
	# return HttpResponse("<h1>Hello World</h1>") # string of HTML code
	return render(request, "home.html", {})

def contact(request, *args, **kwargs):
	print("args, kwargs: ", args, kwargs) # checking args and kwargs in console
	print("User's name that is log in now is: ", request.user) # checking username that is log in (in console)
	# return HttpResponse("<h1>Apiarena contact details</h1>")

	my_context = {
	'my_text' : "this is about me",
	'my_number' : 123,
	'my_list' : [123, 4566, 766, 7777, 7779],
	'test_apiarena' : """<div class="single-about-us">
								<div class="about-us-txt">
									<h2>About us</h2>
									<p>
										We are innovative international distributor with years
										of experience in the video games industry.
										We have connections to dozens of reliable suppliers,
										ensuring timely delivery at a competitive price.
										We welcome new business partners to start a cooperation
										with us.
									</p>

								</div><!--/.about-us-txt-->
							</div>"""
	}

	return render(request, "contact.html", my_context)
 	


	################
	#Pytanie na stack overflow:

	# how can I migrate CSS webpage into Django?

# I'm developing my Django skills and getting to a point when I need to convert a CSS webpage to be able to load it with Django. I need some guidance on what's needed step by step to do so. I don't have CSS experience. 

# I know that I can use `wget`:

# ```wget --page-requisites http://example.com/your/page.html```

# to download whole page. Or, I can use [HTTrack](http://www.httrack.com/) 