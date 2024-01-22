import pandas as pd
import matplotlib.pyplot as plt
from pylatex import Document, Section, Subsection, Figure

#Latex Document
doc = Document()

#doc.preamble.append(Section('示例文档'))

#Add the title
doc.append(Section('示例文档'))

#Add the sub-title
with doc.create(Subsection('数据表格')):
    # Read the data
    data = {'姓名': ['张三', '李四', '王五'],
            '年龄': [20, 25, 30]}
    df = pd.DataFrame(data)

    #Export the Latex-Table
    tabular = df.to_latex()

    #Add the Latex-Table to Latex Document
    doc.append(tabular)

#Add the Sub-title
with doc.create(Subsection('饼状图')):
    #Give the Example-Data
    labels = ['A', 'B', 'C']
    sizes = [15, 30, 45]

    # Draw the Pie chart
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')

    #Export the Latex code
    latex_code = plt.savefig('pie_chart.pdf', format='pdf')

    #Add the Pie-chart to the Latex Document
    with doc.create(Figure()) as plot:
        plot.add_image('pie_chart.pdf', width='120px')
# sve the Documet
doc.generate_pdf('example', clean_tex=False)
