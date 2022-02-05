# Generated by Django 3.2.10 on 2022-02-05 00:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'cart',
            },
        ),
        migrations.CreateModel(
            name='CartCourses',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cart')),
            ],
            options={
                'db_table': 'cart_courses',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'payment',
            },
        ),
        migrations.CreateModel(
            name='CartOrder',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_cart_courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cartcourses')),
                ('id_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.order')),
            ],
            options={
                'db_table': 'cart_order',
            },
        ),
        migrations.AddField(
            model_name='cartcourses',
            name='id_courses',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.course'),
        ),
    ]
