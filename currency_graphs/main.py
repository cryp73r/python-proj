from PIL import Image, ImageFont, ImageDraw
from datetime import datetime, timedelta, date
from pygooglechart import *
import locale
import requests
from pytrends.request import TrendReq
import pandas as pd

pd.set_option('display.max_rows', None)

ALPHAVANTAGE_API_KEY = '###'

locale.setlocale(locale.LC_ALL, 'turkish')

date_time = datetime.now()

def stacked_vertical():
    chart = StackedHorizontalBarChart(280, 150,
                                      x_range=(0, 100))
    chart.set_bar_width(22)
    chart.set_colours(['007BFF', '6C757D','DC3545','28A745','FFC107'])
    chart.add_data(reversed([4, 12, 26, 36, 88]))
    chart.set_axis_labels(Axis.LEFT,
                          reversed(["Dolar","Lira","Euro","Bitcoin","Ethereum"]))
    chart.set_axis_range(Axis.BOTTOM,0,100)
    chart.download('bar-horizontal-stacked.png')


stacked_vertical()


# GET DATA FOR DAILY CHART
def daily_chart_data():
    all_day_list = []
    inday_data = requests.get(
        "https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol=USD&to_symbol=TRY&interval=5min&outputsize=full&apikey={}".format(
            ALPHAVANTAGE_API_KEY)).json()['Time Series FX (5min)']
    for time, values in inday_data.items():
        all_day_list.append(float(values['4. close']))
    return all_day_list


# GET DATA FOR WEEKLY CHART
def weekly_chart_data():
    all_week_list = []
    week_data = requests.get(
        "https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol=USD&to_symbol=TRY&interval=30min&outputsize=full&apikey={}".format(
            ALPHAVANTAGE_API_KEY)).json()["Time Series FX (30min)"]
    for time, values in week_data.items():
        if len(all_week_list) == 336:
            return all_week_list
        else:
            all_week_list.append(float(values["4. close"]))


# DAILY CHART
def create_daily_chart(data, labels=None):
    chart = SimpleLineChart(445, 215, y_range=(min(data), max(data)))
    chart.add_data(data[::-1])
    chart.set_colours(['208020'])
    chart.set_grid(0, 25, 5, 5)
    aralik = (max(data) - min(data)) / 5
    chart.set_axis_labels(Axis.LEFT, [
        '{0:.3g}'.format(min(data)),
        '{0:.3g}'.format(min(data) - aralik),
        '{0:.3g}'.format(min(data) - aralik * 2),
        '{0:.3g}'.format(min(data) - aralik * 3),
        '{0:.3g}'.format(max(data)),
    ])
    chart.set_axis_labels(Axis.BOTTOM,
                          [(datetime.now() - timedelta(hours=24)).strftime(':%H') + ":00",
                           (datetime.now() - timedelta(hours=21)).strftime(':%H') + ":00",
                           (datetime.now() - timedelta(hours=18)).strftime(':%H') + ":00",
                           (datetime.now() - timedelta(hours=15)).strftime(':%H') + ":00",
                           (datetime.now() - timedelta(hours=12)).strftime(':%H') + ":00",
                           (datetime.now() - timedelta(hours=9)).strftime(':%H') + ":00",
                           (datetime.now() - timedelta(hours=6)).strftime(':%H') + ":00",
                           (datetime.now() - timedelta(hours=3)).strftime(':%H') + ":00",
                           datetime.now().strftime('%H') + ":00"])

    chart.download('hourly-tr-usd.png')


# WEEKLY CHART
def create_weekly_chart(data):
    chart2 = SimpleLineChart(445, 215, y_range=(min(data), max(data)))
    chart2.add_data(data[::-1])
    chart2.set_colours(['208020'])
    chart2.set_grid(0, 25, 5, 5)
    aralik = (max(data) - min(data)) / 5
    chart2.set_axis_labels(Axis.LEFT, [
        '{0:.3g}'.format(min(data)),
        '{0:.3g}'.format(min(data) - aralik),
        '{0:.3g}'.format(min(data) - aralik * 2),
        '{0:.3g}'.format(min(data) - aralik * 3),
        '{0:.3g}'.format(max(data)),
    ])
    chart2.set_axis_labels(Axis.BOTTOM, [
        (date.today() - timedelta(days=6)).strftime("%A"),
        (date.today() - timedelta(days=5)).strftime("%A"),
        (date.today() - timedelta(days=4)).strftime("%A"),
        (date.today() - timedelta(days=3)).strftime("%A"),
        (date.today() - timedelta(days=2)).strftime("%A"),
        (date.today() - timedelta(days=1)).strftime("%A"),
        date.today().strftime("%A")])
    chart2.download('weekly-tr-usd.png')


