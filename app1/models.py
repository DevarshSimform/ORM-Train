from django.db import models
from django.contrib.auth.models import Permission

class Author(models.Model):
  firstname = models.CharField(max_length=100)
  lastname = models.CharField(max_length=100)
  address = models.CharField(max_length=200, null=True)
  zipcode = models.IntegerField(null=True)
  telephone = models.CharField(max_length=100, null=True)
  recommendedby = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='recommended_authors', related_query_name='recommended_authors', null=True)
  joindate = models.DateField()
  popularity_score = models.IntegerField()
  followers = models.ManyToManyField('User', related_name='followed_authors', related_query_name='followed_authors')
  def __str__(self):
    return self.firstname + ' ' + self.lastname

class Books(models.Model):

  class Meta:
    permissions = [
      ('can_add', 'Can Add Book'),
      ('can_update_book', 'Can Update Book'),
    ]
  title = models.CharField(max_length=100)
  genre = models.CharField(max_length=200)
  price = models.IntegerField(null=True)
  published_date = models.DateField()
  author = models.ForeignKey('Author', on_delete=models.CASCADE,related_name='books', related_query_name='books')
  publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, related_name='books', related_query_name='books')
  def __str__(self):
    return self.title

class Publisher(models.Model):
  firstname = models.CharField(max_length=100)
  lastname = models.CharField(max_length=100)
  recommendedby = models.ForeignKey('Publisher', on_delete=models.CASCADE, null=True)
  joindate = models.DateField()
  popularity_score = models.IntegerField()
  def __str__(self):
    return self.firstname + ' ' + self.lastname

class User(models.Model):
  username = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  # user_perms_custom = models.ForeignKey('Permission', verbose_name=("User can"), on_delete=models.CASCADE)
  def __str__(self):
    return self.username