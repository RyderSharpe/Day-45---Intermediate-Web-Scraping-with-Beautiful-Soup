import requests
from bs4 import BeautifulSoup

# URLS
login_url = "https://atgrecords.triumf.ca/login.php"
target_url = "https://atgrecords.triumf.ca/your_target_page.php"  # <-- Change this

# User input for login
username = input("Username: ")
password = input("Password: ")

# Start a session
session = requests.Session()

# Login payload
login_payload = {
    "uname": username,
    "pass": password,
    "submit": "Login"
}

# Headers (optional but can help)
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Step 1: Login
response = session.post(login_url, data=login_payload, headers=headers)

if "Logout" in response.text:
    print("✅ Login successful!")

    # Step 2: Fetch target page
    response = session.get(target_url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Example: Print page title
    print("📄 Page title:", soup.title.string if soup.title else "No title found")

    # Example: Print the first table
    table = soup.find("table")
    if table:
        rows = table.find_all("tr")
        for row in rows:
            cols = row.find_all(["td", "th"])
            print([col.get_text(strip=True) for col in cols])
    else:
        print("⚠️ No table found on the page.")

else:
    print("❌ Login failed. Check your username/password or form field names.")
