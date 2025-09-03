import pandas as pd
import dash
from dash import dcc, html
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load and clean the CSV file
df = pd.read_csv("FMTQIK_2025-0903.csv", quotechar='"')

# Clean and convert relevant columns
columns_to_clean = ['Trade Volume', 'Trade Value', 'Transaction', 'TAIEX']
for col in columns_to_clean:
    df[col] = df[col].str.replace(',', '')
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Drop rows with NaN in Date, TAIEX, or Trade Volume
df_clean = df.dropna(subset=['Date', 'TAIEX', 'Trade Volume'])

# Create subplots with 80/20 height ratio
fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                    row_heights=[0.8, 0.2],
                    vertical_spacing=0.05,
                    subplot_titles=("TAIEX Index Over Time", "Trade Volume Over Time"))

# Add TAIEX line
fig.add_trace(go.Scatter(x=df_clean['Date'], y=df_clean['TAIEX'],
                         mode='lines', name='TAIEX'), row=1, col=1)

# Add Trade Volume line
fig.add_trace(go.Scatter(x=df_clean['Date'], y=df_clean['Trade Volume'],
                         mode='lines', name='Trade Volume'), row=2, col=1)

# Update layout
fig.update_layout(height=800, title_text="TAIEX Index and Trade Volume (80/20 Split)")

# Create Dash app
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("TAIEX Dashboard"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)

