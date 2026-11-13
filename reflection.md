# Lab 5 — Reflection

**Student:** Srijan Kumar  
**SRN:** PES1UG24CS467  
**Topic:** Static Code Analysis — Hotel Booking System

### 1. What is static code analysis, and why is it useful?

Static code analysis examines source code without executing the program. It helps identify potential bugs, security vulnerabilities, and coding-style problems early, making software easier to maintain and more reliable.

### 2. What did Pylint, Bandit, and Flake8 help identify?

Pylint identified code-quality issues such as missing docstrings, poor naming, and unused variables. Bandit detected security risks such as unsafe eval usage, weak hashing, and shell execution. Flake8 identified formatting and PEP 8 style violations.

### 3. Which important issues did you fix in the hotel booking program?

I replaced unsafe eval usage with a numeric seasonal-rate calculation, changed MD5 hashing to SHA-256, replaced shell execution with normal Python output, and used secure random generation for booking references. I also corrected exception handling and removed the mutable default argument.

### 4. How did static analysis improve the final program?

Static analysis helped improve the program's security, readability, and maintainability. After making the corrections, Bandit reported no issues, Flake8 reported no style violations, and Pylint achieved a score of 10.00/10. These results demonstrated the value of using multiple analysis tools together.