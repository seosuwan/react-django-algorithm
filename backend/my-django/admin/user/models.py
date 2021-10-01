from django.db import models


class UserVo(models.Model):
    use_in_migrations = True
    username = models.CharField(primary_key=True, max_length=10)
    password = models.CharField(max_length=10)
    name = models.TextField()
    email = models.TextField()
    birth = models.TextField()
    address = models.TextField()

    class Meta:
        db_table = "users"

    def __str__(self):
        return f'[{self.pk}] {self.username}'
