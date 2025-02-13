# Generated by Django 3.2 on 2025-02-12 17:30

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_heading', models.CharField(max_length=50)),
                ('about', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbers', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(max_length=250)),
                ('section', models.CharField(choices=[('Programming', 'Programming'), ('Development', 'Development'), ('GraphicDesign', 'GraphicDesign')], max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('short_title', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=50)),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='uploads/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Introduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro_heading', models.CharField(max_length=50)),
                ('intro', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250)),
                ('profile_image', models.ImageField(upload_to='profile/')),
                ('profes', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=15)),
                ('email_add', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200)),
                ('freelance', models.CharField(choices=[('Availabe', 'Available'), ('Not Available', 'Not Available')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ResubscriptionLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('resubscribed_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('admin_user', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SentEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=100)),
                ('sender_email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=250)),
                ('message', models.TextField()),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_title', models.CharField(max_length=100)),
                ('service_details', models.CharField(max_length=250)),
                ('service_fontawesome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_heading', models.CharField(max_length=100)),
                ('skill_percent', models.CharField(max_length=10)),
                ('skill_color', models.CharField(choices=[('bg-info', 'bg-info'), ('bg-success', 'bg-success'), ('bg-warning', 'bg-warning'), ('bg-danger', 'bg-danger')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SocialLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(choices=[('fab fa-github', 'fab fa-github'), ('fab fa-instagram', 'fab fa-instagram'), ('fab fa-linkedin-in', 'fab fa-linkedin-in'), ('fab fa-facebook-f', 'fab fa-facebook-f'), ('fab fa-twitter', 'fab fa-twitter')], max_length=50)),
                ('link_address', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('unsubscribe_token', models.UUIDField(default=uuid.uuid4, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_details', models.TextField()),
                ('test_client_name', models.CharField(max_length=50)),
                ('test_client_profess', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='testimoniels/')),
            ],
        ),
        migrations.CreateModel(
            name='UnsubscribedUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('unsubscribed_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
