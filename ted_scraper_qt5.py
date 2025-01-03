import sys
import os
import re
import requests
from bs4 import BeautifulSoup
import json
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                           QLineEdit, QPushButton, QTextEdit, QLabel, QHBoxLayout,
                           QMessageBox)

class TranscriptScraperApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('TED Talk Transcript Scraper')
        self.setGeometry(100, 100, 800, 600)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # URL input
        url_label = QLabel('Enter TED Talk URL:')
        layout.addWidget(url_label)
        
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText('https://www.ted.com/talks/...')
        layout.addWidget(self.url_input)
        
        # Buttons layout
        button_layout = QHBoxLayout()
        
        # Scrape button
        self.scrape_button = QPushButton('Get Transcript')
        self.scrape_button.clicked.connect(self.scrape_transcript)
        button_layout.addWidget(self.scrape_button)
        
        # Convert and Save button
        self.markdown_button = QPushButton('Convert to Markdown and Save')
        self.markdown_button.clicked.connect(self.convert_and_save_markdown)
        self.markdown_button.setEnabled(False)
        button_layout.addWidget(self.markdown_button)
        
        layout.addLayout(button_layout)
        
        # Result display
        result_label = QLabel('Transcript:')
        layout.addWidget(result_label)
        
        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)
        layout.addWidget(self.result_display)
        
        # Store the original transcript
        self.original_transcript = ""
        self.talk_title = ""

    def scrape_transcript(self):
        url = self.url_input.text().strip()
        
        if not url:
            self.result_display.setText("Please enter a URL")
            return
        
        try:
            response = requests.get(url)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                script_tag = soup.find('script', {'type': 'application/ld+json'})
                
                if script_tag:
                    try:
                        json_data = json.loads(script_tag.string)
                        self.original_transcript = json_data.get('transcript', 'No transcript found')
                        self.talk_title = json_data.get('name', 'ted_talk')
                        self.result_display.setText(self.original_transcript)
                        self.markdown_button.setEnabled(True)
                    except json.JSONDecodeError:
                        self.result_display.setText("Failed to parse JSON data")
                        self.markdown_button.setEnabled(False)
                else:
                    self.result_display.setText("No script tag with type application/ld+json found")
                    self.markdown_button.setEnabled(False)
            else:
                self.result_display.setText(f"Failed to retrieve the page. Status code: {response.status_code}")
                self.markdown_button.setEnabled(False)
                
        except requests.exceptions.RequestException as e:
            self.result_display.setText(f"Error occurred: {str(e)}")
            self.markdown_button.setEnabled(False)

    def convert_and_save_markdown(self):
        if not self.original_transcript:
            return
            
        # Split into sentences (considering multiple punctuation marks)
        sentences = re.split(r'(?<=[.!?])\s+', self.original_transcript)
        
        # Create markdown content
        markdown_text = f"# {self.talk_title}\n\n"
        
        # Convert each sentence to h3 heading
        for sentence in sentences:
            sentence = sentence.strip()
            if sentence:  # Only process non-empty sentences
                markdown_text += f"### {sentence}\n\n"
        
        # Update display
        self.result_display.setText(markdown_text)
        
        # Save to file
        try:
            # Create filename from talk title
            filename = re.sub(r'[^\w\s-]', '', self.talk_title.lower())
            filename = re.sub(r'[-\s]+', '-', filename)
            filename = f"{filename}.md"
            
            # Get the directory of the current working directory (script execution path)
            filepath = os.path.join(os.getcwd(), filename)
            
            # Write the markdown content
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(markdown_text)
            
            QMessageBox.information(
                self,
                "Success",
                f"Markdown file saved successfully as:\n{filepath}"
            )
            
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Failed to save file: {str(e)}"
            )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TranscriptScraperApp()
    window.show()
    sys.exit(app.exec_())
