# Example and test project to learn how to interface with rabbitMQ

## Lightweight script to monitor rabbitMQ queues and counts
To run:
- Build Images: `sh buildImages.sh`
- Run Docker Compose: `docker-compose up`

Example output:
```
{"timestamp":"2023-05-13T23:25:04Z","service":"rabbitMQ","host":"rabbitmq:15672","queue":""A"","count":"30","rate":"0.4"}
{"timestamp":"2023-05-13T23:25:04Z","service":"rabbitMQ","host":"rabbitmq:15672","queue":""B"","count":"20","rate":"0"}
{"timestamp":"2023-05-13T23:25:04Z","service":"rabbitMQ","host":"rabbitmq:15672","queue":""C"","count":"21","rate":"0"}
{"timestamp":"2023-05-13T23:25:10Z","service":"rabbitMQ","host":"rabbitmq:15672","queue":""A"","count":"30","rate":"0"}
{"timestamp":"2023-05-13T23:25:10Z","service":"rabbitMQ","host":"rabbitmq:15672","queue":""B"","count":"0","rate":"-4"}
{"timestamp":"2023-05-13T23:25:10Z","service":"rabbitMQ","host":"rabbitmq:15672","queue":""C"","count":"23","rate":"0.4"}
{"timestamp":"2023-05-13T23:25:15Z","service":"rabbitMQ","host":"rabbitmq:15672","queue":""A"","count":"31","rate":"0.2"}
{"timestamp":"2023-05-13T23:25:15Z","service":"rabbitMQ","host":"rabbitmq:15672","queue":""B"","count":"0","rate":"0"}
{"timestamp":"2023-05-13T23:25:15Z","service":"rabbitMQ","host":"rabbitmq:15672","queue":""C"","count":"25","rate":"0.4"}
```