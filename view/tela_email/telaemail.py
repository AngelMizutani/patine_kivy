from kivymd.uix.screen import MDScreen 
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty

import time

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

Builder.load_file("view/tela_email/telaemail.kv")

class TelaEmail(MDScreen):
    email_text = ObjectProperty(None)
    assunto_text = ObjectProperty(None)
    mensagem_text = ObjectProperty(None)
    
    def irParaLista(self):
        self.parent.current = 'lista'
        self.email_text.text = ''
        self.mensagem_text.text = ''
        self.assunto_text.text = ''

    def enviarEmail(self):
        label = self.ids.texto_info

        if (self.email_text.text == ''):
            label.text = 'O email é obrigatório!'

        elif (self.assunto_text.text == ''):
            label.text = 'O assunto é obrigatório!'

        elif (self.mensagem_text.text == ''):
            label.text = 'A mensagem é obrigatória!'

        else:
            try:
                self.ids.spinner.active = True

                #Configuração
                host = 'smtp.gmail.com'
                port = 587
                user = 'testeemailpw21@gmail.com'
                password = '123teste456'

                #Criando objeto
                label.text = 'Criando objeto servidor...'
                server = smtplib.SMTP(host, port)

                #Login com servidor
                label.text = 'Acessando o servidor...'
                server.ehlo()
                server.starttls()
                server.login(user, password)

                #Criando mensagem
                message = 'De: ' + self.email_text.text + '\n' + self.mensagem_text.text
                label.text = 'Criando mensagem...'
                email_msg = MIMEMultipart()
                email_msg['From'] = user
                email_msg['To'] = user
                email_msg['Subject'] = '[PATINE_KIVY] - ' + self.assunto_text.text
                email_msg.attach(MIMEText(message, 'plain'))

                #Enviando mensagem
                label.text = 'Enviando mensagem...'
                server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())

                self.ids.spinner.active = False
                label.text = 'Mensagem enviada com sucesso!'
                label.theme_text_color = 'Custom'
                label.text_color = 0, 1, 0, 1
                server.quit()

                self.email_text.text = ''
                self.mensagem_text.text = ''
                self.assunto_text.text = ''

                self.irParaLista()
            
            except Exception as e:
                self.ids.spinner.active = False
                label.text = 'Ocorreu um erro!'
                print(e)