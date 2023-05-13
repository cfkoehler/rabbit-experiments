docker build -f consumer/Dockerfile -t rabbitmq-test:consumer consumer/
docker build -f producer/Dockerfile -t rabbitmq-test:producer producer/
docker build -f monitor/Dockerfile -t rabbitmq-test:monitor monitor/