import webbrowser as wb
import sys
import os
import datetime as dt
import subprocess as sb
import tkinter as tk
import time
import signal
import getpass as gp
import calendar
import email
import smtplib as sl
import smtpd
import json
import winsound
import random
import pyttsx3
import win10toast
import smtplib
import ssl
import tweepy
from win10toast import ToastNotifier
from urllib.request import urlopen

dt = dt.datetime.now()
words = ['google', 'pesquisar', 'procurar na internet por', 'procurar']
Opening_message = "E aí?"
engine = pyttsx3.init()
only_time = dt.now().strftime('%H-%M-%S')
only_date = dt.now().strftime('%d-%m-%Y')
auth = tweepy.OAuthHandler('Twitter auths')
auth.set_access_token('acess tokens')
notif = ToastNotifier()
port = 587
api = tweepy.API(auth)
smtp_server = 'smtp.gmail.com'
edadaiugdaiugdaiugda = open('mydmus1.txt', 'w')
edadaiugdaiugdaiugda.close()
f = open('mydmus1.txt', 'r')
email = f.read()
f.close()
pswv = 0

print(Opening_message)
engine.say(Opening_message)
engine.runAndWait()
gfigfdu = 1
while gfigfdu == 1:
    q = input('>>>')

    if q in ['O que você pode fazer?', 'o que você pode fazer?', 'o que você pode fazer', 'O que voce pode fazer']:
        print('Eu posso fazer muitas coisas diferentes, por exemplo, você pode dizer:')
        engine.say('Eu posso fazer muitas coisas diferentes, por exemplo, voce pode dizer')
        engine.runAndWait()
        print("Que horas é?;")
        engine.say("Que horas e?")
        engine.runAndWait()
        print('Abrir Youtube;')
        engine.say('Abrir Youtube')
        engine.runAndWait()
        print('Definir lembrete;')
        engine.say('Definir lembrete')
        engine.runAndWait()
        print("Vamos jogar um jogo?;")
        engine.say("Vamos jogar um jogo")
        engine.runAndWait()
        print('Abrir site;')
        engine.say('Abrir site')
        engine.runAndWait()
        print("Eu gostaria de mudar meu email;")
        engine.say("Eu gostaria de mudar meu email")
        engine.runAndWait()
        print("E muito mais!")
        engine.say("E muito mais!")
        engine.runAndWait()

    elif q in ["que horas é?", "que horas são", "Que horas é?", "Que horas são?",
               "que horas é", 'que horas são?', "horas?", 'Horas?', 'horas', 'Horas']:
        print(only_time)
        engine.say(only_time)
        engine.runAndWait()

    elif q in ['tweetar', 'Tweetar']:
        engine.say('O que tweetar?')
        engine.runAndWait()
        print('O que tweetar')
        twt = input('>>>')
        api.update_status(twt)

    elif q in ["qual dia é?", "que dia é hoje?", "Qual é a data?", "Que dia é hoje?", 'Que dia é?',
               "qual é o dia", "qual é a data?", 'Qual é o dia', 'que dia é hoje', 'Que dia é hoje']:
        print(only_date)
        engine.say(only_date)
        engine.runAndWait()

    elif q in ["Enviar e-mail", "enviar um email", 'Enviar um email', "enviar e-mail",
               "Enviar email", "enviar email", 'enviar um e-mail', 'Enviar um e-mail']:
        engine.say("Qual e a senha do seu email?")
        engine.runAndWait()
        print("Qual é a senha do " + email + "?")
        password = input('>>>')
        engine.say("Para quem?")
        engine.runAndWait()
        receiver_email = input('E-mail do receptor: ')
        subjectc = input('Assunto: ')
        subject = "Assunto: " + subjectc
        content = input('Conteúdo: ')
        message = subject + "\n" + content

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(str(email), str(password))
            server.sendmail(email, receiver_email, message)

    elif q in ["Definir lembrete", "definir lembrete", "lembrete", "adicionar lembrete",
               'Lembrete', 'Adicionar lembrete']:
        print('Do que devo lembrá-lo?')
        engine.say('Do que devo lembrar?')
        engine.runAndWait()
        text = str(input('>>>'))
        print('Em quantos minutos?')
        engine.say('Em quantos minutos?')
        engine.runAndWait()
        local_time = float(input('>>>'))
        local_time = local_time * 60
        engine.say("Nao feche o programa!")
        engine.runAndWait()
        time.sleep(local_time)
        notif.show_toast("Lembrete!", text, threaded=True, icon_path='none', duration=0)
        print(text)
        engine.say(text)
        engine.runAndWait()
        time.sleep(0.5)

    elif q in ["Vamos jogar um jogo", "vamos jogar um jogo", "Vamos jogar",
               "Chateado", "Estou chateado", "chateado", "estou chateado", "eu não sei",
               "Eu não sei", "não sei", "tédio", "Tédio", "vamos jogar"]:
        print('Você quer jogar um jogo?')
        engine.say('Voce quer jogar um jogo?')
        engine.runAndWait()
        yon = input('>>>')

        if yon == 'sim' or 'Sim':
            num = random.randint(1, 20)
            engine.say('Ok, adivinhe um número de 1 a 20')
            engine.runAndWait()
            at = int(input('Ok, Adivinhe um número de 1 a 20:   '))
            while at != num:
                if at < num:
                    print("Muito baixo")
                    engine.say("Muito baixo")
                    engine.runAndWait()
                elif at > num:
                    print("Muito alto")
                    engine.say("Muito alto")
                    engine.runAndWait()
                at = int(input('Tentar novamente:    '))
            print('Correto')
            engine.say('Correto')
            engine.runAndWait()

    elif q in ["email", "e-mail", "Qual é o meu email", "qual é o endereço do meu email",
               "Qual é o endereço do meu email", "Qual é o meu email?"]:
        print('Seu e-mail é ' + email)
        engine.say('Seu email e ' + email)
        engine.runAndWait()

    elif q in ["abrir unity", "Abrir Unity", "Abrir unity", "abrir Unity", "abrir Unity Hub", "abrir unity hub",
               "Abrir unity hub", "Abrir Unity Hub", "Abrir Unity hub"]:
        print('  ')
        print('Abrindo Unity Hub... ')
        engine.say('Abrindo unity hub')
        engine.runAndWait()
        time.sleep(2)
        os.startfile('C:\\Program Files\\Unity Hub\\Unity hub')
    elif q in ["Eu gostaria de mudar o email", "Eu gostaria de mudar o meu e-mail", "mudar email",
               "Eu gostaria de mudar o e-mail", "mudar meu email"]:
        engine.say('Para que voce deseja alterar seu endereco de email?')
        t = open('mydmus1.txt', 'w')
        print('Para que você deseja alterar seu endereço de e-mail?  ')
        engine.runAndWait()
        email = input('>>>')
        t.write(email)
        t.close()

    elif q in ["abrir maps", "Abrir Maps", "Abrir Google Maps", "Abrir maps", "abrir google maps"]:
        print('  ')
        print('Abrindo Google Maps...')
        engine.say('abrindo google maps')
        engine.runAndWait()
        time.sleep(2)
        wb.open('https://maps.google.com/')

    elif q in ["abrir messagens", "Abrir Messagens", "Abrir messagens", "abrir Messagens"]:
        print('  ')
        print('Abrindo Google Messages...')
        engine.say('abrindo google messages')
        engine.runAndWait()
        time.sleep(2)
        wb.open('https://messages.google.com/web')

    elif q in ['Abrir site', 'abrir site', 'Abrir Site', 'abrir Site']:
        engine.say("Qual e o endereço do site")
        print('Digite o endereço do site (exemplo.com)')
        engine.runAndWait()
        w = input('>>>')
        print('  ')
        print('Abrindo ' + w + '...')
        engine.say('abrindo' + w)
        engine.runAndWait()
        wb.open('https://' + w)

    elif q in ['abrir wikipedia', 'abrir Wikipedia', 'Abrir Wikipedia', 'Abrir wikipedia', 'abrir wiki',
               'Abrir wiki', 'Abrir Wiki', 'abrir Wiki']:
        print('  ')
        print('Abrindo Wikipedia...')
        engine.say('abrindo wikipedia')
        engine.runAndWait()
        time.sleep(2)
        wb.open('https://en.wikipedia.org/wiki/Main_page')

    elif q in ['Soma', 'soma']:
        engine.say('quais sao os 2 numeros para soma')
        print('Quais são os 2 números para soma?')
        engine.runAndWait()
        first = int(input("Primeiro número>  "))
        second = int(input("Segundo número>  "))
        print(first + second)

    elif q in ['subtrair', 'Subtrair']:
        engine.say('quais sao os 2 numeros para subtrair')
        print('Quais são os 2 números para subtrair?')
        engine.runAndWait()
        first = int(input("Primeiro número>  "))
        second = int(input("segundo número>  "))
        print(first - second)

    elif q in ['Multiplicar', 'multiplicar']:
        engine.say('quais sao os 2 numeros para multiplicar')
        print('Quais são os 2 números para multiplicar?')
        engine.runAndWait()
        first = int(input("Primeiro número>  "))
        second = int(input("Segundo número>  "))
        print(first * second)

    elif q in ["Dividir", "dividir"]:
        engine.say('quais sao os 2 numeros para dividir')
        print('Quais são os 2 números para dividir?')
        engine.runAndWait()
        first = int(input("Primeiro número>  "))
        second = int(input("Segundo número>  "))
        print(first / second)

    elif q in ['abrir', 'Abrir']:
        engine.say('o que voce quer que eu abra')
        print("O que você quer que eu abra?")
        engine.runAndWait()
        o = input('>>>')

        if o in ['youtube', 'YouTube', 'Youtube', 'youtube']:
            print('  ')
            print('Abrindo YouTube...')
            time.sleep(2)
            wb.open('https//www.youtube.com/')

        elif o in ['unity', 'Unity', 'Unity Hub', 'Unity hub', "unity hub", 'unity Hub']:
            print('  ')
            print('Abrindo Unity Hub...')
            time.sleep(2)
            os.startfile("C:\\Program Files\\Unity Hub\\Unity hub")

        elif o in ['maps', 'Maps', 'Google Maps', 'Google Mpas', 'google maps']:
            print('  ')
            print('Abrindo Google Maps...')
            time.sleep(2)
            wb.open('https://maps.google.com/')

        elif o in ['messages', 'Messages', 'Google Messages', 'Google Messages']:
            print('  ')
            print('Abrindo Google Messages...')
            time.sleep(2)
            wb.open('https://messages.google.com/web')

        elif o in ['um site', 'Um site', 'Site', 'site']:
            print('Digite o endereço do site (exemplo.com)')
            w = input('>>>')
            print('  ')
            print('Abrindo o site...')
            time.sleep(2)
            wb.open('https://' + w)

        elif o in ['wikipedia', 'Wikipedia', 'wiki', 'Wiki']:
            print('  ')
            print('Abrindo Wikipedia...')
            time.sleep(2)
            wb.open('https://en.wikipedia.org/wiki/Main_Page')

        else:
            engine.say('procurar na internet por' + q)
            engine.runAndWait()
            wb.open('https://www.google.com/search?q=' + q + '&oq=' + q + '&aqs=chrome..69i57.6936j0j9&sourceid=chrome&ie=UTF-8')

    elif q in words:
        if 'google' in q:
            wbs = q.replace('google', '')
            wb.open('https://www.google.com/search?q=' + wbs + '&oq=' + q + '&aqs=chrome..69i57.6936j0j9&sourceid=chrome&ie=UTF-8')
        elif 'pesquisar' in q:
            wbs = q.replace('pesquisar', '')
            wb.open('https://www.google.com/search?q=' + wbs + '&oq=' + q + '&aqs=chrome..69i57.6936j0j9&sourceid=chrome&ie=UTF-8')
        elif 'procurar' in q:
            wbs = q.replace('procurar', '')
            wb.open('https://www.google.com/search?q=' + wbs + '&oq=' + q + '&aqs=chrome..69i57.6936j0j9&sourceid=chrome&ie=UTF-8')

    else:
        engine.say('Pesquisando na internet por' + q)
        engine.runAndWait()
        wb.open('https://www.google.com/search?q=' + q + '&oq=' + q + '&aqs=chrome..69i57.6936j0j9&sourceid=chrome&ie=UTF-8')

