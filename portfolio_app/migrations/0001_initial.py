# Generated by Django 4.2.11 on 2024-03-29 09:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio_app.basemodel')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            bases=('portfolio_app.basemodel',),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio_app.basemodel')),
                ('your_name', models.CharField(max_length=255)),
                ('your_email', models.EmailField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=255)),
            ],
            bases=('portfolio_app.basemodel',),
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio_app.basemodel')),
                ('name', models.CharField(max_length=255)),
                ('degree', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField(max_length=255)),
                ('finished', models.DateField(blank=True, max_length=255, null=True)),
                ('location', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=255)),
            ],
            bases=('portfolio_app.basemodel',),
        ),
        migrations.CreateModel(
            name='MyInfo',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio_app.basemodel')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('image', models.FileField(upload_to='images')),
                ('text', models.CharField(max_length=255)),
                ('birthday', models.DateField(default=django.utils.timezone.now)),
                ('website', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('age', models.SmallIntegerField()),
                ('degree', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('freelance', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('map', models.CharField(max_length=255)),
            ],
            bases=('portfolio_app.basemodel',),
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio_app.basemodel')),
                ('name', models.CharField(max_length=255)),
                ('client', models.CharField(max_length=255)),
                ('project_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('project_url', models.URLField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=255)),
                ('categories', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio_app.category')),
            ],
            bases=('portfolio_app.basemodel',),
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio_app.basemodel')),
                ('about_title', models.CharField(max_length=255)),
                ('happy_clients', models.IntegerField()),
                ('projects', models.IntegerField()),
                ('support', models.IntegerField()),
                ('workers', models.IntegerField()),
            ],
            bases=('portfolio_app.basemodel',),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio_app.basemodel')),
                ('name', models.CharField(max_length=255)),
                ('knowledge', models.CharField(max_length=255)),
            ],
            bases=('portfolio_app.basemodel',),
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio_app.basemodel')),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=255)),
            ],
            bases=('portfolio_app.basemodel',),
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio_app.basemodel')),
                ('image', models.ImageField(upload_to='portfolio')),
                ('name', models.CharField(max_length=255)),
                ('job', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=255)),
            ],
            bases=('portfolio_app.basemodel',),
        ),
        migrations.CreateModel(
            name='PortfolioImage',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio_app.basemodel')),
                ('image', models.ImageField(upload_to='portfolio')),
                ('portfolio_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_images', to='portfolio_app.portfolio')),
            ],
            bases=('portfolio_app.basemodel',),
        ),
    ]
