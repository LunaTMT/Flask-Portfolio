# Portfolio

## Installation

### Open your terminal/console

Navigate to the downloaded folder

<figure><img src=".gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

### Create a virtual environment

#### Windows

`python -m venv venv`&#x20;

#### Linux/Mac

`python3 -m venv venv`

### Activate the virtual environment

#### Windows

`.\venv\Scripts\activate`

#### Linux/Mac

`source venv/bin/activate`

### Install dependencies

`pip install -r requirements.txt`

### Run flask

`flask run`

### View site

Simple hold ctrl or cmd and click on the local host link (127.0.01) as shown below.

<figure><img src=".gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

Please ensure you end the flask run session as is stated in the terminal by pressing ctrl + c, otherwise you might have trouble trying to rerun the server on the port already in use (The one you have just opened but have not shut down correctly).
