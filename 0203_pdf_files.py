import pdftables

my_pdf = open('data/WEF_GlobalCompetitivenessReport_2014-15.pdf', 'rb')
chart_page = pdftables.get_pdf_page(my_pdf, 29)

table = pdftables.page_to_tables(chart_page)


titles = zip(table[0][0], table[0][1])[:5]
print(titles)

all_rows = []
for row_data in table[0][2:]:
    all_rows.extend([row_data[:5], row_data[5:]])

print(all_rows)
