from django.db import models

# Create your models here.


class GithubUser(models.Model):
    """
    Model for GithubUser
    """
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    avatar_url = models.URLField(max_length=255)
    html_url = models.URLField(max_length=255)
    followers = models.IntegerField()
    following = models.IntegerField()
    public_repos = models.IntegerField()
    retrieved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name