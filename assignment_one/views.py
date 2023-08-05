from django.http import HttpResponse

def home(request):
    return HttpResponse('''
                        <h1> Click the link below for Menu </h1>
                        <a href = 'my_app/menu/'>Menu</a>
                        
                        ''')