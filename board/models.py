from django.db import models

from user.models import User


class Board(models.Model):
    use_in_migrations = True
    title = models.TextField(max_length=100)
    body = models.TextField()
    comment = models.TextField()
    writen = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateTimeField()
    update_at = models.DateTimeField()

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        db_table = "board"
