# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.conf import settings
# from django.contrib.auth.decorators import login_required
# import facebook
# # Create your views here.
# def get_facebook_login_url():
#     # Create the Facebook login URL
#     redirect_uri = 'http%3A%2F%2Flocalhost%3A8000%2Ffacebook%2Flogin'  
#     graph = facebook.GraphAPI()
#     login_url = graph.get_auth_url(settings.FACEBOOK_APP_ID, redirect_uri, scope=['user_posts'])
#     return login_url

# def facebookLogin(request):
#     code = request.GET.get("code")
#     print(code)

#     if code:
#         # Initialize the Facebook Graph API with your app credentials
#         graph = facebook.GraphAPI()

#         # Exchange the code for a user access token
#         access_token_info = graph.get_access_token_from_code(code, 'fbHome', settings.FACEBOOK_APP_ID, settings.FACEBOOK_APP_SECRET)

#         # Fetch user data using the obtained access token
#         user_data = graph.get_object('me', access_token=access_token_info['access_token'])

#         # Store user_data in your database or use it as needed
#         # Example: user_id = user_data['id']

#         # Log in the user using Django's authentication system
#         user = login(request, user_data['id'])
#         return redirect('home')
#     else:
#         redirect_url = get_facebook_login_url()
#         return redirect(redirect_url)


# def facebookHome(request):
#     return render(request, 'facebookHome.html')





from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.contrib.auth.decorators import login_required
from urllib.parse import quote
import facebook

def get_facebook_login_url():
    # Properly URL-encode the redirect_uri
    redirect_uri = quote('http://localhost:8000/facebook/login')
    graph = facebook.GraphAPI()
    login_url = graph.get_auth_url(settings.FACEBOOK_APP_ID, redirect_uri, scope=['user_posts'])
    
    return login_url

def facebookLogin(request):
    code = request.GET.get("code")
    print("code",code)
    if code:
        # Initialize the Facebook Graph API with your app credentials
        graph = facebook.GraphAPI()

        # Exchange the code for a user access token
        # Use the same redirect_uri as in get_auth_url
        redirect_uri = 'http://localhost:8000/facebook/login'
        access_token_info = graph.get_access_token_from_code(code, redirect_uri, settings.FACEBOOK_APP_ID, settings.FACEBOOK_APP_SECRET)

        # Fetch user data using the obtained access token
        user_data = graph.get_object('me', access_token=access_token_info['access_token'])

        # Authenticate the user
        user = authenticate(request, username=user_data['id'])

        if user:
            login(request, user)
            return redirect('home')
        else:
            # Handle the case where the user doesn't exist (you may want to create a new user here)
            return render(request, 'error.html', {'message': 'User not found'})
    else:
        redirect_url = get_facebook_login_url()
        print(redirect_url)
        return redirect(redirect_url)

@login_required
def facebookHome(request):
    return render(request, 'facebookHome.html')
