from django.http import HttpResponse

def index(request):
    return HttpResponse(
        '''<h1 style="color: purple;">Hello World</h1>
        <ol>
            <li><a href="https://www.google.com" target="_blank">Google</a></li>
            <li><a href="https://www.youtube.com" target="_blank">YouTube</a></li>
            <li><a href="https://www.facebook.com" target="_blank">Facebook</a></li>
            <li><a href="https://www.instagram.com" target="_blank">Instagram</a></li>
            <li><a href="https://www.twitter.com" target="_blank">Twitter</a></li>
            <li><a href="https://www.linkedin.com" target="_blank">LinkedIn</a></li>
        </ol>
        <br>
        <a href="/about"><button>Go to About Page</button></a>
        '''
    )

def about(request):
    return HttpResponse(
        '''<h1 style="color: green;">Aboutistan</h1>
        <br>
        <a href="/"><button>Back to Home Page</button></a>
        '''
    )

