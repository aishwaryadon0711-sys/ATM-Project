Simple ATM System (OOP Abstraction)
This project demonstrates the core concepts of Object-Oriented Programming (OOP) in Python, specifically focusing on Abstraction and Inheritance.

By using Python's abc (Abstract Base Classes) module, we define a standard interface for an ATM system that ensures any specific bank implementation (like ATM_SBI) provides the necessary functionalities.

🚀 Key Features
Abstraction: Uses the ATM abstract class to define required methods (check_bal, deposit, withdraw).

Security: Simple PIN-based verification for every transaction.

Encapsulation: Manages user data and account balance within the class instance.

Validation: Checks for sufficient funds during withdrawals and validates PIN inputs.

