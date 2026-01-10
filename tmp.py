from dotenv import load_dotenv
import os, modal

load_dotenv()

b2_secret = modal.Secret.from_dict(
    {
        "AWS_ACCESS_KEY_ID": os.environ["B2_KEY_ID"],
        "AWS_SECRET_ACCESS_KEY": os.environ["B2_APP_KEY"],
    }
)

print(b2_secret)
