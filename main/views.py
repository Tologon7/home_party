from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        status = request.POST.get('status')
        message = request.POST.get('message', '')

        if name and status:
            subject = f"RSVP от {name}: {status}"
            body = f"Имя: {name}\nСтатус: {status}\nСообщение: {message}"
            try:
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL or 'no-reply@invite.kg',
                    ['замдиректор@почта.kg'],  # ← сюда почту замдиректора
                    fail_silently=False,
                )
                messages.success(request, 'Спасибо! Ваш ответ отправлен.')
            except Exception as e:
                messages.error(request, f'Ошибка: {e}. Попробуйте позже.')
        else:
            messages.error(request, 'Заполните имя и статус.')

    return render(request, 'main/home.html')