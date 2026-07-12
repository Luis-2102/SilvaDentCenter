from django.db import models


class Specialty(models.Model):
    """Modelo para especialidades odontologicas"""
    title = models.CharField('Titulo', max_length=100)
    short_description = models.TextField('Descripcion corta', max_length=255)
    full_description = models.TextField('Descripcion completa')
    features = models.JSONField('Caracteristicas', default=list, blank=True)
    duration = models.CharField('Duracion estimada', max_length=100)
    icon_svg = models.TextField('Icono SVG', blank=True, default='')
    image = models.ImageField('Imagen', upload_to='specialties/', blank=True, null=True)
    order = models.PositiveIntegerField('Orden', default=0)
    is_active = models.BooleanField('Activo', default=True)
    created_at = models.DateTimeField('Creado', auto_now_add=True)
    updated_at = models.DateTimeField('Actualizado', auto_now=True)

    class Meta:
        verbose_name = 'Especialidad'
        verbose_name_plural = 'Especialidades'
        ordering = ['order', 'title']

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    """Modelo para testimonios de pacientes"""
    name = models.CharField('Nombre', max_length=100)
    initials = models.CharField('Iniciales', max_length=5)
    service = models.CharField('Servicio', max_length=100)
    text = models.TextField('Testimonio')
    rating = models.PositiveIntegerField('Calificacion', default=5)
    avatar = models.ImageField('Avatar', upload_to='testimonials/', blank=True, null=True)
    is_active = models.BooleanField('Activo', default=True)
    order = models.PositiveIntegerField('Orden', default=0)
    created_at = models.DateTimeField('Creado', auto_now_add=True)

    class Meta:
        verbose_name = 'Testimonio'
        verbose_name_plural = 'Testimonios'
        ordering = ['order', '-created_at']

    def __str__(self):
        return f'{self.name} - {self.service}'


class Work(models.Model):
    """Modelo para trabajos/galeria"""
    title = models.CharField('Titulo', max_length=100)
    procedure = models.CharField('Procedimiento', max_length=200)
    description = models.TextField('Descripcion', blank=True)
    image = models.ImageField('Imagen', upload_to='works/', blank=True, null=True)
    is_active = models.BooleanField('Activo', default=True)
    order = models.PositiveIntegerField('Orden', default=0)
    created_at = models.DateTimeField('Creado', auto_now_add=True)

    class Meta:
        verbose_name = 'Trabajo'
        verbose_name_plural = 'Trabajos'
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title


class Partner(models.Model):
    """Modelo para logos de partners/marcas"""
    name = models.CharField('Nombre', max_length=100)
    logo = models.ImageField('Logo', upload_to='partners/', blank=True, null=True)
    website = models.URLField('Sitio web', blank=True)
    is_active = models.BooleanField('Activo', default=True)
    order = models.PositiveIntegerField('Orden', default=0)

    class Meta:
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    """Modelo para mensajes de contacto"""
    name = models.CharField('Nombre', max_length=100)
    phone = models.CharField('Telefono', max_length=20)
    email = models.EmailField('Correo electronico')
    service = models.CharField('Especialidad de interes', max_length=100, blank=True)
    datetime = models.CharField('Fecha y hora deseada', max_length=200, blank=True)
    message = models.TextField('Mensaje', blank=True)
    is_read = models.BooleanField('Leido', default=False)
    created_at = models.DateTimeField('Creado', auto_now_add=True)

    class Meta:
        verbose_name = 'Mensaje de contacto'
        verbose_name_plural = 'Mensajes de contacto'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} - {self.created_at.strftime("%d/%m/%Y")}'


class SiteConfiguration(models.Model):
    """Modelo para configuracion del sitio (singleton)"""
    site_name = models.CharField('Nombre del sitio', max_length=100, default='SILVADENT CENTER')
    tagline = models.CharField('Eslogan', max_length=200, blank=True)
    about_title = models.CharField('Titulo Nosotros', max_length=200, blank=True)
    about_text = models.TextField('Texto Nosotros', blank=True)
    address = models.CharField('Direccion', max_length=200, blank=True)
    phone = models.CharField('Telefono', max_length=20, blank=True)
    whatsapp = models.CharField('WhatsApp', max_length=20, blank=True)
    email = models.EmailField('Correo', blank=True)
    schedule = models.CharField('Horario', max_length=200, blank=True)
    facebook_url = models.URLField('Facebook URL', blank=True)
    instagram_url = models.URLField('Instagram URL', blank=True)
    tiktok_url = models.URLField('TikTok URL', blank=True)
    logo = models.ImageField('Logo', upload_to='site/', blank=True, null=True)

    class Meta:
        verbose_name = 'Configuracion del sitio'
        verbose_name_plural = 'Configuracion del sitio'

    def __str__(self):
        return self.site_name

    def save(self, *args, **kwargs):
        # Ensure only one configuration exists
        if SiteConfiguration.objects.exists() and not self.pk:
            self.pk = SiteConfiguration.objects.first().pk
        super().save(*args, **kwargs)

    @classmethod
    def get_config(cls):
        config, created = cls.objects.get_or_create(pk=1)
        return config
