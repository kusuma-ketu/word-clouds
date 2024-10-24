@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_csv'):
    csv_path = generate_csv()
    return send_file(csv_path, as_attachment=True)

@app.route('generate_wordcloud'):
    wordcloud_path = create_wordcloud()
    return send_file(wordcloud_path)

if __name__ == '__main__':
    app.run(debug=True)