import requests
from database import check_availability, get_available_items
from config import OPENAI_PROXY_URL, OPENAI_MODEL

def classify_email(body):
    if 'inquiry' in body.lower():
        return 'inquiry'
    elif 'review' in body.lower():
        return 'review'
    elif 'help' in body.lower() or 'assist' in body.lower():
        return 'assistance request'
    else:
        return 'other'

def generate_response(prompt):
    headers = {'Content-Type': 'application/json'}
    data = {
        'model': OPENAI_MODEL,
        'messages': [{'role': 'user', 'content': prompt}]
    }
    
    response = requests.post(OPENAI_PROXY_URL, headers=headers, json=data)
    response.raise_for_status()
    return response.json()['choices'][0]['message']['content']

def handle_email(subject, body):
    email_type = classify_email(body)
    
    if email_type == 'inquiry':
        item_name = body
        record = check_availability(item_name)
        if record:
            if record['availability']:
                response = f"The {record['item']} is available at ${record['price']}."
            else:
                available_items = get_available_items()
                response = f"Sorry, the {record['item']} is not available right now. Here are some similar available items: {', '.join([item['item'] for item in available_items])}."
        else:
            response = "Item not found in our database."
    elif email_type == 'review':
        response = generate_response("Thank you for your review! Please share more details.")
    elif email_type == 'assistance request':
        response = generate_response("Please describe the issue you are facing.")
    else:
        response = generate_response("Thank you for your email. Our team will review it and get back to you shortly.")
    
    return response
