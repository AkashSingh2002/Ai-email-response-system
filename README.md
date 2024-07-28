# Film Equipment Inquiry System

This project is designed to classify incoming emails into three categories: inquiries, reviews, and assistance requests. Based on the classification, it provides automated responses using an SQL database and a free OpenAI API proxy.

## Features

1. **Email Classification**: Classifies emails into inquiries, reviews, and assistance requests using AI.
2. **Automated AI Responses**: Uses the OpenAI API to generate intelligent responses based on email content.
3. **Database Integration**: Stores and retrieves film equipment details to handle inquiries about product availability and pricing.

## Prerequisites

- Python 3.6 or higher
- `requests` library

## Project Structure

```plaintext
.
├── config.py
├── database.py
├── email_handler.py
├── main.py
└── README.md
