import pika
import time

connection = pika.BlockingConnection(
   pika.ConnectionParameters('localhost')
)

channel = connection.channel()
channel.queue_declare(queue='hello')

messages = [
   "PRIMEIRA MENSAGEM: [LEMBRETE] CORES DE ROUPAS QUE NAO PODEM SER LAVADAS JUNTAS",
   "SEGUNDA MENSAGEM: ROUPAS AZUIS...",
   "TERCEIRA MENSAGEM: ROUPAS VERDES...",
   "QUARTA MENSAGEM: ROUPAS AMARELAS...",
   "QUINTA MENSAGEM: ROUPAS BRANCAS...",

]

def subMenu():
   mensagem = int(input('DIGITE UM NUMERO ENTRE 1 E 3 PARA UTILIZAR O MENU: '))

   while (mensagem != 3):

      print('\nOPCAO SELECIONADA: [1]')

      if mensagem == 1:

         for message in messages:
            channel.basic_publish(
               exchange='',
               routing_key='hello',
               body=message
            )

            print("\n[X] ENVIADA -> '" + message + "'")
            time.sleep(1)

         print('\nLOTE DE MENSAGENS ENVIADO AS FILIAIS! RETORNANDO AO MENU...\n')

         menuPrincipal()

      elif mensagem == 2:

         print('\nOPCAO SELECIONADA: [2]')
         
         newMessage = input('\nINFORME QUAL MENSAGEM DESEJA ENVIAR AS FILIAIS: ')

         channel.basic_publish(exchange='', routing_key='hello', body=newMessage)

         print('\nRETORNANDO AO MENU PRINCIPAL...\n')

         menuPrincipal()

      else:
         print('\n[ERRO] DIGITE UM NÚMERO ENTRE 1 E 3 PARA USAR O MENU\n')

         menuPrincipal()

      print('\nOPCAO SELECIONADA: [3] ')

      print('\nENCERRANDO O SISTEMA...')

      connection.close()         

def menuPrincipal():
    print('-----------------------------------------------------------')
    print('|               MENU DA MATRIZ (LAVANDERIA)               |')
    print('-----------------------------------------------------------')
    print('|                                                         |')
    print('| [1] ENVIAR LOTE DE MENSAGENS                            |')    
    print('| [2] ENVIAR MENSAGEM ESPECIFICA AS FILIAIS               |')
    print('| [3] SAIR                                                |')
    print('|                                                         |')
    print('-----------------------------------------------------------\n')

    subMenu()

menuPrincipal()

'''
   for message in messages:
      channel.basic_publish(
         exchange='',
         routing_key='hello',
         body=message
      )

      print(" [x] Enviada '" + message + "'")
      time.sleep(1)
'''
connection.close()