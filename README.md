# Microservice Book Recommender System / Book Ranking 

This project demonstrates a simple book recommendation system / Book Ranking ( Learning To Rank - LTR ) implemented using microservice architecture.
It was developed within a short timeframe  with the primary goal of gaining familiarity with microservices.

## Project Overview

This project consists of the following microservices:

- **Data_extractor**: This component is responsible for reading the dataset from an external source, such as a CSV file. The read data is then validated and stored in the database.
- **Database**: A database system, such as MongoDB, where the proccesed dataset is stored.
- **RabbitMQ**: RabbitMQ is used as a messaging tool for communication between services.
- **Data_provider**: This component is used by the model component. It reads the dataset from the database based on requests received from the model.
- **Model**: The main ML model component.
- **Api_gateway**: An API REST interface is provided to interact with the system for obtaining recommendations. This service handles the task of exposing the API.

The project utilizes Docker Compose to orchestrate the microservices.

## Sample JSON Input and Output

Below is an example of the sample JSON input and output for the API gateway:

```json
// Sample JSON input for the API gateway
{
  "uid": 27805,
  "book_list": [
    3310,
    12043,
    45178,
    1219
  ]
}

// Sample JSON output from the API gateway

{
  "result": [
    {
      "score": 0.1866184063642305,
      "rank": 1.0,
      "book_id": 1219
    },
    {
      "score": 0.06636246424900774,
      "rank": 2.0,
      "book_id": 3310
    },
    {
      "score": 0.01976787174440288,
      "rank": 4.0,
      "book_id": 12043
    },
    {
      "score": 0.05708887972970883,
      "rank": 3.0,
      "book_id": 45178
    }
  ],
  "error": {},
  "meta": {
    "elapsed_time(s)": 4.573072671890259
  },
  "status": 200
}
```

## Usage

Build and start the microservices using Docker Compose: `docker-compose up -d`

## Limitations and Improvements

It's important to note the limitations of this project due to its simple implementation within a short time frame and it has room for further enhancements and optimizations.
- Some modules within the project contain hardcoded values, particularly in dealing with data features. It is recommended to enhance the system by implementing a more flexible configuration system that enables easy modification of parameters.
- Consider implementing more sophisticated restart policies for services based on specific failure scenarios for better fault tolerance.
- Implementing database replication mechanisms should be considered to ensure improved data redundancy and availability.
- The logging mechanism in the project has limited functionality. It would be beneficial to expand and improve the logging capabilities to gather comprehensive information and facilitate effective debugging and monitoring.
- The project lacks adequate error handling, fault tolerance mechanisms, and exception management.

## Contact
For any questions or further information about this project, please contact me
at [miladghafouri0@gmail.com]

Thank you for checking out my project! Your feedback and suggestions are highly appreciated.