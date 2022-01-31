#ESSA INTERFACE GRÁFICA USADA PARA CONECTAR NO WIFI SÓ FUNCIONARA NO SISTEMA OPERACIONAL LINUX


import os

wifi = 'pip3 install wifi'
wireless = 'pip3 install wireless'
packaging = 'pip3 install packaging'

#os.system(wifi)
print('CONCLUIDO')
#os.system(wireless)
print('CONCLUIDO')
#os.system(packaging)
print('CONCLUIDO')

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from wifi import Cell
from wireless import Wireless
import requests
import RPi.GPIO as GPIO
import time
import json
import sys
import _thread
import http.client


        

class Application:



    #Método Conectar rede wireless
    def ConectaRede(self):
        try:
            rede = self.rede.get(self.rede.curselection())
        except Exception:
            rede = ""
        if rede == "":
            messagebox.showinfo("Erro", "Favor Selecionar uma rede")
        else:
            ## Conecta na rede wireless
            print (rede)
            senhaRede = self.senhaRede.get()
            if senhaRede == "":
                messagebox.showinfo("Erro", "Favor digitar uma senha para conectar à rede")
            else:
                print (senhaRede)
                wire = Wireless()
                wire.connect(ssid=rede,password=senhaRede)

                wire = Wireless()
                wire.connect(ssid=rede,password=senhaRede)

                dados_rede = {'redeWifi': rede, 'password': senhaRede}  # DICIONÁRIO EM PYTHON
                dados_rede = json.dumps(dados_rede)  # CONVERTE O DICIONARIO PYTHON EM DICIONARIO JSON

                arquivo = open('DadosConectWireless.json', 'w')
                arquivo.write(dados_rede)

                


        

    def __init__(self, master=None):
        

        self.fontePadrao = ("Arial", "10")
        
        self.sextoContainer = Frame(master, background='#dfe4b0')
        self.sextoContainer["pady"] = 5
        self.sextoContainer.place(x=200, y=150)

        self.setimoContainer = Frame(master, background='#dfe4b0')
        self.setimoContainer["pady"] = 1
        self.setimoContainer.place(x=200, y=200)

        self.oitavoContainer = Frame(master, background='#dfe4b0')
        self.oitavoContainer["pady"] = 1
        self.oitavoContainer.place(x=150, y=400)

        self.nonoContainer = Frame(master, background='#dfe4b0')
        self.nonoContainer["pady"] = 1
        self.nonoContainer.place(x=200, y=230)

        self.decimoContainer = Frame(master)
        self.decimoContainer["pady"] = 1
        self.decimoContainer.place(x=200, y=200)

       
      
        ###### SELECIONAR A RDE WIRELESS
        
        self.titulo = Label(self.sextoContainer, text="SELECIONE A REDE WIRELESS",font=self.fontePadrao, background='#dfe4b0')
        self.titulo.pack()

        scrollbar2 = Scrollbar(self.setimoContainer) 
        scrollbar2.pack(side = RIGHT, fill = BOTH) 
        self.rede = Listbox(self.setimoContainer,width=30)

        ct = 0
        cells = Cell.all('wlan0')
        for cell in cells:
            ct = ct + 1
            self.rede.insert(ct, cell.ssid)
        
        self.rede.config(yscrollcommand = scrollbar2.set)
        scrollbar2.config(command = self.rede.yview) 
        self.rede.pack()

        self.senhaLabel = Label(self.oitavoContainer,text="Senha Rede : ", font=self.fontePadrao, background='#dfe4b0')
        self.senhaLabel.pack(side=LEFT)

        self.senhaRede = Entry(self.oitavoContainer)
        self.senhaRede["width"] = 15
        self.senhaRede["font"] = self.fontePadrao
        self.senhaRede.pack(side=LEFT)

        
        self.conectarWifi = Button(self.oitavoContainer)
        self.conectarWifi["text"] = "Conectar rede Wireless"
        self.conectarWifi["font"] = ("Calibri", "8")
        self.conectarWifi["width"] = 20
        self.conectarWifi["command"] = self.ConectaRede
        self.conectarWifi.pack()

        #self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        #self.mensagem.pack()
       

def imprimir():
    variavel = v_check.get()
    if variavel == 'wifi':
        Application(root)
    if variavel == 'cabo':
        tick()
        try:
            arquivo = open('DadosConectWireless.json', 'w')
            arquivo.write('')
        except Exception:
            print('Erro')


def tick(validador = False,sec = None):
    msg['text'] = 'O programa fechará em'
    if validador == False:
        sec = int(10)
    if sec == 0:
        root.destroy()
        
    else:
        sec = sec - 1
        time['text'] = sec
        time.after(1000, lambda : tick(True,sec))
        
        
def interfaceUsuario():
    window =''
    global root
    root = tk.Toplevel(window)
    
    root.geometry("570x500")
    root.configure(background='#dfe4b0')


    titulo = Label(root, text='SELECIONE QUAL FORMA USARÁ PARA CONECTAR A INTERNET', background='#dfe4b0').place(x=140, y=20, height=20)

    global v_check 
    global msg
    global time
    v_check = StringVar()
    box = Frame(root, borderwidth= 1, relief='solid').place(x=180, y=50, width=280, height=60)
    check_Cabo = Radiobutton(root, text='Cabo de rede', command='', value='cabo', variable = v_check).place(x= 185, y= 55)
    check_wifi = Radiobutton(root, text='Rede WiFi', command='', value='wifi', variable = v_check).place(x=185, y=81)
    botao = Button(root, text='OK', command=imprimir, height=1, width=8).place(x=370, y = 78)

    time = Label(root, background='#dfe4b0')
    time.place(x= 355, y=150)
    msg = Label(root, background='#dfe4b0')
    msg.place(x= 220, y=150)

    root.after(30000,root.destroy)
    root.mainloop()


try:
    with open('DadosConectWireless.json', encoding='utf-8') as dados_json:
        dados = json.load(dados_json)  # LE O DICIONARIO JSON
        rede = dados["redeWifi"]
        senhaRede = dados["password"]
        print(rede)
        print(senhaRede)
        wire = Wireless()
        wire.connect(ssid=rede, password=senhaRede)
        print('CONECTOU')
except Exception:
    print('Não existe arquivo')

interfaceUsuario()

    



