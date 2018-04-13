#-*- coding: utf-8 -*-
from pyexchange import Exchange2010Service, ExchangeNTLMAuthConnection
from datetime import datetime
from pytz import timezone

URL = u'https://hqmail.sf.com/EWS/Exchange.asmx'
USERNAME = u'SF\\HaoHe@sf-express.com'
PASSWORD = u"Szsfkj_2017"

# Set up the connection to Exchange
connection = ExchangeNTLMAuthConnection(url=URL,
                                        username=USERNAME,
                                        password=PASSWORD)

service = Exchange2010Service(connection)


event = service.calendar().new_event(
  subject=u"80s Movie Night",
  attendees=[u'HaoHe@sf-express.com'],
  location = u"My house",
)

# ...or afterwards
event.start=timezone("US/Pacific").localize(datetime(2017,11,9,15,0,0))
event.end=timezone("US/Pacific").localize(datetime(2017,11,11,21,0,0))

event.html_body = "test"

# Connect to Exchange and create the event
event.create()