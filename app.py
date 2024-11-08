from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

API_URL = "https://likes-garena-fadai.vercel.app/api?uid={uid}&code=FADAI1900mp"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_likes/<player_id>')
def send_likes(player_id):
    try:
        response = requests.get(API_URL.format(uid=player_id))
        
        if response.status_code == 200:
            data = response.json()
            if 'response' in data:
                response_data = data['response']
                nickname = response_data.get('PlayerNickname', 'غير معروف')
                # Return success response with player nickname
                return jsonify(success=True, nickname=nickname)
            else:
                return jsonify(success=False)
        else:
            return jsonify(success=False)

    except Exception as e:
        print(f"Error: {e}")
        return jsonify(success=False)

if __name__ == '__main__':
    app.run(debug=True)
