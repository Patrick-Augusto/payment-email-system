from flask import Flask, request, jsonify
import pika

app = Flask(__name__)

def send_payment_message(payment_info):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='payment_queue')
    channel.basic_publish(exchange='', routing_key='payment_queue', body=payment_info)
    connection.close()

@app.route('/process_payment', methods=['POST'])
def process_payment():
    payment_info = request.json
    send_payment_message(str(payment_info))
    return jsonify({"message": "Payment processed and message sent to queue."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
