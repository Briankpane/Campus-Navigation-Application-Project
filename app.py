from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Renders the home page where users can search for classes/buildings
    return render_template('index.html')

@app.route('/building/<int:building_id>')
def building_layout(building_id):
    # Renders a page with the layout of the selected building
    return render_template('building_layout.html', building_id=building_id)

@app.route('/building-map/<acronym>')
def building_map(acronym):
    # Renders a generic building map page with the acronym passed in
    return render_template('building_map.html', acronym=acronym)

@app.route('/ACE.html')
def ace_page():
    # Renders the ACE page (make sure ACE.html exists in your templates folder)
    return render_template('ACE.html')

if __name__ == '__main__':
    app.run(debug=True)
