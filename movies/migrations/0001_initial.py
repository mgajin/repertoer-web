# Generated by Django 3.0.2 on 2020-01-13 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cinemas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('released', models.IntegerField()),
                ('runtime', models.IntegerField()),
                ('ticket_price', models.IntegerField()),
                ('poster', models.ImageField(upload_to='posters/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cinemas.Cinema')),
            ],
        ),
    ]
