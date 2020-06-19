from celery import Celery
app = Celery('task', broker='amqp:localhost//')

@app.task
def reverse(string):
	return string[::-1]