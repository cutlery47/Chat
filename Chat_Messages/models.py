from django.db import models

# Create your models here.
class Chat(models.Model):
    name = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "Chats"

class Message(models.Model):
    first_name = models.CharField(blank=True)
    last_name = models.CharField(blank=True)
    message = models.TextField(blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.message)

    class Meta:
        db_table = "Messages"

