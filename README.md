# Password Dictionary Generator

This project provides a versatile tool for generating password dictionaries, offering both a web-based interface and a command-line interface (CLI). It's designed to help with penetration testing and security assessments by creating variations of base passwords, including common substitutions and special characters.

## Features

### Web Version
-   **File Upload:** Upload a text file with base passwords (one per line).
-   **Manual Input:** Manually enter base passwords.
-   **Customizable Variations:** Specify the number of variations to generate per base password.
-   **Special Character Inclusion:** Option to add special characters to variations.
-   **Downloadable Dictionary:** Generated password dictionary available for download.
-   **Interactive Chat:** An integrated chat feature powered by the ChatGPT API to answer questions about password security and usage.
-   **Modern UI:** A Matrix-like background, responsive design, and a draggable/collapsible chat window.

### Terminal (CLI) Version
-   **Manual Input:** Enter base passwords directly in the terminal.
-   **File Input:** Provide a path to a file containing base passwords.
-   **Customizable Variations:** Define the number of variations per password.
-   **Special Character Inclusion:** Option to include special characters.
-   **Output to File:** Save the generated dictionary to a specified file.

## Getting Started

### Prerequisites
Make sure you have Python 3 installed on your system.

### Installation
1.  Clone this repository:
    ```bash
    git clone https://github.com/f50kdev/Python-Network-Hack.git
    cd Python-Network-Hack
    ```
2.  Install the required Python packages:
    ```bash
    pip3 install -r requirements.txt
    ```
    (If `requirements.txt` is not present, you can install them manually: `pip3 install flask python-dotenv openai`)

### Running the Web Version
1.  **Set your OpenAI API Key:** The web application uses the ChatGPT API for its chat feature. You need to set your OpenAI API key as an environment variable.
    ```bash
    export OPENAI_API_KEY='YOUR_OPENAI_API_KEY'
    ```
    Replace `'YOUR_OPENAI_API_KEY'` with your actual API key. **Do not share your API key publicly or commit it to version control.**

2.  **Start the Flask application:**
    ```bash
    python3 app.py
    ```
3.  **Access the application:** Open your web browser and go to `http://127.0.0.1:5000`.

### Running the Terminal (CLI) Version
Execute the `password_generator.py` script directly:

```bash
python3 password_generator.py
```
Follow the on-screen prompts to generate your password dictionary.

## Project Status & Contributions

This project is actively maintained and open for improvements! Feel free to contribute by opening issues for bugs or feature requests, or by submitting pull requests. Your contributions are highly welcome to make this tool even better.

## Creator

**Faustino Henriques**
Email: eadpea2020@gmail.com