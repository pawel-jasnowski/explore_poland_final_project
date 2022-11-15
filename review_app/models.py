from django.db.models import Model, IntegerField, TextField, CharField


# Create your models here.
class Review(Model):
    # name = TextField(max_length = 30)
    rating = IntegerField(max_length=10)
    review_body = TextField(max_length=500)
    