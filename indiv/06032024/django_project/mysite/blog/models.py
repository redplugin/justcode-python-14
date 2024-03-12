from django.db import models

# CREATE TABLE blog_post (
#     id SERIAL PRIMARY KEY,
#     title VARCHAR(30)
# )
#


class Post(models.Model):

    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.pk})"


class Comment(models.Model):
    content = models.TextField()

    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
