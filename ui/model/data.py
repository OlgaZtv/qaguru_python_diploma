from faker import Faker

fake = Faker('en_US')

email_random = fake.email()
full_name = fake.name()
password = fake.random.randint(2, 5)
text_random = fake.text()
comment = fake.text()
