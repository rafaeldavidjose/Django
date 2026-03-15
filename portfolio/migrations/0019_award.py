from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0017_add_slugs_fixed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text='Nome do prémio/reconhecimento do projeto', max_length=200)),
                ('ordem', models.IntegerField(default=0, help_text='Ordem de exibição')),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='awards', to='portfolio.projeto')),
            ],
            options={
                'ordering': ['ordem', 'titulo'],
            },
        ),
    ]