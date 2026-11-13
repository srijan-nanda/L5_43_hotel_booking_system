# Lab 5 — Static Code Analysis: Issue Documentation

**Student:** Srijan Kumar  
**SRN:** PES1UG24CS467  
**File analysed:** hotel_booking_system.py

## Identified Issues

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Shell command execution | Security | 58 | Bandit B605 identifies unsafe shell execution through os.system(). | Replace with a safe Python print operation. |
| Weak MD5 hashing | Security | 47 | Bandit B324 identifies MD5 as an insecure hashing algorithm. | Replace MD5 with SHA-256. |
| Unsafe eval usage | Security | 42 | Bandit B307 identifies eval() as potentially unsafe because it evaluates arbitrary expressions. | Replace dynamic evaluation with a safe numeric rate parameter. |
| Hard-coded secret | Security | 62 | Bandit B105 detects a hard-coded reservation token. | Read the secret from an environment variable or remove the demonstration secret. |
| Insecure random generator | Security | 51 | Bandit B311 warns that the standard random module is unsuitable for security-sensitive values. | Use the secrets module for booking references. |
| Broad exception handling | Bug/Security | 26 | Bare except catches every exception and hides unexpected errors. Bandit B110 also flags the suppressed exception. | Catch the expected exception explicitly and handle it. |
| Mutable default argument | Bug | 15 | booking_log=[] can retain shared state between function calls. | Use None as the default and initialize a new list inside the function. |
| Unused import | Style | 6 | The math module is imported but never used. | Remove the unused import. |
| Unused variables | Maintainability | 31, 41 | cleaning_deposit and base_price are assigned but not used. | Remove unnecessary variables or use them meaningfully. |
| File handling | Maintainability | 55–58 | The file is opened and closed manually without a context manager or explicit encoding. | Use with open() and specify UTF-8 encoding. |
| Comparison to None | Style | 32 | Flake8 E711 recommends identity comparison rather than equality comparison with None. | Use `is None`. |
| Line too long | Style | 19 | Flake8 E501 reports a line exceeding the configured length. | Split the line appropriately. |
| Missing newline | Style | 73 | Flake8 W292 reports no newline at the end of the file. | Add a final newline. |
| Missing function docstrings | Maintainability | 46, 50, 54, 61 | Pylint C0116 reports missing function descriptions. | Add meaningful docstrings. |
| Invalid variable name | Style | 55 | Pylint C0103 flags the single-letter variable name f. | Rename it to a descriptive name. |

## Summary

The original analysis identified security vulnerabilities, potential bugs, maintainability problems, and formatting violations. The fixes will prioritize all Bandit findings, resolve Flake8 violations, and improve the Pylint score to above 9.5/10 while preserving the intended hotel booking functionality.