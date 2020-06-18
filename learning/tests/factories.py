import factory.django

from learning.models import Course, Lesson, Poll, PollAnswer


class CourseFactory(factory.DjangoModelFactory):
    name = factory.Faker('sentence', nb_words=5)
    description = factory.Faker('paragraphs', nb=3)
    img = factory.django.ImageField()
    slug = factory.Faker('slug')
    duration = factory.Faker('time_delta')

    class Meta:
        model = Course


class LessonFactory(factory.DjangoModelFactory):
    course = factory.SubFactory(CourseFactory)
    name = factory.Faker('sentence', nb_words=5)
    description = factory.Faker('paragraphs', nb=3)
    slug = factory.Faker('slug')

    class Meta:
        model = Lesson


class PollFactory(factory.DjangoModelFactory):
    question = factory.Faker('sentence', nb_words=5)
    number = factory.Sequence(lambda n: n)
    lesson = factory.SubFactory(LessonFactory)

    class Meta:
        model = Poll


class PollAnswerFactory(factory.DjangoModelFactory):
    poll = factory.SubFactory(PollFactory)
    choice_text = factory.Faker('sentence', nb_words=2)
    is_correct = factory.Faker('pybool')

    class Meta:
        model = PollAnswer
