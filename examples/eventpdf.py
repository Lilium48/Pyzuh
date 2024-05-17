import pyzuh
from pyzuh import events
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# Define your API URL and JWT token
api_url = "https://your-api-url.com"
jwt_token = "your-jwt-token"

# Create an instance of your class
client = pyzuh.YourClassName(api_url, jwt_token)

# Define a list of events
events = [
    {"event_type": "login_attempt", "username": "user1", "timestamp": "2024-05-15T12:00:00", "source_ip": "192.168.1.1"},
    {"event_type": "file_access", "filename": "file1.txt", "action": "read", "timestamp": "2024-05-15T12:05:00", "username": "user2"}
    # Add more events as needed
]

# Call the ingest_events method to send the events
try:
    response = client.ingest_events(events, pretty=True, wait_for_complete=False)
    print("Response:", response)
except ValueError as e:
    print("Error:", e)

# Generate PDF report
def generate_pdf(events, filename):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    table_data = [['Event Type', 'Timestamp', 'Details']]

    # Populate table data
    for event in events:
        event_type = event.get('event_type', '')
        timestamp = event.get('timestamp', '')
        details = ', '.join([f"{key}: {value}" for key, value in event.items() if key not in ['event_type', 'timestamp']])
        table_data.append([event_type, timestamp, details])

    # Create table
    table = Table(table_data)
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])
    table.setStyle(style)

    # Build PDF
    doc.build([table])

# Generate PDF report
generate_pdf(events, 'event_report.pdf')
print("PDF report generated successfully.")
