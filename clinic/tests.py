from io import BytesIO

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from PIL import Image

from .models import Work


class WorksModalTests(TestCase):
    def test_works_list_endpoint_returns_only_active_items(self):
        visible_work = Work.objects.create(
            title='Trabajo visible',
            procedure='Implante',
            is_active=True,
        )
        Work.objects.create(
            title='Trabajo oculto',
            procedure='Ortodoncia',
            is_active=False,
        )

        response = self.client.get(reverse('clinic:works_list'))

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data['works']), 1)
        self.assertEqual(data['works'][0]['title'], visible_work.title)

    def test_home_renders_uploaded_work_image_in_modal(self):
        image_file = BytesIO()
        Image.new('RGB', (800, 600), color='red').save(image_file, format='PNG')
        image_file.seek(0)

        work = Work.objects.create(
            title='Restauración estética',
            procedure='Carillas',
            image=SimpleUploadedFile('work.png', image_file.read(), content_type='image/png'),
            is_active=True,
        )

        response = self.client.get(reverse('clinic:home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'worksGalleryGrid')
        self.assertContains(response, 'Cargando trabajos...')

    def test_home_does_not_render_placeholder_when_work_has_no_image(self):
        Work.objects.create(
            title='Caso sin imagen',
            procedure='Implante',
            image=None,
            is_active=True,
        )

        response = self.client.get(reverse('clinic:home'))

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Imagen procedimiento')
