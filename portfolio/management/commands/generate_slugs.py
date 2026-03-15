from django.core.management.base import BaseCommand
from django.utils.text import slugify
from portfolio.models import Projeto, Tecnologia

class Command(BaseCommand):
    help = 'Generate slugs for existing projects and technologies'

    def handle(self, *args, **options):
        # Generate slugs for projects
        projetos_updated = 0
        for projeto in Projeto.objects.filter(slug__isnull=True):
            projeto.slug = slugify(projeto.titulo)
            
            # Ensure unique slug
            original_slug = projeto.slug
            counter = 1
            while Projeto.objects.filter(slug=projeto.slug).exclude(pk=projeto.pk).exists():
                projeto.slug = f"{original_slug}-{counter}"
                counter += 1
            
            projeto.save()
            projetos_updated += 1
            self.stdout.write(f"Updated project: {projeto.titulo} -> {projeto.slug}")

        # Generate slugs for technologies
        tecnologias_updated = 0
        for tecnologia in Tecnologia.objects.filter(slug__isnull=True):
            tecnologia.slug = slugify(tecnologia.nome)
            
            # Ensure unique slug
            original_slug = tecnologia.slug
            counter = 1
            while Tecnologia.objects.filter(slug=tecnologia.slug).exclude(pk=tecnologia.pk).exists():
                tecnologia.slug = f"{original_slug}-{counter}"
                counter += 1
            
            tecnologia.save()
            tecnologias_updated += 1
            self.stdout.write(f"Updated technology: {tecnologia.nome} -> {tecnologia.slug}")

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully updated {projetos_updated} projects and {tecnologias_updated} technologies with slugs'
            )
        )