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
  <!-- <img src="https://i.imgur.com/g25E032.gif" alt="Terminal Animation" width="700"/> -->
  <!-- GIF removed due to unavailability. Replace with a new URL when available! -->
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
