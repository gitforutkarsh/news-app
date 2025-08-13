# NewsApp
A simple desktop application built with Python and Tkinter to fetch and display the latest news headlines from the News [
API](https://newsapi.org). The app features a user-friendly interface with navigation buttons to browse articles, view images, titles, and descriptions, and open full articles in a web browser.


# Features

- Fetches top news headlines from the News API (US region by default).
- Displays article images, titles, and descriptions in a clean Tkinter GUI.
- Supports navigation between articles with "Prev" and "Next" buttons.
- Includes a "Read More" button to open the full article in a web browser.
- Handles errors gracefully (e.g., missing images, failed API requests).
- Configurable API key via environment variables for security.

# Prerequisites
- Python 3.6 or higher
- A News API key 

# Steps

1) Clone the Repository:
```bash
git clone https://github.com/yourusername/newsapp.git
cd newsapp
```

2) Install Dependencies:Install the required Python packages using pip:
```bash
pip install requests pillow python-dotenv
```


4) Set Up the News API Key:
- Create a .env file in the project directory.
- Add your News API key: ```NEWS_API_KEY=your_news_api_key_here```
-  Replace your_news_api_key_here with your actual API key from newsapi.org.


4) Run the Application:
```bash
python news_app.py
```



# Usage

- Launch the application using the command above.
- The app will fetch and display the latest news headlines.
- Use the Prev and Next buttons to navigate between articles.
- Click Read More to open an article in your default web browser.
- If news fails to load (e.g., due to network issues or an invalid API key), an error message will appear with a Retry button.




