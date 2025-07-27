from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple rule-based response
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "course" in user_input or "program" in user_input:
        return "We offer B.Tech, M.Tech, MBA, and PhD programs in various disciplines."
    elif "hi" in user_input or "hello" in user_input:
        return "Hello, How I help you ?"
    elif "admission" in user_input:
        return "Admissions open in April. You can apply online via our official website."
    elif "fee" in user_input or "fees" in user_input:
        return "The fee structure varies by course. Please visit the Fees section on our website."
    elif "hostel" in user_input or "accommodation" in user_input:
        return "We provide separate hostel facilities for boys and girls with good amenities."
    elif "placement" in user_input:
        return "Our placement cell has a 90% placement rate with top companies visiting every year."
    elif "contact" in user_input or "email" in user_input:
        return "You can reach us at contact@college.edu or call 1800-123-456."
    elif "thanks" in user_input or "thank you" in user_input:
        return "You're welcome! Happy to help."
    elif "exit" in user_input or "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure about that. Please visit our website or contact the admin office for details."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_text = request.form["msg"]
    response = chatbot_response(user_text)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)