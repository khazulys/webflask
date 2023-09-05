from flask import Flask, render_template, request, flash
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Ganti dengan kunci rahasia Anda

# Fungsi untuk mengirim email
def send_to_telegram(name, email, message):

    apiToken = '6481542434:AAGRFKskAnYAM9LiymOZD4AUVoQcYQnwyHY'
    chatID = '6155340412'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
    messages = f'Nama: {name}\nEmail: {email}\nPesan: {message}'
    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': messages})
        return response.text
    except Exception as e:
        return e


@app.route('/', methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        if send_to_telegram(name, email, message):
            flash('Pesan Anda telah berhasil dikirim.', 'success')
        else:
            flash('Gagal mengirim pesan. Silakan coba lagi nanti.', 'danger')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
