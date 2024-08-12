import pika
import smtplib
from email.mime.text import MIMEText

def send_email(payment_info):
    print(f"Enviando email de confirmação para: {payment_info}")

def callback(ch, method, properties, body):
    payment_info = body.decode()
    send_email(payment_info)

def consume_payment_queue():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='payment_queue')
    channel.basic_consume(queue='payment_queue', on_message_callback=callback, auto_ack=True)
    print(' [*] Aguardando mensagens. Para sair, pressione CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    consume_payment_queue()
