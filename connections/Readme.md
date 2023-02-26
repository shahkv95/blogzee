## Introduction

This project provides a client-server based implementation using python sockets to showcase the differences between long-lived connections and new connections in particular.

The server script listens for incoming connections and returns a response to the client based on the request received.
The client script, on the other hand, establishes a connection with the server and sends a message.

Depending on the type of connection, o.e. either long-lived or new connections, the client script either closes the connection after a single message or maintains the connection for multiple transactions to take place.

## Requirements

- Python 3.x
- Pipenv (optional)

## Installation

1. Clone the repository:
   ```bash
   $ git clone git@github.com:shahkv95/networkz.git
   $ cd networkz
   ```
2. Activate the virtual environment

   ```bash
   PIPENV_VENV_IN_PROJECT=true pipenv shell
   ```

   You can also use any of the other virtual environment

3. Install the dependencies using pipenv:
   ```bash
   $ pipenv install
   ```

## Usage

1. Start the server
   ```bash
   $ python3 server/server.py
   ```
2. In a new terminal, start the client script
   ```bash
   $ python3 client/client.py
   ```

## Configuration

The server and client can be configured by editing the config.py file.

### Server Configuration

- HOST: The hostname or IP address of the server. Default is '127.0.0.1'.
- PORT: The port number on which the server listens. Default is 12345.
- BUFFER_SIZE: The size of the buffer used to receive data from the client. Default is 1024.

### Client Configuration

- HOST: The hostname or IP address of the server. Default is '127.0.0.1'.
- PORT: The port number on which the server listens. Default is 12345.
- BUFFER_SIZE: The size of the buffer used to receive data from the server. Default is 1024.
- NUM_RUNS = 20: The number of times a function should be run in order to calculate the average latency between the two functions.

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE. See the LICENSE file for details.

## Credits

This project was created by Kush Shah.
