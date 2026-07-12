from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.templatetags.static import static
from .models import (
    Specialty, Testimonial, Work, Partner,
    ContactMessage, SiteConfiguration
)


def home(request):
    """Vista principal de la pagina de inicio"""
    config = SiteConfiguration.get_config()
    specialties = Specialty.objects.filter(is_active=True)[:8]
    all_specialties = Specialty.objects.filter(is_active=True)
    testimonials = Testimonial.objects.filter(is_active=True)
    works = Work.objects.filter(is_active=True)
    partners = Partner.objects.filter(is_active=True)

    context = {
        'config': config,
        'specialties': specialties,
        'all_specialties': all_specialties,
        'testimonials': testimonials,
        'works': works,
        'partners': partners,
    }
    return render(request, 'home.html', context)


def specialty_detail(request, pk):
    """Vista para mostrar detalles de una especialidad"""
    specialty = get_object_or_404(Specialty, pk=pk, is_active=True)
    config = SiteConfiguration.get_config()

    context = {
        'specialty': specialty,
        'config': config,
    }
    return render(request, 'partials/specialty_detail.html', context)


def works_list(request):
    """Vista para devolver los trabajos activos en formato JSON."""
    works = Work.objects.filter(is_active=True).order_by('order', '-created_at')
    payload = []

    for work in works:
        payload.append({
            'id': work.id,
            'title': work.title,
            'procedure': work.procedure,
            'image_url': work.image.url if work.image else None,
        })

    return JsonResponse({'works': payload})


@require_POST
@csrf_exempt
def contact_form(request):
    """Vista para procesar el formulario de contacto"""
    name = request.POST.get('name', '')
    phone = request.POST.get('phone', '')
    email = request.POST.get('email', '')
    service = request.POST.get('service', '')
    datetime = request.POST.get('datetime', '')

    if name and phone and email:
        # Guardar en base de datos
        ContactMessage.objects.create(
            name=name,
            phone=phone,
            email=email,
            service=service,
            datetime=datetime,
        )
        return JsonResponse({'success': True, 'message': 'Mensaje enviado correctamente'})

    return JsonResponse({'success': False, 'message': 'Por favor complete todos los campos requeridos'})
