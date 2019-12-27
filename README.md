# tornado-demo
Play with tornado and async tools

ORIGIN: https://github.com/zetaops/websocket-tornado-rabbitmq-example

### Run
#### Start RabbitMQ
```
docker run -d --hostname my-rabbit --name some-rabbit -p 15672:15672 -p 5672:5672 -p 5671:5671 -p 25672:25672 -p 4369:4369 rabbitmq:3-management
```
#### Start worker processes
```
python worker.py manage=3
```
#### Start Tornado
```
python app.py
```

### Use
1. Open index page `http://127.0.0.1:8888/` and enter number
2. Check RabbitMQ web `http://127.0.0.1:15672/` username/password: guest