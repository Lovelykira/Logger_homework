from django.contrib.auth.models import User
from django.db import models


class Log(models.Model):
    logger_name = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    level = models.CharField(max_length=100)
    message = models.TextField(default="")
    sender = models.ForeignKey(User)

    def __str__(self):
        return "{}\n {}\n {}\n {}".format(self.logger_name, self.time, self.level, self.message, self.sender)
