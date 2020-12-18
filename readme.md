# Flask - RabbitMQ Message Broker

Microservices communication example with rabbitMQ as a message broker

## Start Project

`docker-compose up`

## Usage

`curl localhost:5000/job/hey`

And the worker will make a response, in this case will be something like this:
`Hey there!`
