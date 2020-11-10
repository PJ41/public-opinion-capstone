from django.db import models
from datetime import datetime


class Post(models.Model):
    header = models.CharField(max_length=50)
    body = models.TextField(max_length=250, default='')
    # post_submitter_name = models.CharField(max_length=100)  # name os student who posted post
    # post_submitter_username = models.CharField(max_length=10)  # username of person who submitted Post
    date_published = models.DateTimeField(default=datetime.now, blank=True)

    @classmethod
    def create(cls, header, body, post_submitter_username):
        post = cls(header=header, body=body, post_submitter_username=post_submitter_username)
        return post

    def __str__(self):
        return self.header

