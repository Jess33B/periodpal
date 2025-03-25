# README.md

# PeriodPal

PeriodPal is a Flask web application designed to help users track their menstrual cycles, providing insights and personalized recommendations.

## Features

- User authentication (login and registration)
- Cycle tracking and predictions
- User-friendly interface with responsive design
- Data visualization and insights

## Project Structure

```
periodpal
├── app
│   ├── __init__.py
│   ├── models
│   │   ├── __init__.py
│   │   └── user.py
│   ├── routes
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── main.py
│   ├── static
│   │   ├── css
│   │   │   └── style.css
│   │   └── js
│   │       └── main.js
│   └── templates
│       ├── base.html
│       ├── home.html
│       └── auth
│           ├── login.html
│           └── register.html
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/periodpal.git
   cd periodpal
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:

```bash
python run.py
```

Visit `http://127.0.0.1:5000` in your web browser to access the application.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features you'd like to add.

## License

This project is licensed under the MIT License. See the LICENSE file for details.