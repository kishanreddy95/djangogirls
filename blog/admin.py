from django.contrib import admin
from .models import Post

# Next line is used to make the model 'Post' visible on the admin page (pass = djangogirls)
admin.site.register(Post)
