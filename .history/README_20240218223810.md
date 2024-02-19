# My Docker Project

This project demonstrates how to set up a Docker environment to run a Python application that processes data from text files. It includes a Dockerfile for building a custom Docker image and a `docker-compose.yml` for easy deployment.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Docker and Docker Compose installed on your system. Follow the installation guides on the [Docker website](https://docs.docker.com/get-docker/) and the [Docker Compose documentation](https://docs.docker.com/compose/install/).

## Project Structure

my_docker_project/
├── data/ # Directory for input text files
├── app/ # Python script and other source files
├── data/ # data directory with IF.txt and Limerick-1.txt
├── output/ # Directory where result.txt is saved
├── Dockerfile # Dockerfile for building the image
└── docker-compose.yml # Docker Compose file for deployment

## Usage

### Prepare Data:
   Place your `IF.txt` and `Limerick-1.txt` files inside the `data/` directory if not placed already.

### Build and Run with Docker:
   To build the Docker image and run the container, execute the following commands in your project's root directory:

    docker-compose up

The docker-compose.yml file is configured to mount the data/ directory into the container and execute the Python script automatically.

### Outputs
The Python script will generate a result.txt file inside the container at /home/output/, which will contain the processing results. To view the output on the console, the script is set to print the contents of result.txt before the container exits.

### Customization
You can modify the Python script under the app/ directory to add additional functionalities or process different files as per your requirements.