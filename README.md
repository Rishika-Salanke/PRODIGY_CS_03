This project is a simple Python-based tool to evaluate password strength.
Using Python’s `re` library, the tool analyzes a password, scores its complexity on a scale of 1-5, and provides feedback for improving weak or moderate passwords.

How It Works:
The tool uses regular expressions to assess various password characteristics, such as length, use of upper and lowercase letters, numbers, and special characters.
Based on these checks, it assigns a score to the password and categorizes its strength.

Scoring Criteria
- **Score 1-2:** Weak password
- **Score 3-4:** Moderate password
- **Score 5:** Strong password

Feedback
The tool provides customized feedback to help users strengthen weak or moderate passwords by recommending specific improvements.

Prerequisites
This tool requires Python and the `re` library (included in Python by default).

Installation
Clone this repository and run the script in any Python environment.

```bash
git clone https://github.com/yourusername/password-complexity-checker.git
cd password-complexity-checker
