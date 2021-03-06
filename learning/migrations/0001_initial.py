# Generated by Django 3.0.7 on 2020-06-17 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Назва курса')),
                ('description', models.TextField(verbose_name='Опис')),
                ('img', models.ImageField(upload_to='img/', verbose_name='Зображення курса')),
                ('duration', models.DurationField(verbose_name='Тривалість курса')),
                ('slug', models.SlugField(max_length=130, unique=True)),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курси',
            },
        ),
        migrations.CreateModel(
            name='CourseAreas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Області')),
                ('description', models.TextField(verbose_name='Опис')),
            ],
            options={
                'verbose_name': 'Області навчання',
                'verbose_name_plural': 'Області навчання',
            },
        ),
        migrations.CreateModel(
            name='FormatCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Тип курса')),
            ],
            options={
                'verbose_name': 'Тип курса',
                'verbose_name_plural': 'Тип курса',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Мова курса')),
            ],
            options={
                'verbose_name': 'Мова курса',
                'verbose_name_plural': 'Мова курса',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Назва')),
                ('description', models.TextField(max_length=1000, verbose_name='Опис урока')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='learning.Course', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
        migrations.CreateModel(
            name='TypeRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Тип оцінювання')),
            ],
            options={
                'verbose_name': 'Тип оцінювання',
                'verbose_name_plural': 'Тип оцінювання',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Ім`я')),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Вік')),
                ('skills', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='skill_teacher', to='learning.CourseAreas')),
            ],
            options={
                'verbose_name': 'Мова викладання',
                'verbose_name_plural': 'Мови викладання',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100, verbose_name='Ім`я')),
                ('text', models.TextField(max_length=2000, verbose_name='Текст відгука')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='learning.Course', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Відгук',
                'verbose_name_plural': 'Відгуки',
            },
        ),
        migrations.CreateModel(
            name='LessonDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст курса')),
                ('img', models.ImageField(upload_to='course_lesson/', verbose_name='Зображення')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning.Lesson')),
            ],
            options={
                'verbose_name': 'Інформація про курс',
                'verbose_name_plural': 'Інформація про курс',
            },
        ),
        migrations.CreateModel(
            name='CourseShots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Опис')),
                ('img', models.ImageField(upload_to='course_shots/', verbose_name='Зображення')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning.Course', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Кадр курса',
                'verbose_name_plural': 'Кадры курса',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='areas',
            field=models.ManyToManyField(related_name='areas_course', to='learning.CourseAreas', verbose_name='Область курса'),
        ),
        migrations.AddField(
            model_name='course',
            name='format_course',
            field=models.ManyToManyField(related_name='format_type', to='learning.FormatCourse', verbose_name='Тип курса'),
        ),
        migrations.AddField(
            model_name='course',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='language_course', to='learning.Language', verbose_name='Мова курса'),
        ),
        migrations.AddField(
            model_name='course',
            name='type_rating',
            field=models.ManyToManyField(related_name='rating_type', to='learning.TypeRating', verbose_name='Формат перевірки'),
        ),
    ]
