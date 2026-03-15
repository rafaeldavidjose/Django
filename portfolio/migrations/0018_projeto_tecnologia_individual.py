from django.db import migrations, models
import django.db.models.deletion

def migrate_existing_relations(apps, schema_editor):
    Projeto = apps.get_model('portfolio', 'Projeto')
    Tecnologia = apps.get_model('portfolio', 'Tecnologia') 
    ProjetoTecnologia = apps.get_model('portfolio', 'ProjetoTecnologia')
    
    for projeto in Projeto.objects.all():
        for ordem, tecnologia in enumerate(projeto.tecnologias.all()):
            ProjetoTecnologia.objects.create(
                projeto=projeto,
                tecnologia=tecnologia,
                ordem_no_cartao=ordem + 1,
                mostrar_no_cartao=True
            )

def reverse_migration(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0017_add_slugs_fixed'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjetoTecnologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordem_no_cartao', models.IntegerField(default=999, help_text='Ordem de exibição no cartão do projeto (menor número = maior prioridade)')),
                ('mostrar_no_cartao', models.BooleanField(default=True, help_text='Se deve aparecer no cartão do projeto')),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.projeto')),
                ('tecnologia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.tecnologia')),
            ],
            options={
                'verbose_name': 'Tecnologia do Projeto',
                'verbose_name_plural': 'Tecnologias do Projeto',
                'ordering': ['ordem_no_cartao', 'tecnologia__nome'],
            },
        ),
        
        migrations.AlterUniqueTogether(
            name='projetotecnologia',
            unique_together={('projeto', 'tecnologia')},
        ),
        
        migrations.RunPython(migrate_existing_relations, reverse_migration),
        
        migrations.RemoveField(
            model_name='projeto',
            name='tecnologias',
        ),
        
        migrations.AddField(
            model_name='projeto',
            name='tecnologias',
            field=models.ManyToManyField(
                blank=True, 
                related_name='projetos', 
                through='portfolio.ProjetoTecnologia', 
                to='portfolio.tecnologia'
            ),
        ),
    ]