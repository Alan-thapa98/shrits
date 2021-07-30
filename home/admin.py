from django.contrib import admin

# Register your models here.


from .models import Post
from .models import Video
from .models import VideoComment
from .models import ShareitsUser
from .models import Profile, Relationship


admin.site.register(Profile)
admin.site.register(Relationship)

admin.site.register(Post)
admin.site.register(ShareitsUser)
admin.site.register(Video)
admin.site.register(VideoComment)
