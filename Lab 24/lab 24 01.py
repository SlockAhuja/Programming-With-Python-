

import pandas as pd
import plotly.express as px
import plotly.io as pio

# Use a static renderer Spyder can display (SVG). If svg doesn't work, try 'png'.
pio.renderers.default = 'svg'   # <-- Spyder-friendly

# Sample data
data = {
    'Product': ['A', 'B', 'C', 'D', 'E'],
    'Sales': [100, 200, 150, 300, 250],
    'Profit': [30, 70, 50, 120, 90]
}
df = pd.DataFrame(data)

# 1) Bar chart
fig = px.bar(df, x='Product', y='Sales', title='Sales by Product')
fig.show()

# 2) Line chart
fig = px.line(df, x='Product', y='Profit', title='Profit by Product')
fig.show()

# 3) Scatter plot
fig = px.scatter(df, x='Sales', y='Profit', color='Product', title='Sales vs Profit')
fig.show()

# 4) Enhanced bar chart
fig = px.bar(df, x='Product', y='Sales', title='Sales by Product (Enhanced)',
             color='Profit', text='Sales')
fig.update_layout(xaxis_title='Product', yaxis_title='Sales',
                  legend_title='Profit', template='plotly_dark')
fig.show()

# 5) Export HTML (works without kaleido)
fig.write_html('sales_by_product.html')
print("Saved interactive HTML: sales_by_product.html")

# Optional: to save a static image (PNG/SVG), uncomment the next line:
# fig.write_image('sales_by_product.png')   # requires kaleido & compatible versions
