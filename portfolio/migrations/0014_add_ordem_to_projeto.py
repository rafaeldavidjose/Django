from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_contacto'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='ordem',
            field=models.IntegerField(default=0, help_text='Ordem de exibição (menor número aparece primeiro)'),
        ),
    ]