# Malicious URL Classifier

This is the project for the Artificial Intelligence for Cybersecurity course of the University of Pisa.

## Table of Contents

- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Running the Application](#running-the-application)
- [Stopping the Application](#stopping-the-application)
- [Licence](#licence)

## Project Structure

The repository is organized as follows:
```
malicious-url-classifier/
├── app/
├── datasets/
│ ├── kaggle.csv
│ └── dataset.csv
├── Dockerfile
├── docker-compose.yml
├── Malicious_URL.ipynb
├── decision_tree.svg
├── Presentation.pdf
└── README.md
```

### Folder Descriptions

- **app/**: Contains the sample application code and its dependencies.
- **datasets/**: Contains the datasets used for this project.
    - **kaggle.csv**: the initial raw dataset for the benign URLs.
    - **dataset.csv**: the final dataset obtained after the feature extraction process.
- **Dockerfile**: Dockerfile for the sample application.
- **docker-compose.yml**: Docker Compose configuration file.
- **Malicious_URL.ipynb**: Jupyter Notebook of the project.
- **decision_tree.svg**: An image of the final decision tree extracted.
- **Presentation.pdf**: The presentation used for this project.
- **README.md**: This document.

## Prerequisites

Before running the application, ensure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Running the Application

1. **Clone the repository**:
    ```sh
    git clone https://github.com/gabrielepongelli/malicious-url-classifier.git
    cd malicious-url-classifier
    ```

2. **Build and run the containers**:
    ```sh
    docker compose up --build
    ```

    This command will build the Docker images and start the containers as defined in the `docker-compose.yml` file.

3. **Access the application**:
    - The application will be available at `http://localhost:5000`.

## Stopping the Application

To stop the application and remove the containers, run:

```sh
docker compose down
```

This command stops and removes all the containers defined in the `docker-compose.yml` file.

## Licence

This project is licensed under the MIT License - see the LICENSE file for details.