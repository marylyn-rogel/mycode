import requests
import json

def get_questions_and_answers():
    url = "https://opentdb.com/api.php?amount=3&category=12&difficulty=easy&type=boolean"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        results = data.get("results", [])

        for result in results:
            question = result.get("question", "")
            correct_answer = result.get("correct_answer", "")
            
            # Printing the question and answer for each set
            print("Question:", question)
            print("Answer:", correct_answer)
            print("------------------------------")

get_questions_and_answers()
