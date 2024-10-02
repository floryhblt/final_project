from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load the CSV data
file_path = r'C:/Users/flori/Documents/Ironhack/final_proejct/data/clean/df_final.csv'
df = pd.read_csv(file_path)

# Sample 1000 rows for each region
sample_size = 1000
df_idf_sampled = df[df['Location'] == 'Grand Paris']
df_lyon_sampled = df[df['Location'] == 'Grand Lyon']
df_am_sampled = df[df['Location'] == 'Aix-Marseille']

# Convert sampled data to lists for rendering
idf_sampled_list = df_idf_sampled.to_dict(orient='records')
lyon_sampled_list = df_lyon_sampled.to_dict(orient='records')
am_sampled_list = df_am_sampled.to_dict(orient='records')

# Home route
@app.route('/')
def home():
    return '''
    <h1>Location Sample Pages</h1>
    <ul>
        <li><a href="/idf">Grand Paris</a></li>
        <li><a href="/lyon">Grand Lyon</a></li>
        <li><a href="/am">Aix-Marseille</a></li>
    </ul>
    '''

# Île-de-France route
@app.route('/idf')
def idf_page():
    return render_template('locations.html', location="Grand Paris", data=idf_sampled_list)

# Lyon route
@app.route('/lyon')
def lyon_page():
    return render_template('locations.html', location="Grand Lyon", data=lyon_sampled_list)

# Aix-Marseille route
@app.route('/am')
def am_page():
    return render_template('locations.html', location="Aix-Marseille", data=am_sampled_list)

if __name__ == '__main__':
    app.run(debug=True)
