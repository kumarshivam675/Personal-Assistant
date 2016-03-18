import requests


def uploadComment(phone_number, body, tender_serial, url):
    base_url = "http://192.168.113.60:3000/"
    payload = {"comment[phone_number]": phone_number, "comment[body]": body, "comment[tender_serial]": tender_serial,
           "comment[image_url]": url}
    requests.post(base_url+"comments.json", data=payload)
