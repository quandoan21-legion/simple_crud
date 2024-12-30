# Teammate Management System

This project is a web-based application for managing teammates. It allows users to add, update, and list teammates with details such as username, password, name, email, and active status.

## Technologies Used

- Python
- Flask
- SQLAlchemy
- HTML
- CSS
- JavaScript

## Project Structure
```aiignore
teammate-management-system/
├── app/
│   ├── controllers/
│   │   ├── index_controller.py
│   │   ├── teammate_controller.py
│   │   ├── new_teammate_controller.py
│   │   ├── teammate_info_controller.py
│   │   └── validate_teammate.py
│   ├── models/
│   │   └── teammate_model.py
│   ├── templates/
│   │   ├── login.html
│   │   ├── teammates.html
│   │   ├── new-teammates.html
│   │   ├── teammate-info.html
│   │   ├── change-password.html
│   │   └── user.html
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   ├── __init__.py
│   └── tests/
│       └── test_login_controller.py
├── migrations/
├── venv/
├── requirements.txt
├── README.md
└── run.py
```
## Setup Instructions

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/teammate-management-system.git
    cd teammate-management-system
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the application:
    ```sh
    python3 run.py  
    ```

## Usage

- Navigate to `http://127.0.0.1:5000/` to login.
- Use the following credentials to login as superuser:
    - Username: admin1
    - Password: admin12345
- Click on "Add New Teammate" to add a new teammate.
- Click on "edit" next to a teammate to update their information.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.# simple_crud
