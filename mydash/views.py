from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from plotly.offline import plot
import plotly.graph_objects as go


@login_required
def mydash(request):
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