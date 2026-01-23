from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        status = request.POST.get('status', '').strip()
        message_text = request.POST.get('message', '').strip()

        # если гость ничего не написал
        if not message_text:
            message_text = '— без комментария —'

        if name and status:
            subject = f"RSVP: {name} — {status}"

            text_content = (
                f"Имя: {name}\n"
                f"Статус: {status}\n"
                f"Сообщение: {message_text}"
            )

            html_content = f"""
            <html>
              <body style="font-family: Arial, sans-serif; background:#f8f5f0; padding:20px;">
                <div style="max-width:600px; margin:auto; background:#ffffff; border-radius:12px; padding:30px;">
                  <h2 style="color:#1f2a44; margin-top:0;">Жооп тойго</h2>

                  <p><b>Имя:</b> {name}</p>
                  <p><b>Статус:</b> {status}</p>
                  <p><b>Сообщение:</b><br>{message_text}</p>

                  <hr style="margin:30px 0; border:none; border-top:1px solid #eee;">

                  <p style="font-size:12px; color:#888;">
                    Уй тойго чакыруу сайтынан жөнөтүлдү
                  </p>
                </div>
              </body>
            </html>
            """

            try:
                email = EmailMultiAlternatives(
                    subject,
                    text_content,
                    settings.DEFAULT_FROM_EMAIL,
                    ['asel2006.82@mail.ru'],
                )
                email.attach_alternative(html_content, "text/html")
                email.send()

                messages.success(request, 'Сообщение отправлено ✔️')
            except Exception as e:
                messages.error(request, 'Ошибка отправки. Попробуйте позже.')

            return redirect('home')

        messages.error(request, 'Заполните имя и статус.')
        return redirect('home')

    return render(request, 'main/home.html')
