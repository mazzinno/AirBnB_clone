# Airbnb Clone - Python

## Project Description



This project is a simplified Python implementation of an Airbnb clone. It aims to replicate some of the basic functionalities of the Airbnb platform, allowing users to manage and book accommodations. The project includes a command-line interface (CLI) for users to interact with the system.


## Command Interpreter

The command interpreter is a text-based interface that enables users to interact with the Airbnb clone. It interprets user commands and performs corresponding actions, such as creating listings, booking accommodations, and managing user accounts.


## How to Start

1. **Clone the Repository:**
   ```
   git clone https://github.com/your-username/airbnb-clone-python.git
   cd airbnb-clone-python
   ```

2. **Install Dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Run the Command Interpreter:**
   ```
   python airbnb_cli.py
   ```

## How to Use

Once the command interpreter is running, you can interact with the Airbnb clone by entering commands. Here are some of the available commands:


- `create_user`: Create a new user account.
  ```
  > create_user JohnDoe
  ```

- `create_listing`: Create a new accommodation listing.
  ```
  > create_listing "Cozy Apartment" 2 "123 Main St"
  ```

- `book_accommodation`: Book an accommodation for a specific user.
  ```
  > book_accommodation JohnDoe "Cozy Apartment" 2023-12-01 2023-12-10
  ```

- `list_accommodations`: List all available accommodations.
  ```
  > list_accommodations
  ```

- `user_bookings`: Display the bookings for a specific user.
  ```
  > user_bookings JohnDoe
  ```

- `exit` or `quit`: Exit the command interpreter.
  ```
  > exit
  ```

## Examples

1. **Creating a User:**
   ```
   > create_user AliceSmith
   User AliceSmith created it successfully.
   ```

2. **Creating a Listing:**
   ```
   > create_listing "Downtown Loft" 4 "456 Oak St"
   Listing "Downtown Loft" created successfully.
   ```


3. **Booking an Accommodation:**
   ```
   > book_accommodation AliceSmith "Downtown Loft" 2023-11-20 2023-11-25
   Accommodation booked successfully for AliceSmith from 2023-11-20 to 2023-11-25.
   ```

4. **Listing Accommodations:**
   ```
   > list_accommodations
   Available Accommodations:
   1. "Downtown Loft" - Max Guests: 4 - Address: 456 Oak St
   ```

5. **User Bookings:**
   ```
   > user_bookings AliceSmith
   Bookings for User AliceSmith:
   1. "Downtown Loft" - Check-in: 2023-11-20 - Check-out: 2023-11-25
   ```

## Created and Reviewed By:
```
Hamza Esadik | hamza.esadik.m@gmail.com
```
```
Yassine Amgarou | yassineamgarou@gmail.com
```
