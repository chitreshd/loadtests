def email_payload(timestamp, emails):
    toList = [{"email": email} for email in emails]
    jsonStr = {
        "body": "Test email: This is a drill {}".format(timestamp),
        "subject": "Test drill {}".format(timestamp),
        "to": toList
    }
    return jsonStr