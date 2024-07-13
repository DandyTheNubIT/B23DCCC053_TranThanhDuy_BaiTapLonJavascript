
from flask import Flask, render_template
from flask_mail import Mail, Message


app = Flask(__name__)

app.config['SECRET_KEY'] = "tsfyguaistyatuis589566875623568956"

app.config['MAIL_SERVER'] = "smtp.googlemail.com"

app.config['MAIL_PORT'] = 587

app.config['MAIL_USE_TLS'] = True

app.config['MAIL_USERNAME'] = "tduy527@gmail.com"

app.config['MAIL_PASSWORD'] = "nbyj tode paks lgun"

mail = Mail(app)

@app.route("/",methods=["GET"])
def index():
	return "Index"

@app.route("/send_email/<email>",methods=["GET"])
def send_email(email):
	msg_title = "Thông tin vé đặt hàng"
	sender = "noreply@app.com"
	msg = Message(msg_title,sender=sender,recipients=[email])
	msg_body = ("Chào mừng bạn đã đến với Vexere chúng tôi. Thông tin chi tiết vé bạn đã đặt: Người đặt: Trần Thành Duy. Email: tduy527@gmail.com. SĐT: 0123456789. Ngày đặt: 13/7/2024. Hãng máy bay: Vietnam Airlines. Số chuyến bay: AIRBUS A17")
	msg.body = ""
	data = {
		'app_name': "vexere",
		'title': msg_title,
		'body': msg_body,
	}

	msg.html = render_template("email.html", data = data)

	try:
		mail.send(msg)
		return "Email đã được gửi. Vui lòng kiểm tra hộp thư đến tài khoản Gmail của bạn."
	except Exception as e:
		print(e)
		return f"Hiện tại vẫn chưa thể gửi được Email. Vui lòng thử lại sau.{e}"

if __name__ == "__main__":
	app.run(debug=True)