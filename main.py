import requests
import os
import re
import time
import sys
import http.server
import socketserver
import threading
from requests.exceptions import RequestException

class MyHandler(http.server.SimpleHTTPRequestHandler):
def do_GET(self):
self.send_response(200)
self.send_header('Content-type', 'text/plain')
self.end_headers()
self.wfile.write(b"TH3 UNB3T34BL3 L3G3ND FYT3R PANKU DON HERE")

class FacebookCommenter:
def init(self):
self.comment_count = 0

def comment_on_post(self, cookies, post_id, comment, delay):  
    with requests.Session() as r:  
        r.headers.update({  
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7',  
            'sec-fetch-site': 'none',  
            'accept-language': 'id,en;q=0.9',  
            'Host': 'mbasic.facebook.com',  
            'sec-fetch-user': '?1',  
            'sec-fetch-dest': 'document',  
            'accept-encoding': 'gzip, deflate',  
            'sec-fetch-mode': 'navigate',  
            'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.166 Mobile Safari/537.36',  
            'connection': 'keep-alive',  
        })  

        response = r.get('https://mbasic.facebook.com/{}'.format(post_id), cookies={"cookie": cookies})  

        next_action_match = re.search('method="post" action="([^"]+)"', response.text)  
        if next_action_match:  
            self.next_action = next_action_match.group(1).replace('amp;', '')  
        else:  
            print("<Error> Next action not found")  
            return  

        fb_dtsg_match = re.search('name="fb_dtsg" value="([^"]+)"', response.text)  
        if fb_dtsg_match:  
            self.fb_dtsg = fb_dtsg_match.group(1)  
        else:  
            print("<Error> fb_dtsg not found")  
            return  

        jazoest_match = re.search('name="jazoest" value="([^"]+)"', response.text)  
        if jazoest_match:  
            self.jazoest = jazoest_match.group(1)  
        else:  
