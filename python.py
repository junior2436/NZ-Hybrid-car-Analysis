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
    all_by_month = df.loc["ALFA ROMEO":"YAMAHA", all_months()]
    hybrid_by_month = total_by_month.loc[total_by_month["TYPE"].isin(hybrid_types)]
    bar_chart = pygal.HorizontalStackedBar()
    bar_chart.x_labels = all_months()

    def create_all_month():
        bar_chart = pygal.StackedBar(x_label_rotation=90)
        bar_chart.title = "All types of cars by month"
        bar_chart.x_labels = all_months()
        tmp = np(total_by_month)[0]
        bar_chart.add(tmp[0], tmp[1:])
        bar_chart.render_to_file('all_month.svg')
    create_all_month()

    def create_all_sum():
        bar_chart = pygal.Bar(x_label_rotation=90)
        bar_chart.title = "All types of cars in sum"
        for i, j in zip(all_by_month.index.values, np(all_by_month)):
            bar_chart.add(i, sum(j))
        bar_chart.render_to_file('all_sum.svg')
    create_all_sum()

    def create_hybrid_month():
        bar_chart = pygal.StackedBar(x_label_rotation=90)
        bar_chart.title = "Hybrid types of cars by month"
        bar_chart.x_labels = all_months()
        for i in np(hybrid_by_month):
            bar_chart.add(i[0], i[1:])
        bar_chart.render_to_file('hybrid_month.svg')
    create_hybrid_month()

    def create_hybrid_sum():
        bar_chart = pygal.Bar(x_label_rotation=90)
        bar_chart.title = "Hybrid types of cars in sum"
        for i in np(hybrid_by_month):
            bar_chart.add(i[0], sum(i[1:]))
        bar_chart.render_to_file('hybrid_sum.svg')
    create_hybrid_sum()

    def create_hybrid_per_total_percent_month():
        tmp = []
        for i, j in list(zip(np(total_by_month)[-1], np(total_by_month)[0]))[1:-3]:
            tmp.append((i/j)*100//0.01/100)
        line_chart = pygal.Line(x_label_rotation=90)
        line_chart.title = "Hybrid per total in percent"
        line_chart.x_labels = all_months()
        line_chart.add("hybrid", tmp)
        line_chart.render_to_file('hybrid_per_total_percent_month.svg')
    create_hybrid_per_total_percent_month()

    def create_hybrid_change_percent():
        tmp = [0]
        for i in range(2, len(np(total_by_month)[-1][:-3])):
            tmp.append(np(total_by_month)[-1][i]-np(total_by_month)[-1][i-1])
        line_chart = pygal.Line(x_label_rotation=90)
        line_chart.title = "Hybrid change form previous month"
        line_chart.x_labels = all_months()
        line_chart.add("change from previous month", tmp)
        line_chart.render_to_file('hybrid_change_percent.svg')
        print(tmp)
    create_hybrid_change_percent()



    print(all_by_month.index.values)
    print(np(all_by_month))

    print(np(hybrid_by_month))

    print(np(total_by_month)[0])
    print(np(total_by_month)[-1])
    tmp1 = list(zip(np(total_by_month)[0], np(total_by_month)[-1]))
    print(tmp1)
    tmp2 = []
    for i, j in tmp1[1:-3]:
        tmp2.append((j/i)*100//0.01/100)
    print(tmp2)

    
    
    
main()
