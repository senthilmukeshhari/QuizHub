# Generated by Django 4.2 on 2024-01-02 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quizapp', '0007_awardsquestion_related_img_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentAffairsQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagery', models.CharField(default='Current Affairs', max_length=50, null=True)),
                ('question_no', models.IntegerField(null=True)),
                ('question', models.TextField(max_length=500, null=True)),
                ('opt1', models.CharField(max_length=80, null=True)),
                ('opt2', models.CharField(max_length=80, null=True)),
                ('opt3', models.CharField(max_length=80, null=True)),
                ('opt4', models.CharField(max_length=80, null=True)),
                ('correct_opt', models.CharField(max_length=80, null=True)),
                ('related_img', models.ImageField(null=True, upload_to='questions/related_images/current_affairs')),
            ],
        ),
        migrations.CreateModel(
            name='HistoryQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagery', models.CharField(default='History', max_length=50, null=True)),
                ('question_no', models.IntegerField(null=True)),
                ('question', models.TextField(max_length=500, null=True)),
                ('opt1', models.CharField(max_length=80, null=True)),
                ('opt2', models.CharField(max_length=80, null=True)),
                ('opt3', models.CharField(max_length=80, null=True)),
                ('opt4', models.CharField(max_length=80, null=True)),
                ('correct_opt', models.CharField(max_length=80, null=True)),
                ('related_img', models.ImageField(null=True, upload_to='questions/related_images/history')),
            ],
        ),
        migrations.CreateModel(
            name='PlantsAndAnimalQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagery', models.CharField(default='Plants and Animal', max_length=50, null=True)),
                ('question_no', models.IntegerField(null=True)),
                ('question', models.TextField(max_length=500, null=True)),
                ('opt1', models.CharField(max_length=80, null=True)),
                ('opt2', models.CharField(max_length=80, null=True)),
                ('opt3', models.CharField(max_length=80, null=True)),
                ('opt4', models.CharField(max_length=80, null=True)),
                ('correct_opt', models.CharField(max_length=80, null=True)),
                ('related_img', models.ImageField(null=True, upload_to='questions/related_images/plants_and_animal')),
            ],
        ),
        migrations.CreateModel(
            name='ZoologyQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagery', models.CharField(default='Zoology', max_length=50, null=True)),
                ('question_no', models.IntegerField(null=True)),
                ('question', models.TextField(max_length=500, null=True)),
                ('opt1', models.CharField(max_length=80, null=True)),
                ('opt2', models.CharField(max_length=80, null=True)),
                ('opt3', models.CharField(max_length=80, null=True)),
                ('opt4', models.CharField(max_length=80, null=True)),
                ('correct_opt', models.CharField(max_length=80, null=True)),
                ('related_img', models.ImageField(null=True, upload_to='questions/related_images/zoology')),
            ],
        ),
        migrations.DeleteModel(
            name='AwardsQuestion',
        ),
        migrations.DeleteModel(
            name='CurrencyQuestion',
        ),
        migrations.DeleteModel(
            name='HealthQuestion',
        ),
        migrations.DeleteModel(
            name='TechQuestion',
        ),
        migrations.AlterField(
            model_name='sportsquestion',
            name='related_img',
            field=models.ImageField(null=True, upload_to='questions/related_images/sports'),
        ),
    ]
