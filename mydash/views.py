from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from plotly.offline import plot
import plotly.graph_objects as go

from django.http import HttpResponse
import math
import requests
from random import random
import time



def get_test2(request):
    your_link = "https://www.tronalddump.io/random/quote"
    result = requests.get(your_link).json()
    return HttpResponse(result['value'])


def get_test(request):
    def getrandomnumbers():

        xaxis = []
        yaxis = []

        for i in range(1, 10):
            xaxis.append(i)
            yaxis.append(math.floor(random() * 100))

        time.sleep(5)
        return xaxis, yaxis

    # plot original
    def scatter2():
        x1, y1 = getrandomnumbers()

        trace = go.Scatter(
            x = x1,
            y = y1
        )

        layout = dict(
            title='Simple Graph 2',
            xaxis=dict(range=[min(x1), max(x1)]),
            yaxis=dict(range=[min(y1), max(y1)]),
        )

        fig = go.Figure(data=[trace], layout=layout)
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div


    return HttpResponse(scatter2())



@login_required
def mydash(request):
    # BITCOIN API URL
    # https://api.coindesk.com/v1/bpi/currentprice.json
    # your_link = ""
    # result = requests.get(your_link)



    # plot original
    def scatter():
        x1 = [1,2,3,4]
        y1 = [30,36,25,45]

        trace = go.Scatter(
            x = x1,
            y = y1
        )

        layout = dict(
            title='Simple Graph',
            xaxis=dict(range=[min(x1), max(x1)]),
            yaxis=dict(range=[min(y1), max(y1)]),
        )

        fig = go.Figure(data=[trace], layout=layout)
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div




    context = {
        'plot': scatter()
    }

    return render(request, 'mydash/home.html', context)