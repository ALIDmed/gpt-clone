import re

def extract_emails(text):
    """Extracts all email addresses from the given text."""
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_pattern, text)


if __name__ == "__main__":

    sample_text = """
    Here are some emails:
    alice@example.com
    bob.smith@workplace.org
    charlie123@school.edu
    """

    emails = extract_emails(sample_text)
    print("Extracted emails:", emails)