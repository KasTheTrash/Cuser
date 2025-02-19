# Cuser - User Creation Utility

## Overview
Cuser (Custom User Creator) is a lightweight desktop application built with Python/Tkinter that provides a secure interface for creating new users in a PostgreSQL database. The application features a clean, modern UI for adding users with different permission levels and secure password handling, making it an ideal tool for system administrators and user management tasks.

## Features
- Secure user creation with password hashing (bcrypt)
- Email validation
- Multi-level permission system (3 levels)
- PostgreSQL database integration
- Modern Tkinter GUI interface
- Input validation and error handling
- Responsive user feedback
- Tab-order navigation support

## Technical Stack
- Python 3.x
- Tkinter for GUI
- PostgreSQL for database
- psycopg2 for database connectivity
- bcrypt for password encryption
- Custom asset management

## Prerequisites
- Python 3.x
- PostgreSQL Server
- Required Python packages:
  ```
  psycopg2
  bcrypt
  ```

## Database Configuration
The application requires a PostgreSQL database with the following configuration:
```
Database Name: StoreManager
Host: localhost
Port: 5432
User: postgres
```

### Required Database Tables
- `users` (id, username, password, email)
- `user_permissions` (user_id, permissions_id)

## Installation
1. Clone the repository
   ```bash
   git clone https://github.com/KasTheTrash/cuser.git
   ```

2. Install required packages
   ```bash
   pip install psycopg2 bcrypt
   ```

3. Set up the PostgreSQL database using the provided schema

4. Run the application
   ```bash
   python cuser.py
   ```

## Security Features
- Password hashing using bcrypt
- Case-insensitive username storage
- Secure database connections
- Input sanitization

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
Feel free to use, modify and changes everything in this repository!!!

## Author
[kasTheTrash]

## Acknowledgments
- Icons and assets designed for Cuser
- Built with security and user experience in mind