def create_weekly_google_chart(data):
    chart3 = SimpleLineChart(445, 215, y_range=(min(data), max(data)))
    chart3.add_data(data)
    chart3.set_colours(["9b0000"])
    chart3.set_grid(0, 25, 5, 5)
    chart3.set_axis_labels(Axis.BOTTOM, [
        (date.today() - timedelta(days=6)).strftime("%A"),
        (date.today() - timedelta(days=5)).strftime("%A"),
        (date.today() - timedelta(days=4)).strftime("%A"),
        (date.today() - timedelta(days=3)).strftime("%A"),
        (date.today() - timedelta(days=2)).strftime("%A"),
        (date.today() - timedelta(days=1)).strftime("%A"),
        date.today().strftime("%A")])
    aralik = (max(data) - min(data)) / 5
    chart3.set_axis_labels(Axis.LEFT, [
        '{0:.3g}'.format(min(data)),
        '{0:.3g}'.format(min(data)- aralik),
        '{0:.3g}'.format(min(data) - aralik*2),
        '{0:.3g}'.format(min(data) - aralik*3),
        '{0:.3g}'.format(max(data)),
    ])
    chart3.download('weekly-google-usd.png')


def weekly_google_interests(currData):
    data_list = []
    pytrends = TrendReq(hl='tr-TR', tz=360)
    pytrends.build_payload(
        kw_list=["dolar"],
        cat=0,
        timeframe='now 7-d',
        geo='TR',
        gprop='')
    data = pytrends.interest_over_time()
    data_frame = pd.DataFrame(data)['dolar']
    for a, b in data_frame.items():
        data_list.append(float(b))
    old_min = min(data_list)
    old_max = max(data_list)
    new_min = min(currData)
    new_max = max(currData)
    converted_list = []
    for item in data_list:
        converted_list.append(((item - old_min) / (old_max - old_min)) * (new_max - new_min) + new_min)
    return converted_list


def daily_google_interests(currData):
    data_list = []
    pytrends = TrendReq(hl='tr-TR', tz=360)
    pytrends.build_payload(
        kw_list=["dolar"],
        cat=0,
        timeframe='now 1-d',
        geo='TR',
        gprop='')
    data = pytrends.interest_over_time()
    data_frame = pd.DataFrame(data)['dolar']
    for a, b in data_frame.items():
        data_list.append(float(b))
    old_min = min(data_list)
    old_max = max(data_list)
    new_min = min(currData)
    new_max = max(currData)
    converted_list = []
    for item in data_list:
        converted_list.append(((item - old_min) / (old_max - old_min)) * (new_max - new_min) + new_min)
    return converted_list


def create_daily_google_chart(data):
    chart3 = SimpleLineChart(445, 215, y_range=(min(data), max(data)))
    chart3.add_data(data)
    chart3.set_colours(["9b0000"])
    chart3.set_grid(0, 25, 5, 5)
    chart3.set_axis_labels(Axis.BOTTOM,  [(datetime.now() - timedelta(hours=24)).strftime(':%H') + ":00",
                           (datetime.now() - timedelta(hours=21)).strftime(':%H') + ":00",
                           (datetime.now() - timedelta(hours=18)).strftime(':%H') + ":00",
                           (datetime.now() - timedelta(hours=15)).strftime(':%H') + ":00",
                           (datetime.now() - timedelta(hours=12)).strftime(':%H') + ":00",
                           (datetime.now() - timedelta(hours=9)).strftime(':%H') + ":00",
                           (datetime.now() - timedelta(hours=6)).strftime(':%H') + ":00",
                           (datetime.now() - timedelta(hours=3)).strftime(':%H') + ":00",
                           datetime.now().strftime('%H') + ":00"])
    aralik = (max(data) - min(data)) / 5
    chart3.set_axis_labels(Axis.LEFT, [
        '{0:.3g}'.format(min(data)),
        '{0:.3g}'.format(min(data) - aralik),
        '{0:.3g}'.format(min(data) - aralik * 2),
        '{0:.3g}'.format(min(data) - aralik * 3),
        '{0:.3g}'.format(max(data)),
    ])
    chart3.download('daily-google-usd.png')

create_daily_google_chart(daily_google_interests(currData=daily_chart_data()))
create_daily_chart(data=daily_chart_data())
create_weekly_chart(data=weekly_chart_data())
create_weekly_google_chart(data=weekly_google_interests(weekly_chart_data()))


main_image = Image.open("example.png")
draw = ImageDraw.Draw(main_image)
font = ImageFont.truetype("fonts/Roboto-Regular.ttf", 24)
#draw.text((85, 150), '{0:.6g}'.format(00.00), fill='black', font=font)

chart_1 = Image.open("hourly-tr-usd.png")

chart_2 = Image.open("weekly-tr-usd.png")

chart_3 = Image.open("weekly-google-usd.png")

chart_4 = Image.open("daily-google-usd.png")

chart_5 = Image.open("bar-horizontal-stacked.png")

Image.blend(chart_4,chart_1,.7).save("out2.png")

Image.blend(chart_3, chart_2,.7).save("out.png")

output = Image.open("out.png")

output2 = Image.open("out2.png")

main_image.paste(output2, (60, 290))

main_image.paste(output, (522, 290))

main_image.paste(chart_5,(690,60))

main_image.save("final.png")

