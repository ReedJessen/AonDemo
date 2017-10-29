import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import numpy as np



class IPStreetCharting:


    def _prep_owner_data(self,merged_results):

        merged_results = merged_results[pd.notnull(merged_results['current_owner'])]
        merged_results = merged_results[merged_results['current_owner'] != '']
        # merged_results = merged_results.set_index(['current_owner'],drop=False)
        data = merged_results.groupby(['current_owner']).size().nlargest(10)\
            .sort_values(ascending=False).to_frame('size').reset_index()

        return data



    def owner_distribution_chart(self,merged_results):
        owner_data = self._prep_owner_data(merged_results)
        chart_data = [go.Bar(
            x=owner_data['current_owner'],
            y=owner_data['size']
        )]
        layout = go.Layout(
            title='Ownership Distribution of Semantic Results'
        )
        fig = go.Figure(data=chart_data, layout=layout)
        url = py.plot(fig, filename='owners-bar-chart')
        print(url)

    def closeness_density_chart(self,data):
        y = data['relevence_score']
        x = data['application_date']
        print(x)
        print(y)

        x_axis_max = float(max(y)) + 1
        x_axis_min = float(min(y)) - 1

        trace = go.Scatter(
            x=x,
            y=y,
            mode='markers',
            text=data['current_owner'],
            marker=dict(
                size=10,
                color='rgba(152, 0, 0, .8)',
                line=dict(
                    width=2,
                    color='rgb(0, 0, 0)'
                )
            )
        )

        layout = dict(title='Prior Art Density Landscape- 13/952,450',
                      yaxis=dict(
                          range=[x_axis_min, x_axis_max],
                          showticklabels=False,
                          title='<- Less Relevant | More Relevant ->'
                      ),
                      xaxis=dict(
                          autorange=True,
                          showgrid=False,
                          zeroline=False,
                          showline=False,
                          autotick=True,
                          ticks='',
                          showticklabels=False,
                      )
                      )
        data = [trace]
        fig = go.Figure(data=data, layout=layout)
        url = py.plot(fig, filename='Prior Art Density Landscape-13952450')
        print(url)

