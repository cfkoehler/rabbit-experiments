FROM bash:4.4.23

COPY monitor.sh /monitor.sh
RUN chmod +x /monitor.sh
RUN apk update && apk add jq curl
ENV host=localhost:15672
ENV username=guest
ENV password=guest
ENV service=rabbitMQ
ENV interval=5
ENTRYPOINT bash ./monitor.sh -u $username -p $password -h $host -s $service -i $interval