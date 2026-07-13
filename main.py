import requests, smtplib, os
yahoo_email = os.environ.get("YAHOO_EMAIL")
yahoo_password = os.environ.get("YAHOO_PASSWORD")
lay_email = os.environ.get("LAY_EMAIL")

response = requests.get(url="https://www.floatrates.com/daily/usd.json")
response.raise_for_status()
data = response.json()
rate = data["cad"]["rate"]

with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
    connection.starttls()
    connection.login(user=yahoo_email, password=yahoo_password)
    connection.sendmail(from_addr=yahoo_email, to_addrs=lay_email, msg=f"From: {yahoo_email}\nTo: {lay_email}\nSubject: current US to CAD exchange rate\n\n1 US dollar is equal to {rate} CAD dollars")
    
