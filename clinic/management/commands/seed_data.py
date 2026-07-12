from django.core.management.base import BaseCommand
from clinic.models import Specialty, Testimonial, Work, Partner, SiteConfiguration


class Command(BaseCommand):
    help = 'Populate database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')

        # Create Site Configuration
        config, created = SiteConfiguration.objects.get_or_create(pk=1, defaults={
            'site_name': 'SILVADENT CENTER',
            'tagline': 'Sonrisas con caracter',
            'about_title': 'Un centro pensado para una relacion de confianza a largo plazo',
            'about_text': 'No creemos en visitas aisladas. Disenamos planes de tratamiento con seguimiento real.',
            'address': 'Av. de los Especialistas y Calle Cinco Esquinas, Quito',
            'phone': '+593 98 881 4811',
            'whatsapp': '593988814811',
            'email': 'hola@silvadent.com',
            'schedule': 'Lun - Vie: 08:00 - 19:00 - Sab: 09:00 - 14:00',
        })
        if created:
            self.stdout.write(self.style.SUCCESS('Site configuration created'))

        # Create Specialties
        specialties_data = [
            {
                'title': 'Ortodoncia',
                'short_description': 'Brackets y alineadores para corregir la posicion dental y mejorar tu mordida.',
                'full_description': 'La ortodoncia es la especialidad que se encarga de corregir la posicion de los dientes y los huesos maxilares para lograr una sonrisa armoniosa y funcional. Utilizamos las tecnicas mas avanzadas incluyendo brackets tradicionales, brackets ceramicos esteticos y alineadores invisibles de ultima generacion.',
                'features': ['Brackets metalicos y ceramicos', 'Alineadores invisibles', 'Ortodoncia lingual', 'Control de tratamiento digital', 'Resultados visibles desde el primer mes'],
                'duration': '12 - 24 meses segun el caso',
                'icon_svg': '<path d="M4 4h16v6a4 4 0 01-4 4H8a4 4 0 01-4-4V4zM9 14v3a3 3 0 006 0v-3"/>'
            },
            {
                'title': 'Implantes Dentales',
                'short_description': 'Recuperamos piezas perdidas con implantes de titanio de ultima generacion.',
                'full_description': 'Los implantes dentales son la solucion mas avanzada para reemplazar dientes perdidos. Consisten en tornillos de titanio biocompatible que se insertan en el hueso maxilar, funcionando como raices artificiales. Sobre ellos se colocan coronas individuales, puentes o protes fias completas.',
                'features': ['Implantes de titanio grado medico', 'Diagnostico 3D con tomografia', 'Cirugia minimamente invasiva', 'Coronas de porcelana naturales', 'Garantia extendida'],
                'duration': '3 - 6 meses por implante',
                'icon_svg': '<path d="M12 3v6M12 9c-3 0-4 2-4 5s1 7 4 7 4-4 4-7-1-5-4-5z"/>'
            },
            {
                'title': 'Diseno de Sonrisa',
                'short_description': 'Planificacion estetica digital para armonizar forma, color y proporcion.',
                'full_description': 'El diseno de sonrisa es un proceso integral que combina arte y ciencia para crear la sonrisa perfecta para tu rostro. Mediante tecnologia digital de ultima generacion, analizamos la proporcion facial, forma de los labios, color de la piel y caracteristicas unicas.',
                'features': ['Analisis facial digital', 'Simulacion 3D del resultado', 'Carillas de porcelana', 'Encerado diagnostico', 'Fotografia profesional antes/despues'],
                'duration': '2 - 4 semanas segun tratamiento',
                'icon_svg': '<path d="M12 2l2 5 5 .6-3.8 3.6.9 5.3L12 13.9 7.9 16.5l.9-5.3L5 7.6 10 7z"/>'
            },
            {
                'title': 'Blanqueamiento Dental',
                'short_description': 'Dientes mas blancos de forma segura con protocolos supervisados.',
                'full_description': 'El blanqueamiento dental profesional es el tratamiento estetico mas solicitado para lograr una sonrisa radiante. Utilizamos geles de peroxido de alta concentracion activados con luz LED de ultima generacion, garantizando resultados inmediatos y duraderos.',
                'features': ['Blanqueamiento laser LED', 'Kit domiciliario incluido', 'Hasta 8 tonos mas blanco', 'Resultados inmediatos', 'Procedimiento indoloro'],
                'duration': '1 - 2 sesiones de 60 minutos',
                'icon_svg': '<circle cx="12" cy="12" r="5"/><path d="M12 1v3M12 20v3M4.2 4.2l2 2M17.8 17.8l2 2M1 12h3M20 12h3M4.2 19.8l2-2M17.8 6.2l2-2"/>'
            },
            {
                'title': 'Odontopediatria',
                'short_description': 'Cuidado dental especializado y amigable para ninos y adolescentes.',
                'full_description': 'La odontopediatria se especializa en el cuidado bucal de ninos desde la primera infancia hasta la adolescencia. Nuestro equipo esta capacitado para crear un ambiente amigable y sin miedo, donde los mas pequenos se sientan comodos y seguros.',
                'features': ['Primera visita sin miedo', 'Sellantes preventivos', 'Aplicacion de fluor', 'Tratamiento de caries en dientes de leche', 'Ortodoncia preventiva infantil'],
                'duration': 'Control cada 6 meses',
                'icon_svg': '<circle cx="12" cy="9" r="4"/><path d="M8 21c0-3 2-4 4-4s4 1 4 4"/>'
            },
            {
                'title': 'Endodoncia',
                'short_description': 'Tratamiento de conducto para salvar piezas danadas o infectadas.',
                'full_description': 'La endodoncia es el tratamiento que permite salvar dientes severamente danados o infectados, evitando su extraccion. Consiste en la remocion del tejido pulpar afectado, la limpieza y desinfeccion del sistema de conductos radiculares.',
                'features': ['Microscopio dental', 'Localizador apical digital', 'Tratamiento en una cita', 'Anestesia local efectiva', 'Restauracion con corona'],
                'duration': '1 - 2 sesiones',
                'icon_svg': '<path d="M12 2v20M8 6h8M8 18h8M6 12h12"/>'
            },
            {
                'title': 'Cirugia Oral',
                'short_description': 'Procedimientos quirurgicos seguros con protocolos de esterilizacion estrictos.',
                'full_description': 'La cirugia oral abarca procedimientos quirurgicos en la cavidad bucal, desde extracciones complejas hasta cirugias maxilofaciales. Contamos con un quirófano equipado con los mas altos estandares de bioseguridad.',
                'features': ['Extraccion de cordales', 'Cirugia de quistes', 'Injertos oseos', 'Cirugia pre-implante', 'Postoperatorio supervisado'],
                'duration': 'Segun complejidad del caso',
                'icon_svg': '<path d="M12 2a5 5 0 015 5c0 3-2 4-2 7v3H9v-3c0-3-2-4-2-7a5 5 0 015-5zM9 21h6"/>'
            },
            {
                'title': 'Periodoncia',
                'short_description': 'Salud de encias y tejidos de soporte para una base dental fuerte.',
                'full_description': 'La periodoncia trata las enfermedades de las encias y los tejidos que soportan los dientes. La enfermedad periodontal es la principal causa de perdida de dientes en adultos.',
                'features': ['Diagnostico periodontal completo', 'Raspado y alisado radicular', 'Injertos gingivales', 'Cirugia de reduccion de bolsas', 'Mantenimiento periodontal'],
                'duration': '4 - 6 sesiones segun gravedad',
                'icon_svg': '<path d="M3 13c3-6 15-6 18 0M6 13v3a2 2 0 002 2h8a2 2 0 002-2v-3"/>'
            },
            {
                'title': 'Protesis Dental',
                'short_description': 'Recupera tu funcion masticatoria y estetica con protes fias de alta calidad.',
                'full_description': 'Las protes fias dentales reemplazan uno o varios dientes perdidos, devolviendo la funcion masticatoria, el habla y la estetica. Ofrecemos protes fias fijas como coronas y puentes sobre dientes naturales o implantes.',
                'features': ['Protes fias fijas (coronas y puentes)', 'Protes fias removibles', 'Protes fias sobre implantes', 'Materiales esteticos (zirconio, porcelana)', 'Ajustes personalizados'],
                'duration': '2 - 4 semanas',
                'icon_svg': '<path d="M4 8a4 4 0 004 4 4 4 0 004-4M8 20v-8M20 8a4 4 0 01-4 4 4 4 0 01-4-4M16 20v-8"/>'
            },
            {
                'title': 'Odontologia General',
                'short_description': 'Revisiones, limpiezas, obturaciones y todo el cuidado basico.',
                'full_description': 'La odontologia general es la base de una buena salud bucal. Incluye diagnosticos preventivos, limpiezas profesionales, tratamiento de caries, obturaciones esteticas, y todo el cuidado necesario para mantener tu boca sana.',
                'features': ['Examen bucal completo', 'Limpieza profesional', 'Obturaciones esteticas', 'Tratamiento de sensibilidad', 'Radiografias digitales'],
                'duration': 'Control cada 6 meses',
                'icon_svg': '<path d="M12 3c-2.2 0-3.6 1.3-5 1.3S4.2 3 3 3c0 4 .6 7 1.4 10.4.6 2.6 1.2 5.6 3 5.6 1.6 0 1.6-2.8 2.3-4.8.3-.9.7-1.6 1.3-1.6s1 .7 1.3 1.6c.7 2 .7 4.8 2.3 4.8 1.8 0 2.4-3 3-5.6C18.4 10 19 7 19 3c-1.2 0-2.6 1.3-4 1.3S14.2 3 12 3z"/>'
            },
            {
                'title': 'Radiologia Dental',
                'short_description': 'Diagnostico preciso con radiografias digitales y tomografia 3D.',
                'full_description': 'La radiologia dental es fundamental para el diagnostico preciso de condiciones no visibles a simple vista. Contamos con tecnologia de radiacion ultrabaja que minimiza la exposicion.',
                'features': ['Radiografias panoramicas', 'Tomografia 3D (CBCT)', 'Radiografias periapicales', 'Baja radiacion', 'Resultados inmediatos'],
                'duration': 'Resultados en el momento',
                'icon_svg': '<rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/>'
            },
            {
                'title': 'Cuidado Geriatrico',
                'short_description': 'Atencion especializada para adultos mayores con enfoque en comodidad.',
                'full_description': 'El cuidado odontologico geriatrico requiere consideraciones especiales. Nuestro equipo esta capacitado para atender a adultos mayores con paciencia, respeto y comprension.',
                'features': ['Tratamientos adaptados', 'Prevencion de sequedad bucal', 'Cuidado de protesis existentes', 'Atencion domiciliaria disponible', 'Coordinacion con medicos tratantes'],
                'duration': 'Segun necesidades del paciente',
                'icon_svg': '<circle cx="12" cy="12" r="9"/><path d="M9 9h.01M15 9h.01M9 15c1.5 1 4.5 1 6 0"/>'
            },
        ]

        for i, data in enumerate(specialties_data):
            specialty, created = Specialty.objects.get_or_create(
                title=data['title'],
                defaults={
                    'short_description': data['short_description'],
                    'full_description': data['full_description'],
                    'features': data['features'],
                    'duration': data['duration'],
                    'icon_svg': data['icon_svg'],
                    'order': i,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Specialty created: {data["title"]}'))

        # Create Testimonials
        testimonials_data = [
            {'name': 'Maria Fernanda C.', 'initials': 'MF', 'service': 'Diseno de sonrisa', 'text': 'Excelente atencion de principio a fin. El equipo explica cada paso del tratamiento y eso me dio mucha confianza. Los resultados superaron mis expectativas.'},
            {'name': 'Andres G.', 'initials': 'AG', 'service': 'Ortodoncia', 'text': 'Llevaba anos posponiendo mi tratamiento de ortodoncia. Con el plan personalizado que me armaron, por fin lo termine. Muy profesionales.'},
            {'name': 'Daniela P.', 'initials': 'DP', 'service': 'Odontopediatria', 'text': 'Mi hijo le tenia miedo al dentista y aqui lo trataron con muchisima paciencia. Ahora va contento a sus controles. Totalmente recomendado.'},
            {'name': 'Carlos R.', 'initials': 'CR', 'service': 'Implantes dentales', 'text': 'Despues de anos sin una pieza dental, finalmente me atrevi con el implante. El proceso fue mucho mas facil de lo que imagine.'},
            {'name': 'Patricia M.', 'initials': 'PM', 'service': 'Blanqueamiento', 'text': 'El blanqueamiento quedo increible. Las doctoras fueron muy claras con las indicaciones y los resultados son exactamente los que esperaba.'},
            {'name': 'Roberto S.', 'initials': 'RS', 'service': 'Endodoncia', 'text': 'Tenia mucho miedo del tratamiento de conducto pero fue totalmente indoloro. La atencion fue impecable y el seguimiento muy atento.'},
        ]

        for i, data in enumerate(testimonials_data):
            testimonial, created = Testimonial.objects.get_or_create(
                name=data['name'],
                defaults={
                    'initials': data['initials'],
                    'service': data['service'],
                    'text': data['text'],
                    'order': i,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Testimonial created: {data["name"]}'))

        # Create Works
        works_data = [
            {'title': 'Transformacion de Sonrisa', 'procedure': 'Diseno digital + carillas'},
            {'title': 'Caso de Ortodoncia', 'procedure': 'Alineadores invisibles'},
            {'title': 'Rehabilitacion Total', 'procedure': 'Implantes + protes fias'},
            {'title': 'Blanqueamiento Profesional', 'procedure': 'Laser + kit domiciliario'},
            {'title': 'Cirugia de Cordales', 'procedure': 'Extraccion quirurgica'},
            {'title': 'Tratamiento de Encias', 'procedure': 'Raspado y alisado'},
            {'title': 'Restauracion Estetica', 'procedure': 'Carillas de porcelana'},
            {'title': 'Caso Pediatrico', 'procedure': 'Sellantes + fluorizacion'},
            {'title': 'Protesis Removible', 'procedure': 'Protesis flexible'},
        ]

        for i, data in enumerate(works_data):
            work, created = Work.objects.get_or_create(
                title=data['title'],
                defaults={
                    'procedure': data['procedure'],
                    'order': i,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Work created: {data["title"]}'))

        # Create Partners
        partners_data = [
            'Johnson & Johnson', 'Colgate', '3M Dental', 'Philips',
            'Dentsply', 'Ivoclar', 'SDI', 'Kerr'
        ]

        for i, name in enumerate(partners_data):
            partner, created = Partner.objects.get_or_create(
                name=name,
                defaults={'order': i},
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Partner created: {name}'))

        self.stdout.write(self.style.SUCCESS('All sample data created successfully!'))
