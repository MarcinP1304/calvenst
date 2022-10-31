# imports
from calendar import calendar
from icalendar import Calendar, Event
from pathlib import Path
import yfinance as yf
import pandas as pd
import os

# get stock info
tickerlist = list(map(str, input("Enter tickers separeted by spaces: ").split()))

# init the calendar
cal = Calendar()

# Some properties are required to be compliant with RFC5545 SPECIFICATIONS
cal.add('prodid', '-//Calvenst - calendar for call earnings.//')
cal.add('version', '2.0')

for item in tickerlist:
   ticker = yf.Ticker(item)
   df = pd.DataFrame(ticker.calendar)

   # Add event subcomponents
   event = Event()
   event.add('summary', f'Earnings call {ticker.info["shortName"]}')
   event.add('dtstart', df.head(1).iloc[0, 0])

   # Add the event to the calendar
   cal.add_component(event)

# Write to disk
calendar_name = input('Enter your calendar name:')
directory = Path.cwd()
f = open(os.path.join(directory, f'{calendar_name}.ics'), 'wb')
f.write(cal.to_ical())
f.close()