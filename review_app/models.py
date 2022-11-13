from django.db.models import Model, IntegerField, TextField


# Create your models here.
class Review(Model):
    rating = IntegerField(max_length=10)
    review_body = TextField(max_length=500)
