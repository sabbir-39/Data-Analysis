import plotly.graph_objs as go
import plotly

def visualize_the_data(data_in_x_axis, data_in_y_axis, x_axis_label, y_axis_label, link_name):

    title = y_axis_label

    plot_data = go.Scatter(
        x=data_in_x_axis,
        y=data_in_y_axis,
        mode='lines+markers',
        line=dict(color='#CCDDCC',
                  width=2,
                  dash='dot'),
        marker=dict(
            color='firebrick',
            size=3),
        name="Title")

    data = [plot_data]

    layout = go.Layout(

        title=go.layout.Title(text=title, x=0),

        xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text=x_axis_label, font=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'))),

        yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(
            text=y_axis_label,
            font=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'))))

    fig = go.Figure(data, layout=layout)
    plotly.offline.plot(fig, filename=link_name + ".html", auto_open=True)
