# Watson 🔍
![npm bundle size (version)](https://img.shields.io/badge/version-0.0.1-darkblue)  ![npm bundle size (version)](https://img.shields.io/badge/language-python3-yellow) 

tl;dr automated search via Terminal


A Python script that automates developer-focused web searches directly from the terminal, searching across curated technical resources like Stack Overflow, GitHub, and other developer platforms.

## Usage
  ```bash
   s How to create a class in Cpp ?
   ```
thanks to the s sign a search can be done.

## Features 🚀
- Instant terminal-based searching
- Focused on developer resources (Stack Overflow, GitHub, MDN, etc.)

## Installation 📦

### Requirements
- Python 3.8+
- pip package manager

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Dave200s1/Watson.git
   cd Watson
2. Make it a executable:
    ```bash
   chmod +x main.py
   ```
3. Create a alias (Fish-shell example)
     * 3.1
    ```bash
     sudo nano ~/.config/fish/config.fish
    ```
    * 3.2 (The path where you have save the script)
    ```bash
     alias s 'python3 ~/PathTo/main.py' -s
    ```
    * 3.3
   ```bash
     source ~/.config/fish/config.fish
    ```

   



   
