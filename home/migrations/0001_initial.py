# Generated by Django 3.1.2 on 2021-02-26 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=14)),
                ('slug', models.CharField(max_length=130)),
                ('views', models.IntegerField(default=0)),
                ('timeStamp', models.DateTimeField(blank=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ShareitsUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=200)),
                ('pass1', models.CharField(max_length=200)),
                ('pass2', models.CharField(max_length=200)),
                ('Userfriends', models.IntegerField(default=0)),
                ('UserSubs', models.IntegerField(default=0)),
                ('Userposts', models.IntegerField(default=0)),
                ('timeStamp', models.DateTimeField(blank=True)),
                ('image', models.ImageField(default='', upload_to='shop/userimg')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('Video_id', models.AutoField(primary_key=True, serialize=False)),
                ('Video_url', models.FileField(default='', max_length=5000, upload_to='video/Videos')),
                ('Video_name', models.CharField(max_length=5000)),
                ('views', models.IntegerField(default=0)),
                ('Category', models.CharField(default='', max_length=5000)),
                ('Desc', models.CharField(max_length=9000)),
                ('Tages', models.CharField(default='', max_length=5000)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
        migrations.CreateModel(
            name='VideoComment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.videocomment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
