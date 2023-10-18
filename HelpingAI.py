from flask import Flask, render_template, request
import google.generativeai as palm

app = Flask(__name__)

# Replace 'your_api_key' with your actual API key
palm.configure(api_key="AIzaSyCnrcQWTEedcGuEsJ9Uhbj_ZS9B2nozMiU")

defaults = {
    'model': 'models/text-bison-001',
    'temperature': 1,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
    'max_output_tokens': 1024,
    'stop_sequences': [],
    'safety_settings': [
        {"category": "HARM_CATEGORY_DEROGATORY", "threshold": 4},
        {"category": "HARM_CATEGORY_TOXICITY", "threshold": 4},
        {"category": "HARM_CATEGORY_VIOLENCE", "threshold": 4},
        {"category": "HARM_CATEGORY_SEXUAL", "threshold": 4},
        {"category": "HARM_CATEGORY_MEDICAL", "threshold": 4},
        {"category": "HARM_CATEGORY_DANGEROUS", "threshold": 4},
    ],
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    user_input = request.form['user_input']

    # Your generative AI code here
    prompt = f"""Hello! I am HelpingAI. I am developed by Abhay koul, the main function of  HelpingAI is to make learning and education easier and more convenient for students. My purpose is to simplify your learning journey by providing personalized assistance, innovative teaching methods, and tailored resources to meet your unique needs. I am here to make your educational experience more enjoyable and effective. Feel free to ask me any questions or let me know how I can assist you in your learning adventure! and also in many more things from your life. Also HelpingAI was initially developed for S.U.P.E.R.B.O.T. and vortexAI, for more info visit: https://github.com/HelpingAI , https://replit.com/@Devastation-war ,join discord https://discord.gg/2EeZcJjyRd
    input: {user_input}
    output:"""
    response = palm.generate_text(**defaults, prompt=prompt)

    return render_template('index.html', user_input=user_input, response=response.result)

if __name__ == '__main__':
    app.run(debug=True)
