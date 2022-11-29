import pika

def callback(ch, method, properties, body):
   print(" [x] RECEBIDO ->  %r" % body)

connection = pika.BlockingConnection(
   pika.ConnectionParameters('localhost')
)

channel = connection.channel()
channel.queue_declare(queue='sistemas_distribuidos')
channel.basic_consume(
   queue='sistemas_distribuidos',
   auto_ack=True,
   on_message_callback=callback
)
print('-----------------------------------------------------------')
print('|      FILIAL: CANAL DE RECEBIMENTO DE MENSAGENS          |')
print('-----------------------------------------------------------\n')

print(' [*] AGUARDANDO POR MENSAGENS DA MATRIZ... PARA SAIR DESTE CANAL PRESSIONE: "CTRL+C"')

channel.start_consuming()