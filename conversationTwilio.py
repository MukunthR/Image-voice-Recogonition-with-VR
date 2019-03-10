# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 05:17:45 2019

@author: Harsh Kava
"""

from flask import Flask, request, session, redirect
from twilio.twiml.messaging_response import MessagingResponse
from urllib.parse import urlencode
from twilio.twiml.voice_response import VoiceResponse, Say
from twilio.twiml.voice_response import Pause, VoiceResponse, Say
from twilio.rest import Client

# The session object makes use of a secret key.
account_sid = 'AC3c42c788114a773044b143f2cb94fdda'
auth_token = '60b52300e6e1b628cc8b45a3637fcb19'


from twilio.twiml.messaging_response import MessagingResponse


import csv



data ={}




with open('Books_data.csv', encoding="utf8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data[row["Book Name"].lower()] = row["Description"]


greetings =['holla','hi', 'hello','wassup','what\'s up', 'davinci']
good_feeling = ['fabulous','awesome','energetic','great', 'good','enjoyable', 'pleasing', 'pleasurable', 'delightful', 'great', 'nice', 'lovely', 'amusing', 'diverting', 'jolly', 'merry', 'lively', 'festive', 'cheerful']
bad_feeling =[ 'poor', 'inferior', 'unsatisfactory', 'deficient', 'imperfect', 'defective', 'faulty', 	'unpleasant', 'disagreeable', 'unwelcome', 'unfortunate', 'unfavorable', 'unlucky', 'adverse', 'nasty']


book_name ='harry potter'
category = 'romance'
book_auth = 'Harsh Kava'
book_link = 'https://www.goodreads.com/book/show/10818853-fifty-shades-of-grey'
book_Short_desc =""


app = Flask(__name__)
bookName =""

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    user  =request.values.get('From', None)
    
    
    resp = MessagingResponse()
    
    if (str(body).strip().lower() in greetings):
        resp.message("Hello ! How are you doing today ?")
        return str(resp)
    
    elif ('good' in str(body).strip().lower() or
          'great' in str(body).strip().lower() or
          'awesome'  in str(body).strip().lower() or
          'fabulous' in str(body).strip().lower()
          ):
        resp.message("That's good to hear. \n Which book would you like to read ?")
        return str(resp)
    
    elif (str(body).strip().lower() in bad_feeling):
        resp.message("Don't worry if you have a bad day, remember there are people who have ex's name tattooed on their body.")
        return str(resp)
    
    elif(str(body).strip().lower() in data.keys()):
        print(str(body).lower())
        #resp.message('Book: '+str(body).strip() + '\n'+ 'Category: '+category + '\n'+ 'Book_auth: '+book_auth +'\n'+ 'Book: '+book_link +'. \n  ### Do you want to hear a summary of this book ?')
        resp.message('Book Found! \n  ### Calling you to give a summary of this book now!')
        bookName = str(body).strip().lower()
        #return str(resp)
    
    #elif(str(body).strip().lower() == 'yes'):
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                 body='Calling you now...',
                 from_='+12015483471',
                 to=user
             )
        print(message.sid)
        
        
        
        messages = client.messages.list()
        msg =  messages[-1]

        #print(msg.body.strip().lower())
        
        x ={}
        x['Book'] =bookName
        x['User'] =user
        
        call = client.calls.create(
                        url='http://855af697.ngrok.io/voice?'+urlencode(x),
                        to=user,
                        from_='+12015483471'
                    )
        
        #resp.message()
        return str(resp)
        
    
    elif (str(body).strip().lower() == 'no'):
        resp.message("Sure No problem. \n Have a good day!")
        return str(resp)
    
    else :
        from urllib.parse import quote
        qstr = quote(str(body).lower())
        #print(str(qstr))
        resp.message("Sorry.. I couldn't find anything related in database. \n But here is the result on Google for it:: https://www.google.com/search?q="+qstr)  # 
        return str(resp)
    # Start our TwiML response



@app.route("/voice", methods=['GET', 'POST'])
def voice():
    
    Book = request.values['Book']
    user = request.values['User']
    
    print(Book)
    summary= data.get(Book, None)
    
 #   print(user)
    resp = VoiceResponse()
    if (summary is None):
        say = Say('Hi.. ....... This is DaVinci.  Sorry There is no summary available at this point of time. Sorry for inconvenience ', voice='Aditi')
        resp.append(say)
    else:
        say = Say('Hi.. ....... This is DaVinci.  This is the summary of the book you requested...... ', voice='Aditi')
        say.ssml_break(strength='x-weak', time='3000ms')
        #say.pause(length=3)
        say.ssml_emphasis('Starting to read the summary now...', level='moderate')
        #say.pause(length=2)
        say.ssml_break(strength='x-weak', time='4000ms')
        say.ssml_p(summary)
        #say.pause(length=3)
        say.ssml_break(strength='x-weak', time='3000ms')
        say.ssml_emphasis ('Summary Finished. Thank you for listening', level='moderate')
        resp.append(say)

    return str(resp)  
# =============================================================================
#     client = Client(account_sid, auth_token)
#     call = client.calls.create(
#                         method='GET',
#                         status_callback_event=['initiated', 'answered'],
#                         status_callback_method='POST',
#                         url='http://demo.twilio.com/docs/voice.xml',
#                         to=callTo,
#                         from_='+12015483471'
#                     )
# 
#     print(call.sid)
# # =============================================================================
# #     call = client.calls.create(
# #                             url='http://demo.twilio.com/docs/voice.xml',
# #                             to='+14155551212',
# #                             from_='+15017122661'
# #                         )
# #     
# #     print(call.sid)
# # =============================================================================
#     
# =============================================================================
    
    
    
    
# =============================================================================
# 
#     # Determine the right reply for this message
#     if body == 'hello':
#         resp.message("Hi!")
#     elif body == 'bye':
#         resp.message("Goodbye")
# 
#     return str(resp)
# 
# =============================================================================
if __name__ == "__main__":
    app.run()