"""Flatten"""
def all_months():
    """create list of all months"""
    years = [str(i) for i in range(2012, 2018)]
    months = ["JAN", "FEB", "MAY", "APR", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    all_months = []
    for i in years:
        for j in months:
            all_months.append(i+"-"+j)
    return all_months

def main():
    """Flatten"""
    import pandas as pd
    from numpy import array as np
    import pygal
    df = pd.read_excel("data.xlsx")
    df.set_index("BRAND", inplace=True)
    hybrid_types = ("Electric", "Petrol Hybrid", "Diesel Hybrid", "Plug-In Petrol Hybrid")
    total_by_month = df.loc["TOTAL", ["TYPE"]+all_months()]
    total_by_year = df.loc["TOTAL", ["TYPE"]+[str(i)+"-YTD" for i in range(2012, 2018)]]
    hybrid_by_month = total_by_month.loc[total_by_month["TYPE"].isin(hybrid_types)]
    bar_chart = pygal.HorizontalStackedBar()
    bar_chart.x_labels = all_months()

    def create_horizontalstackedbar(lst, label):
        bar_chart = pygal.HorizontalStackedBar()
        bar_chart.x_labels = label
        for i in np(lst):
            bar_chart.add(i[0], i[1:])
        bar_chart.render_to_file('horizontal_stacked_bar_chart.svg')

    def create_dot(lst, label):
        dot_chart = pygal.Dot(x_label_rotation=90)
        dot_chart.x_labels = label
        for i in np(lst):
            dot_chart.add(i[0], i[1:])
        dot_chart.render_to_file('dot_chart.svg')

    def create_pyramid(lst, label):
        pyramid_chart = pygal.Pyramid(human_readable=True, legend_at_bottom=True)
        pyramid_chart.x_labels = label
        for i in np(lst)[:-1]:
            pyramid_chart.add(i[0], i[1:])
        pyramid_chart.render_to_file('pyramid_chart.svg')

    create_horizontalstackedbar(hybrid_by_month, all_months())

    create_dot(hybrid_by_month, all_months())

    
    
    
main()
