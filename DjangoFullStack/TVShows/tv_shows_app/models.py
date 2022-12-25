from django.db import models
from datetime import datetime

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = 'Title should be at least 2 characters.'
        title_list = []
        for _dict in Show.objects.all().values('title'):
            title_list.append(_dict['title'])
        if postData['title'] in title_list:
            errors['unique-title'] = 'This title already exists.' # for show in Show.objects.all(): --> if show.title == postData['title']: --> line 14
        if len(postData['network']) < 3:
            errors['network'] = 'Network should be at least 3 characters.'
        if len(postData['description']) in range(2, 10):
            errors['description'] = 'Description should be at least 10 characters.'
        # if len(postData['release-date']) < 10:
        #     errors['release-date'] = 'Release date is required.'
        # if datetime.strptime(postData['release-date'], "%Y-%m-%d").date() > datetime.now().date():
        #     errors['past'] = 'Release date cannot be in the future!'
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

def showAllTVshows():
    return Show.objects.all()

def createTVShow(request):
    if request.POST['release-date']:
        Show.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date = request.POST['release-date'],
            description=request.POST['description']
        )
    else:
        Show.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date = None,
            description=request.POST['description']
        )

def showLastTVShow():
    return Show.objects.last()

def getTVShow(id):
    return Show.objects.get(id=id)

def updateTVShow(request):
    show = Show.objects.get(id=request.POST['showId'])
    show.title = request.POST['title']
    show.network = request.POST['network']
    show.release_date = request.POST['release-date']
    show.description = request.POST['description']
    show.save()

def deleteTVShow(id):
    TVShow = Show.objects.get(id = id)
    TVShow.delete()