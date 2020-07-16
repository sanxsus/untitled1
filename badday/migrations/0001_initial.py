from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField(help_text='Enter a brief description of the book', max_length=1000)),
                ('id', models.AutoField(help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False)),
            ],
        ),
    ]
