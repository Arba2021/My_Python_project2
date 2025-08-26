# Password Fortress & Generator

<div align="center">
  ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗
  ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
  ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
  ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
  ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
  ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝

🛡️ Password Fortress & Generator 🛡️
A Command-Line Powerhouse for Crafting Unbreakable Passwords 🚀

</div>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Security-SHA--256%20Hashing-red?style=for-the-badge&logo=lock" alt="Security">
</p>

<p align="center">
  Welcome to <strong>Password Fortress</strong>, a slick and secure command-line password generator built with Python. Forge passwords that laugh in the face of hackers! With entropy calculations, SHA-256 hashing, and customizable options, it’s your ultimate weapon for creating bulletproof passwords. 😎
</p>

<p align="center">
  <img src="https://i.imgur.com/g25E032.gif" alt="Terminal Animation" width="700"/>
</p>

## 🌟 Features

* **Customizable Character Sets**: Uppercase, lowercase, digits, symbols.
* **Entropy Insights**: Measures password strength in bits with `log2(pool_size ^ length)`.
* **Strength Feedback**: Labels as <font color="red">Weak</font>, <font color="orange">Medium</font>, or <font color="green">Strong</font>.
* **Stealth Mode**: Hide passwords in the console for extra security.
* **Secure Hashing**: Save passwords as SHA-256 hashes.
* **Flexible Outputs**: Export to `.txt`, `.csv`, or `.json`.
* **Custom Prefixes**: Add personal starters to passwords.
* **Cross-Platform Colors**: Uses `colorama` for console color on any OS.

## 🚀 Getting Started

### Prerequisites

* **Python 3.10+**
* Install required package:

```bash
pip install colorama
```

### Quick Start

```bash
git clone https://github.com/Arba2021/My_Python_project2.git
cd My_Python_project2
python password_generator.py
```

### Example Session

```
Welcome to the Advanced Password Generator
How many passwords? 3
Length of each password? 12
Show passwords in console? (y/n): y
--- Character Set Selection ---
Enter choice: (a = all, c = custom): a
Include custom prefix? (y/n): y
Enter your custom prefix: Secure

--- Generated Passwords ---
Password 1: SecureK7@mP9 -> Strong (Entropy: 71.45 bits)
Password 2: Securex#2jL$ -> Strong (Entropy: 71.45 bits)
Password 3: Secure9nQz!v -> Strong (Entropy: 71.45 bits)

Save passwords to a file? (txt/csv/json/none): json
Hash passwords before saving for security? (y/n): y
✅ Hashed passwords saved to passwords.json
```

## 🔒 Security Tips

* **Hash It**: Always hash passwords when saving. SHA-256 is one-way.
* **No Plain Text**: Never save unhashed passwords.
* **Entropy Goals**: Aim for >80 bits for elite security.
* **Password Managers**: Store generated passwords in encrypted managers.

## 📄 License

This project is licensed under the MIT License.
