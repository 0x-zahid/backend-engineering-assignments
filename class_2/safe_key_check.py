student = {
    "name": "Zahid",
    "age": 22,
    "email": "zahid@example.com"
}

email = student.get("email")

if email:
    print(f"Email: {email}")
else:
    print(f"Email not found")