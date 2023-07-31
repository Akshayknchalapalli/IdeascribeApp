from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'


@app.route("/", methods=["GET", "POST"], endpoint="generated_ideas")
def index():
    idea_lines = None
    idea_prompt = None
    if request.method == "POST":
        prompt = request.form.get("prompt")
        idea_prompt = prompt  # Save the prompt to display separately

        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=200,  # Increase the number of tokens to get more complete responses
            temperature=0.7,
            n=5,
            stop=None
        )

        choices = response.choices
        idea_lines = [choice['text'].strip() for choice in choices if choice['text'].strip()]

    return render_template("index.html", idea_lines=idea_lines, idea_prompt=idea_prompt)

if __name__ == "__main__":
    app.run(debug=True)
