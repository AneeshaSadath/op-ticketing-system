from celery import Celery


app = Celery(
    broker="amqp://guest:guest@my_rabbitmq",
    backend="rpc://",
    include=["tasks"],
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="Europe/Oslo",
    enable_utc=True,
)


@app.task(name="tasks")
def op_ticket_generator(id, data):
    with open("op_ticket.txt", "w+") as fp:
        text_list = [
            f"OP Number : {id}\n",
            f"Name : {data['first_name'] + ' ' + data['last_name']}\n",
            f"Gender : {data['gender']}\n",
            f"Age : {data['age']}\n",
            f"Place : {data['address_1']+','+ data['address_2']}\n",
            "Diagnosis : ",
        ]
        fp.writelines(text_list)
