*WeatherBud*

This is a Python application that checks the weather forecast for Bhopal, India, and sends an automated text message to a specified phone number, informing the user whether it will rain or not on that day.

Prerequisites - Before running this application, make sure you have the following:
Python installed on your system (version 3.6 or later)
A Twilio account with an active phone number
An OpenWeatherMap API key

Setup

Clone or download the repository to your local machine.
Install the required Python packages.
Set up environment variables for your OpenWeatherMap API key and Twilio authentication token.
Update the Python script with your Twilio account SID and the phone numbers you want to send and receive the messages from.

Usage

The application will automatically run every morning and check the weather forecast for the day. If the forecast indicates rain, it will send a text message to the specified phone number with the message "Finna Rain Innit ☔️". If no rain is expected, it will send a text message with the message "Not Finna Rain Innit ☔️".
You can set up a cron job or a scheduled task to run the Python script automatically at the desired time each day.
Contributing
If you want to contribute to this project, feel free to submit pull requests or open issues for bug reports or feature requests.

License

This project is licensed under the MIT License.
