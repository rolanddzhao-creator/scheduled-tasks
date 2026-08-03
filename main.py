import requests, smtplib, os
my_email = os.environ.get("MY_EMAIL")
my_password = os.environ.get("MY_PASSWORD")
lay_email = os.environ.get("LAY_EMAIL")

response = requests.get(url="https://www.floatrates.com/daily/usd.json")
response.raise_for_status()
data = response.json()
rate = float(data["cad"]["rate"])

with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connection:
    connection.login(user=my_email, password=my_password)
    msg = f"Subject: Current US to CAD exchange rate\n\n1 US dollar is equal to {rate:.4f} CAD dollars"
    connection.sendmail(from_addr=my_email, to_addrs=lay_email, msg=msg)
