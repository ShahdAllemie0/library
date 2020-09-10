# Generated by Django 3.1.1 on 2020-09-10 07:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0008_remove_membership_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='borrow',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='membership',
            name='book',
            field=models.ManyToManyField(to='library.Book'),
        ),
        migrations.DeleteModel(
            name='Borrow',
        ),
        migrations.AddField(
            model_name='library',
            name='books',
            field=models.ManyToManyField(to='library.Book'),
        ),
        migrations.AddField(
            model_name='library',
            name='librarian',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='library',
            name='membership',
            field=models.ManyToManyField(to='library.Membership'),
        ),
    ]