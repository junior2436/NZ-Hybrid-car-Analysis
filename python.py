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
    brand_hybrid_by_month = df.loc[df["TYPE"].isin(hybrid_types), ["TYPE"]+all_months()]
    sum_brand_hybrid = [(i, j[0], sum(j[1:])) for i, j in \
    zip(brand_hybrid_by_month.index.values,np(brand_hybrid_by_month)) if i != "TOTAL"]

    def create_brand_hybrid_sum():
        """create graph"""
        bar_chart = pygal.Bar(x_label_rotation=90)
        bar_chart.title = "ผลรวมของรถยนต์ไฮบริดแต่ละรุ่น"
        for i, j, k in sum_brand_hybrid:
            bar_chart.add(i+" "+j, k)
        bar_chart.render_to_file('All_brands_of_hybrids.svg')
    create_brand_hybrid_sum()

    def create_all_month():
        """create graph"""
        bar_chart = pygal.Bar(x_label_rotation=90)
        bar_chart.title = "ผลรวมของรถยนต์แต่ละเดือน"
        bar_chart.x_labels = all_months()
        tmp = np(total_by_month)[0]
        bar_chart.add(tmp[0], tmp[1:])
        bar_chart.render_to_file('All_cars_each_month.svg')
    create_all_month()

    def create_all_sum():
        """create graph"""
        bar_chart = pygal.Bar(x_label_rotation=90)
        bar_chart.title = "ผลรวมของรถยนต์แต่ละยี่ห้อ"
        for i, j in zip(all_by_month.index.values, np(all_by_month)):
            bar_chart.add(i, sum(j))
        bar_chart.render_to_file('All_cars_each_brand.svg')
    create_all_sum()

    def create_hybrid_month():
        """create graph"""
        bar_chart = pygal.StackedBar(x_label_rotation=90)
        bar_chart.title = "ผลรวมของรถยนต์ไฮบริดแต่ละประเภทของแต่ละเดือน"
        bar_chart.x_labels = all_months()
        for i in np(hybrid_by_month):
            bar_chart.add(i[0], i[1:])
        bar_chart.render_to_file('All_hybrid_each_month.svg')
    create_hybrid_month()

    def create_hybrid_sum():
        """create graph"""
        bar_chart = pygal.Bar(x_label_rotation=90)
        bar_chart.title = "ผลรวมรถยนต์ไฮบริดแต่ละประเภท"
        for i in np(hybrid_by_month):
            bar_chart.add(i[0], sum(i[1:]))
        bar_chart.render_to_file('All_hybrid_each_type.svg')
    create_hybrid_sum()

    def create_hybrid_per_total_percent_month():
        """create graph"""
        tmp = []
        for i, j in list(zip(np(total_by_month)[-1], np(total_by_month)[0]))[1:-3]:
            tmp.append((i/j)*100//0.01/100)
        line_chart = pygal.Line(x_label_rotation=90)
        line_chart.title = "เปอเซ็นของรถยนต์ไฮบริดในแต่ละเดือนเทียบกับรถยนต์ทุกประเภท"
        line_chart.x_labels = all_months()
        line_chart.add("hybrid", tmp)
        line_chart.render_to_file('All_hybrid_percent_month.svg')
    create_hybrid_per_total_percent_month()

    def create_hybrid_change_percent():
        """create graph"""
        tmp = [0]
        for i in range(2, len(np(total_by_month)[-1][:-3])):
            tmp.append(np(total_by_month)[-1][i]-np(total_by_month)[-1][i-1])
        line_chart = pygal.Line(x_label_rotation=90)
        line_chart.title = "อัตราการเปล่ยนแปลงของรถยนต์ไฮบริดจากเดือนก่อนหน้า"
        line_chart.x_labels = all_months()
        line_chart.add("change from previous month", tmp)
        line_chart.render_to_file('Change_hybrid_prevmonth.svg')
    create_hybrid_change_percent()

main()
