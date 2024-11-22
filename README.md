## RainCoatReminder
This project lets you setup a reminder to send you an email for a raincoat at a particular time when the weather in the city becomes rainy or hazy.

## Technologies
- Built using Python 
- with 'schedule' library for scheduling the weather reminder 
- OpenWeatherMap api for fetching weather information
- google-api-python-client for sending email 

## Setup
### 1. Set Up a Google Cloud Project
- Go to the [Google Cloud Console](https://console.cloud.google.com/).
- Create a new project or use an existing one.
- Enable the **Gmail API** for your project.

### 2. Set Up OAuth 2.0 Credentials
- Create OAuth 2.0 client credentials.
- Select **Desktop App** as the Application type when creating the OAuth client ID.
- Download the JSON file containing your client ID and client secret.
- Place this file in the project directory and update the `CREDS_FILE` path in `constants.py`.

### 3. Install dependencies
```bash
pip3 install -r requirements.txt
```
### 4. Setup .env
```bash
SENDER_EMAIL="complete gmail address"
RECIPIENT_EMAIL="complete gmail address"
API_KEY="Open weather map api key"
```
### 5. Run the Application
Use the following command to send emails:
```bash
python3 main.py
```

## Authentication Process
On the first run, you will be redirected to a browser to grant the necessary permissions to your Google account for email access.

