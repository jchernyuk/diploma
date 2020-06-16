from django.db import models
from django import forms
from django.db import models
from django.urls import reverse


class CourseAreas(models.Model):
    name = models.CharField("Області", max_length=150)
    description = models.TextField("Опис")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Області навчання"
        verbose_name_plural = "Області навчання"


class TypeRating(models.Model):
    name = models.CharField("Тип оцінювання", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип оцінювання"
        verbose_name_plural = "Тип оцінювання"


class FormatCourse(models.Model):
    name = models.CharField("Тип курса", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип курса"
        verbose_name_plural = "Тип курса"


class Language(models.Model):
    name = models.CharField("Мова курса", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Мова курса"
        verbose_name_plural = "Мова курса"


class Teacher(models.Model):
    name = models.CharField("Ім'я", max_length=50)
    age = models.PositiveSmallIntegerField("Вік", default=0)
    skills = models.ForeignKey(
        CourseAreas, related_name="skill_teacher", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Мова викладання"
        verbose_name_plural = "Мови викладання"


class Course(models.Model):
    name = models.CharField("Назва курса", max_length=250)
    description = models.TextField("Опис")
    img = models.ImageField("Зображення курса", upload_to="img/")
    format_course = models.ManyToManyField(
        FormatCourse, verbose_name="Тип курса", related_name="format_type")
    type_rating = models.ManyToManyField(
        TypeRating, verbose_name="Формат перевірки", related_name="rating_type")
    language = models.ForeignKey(Language, verbose_name="Мова курса", related_name="language_course",
                                 on_delete=models.SET_NULL, null=True)
    duration = models.TimeField("Тривалість курса")
    areas = models.ManyToManyField(
        CourseAreas, verbose_name="Область курса", related_name="areas_course")
    slug = models.SlugField(max_length=130, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('CourseListByCategory', args=[self.slug])

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курси"


class CourseShots(models.Model):
    title = models.CharField("Заголовок", max_length=120)
    description = models.TextField("Опис")
    img = models.ImageField("Зображення", upload_to="course_shots/")
    course = models.ForeignKey(
        Course, verbose_name="Курс", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Кадр курса"
        verbose_name_plural = "Кадры курса"


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Ім'я", max_length=100)
    text = models.TextField("Текст відгука", max_length=2000)
    parent = models.ForeignKey(
        'self', verbose_name="Батько", on_delete=models.CASCADE, blank=True, null=True)
    course = models.ForeignKey(
        Course, verbose_name="Курс",  on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.text}"

    class Meta:
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"

# добавил related names для общения с ормом джанги


class Lessons(models.Model):
    course = models.ForeignKey(
        Course, verbose_name="Курс", related_name='lessons', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField("Назва", max_length=250)
    description = models.TextField("Опис урока", max_length=1000)
    slug = models.SlugField(
        max_length=200, db_index=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def get_absolute_url(self):
        return reverse('CourseDetail', args=[self.slug])


class LessonsInside(models.Model):
    text = models.TextField("Текст курса")
    img = models.ImageField("Зображення", upload_to="course_lesson/")
    parent = models.ForeignKey(
        Lessons, verbose_name="Родитель", on_delete=models.CASCADE)

    def __str__(self):
        return self

    class Meta:
        verbose_name = "Інформація про курс"
        verbose_name_plural = "Інформація про курс"
