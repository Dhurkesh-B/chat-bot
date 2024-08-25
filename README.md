# Chat-Bot using Streamlit, LangChain, and Google Generative AI

Welcome to the **Chat-Bot** project! This application is an interactive Q&A chatbot built using **Streamlit**, **LangChain**, and **Google Generative AI**. The bot is designed to answer user queries based on data provided by the user in a file.

## 🚀 Project Overview

This chatbot allows users to ask questions based on data loaded from a file. By leveraging LangChain's prompt templates and Google's Gemini model, the chatbot provides accurate and relevant responses, making it a powerful tool for data exploration.

## 💡 Key Features

- **Interactive Chat Interface**: Maintains a session-based chat history, offering a smooth and engaging user experience.
- **Custom Data Loading**: Users can easily load their own data files, making the chatbot adaptable to various use cases.
- **Seamless Integration**: Built with Streamlit, the app combines a clean UI with powerful backend processing.

## 🔧 Technology Stack

- **Streamlit**: For building the interactive user interface.
- **LangChain**: To handle the prompt templates and processing.
- **Google Generative AI (Gemini 1.5)**: To power the chatbot with AI-generated responses.
- **Python**: The programming language used for backend logic and processing.

## 📋 Requirements

To run this project locally, you need to have the following installed:

- Python 3.7 or later
- Pip (Python package installer)
- A `.env` file with your environment variables (such as API keys)

## 📦 Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Dhurkesh-B/chat-bot.git
   cd chat-bot
   ```

2. **Install the Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables:**

   Create a `.env` file in the project directory and add your environment variables (e.g., API keys).

   ```bash
   touch .env
   ```

   Add the following lines to your `.env` file:

   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

4. **Run the App:**

   ```bash
   streamlit run app.py
   ```

   The app will be accessible at `http://localhost:8501`.

## 🛠️ Usage

1. **Load Your Data:**

   Place your data file (e.g., `info.txt`) in the project directory. The file should contain the information that the chatbot will use to answer questions.

2. **Ask Questions:**

   Enter your query in the chat input box, and the chatbot will respond based on the loaded data.

## 🌟 Live Demo

Check out the live demo of the chatbot here: [Chat-Bot Live App](https://chat-bot-dhurkeshb.streamlit.app/)

## 🤝 Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## 📧 Contact

For any questions or suggestions, feel free to reach out:

- **Name**: Dhurkesh B.
- **Email**: dhurkeshmyself@gmail.com
- **LinkedIn**: [Dhurkesh B.](https://www.linkedin.com/in/dhurkeshb/)
