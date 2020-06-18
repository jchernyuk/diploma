import factory

from users.models import User


class UserFactory(factory.DjangoModelFactory):
    username = factory.Faker('user_name')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    is_superuser = factory.Faker('pybool')
    is_staff = factory.Faker('pybool')

    class Meta:
        model = User
