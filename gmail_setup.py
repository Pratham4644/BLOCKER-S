import os
from composio import Composio

def send_test_email():
    # Load API key
    api_key = os.getenv( "ak_XMJVfCshfnBBVITrsvzd")

    # Initialize client
    client = Composio(api_key=api_key)

    # ✅ Use the new correct structure for executing a tool
    try:
        response = client.tools.execute(
            tool="gmail",  # Toolkit name
            action="send_email",  # Action name inside toolkit
            arguments={  # ✅ renamed from 'input' to 'arguments'
                "auth_config_id": "ac_vgGaYaC5Ct7Z",  # your Gmail config ID
                "to": "prathamps8666@gmail.com",
                "subject": "Test Email from CodeSahayak 🚀",
                "body": "Hello bro! This is a test email sent via your CodeSahayak Gmail integration."
            }
        )

        print("✅ Email sent successfully!")
        print("Response:", response)

    except Exception as e:
        print("❌ Error sending email:", str(e))


if __name__ == "__main__":
    send_test_email()
