from django.shortcuts import render
from django.http import HttpResponse
from contato.contato_form import FormContato
from django.utils.html import strip_tags

from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from blog import settings

def contato(request):
    return render(request, 'contato/contato.html', {'form': FormContato()})


def processa_contato(request):

    if request.method == 'POST':
        contato = FormContato(request.POST)

        if contato.is_valid():
            try:
                enviar_email(contato)
                enviar_email_com_template(contato)
                obj_contato = contato.save()
                obj_contato.save()

                messages.success(request, 'Mensagem encaminhada com sucesso!')
                return render(request, 'contato/contato.html', {'form': FormContato()})

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        else:
            return render(request, 'contato/contato.html', {'form': contato})

    return render(request, 'contato/contato.html', {'form': FormContato()})



def enviar_email(contato):
    send_mail(contato.cleaned_data['assunto'],
              contato.cleaned_data['mensagem'],
              contato.cleaned_data['email'],
              [settings.EMAIL_HOST_USER],
              fail_silently=False)


# este método faz encaminhamento de email utilizando templates html para formatar o corpo do email.
def enviar_email_com_template(contato):

 
    html_content = render_to_string('email_templates/confirmacao_mensagem.html',
                                    {'nome': contato.cleaned_data['nome'],
                                     'assunto': contato.cleaned_data['assunto']})

   
    text_content = strip_tags(html_content)

 
    msg = EmailMultiAlternatives(contato.cleaned_data['assunto'],
                                 text_content,
                                 settings.EMAIL_HOST_USER,
                                 [contato.cleaned_data['email']])

    msg.attach_alternative(html_content, "text/html")

    msg.send()