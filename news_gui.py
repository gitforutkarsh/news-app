import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk, Image
import io
import webbrowser
import os
from dotenv import load_dotenv

class NewsApp:
    def __init__(self):
        # Load API key from environment variable
        load_dotenv()
        self.api_key = os.getenv('NEWS_API_KEY', 'default_key')  # Replace 'default_key' with a fallback or error

        # Fetch data from News API
        self.data = self.fetch_news()
        self.current_index = 0

        # Initialize GUI
        self.load_gui()

        # Load first news item or error message
        if self.data and self.data.get('articles'):
            self.load_news_item(self.current_index)
        else:
            self.display_error_message()

    def fetch_news(self):
        try:
            response = requests.get(
                f'https://newsapi.org/v2/top-headlines?country=us&apiKey={self.api_key}',
                timeout=10
            )
            response.raise_for_status()  # Raise an exception for bad status codes
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching news: {e}")
            return None

    def load_gui(self):
        self.root = Tk()
        self.root.geometry('600x800')
        self.root.resizable(True, True)
        self.root.title('My News')
        self.root.configure(bg="#333")

        self.main_frame = Frame(self.root, bg='#333')
        self.main_frame.pack(fill=BOTH, expand=True)

    def clear(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def load_image(self, url):
        try:
            if url:
                raw_data = urlopen(url).read()
                im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
                return ImageTk.PhotoImage(im)
        except:
            # Fallback to a placeholder image (ideally a local file)
            placeholder_url = 'https://via.placeholder.com/350x250?text=No+Image'
            raw_data = urlopen(placeholder_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            return ImageTk.PhotoImage(im)

    def load_news_item(self, index):
        self.clear()
        article = self.data['articles'][index]

        # Load and display image
        img_url = article.get('urlToImage')
        photo = self.load_image(img_url)
        label = Label(self.main_frame, image=photo, bg='#333')
        label.image = photo
        label.pack(pady=(10, 20))

        # Display title
        title = article.get('title', 'No title available')
        heading = Label(self.main_frame, text=title, bg='#333', fg='white', wraplength=550, justify='center')
        heading.config(font=('verdana', 15, 'bold'))
        heading.pack(pady=(10, 20))

        # Display description
        description = article.get('description', 'No description available')
        details = Label(self.main_frame, text=description, bg='#333', fg='white', wraplength=550, justify='center')
        details.config(font=('verdana', 12))
        details.pack(pady=(10, 20))

        # Navigation buttons
        self.create_navigation_buttons(index)

    def create_navigation_buttons(self, index):
        frame = Frame(self.main_frame, bg='#333')
        frame.pack(expand=True, fill=BOTH)

        # Previous button (disabled if at first article)
        prev = Button(frame, text='Prev', width=16, height=3, command=lambda: self.load_news_item(index - 1))
        prev.pack(side=LEFT, padx=5)
        prev.config(state=NORMAL if index > 0 else DISABLED)

        # Read More button
        read = Button(frame, text='Read More', width=16, height=3, command=lambda: self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT, padx=5)

        # Next button (disabled if at last article)
        next = Button(frame, text='Next', width=16, height=3, command=lambda: self.load_news_item(index + 1))
        next.pack(side=LEFT, padx=5)
        next.config(state=NORMAL if index < len(self.data['articles']) - 1 else DISABLED)

    def open_link(self, url):
        if url:
            webbrowser.open(url)

    def display_error_message(self):
        self.clear()
        error_message = Label(self.main_frame, text="Failed to load news. Please try again later.", bg='#333', fg='white', font=('verdana', 15, 'bold'))
        error_message.pack(pady=(100, 20))

        # Add retry button
        retry = Button(self.main_frame, text='Retry', width=16, height=3, command=self.retry_fetch)
        retry.pack(pady=10)

    def retry_fetch(self):
        self.data = self.fetch_news()
        if self.data and self.data.get('articles'):
            self.current_index = 0
            self.load_news_item(self.current_index)
        else:
            self.display_error_message()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    obj1 = NewsApp()
    obj1.run()