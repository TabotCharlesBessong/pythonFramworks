# Basic HTTP Login Project

This project implements a simple HTTP login system using Flask. It includes a basic login form where users can enter their credentials.

## Project Structure

```
basic-http-login
├── src
│   ├── app.py          # Entry point of the application
│   └── templates
│       └── login.html  # HTML structure for the login form
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## Requirements

To run this project, you need to have Python installed along with Flask. You can install the required dependencies by running:

```
pip install -r requirements.txt
```

## Running the Application

1. Navigate to the `src` directory:
   ```
   cd src
   ```

2. Run the application:
   ```
   python app.py
   ```

3. Open your web browser and go to `http://127.0.0.1:5000/login` to access the login form.

## Usage

- Enter your username and password in the form fields and click the submit button to log in.
- The application will handle the form submission and provide appropriate feedback.

## License

This project is open source and available under the MIT License.