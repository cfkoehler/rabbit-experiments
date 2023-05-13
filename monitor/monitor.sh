#!/bin/bash

Help()
{
   # Display Help
   echo "Query RabbitMQ managemnt endpoint at specific interval to collect total queue size and incoming rates"
   echo
   echo "Syntax: monitor.sh [h|u|p|s|i]"
   echo "required params:"
   echo "h     RabbitMQ host and port (exp: 'localhost:15672')"
   echo "u     RabbitMQ username (exp: 'guest')"
   echo "p     RabbitMQ password (exp: 'guest')"
   echo "s     Service name to have in output message"
   echo "i     Polling interval in Seconds (exp: '10')"
   echo
}

if [ $# == 0 ] ; then
    Help
    exit 1;
fi

while getopts :h:a:u:p:s:i: flag
do
    case "${flag}" in
        h) host=${OPTARG};;
        u) username=${OPTARG};;
        p) password=${OPTARG};;
        s) service=${OPTARG};;
        i) interval=${OPTARG};;
        \?) 
            echo "Error: Invalid option"
            Help
            exit 1;;
    esac
done

while true 
do
    JSON_FMT='{"timestamp":"%s","service":"%s","host":"%s","queue":"%s","count":"%s","rate":"%s"}\n'
    STATS=$(curl -s -u ${username}:${password} http://${host}/api/queues)
    TIME=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
    if [ -z "$STATS" ] || [ $STATS = "[]" ]
    then
        echo "ERROR: Empty or no response from endpoint."
    else
        items=$(echo $STATS | jq -c -r '.[]')
        for item in ${items[@]}; do
            QUEUE_NAME=$(echo $item | jq .name)
            QUEUE_COUNT=$(echo $item | jq .messages)
            QUEUE_INCOME_RATE=$(echo $item | jq .messages_details.rate)
            if [ -z "$QUEUE_NAME" ]
            then
                echo "ERROR: No Queue Name found in response"
            elif [ -z "$QUEUE_COUNT" ]
            then
                echo "ERROR: No Queue count found in response"
            elif [ -z "$QUEUE_INCOME_RATE" ]
            then
                echo "ERROR: No Queue rate found in response"
            else
                printf "$JSON_FMT" "$TIME" "$service" "$host" "$QUEUE_NAME" "$QUEUE_COUNT" "$QUEUE_INCOME_RATE"
            fi
        done
    fi
    sleep $interval
done
