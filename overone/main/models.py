from django.db import models


class Feedback(models.Model):
    name = models.CharField('Имя', max_length=20)
    email = models.EmailField('Почта')
    message = models.TextField('Сообщение')



    def __str__(self):
        return self.email
