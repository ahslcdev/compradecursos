from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True

class Category(Base):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'categories'

class Payment(Base):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'payment'

class Course(Base):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    # image = models.ImageField(upload_to='media/')

    class Meta:
        db_table = 'course'

class Cart(Base):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cart'

class CartCourses(Base):
    id = models.AutoField(primary_key=True)
    id_cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    id_courses = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cart_courses'


class Order(Base):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField(default=False)

    class Meta:
        db_table = 'order'

        
class CartOrder(Base):
    id = models.AutoField(primary_key=True)
    id_order = models.ForeignKey(Order, on_delete=models.CASCADE)
    id_cart_courses = models.ForeignKey(CartCourses, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cart_order'

