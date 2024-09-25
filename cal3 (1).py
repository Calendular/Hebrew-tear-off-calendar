from pyluach import dates , hebrewcal
from pyluach.dates import HebrewDate
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import datetime





def strrevers(s):
 return s[::-1]

def hebrewweekwame(w):
  weeknames= ("ראשון","שני","שלישי","רביעי","חמישי","שישי","שבת")
  return "יום "+weeknames[w-1]


test=hebrewcal
startdate = datetime.date(2024, 1, 1)
pdfmetrics.registerFont(TTFont('alef', '/usr/share/fonts/truetype/alef/TTF/Alef-regular.ttf'))
c = canvas.Canvas("365.pdf", pagesize=(200, 100))



for DayInYear in range(0, 366, 1):
    c.setFont('alef', 6)
    c.drawString(2, 2, str(DayInYear + 1))
    ThisDay = startdate + datetime.timedelta(days=DayInYear)
    c.setFont('alef', 14)
    c.drawRightString(157, 5, ThisDay.strftime('%A %d/%m/%Y'))
    GD=dates.GregorianDate (ThisDay.year , ThisDay.month , ThisDay.day )
    HD=GD.to_heb()
    SHD=HebrewDate( HD.year, HD.month, HD.day)
    c.drawString(5, 20, strrevers(HD.hebrew_date_string(True) ))
    c.drawString(5, 35, strrevers(hebrewweekwame( int(SHD.weekday()))))
    #drawing holidays , in big font
    c.setFont('alef', 20)
    h=SHD.festival(israel=True,hebrew=True,include_working_days=True)
    if h: c.drawString(5, 85, strrevers(str(h))) #only  if there is some holiday
    c.rect(0, 0, 200, 100) #drawing rectangle
    c.showPage()
c.save()
