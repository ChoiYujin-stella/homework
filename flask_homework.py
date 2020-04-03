from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('Italia.html')

##################
db.signup

@app.route('/signup', methods=['POST'])
def write_data():
	# 1. 클라이언트가 준 title, author, review 가져오기.
    name_recieve = request.form["name_give"]
    phone_recieve = request.form["phone_give"]
    people_recieve = request.form["people_give"]
    email_recieve = request.form["email_give"]

	# 2. DB에 정보 삽입하기
    doc ={
        'name' : name_recieve,
        'phone' : phone_recieve,
        'people' : people_recieve,
        'email' : email_recieve
    }
    db.signup.insert_one(doc)
	# 3. 성공 여부 & 성공 메시지 반환하기
    return jsonify({'result': 'success', 'msg': '성공적으로 신청되었습니다.'})


@app.route('/signup', methods=['GET'])
def read_data():
		# 1. 모든 reviews의 문서를 가져온 후 list로 변환합니다.
        signup = list(db.signup.find({}, {'_id':False}))
		# 2. 성공 메시지와 함께 db를 보냅니다.
        return jsonify({'result': 'success' , 'signup': signup })


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)