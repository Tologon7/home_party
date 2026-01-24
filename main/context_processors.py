# main/context_processors.py
from django.conf import settings

def site_settings(request):
    """Добавляет настройки сайта в контекст шаблонов."""
    return {
        'SITE_NAME': getattr(settings, 'SITE_NAME', 'Ак-өргө тойуна чакыруу'),
        'SITE_DOMAIN': getattr(settings, 'SITE_DOMAIN', 'localhost:8000'),
        'CONTACT_EMAIL': getattr(settings, 'CONTACT_EMAIL', ''),
        'CONTACT_PHONE': getattr(settings, 'CONTACT_PHONE', ''),
        'INVITATION': getattr(settings, 'INVITATION', {}),
    }