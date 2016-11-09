from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class BookStore(models.Model):
    """
    Book Model 

    Fields (title, author, category, date_created and date_updated)
    
    """
    category_choices = (
        ('art','Art'),
        ('nature','Nature'),
        ('history','History'),
        ('music','Music'),
    )
    title = models.CharField(max_length=270)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=category_choices)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        # Support Python 3 for object represantation
        return "{}".format(self.title)

    def __unicode__(self):
        # Support Python 2 for object represantation
        return "{}".format(self.title)

    def get_absolute_url(self):
        # After saving point the redirect to index page
        return reverse('book:list')

    # Order results returned basing on the last record in the database
    class Meta:
        ordering = ['-id']
