from flask import Flask, render_template, send_file, url_for
import qrcode
import io

app = Flask(__name__)

# URL of the AR scene
AR_URL = "http://localhost:5000/ar"

@app.route("/")
def index():
    # Redirect straight to QR code for scanning
    return f'<h1>Scan this QR code to view AR</h1><img src="{url_for("qr_code")}" />'

@app.route("/qr.png")
def qr_code():
    # Generate QR code pointing to AR scene
    img = qrcode.make(AR_URL)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return send_file(buf, mimetype="image/png")

@app.route("/ar")
def ar_scene():
    return render_template("ar_scene.html")

if __name__ == "__main__":
    app.run(debug=True)
