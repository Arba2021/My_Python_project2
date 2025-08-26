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
  <!-- Badges -->
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Security-SHA--256%20Hashing-red?style=for-the-badge&logo=lock" alt="Security">
</p>

<p align="center">
  Welcome to <strong>Password Fortress</strong>, a slick and secure command-line password generator built with Python. This isn’t just a tool—it’s a vault of security and style, forging passwords that laugh in the face of hackers. With entropy calculations, SHA-256 hashing, and customizable options, it’s your ultimate weapon for creating bulletproof passwords! 😎
</p>

<p align="center">
  <img src="https://i.imgur.com/g25E032.gif" alt="Terminal Animation" width="700"/>
</p>

## 🌟 Why This Rocks
- **Customizable Character Sets**: Mix uppercase, lowercase, digits, and special characters to craft your perfect password recipe. 🛠️
- **Entropy Insights**: Measure password strength in bits with `log2(pool_size ^ length)`. Higher bits = tougher to crack! 🧠
- **Strength Feedback**: Real-time analysis labels passwords as <font color="red">Weak</font>, <font color="orange">Medium</font>, or <font color="green">Strong</font>. 🌈
- **Stealth Mode**: Hide passwords in the console ([hidden]) for sneaky, secure generation. 🕵️‍♂️
- **Secure Hashing**: Save passwords as SHA-256 hashes to keep them locked tight. 🔒
- **Flexible Outputs**: Export to `.txt`, `.csv`, or `.json` for all your data needs. 💾
- **Custom Prefixes**: Add a personal touch to your passwords with custom starters. ✍️
- **Cross-Platform Vibes**: Thanks to `colorama`, the console pops with color on any system. 🎨

## 🚀 Get Started

### Prerequisites
- **Python 3.10+** (we’re modern like that 🐍)
- Install the required package:
  ```bash
  pip install colorama

 Example Outputbash

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

 Security FirstHash It: Always hash passwords (y) when saving. SHA-256 is a one-way fortress—hackers can’t reverse it! 
No Plain Text: Saving unhashed passwords is risky. The tool warns you to stay secure. 
Entropy Goals: Aim for >80 bits for elite security. Longer passwords + diverse characters = win. 
Password Managers: Use this tool to generate passwords, then store them in an encrypted manager.

