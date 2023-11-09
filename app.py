from flask import Flask, request, jsonify, render_template
import openai

# Flask 앱과 OpenAI API 키 설정
app = Flask(__name__)
openai.api_key = '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'

# 웹 페이지 템플릿 로딩
@app.route('/')
def home():
    return render_template('index.html')  # index.html에는 사용자 입력 폼이 있어야 함

# 챗봇 API 엔드포인트
@app.route('/chat', methods=['POST'])
def chat():
    # 사용자 입력 받기
    user_message = request.json.get('message')

    # OpenAI API를 사용하여 응답 생성
    response = openai.Completion.create(
        engine="text-davinci-003",  # 가장 최신의 GPT 모델 사용
        prompt=f"좋아하는 향기의 형용사는 {user_message}향이야. 이런 향을 가진 향수를 추천해줘.  답변으로 향수이름과 이 향수에 대한 설명을 알려줘",
        max_tokens=2000,
        n=1,
        stop=None,
        temperature=0.5
    )

    # 생성된 텍스트 추출
    bot_message = response.choices[0].text.strip()

    # 추천 결과를 JSON 형태로 반환
    return jsonify({'message': bot_message})

# 서버 실행
if __name__ == '__main__':
    app.run(debug=True)
