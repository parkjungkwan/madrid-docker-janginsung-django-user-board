from django.db import models


class User(models.Model):
    use_in_migrations = True
    user_email = models.TextField()
    password = models.CharField(max_length=10)
    user_name = models.TextField()
    phone = models.TextField()
    birth = models.TextField()
    address = models.TextField(blank=True)
    job = models.TextField()
    user_interests = models.TextField()

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        db_table = "users"

