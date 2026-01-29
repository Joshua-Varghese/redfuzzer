# 🔍 RedFuzzer: Subdomain & Directory Enumerator

RedFuzzer is a lightweight Python tool for subdomain and directory fuzzing, designed for reconnaissance and quick enumeration during penetration testing or bug bounty hunting.

---

## ⚙️ Features

- 🌐 **Subdomain Enumeration**: Discover subdomains using wordlist-based fuzzing
- 📁 **Directory Fuzzing**: Find hidden directories and paths on target websites
- 📦 **Minimal Dependencies**: Only requires `requests` and standard library modules
- ⚡ **Fast & Lightweight**: Simple codebase with no unnecessary overhead
- 🔧 **Easy to Use**: Straightforward command-line interface

---

## 📋 Prerequisites

Before using RedFuzzer, make sure you have:

- Python 3.6 or higher
- `requests` library

Install dependencies:
```bash
pip install requests
```

---

## 🚀 Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd redfuzzer
```

2. Install required dependencies:
```bash
pip install requests
```

---

## 📖 Usage

### Command Syntax
```bash
python3 rf.py <target-url> <option> <wordlist-file>
```

### Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `<target-url>` | The target domain with protocol | `https://example.com` |
| `<option>` | Type of fuzzing: `subdomain` or `dir` | `subdomain` |
| `<wordlist-file>` | Path to wordlist file (one entry per line) | `wordlist.txt` |

### Examples

**Enumerate Subdomains:**
```bash
python3 rf.py https://example.com subdomain subdom.txt
```

**Fuzz Directories:**
```bash
python3 rf.py https://example.com dir wordlist.txt
```

**With Custom Wordlist:**
```bash
python3 rf.py https://target.com subdomain custom-wordlist.txt
```

---

## 📁 Project Structure

```
redfuzzer/
├── rf.py              # Main script for subdomain and directory fuzzing
├── urlfilter.py       # Utility module for URL domain filtering
├── subdom.txt         # Sample subdomain wordlist
└── README.md          # Documentation
```

---

## 🔧 How It Works

### 1. **Subdomain Enumeration** (`subdomain` option)
- Takes each word from the wordlist
- Constructs a URL: `scheme://subdomain.basedomain`
- Sends HTTP requests and logs response status codes
- Collects all valid subdomains (those that don't error out)

### 2. **Directory Fuzzing** (`dir` option)
- Takes each word from the wordlist
- Constructs a URL: `scheme://basedomain/directory`
- Sends HTTP requests and checks for status code 200
- Collects all directories that return a 200 status code

### 3. **Domain Filtering**
- The `urlfilter.py` module removes `www.` prefix from domain names
- Normalizes domains for consistent enumeration

---

## 📝 Wordlist Format

Wordlists should be plain text files with one entry per line:

**Example (subdom.txt):**
```
www
mail
admin
test
api
dev
staging
backup
```

---

## ⚠️ Important Disclaimer

**LEGAL WARNING:** This tool sends requests to target servers that will be logged in their network activity. 

- **Only use this tool on systems you own or have explicit written permission to test**
- Unauthorized network scanning may be illegal in your jurisdiction
- The author is not responsible for misuse of this tool
- Always follow responsible disclosure practices
- Comply with all applicable laws and regulations

---

## 🔍 Output

The tool displays real-time progress with:
- Current request count and total wordlist size
- HTTP status codes for each request
- Final URL being tested
- Summary of all discovered subdomains/directories at the end

**Example Output:**
```
Enumerating Subdomains of example.com

(1 of 100) www: 301-->https://www.example.com
(2 of 100) mail: 404-->https://mail.example.com
(3 of 100) admin: 200-->https://admin.example.com
...
Subdomain Enumeration Finished
Valid subdomains are -->[www, admin, ...]
```

---

## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'requests'` | Run `pip install requests` |
| `FileNotFoundError: wordlist.txt` | Ensure the wordlist file exists in the current directory or provide the full path |
| `requests.exceptions.ConnectionError` | Check your internet connection or the target domain availability |
| Connection timeouts on large wordlists | Target server may be rate-limiting; consider adding delays between requests |

---

## 📚 Future Improvements

- [ ] Add threading/multiprocessing for faster enumeration
- [ ] Support for custom headers and user-agent rotation
- [ ] Timeout and retry configuration
- [ ] Response filtering by status code
- [ ] Export results to JSON/CSV formats
- [ ] Proxy support (HTTP/HTTPS/SOCKS5)
- [ ] Colored output for better readability
- [ ] Verbose mode for detailed logging
- [ ] Exclude status codes option


---

## 👤 Author

[Joshua Varghese/Joshua-Varghese]

---

## 💬 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## ❓ Questions & Support

For issues, feature requests, or questions, please:
- Open an issue on GitHub
- Contact the maintainers
- Check existing documentation for solutions
