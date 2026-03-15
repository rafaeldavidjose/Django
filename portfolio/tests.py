from django.test import TestCase, Client
from django.urls import reverse, resolve
from portfolio.models import Projeto, Tecnologia, Disciplina, Docente
from portfolio.views import projetos_view, tecnologias_view


class ModelsTest(TestCase):
    fixtures = ['db.json']

    def test_str_methods(self):
        projeto = Projeto.objects.first()
        tecnologia = Tecnologia.objects.first()
        disciplina = Disciplina.objects.first()
        docente = Docente.objects.first()

        self.assertEqual(str(projeto), projeto.titulo)
        self.assertEqual(str(tecnologia), tecnologia.nome)
        self.assertEqual(str(disciplina), disciplina.nome)
        self.assertEqual(str(docente), docente.nome)

    def test_relationships(self):
        projeto = Projeto.objects.first()
        self.assertIsNotNone(projeto.disciplina)
        self.assertGreaterEqual(projeto.tecnologias.count(), 0)


class UrlsTest(TestCase):
    def test_projetos_url_resolves_to_correct_view(self):
        url = reverse('portfolio:projetos')
        self.assertEqual(resolve(url).func, projetos_view)

    def test_tecnologias_url_resolves_to_correct_view(self):
        url = reverse('portfolio:tecnologias')
        self.assertEqual(resolve(url).func, tecnologias_view)


class ViewsTest(TestCase):
    fixtures = ['db.json']

    def setUp(self):
        self.client = Client()

    def test_index_view_returns_200_and_uses_template(self):
        response = self.client.get(reverse('portfolio:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/index.html')

    def test_projetos_view_returns_200_and_displays_projects(self):
        response = self.client.get(reverse('portfolio:projetos'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'My Projects')
        for projeto in Projeto.objects.all():
            self.assertContains(response, projeto.titulo)

    def test_tecnologias_view_returns_200_and_uses_template(self):
        response = self.client.get(reverse('portfolio:tecnologias'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/tecnologias.html')
        for tecnologia in Tecnologia.objects.all():
            self.assertContains(response, tecnologia.nome)