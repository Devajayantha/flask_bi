from datetime import datetime

# Helper function to get the current timestamp
def get_current_timestamp():
    current_datetime = datetime.now()

    # Convert to UTC timezone, i tried to use tzinfo=pytz.UTC but it doesn't work, so i use this instead for workaround
    return current_datetime.strftime('%Y-%m-%d') + 'T00:00:00+07:00'