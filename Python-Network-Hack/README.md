# Python Network Security Toolkit

A collection of Python scripts for network security analysis and testing using Scapy. This toolkit provides various network security tools for educational and authorized security testing purposes.

## 👨‍💻 Author

**Faustino**

- 📧 Email: eadpea2020@gmail.com
- 🔗 LinkedIn: [Faustino Henriques]
- 📸 Instagram: Henriques.dev

## ⚠️ Disclaimer

This toolkit is intended for:
- Educational purposes
- Authorized security testing
- Network security research
- System administration and security auditing

**IMPORTANT**: Only use these tools on networks you own or have explicit permission to test. Unauthorized network scanning or testing may be illegal.

## 🛠️ Requirements

- Python 3.7+
- Scapy
- Required Python packages (install via `pip install -r requirements.txt`):
  - scapy
  - netfilterqueue
  - python-nmap

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Python-Network-Hack.git
cd Python-Network-Hack
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Features

- Network scanning and discovery
- Packet manipulation and analysis
- ARP spoofing detection
- Network traffic monitoring
- Custom packet crafting

## 📋 Usage

Each script in this toolkit serves a specific purpose. Here are some examples:

### Network Scanner
```bash
python network_scanner.py -t 192.168.1.1/24
```

### ARP Spoofer
```bash
python arp_spoofer.py -t 192.168.1.5 -g 192.168.1.1
```

### Packet Sniffer
```bash
python packet_sniffer.py -i eth0
```

## 🔒 Security Best Practices

1. Always obtain proper authorization before testing
2. Document all testing activities
3. Follow responsible disclosure practices
4. Keep tools and dependencies updated
5. Use in controlled environments

## 📚 Documentation

Detailed documentation for each tool can be found in the `docs` directory.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Legal Notice

The authors of this toolkit are not responsible for any misuse or damage caused by this program. This toolkit is for educational purposes only.