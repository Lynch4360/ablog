from django.db import models
# we want to be able to connect to that superuser we created and use it in our model
from django.contrib.auth.models import User
# this is for blog posts


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # next we just define things we want in our blog, we define that right here
    # the foreign key is from the superuser,
    # if we create something like 10 blog posts and then later on we delete the user admin,
    # this will delete the admin blogposts it will CASCADE and delete them all
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    # this will allow our admin page to see the title and the author.
    # rather than a string of weird numbers
