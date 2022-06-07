from django.contrib import admin
from .models import Post,Followers,Comment,Profile

# Register your models here.
# admin.site.register(Post)
admin.site.register(Followers)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Post)
