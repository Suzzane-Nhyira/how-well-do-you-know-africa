import random
import time

# ─── Questions by Category ────────────────────────────────────────────────────
QUESTIONS = {
    "🇬🇭 Ghana History": [
        {
            "question": "Ghana gained independence from Britain in which year?",
            "options": ["1957", "1960", "1963", "1945"],
            "answer": "1957"
        },
        {
            "question": "Who was Ghana's first president?",
            "options": ["John Mahama", "Kwame Nkrumah", "Jerry Rawlings", "Kofi Atta"],
            "answer": "Kwame Nkrumah"
        },
        {
            "question": "Which country was formerly known as the Gold Coast?",
            "options": ["Nigeria", "Ivory Coast", "Ghana", "Senegal"],
            "answer": "Ghana"
        },
        {
            "question": "What is the traditional cloth of Ghana called?",
            "options": ["Ankara", "Batik", "Kente", "Dashiki"],
            "answer": "Kente"
        },
        {
            "question": "The Ashanti Kingdom is located in which country?",
            "options": ["Nigeria", "Ivory Coast", "Ghana", "Togo"],
            "answer": "Ghana"
        },
        {
            "question": "What is the currency of Ghana?",
            "options": ["Naira", "Cedi", "Shilling", "Franc"],
            "answer": "Cedi"
        },
        {
            "question": "What is the capital city of Ghana?",
            "options": ["Kumasi", "Accra", "Tamale", "Cape Coast"],
            "answer": "Accra"
        },
    ],

    "🌍 African Geography": [
        {
            "question": "Which African country has the largest population?",
            "options": ["Ethiopia", "Egypt", "South Africa", "Nigeria"],
            "answer": "Nigeria"
        },
        {
            "question": "What is the longest river in Africa?",
            "options": ["Congo River", "Niger River", "Nile River", "Zambezi River"],
            "answer": "Nile River"
        },
        {
            "question": "What is the largest country in Africa by area?",
            "options": ["Sudan", "Congo", "Algeria", "Libya"],
            "answer": "Algeria"
        },
        {
            "question": "Which ocean borders the west coast of Africa?",
            "options": ["Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean"],
            "answer": "Atlantic Ocean"
        },
        {
            "question": "Mount Kilimanjaro is located in which country?",
            "options": ["Kenya", "Tanzania", "Uganda", "Ethiopia"],
            "answer": "Tanzania"
        },
        {
            "question": "Which African country has the most pyramids?",
            "options": ["Egypt", "Sudan", "Ethiopia", "Libya"],
            "answer": "Sudan"
        },
        {
            "question": "What is the smallest country in Africa?",
            "options": ["Gambia", "Djibouti", "Seychelles", "Eswatini"],
            "answer": "Seychelles"
        },
    ],

    "🏆 African Culture & People": [
        {
            "question": "Which country is known as the 'Rainbow Nation'?",
            "options": ["Kenya", "South Africa", "Tanzania", "Rwanda"],
            "answer": "South Africa"
        },
        {
            "question": "Who was the first African to win a Nobel Peace Prize?",
            "options": ["Kofi Annan", "Nelson Mandela", "Albert Luthuli", "Wangari Maathai"],
            "answer": "Albert Luthuli"
        },
        {
            "question": "Which African country is the birthplace of coffee?",
            "options": ["Kenya", "Ethiopia", "Uganda", "Tanzania"],
            "answer": "Ethiopia"
        },
        {
            "question": "What is the most widely spoken language in Africa?",
            "options": ["Swahili", "Arabic", "Hausa", "Zulu"],
            "answer": "Arabic"
        },
        {
            "question": "Which African city is known as the 'City of a Thousand Minarets'?",
            "options": ["Tunis", "Casablanca", "Cairo", "Khartoum"],
            "answer": "Cairo"
        },
        {
            "question": "The Great Zimbabwe ruins are located in which country?",
            "options": ["Zambia", "Zimbabwe", "Mozambique", "Botswana"],
            "answer": "Zimbabwe"
        },
        {
            "question": "Which African country hosted the first FIFA World Cup on African soil?",
            "options": ["Nigeria", "Kenya", "South Africa", "Egypt"],
            "answer": "South Africa"
        },
    ],

    "💡 Africa & Technology": [
        {
            "question": "Which African country has the highest number of tech startups?",
            "options": ["Ghana", "Kenya", "Nigeria", "South Africa"],
            "answer": "Nigeria"
        },
        {
            "question": "M-Pesa, the famous mobile money service, originated in which country?",
            "options": ["Ghana", "Nigeria", "Kenya", "Tanzania"],
            "answer": "Kenya"
        },
        {
            "question": "Which African city is often called the 'Silicon Savannah'?",
            "options": ["Lagos", "Accra", "Nairobi", "Cape Town"],
            "answer": "Nairobi"
        },
        {
            "question": "Which African country laid the first undersea fibre optic cable on the continent?",
            "options": ["South Africa", "Egypt", "Nigeria", "Ghana"],
            "answer": "South Africa"
        },
        {
            "question": "Andela, a famous African tech talent company, was founded in which country?",
            "options": ["Kenya", "Ghana", "Nigeria", "Rwanda"],
            "answer": "Nigeria"
        },
    ],
}


# ─── Helpers ──────────────────────────────────────────────────────────────────
def print_line():
    print("─" * 52)

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


# ─── Welcome Screen ───────────────────────────────────────────────────────────
def show_welcome():
    print("\n")
    print_line()
    slow_print("   🌍  HOW WELL DO YOU KNOW AFRICA?  🌍")
    print_line()
    slow_print("   Challenge your knowledge of the world's")
    slow_print("   most fascinating and misunderstood continent.")
    print_line()
    input("\n   Press ENTER to continue... ")
    print()


# ─── Category Menu ────────────────────────────────────────────────────────────
def choose_category():
    categories = list(QUESTIONS.keys())

    print_line()
    slow_print("   📂  CHOOSE A CATEGORY\n")
    for i, cat in enumerate(categories):
        print(f"   {i + 1}.  {cat}  ({len(QUESTIONS[cat])} questions)")
    print()

    while True:
        choice = input("   Enter a number (1–{}): ".format(len(categories))).strip()
        if choice.isdigit() and 1 <= int(choice) <= len(categories):
            selected = categories[int(choice) - 1]
            print()
            slow_print(f"   Great choice! Starting: {selected}\n")
            return selected
        print("   ⚠️  Please enter a valid number.")


# ─── Ask a Single Question ────────────────────────────────────────────────────
def ask_question(number, total, q_data):
    options = q_data["options"][:]
    random.shuffle(options)

    print_line()
    print(f"   Question {number} of {total}")
    print()
    slow_print(f"   ❓ {q_data['question']}")
    print()

    for i, option in enumerate(options):
        print(f"      {chr(65 + i)}.  {option}")

    print()

    while True:
        answer = input("   Your answer (A/B/C/D): ").strip().upper()
        if answer in ["A", "B", "C", "D"]:
            break
        print("   ⚠️  Please enter A, B, C, or D only.")

    chosen = options[ord(answer) - ord("A")]

    if chosen == q_data["answer"]:
        slow_print("\n   ✅  Correct! Well done!\n")
        return True
    else:
        slow_print(f"\n   ❌  Wrong! The answer was: {q_data['answer']}\n")
        return False


# ─── Results ──────────────────────────────────────────────────────────────────
def show_results(score, total, category):
    percentage = int((score / total) * 100)

    print_line()
    slow_print("   🏁  QUIZ COMPLETE!")
    print_line()
    print(f"\n   Category :  {category}")
    print(f"   Score    :  {score} / {total}  ({percentage}%)\n")

    if percentage == 100:
        slow_print("   🏆  PERFECT! You really know your Africa!")
    elif percentage >= 80:
        slow_print("   🌟  Excellent! Impressive knowledge!")
    elif percentage >= 60:
        slow_print("   👏  Good job! You know quite a bit!")
    elif percentage >= 40:
        slow_print("   📚  Not bad — keep exploring Africa!")
    else:
        slow_print("   💪  Keep learning — Africa's story is worth knowing!")

    print()
    print_line()


# ─── Main ─────────────────────────────────────────────────────────────────────
def main():
    show_welcome()

    while True:
        category = choose_category()
        questions = random.sample(QUESTIONS[category], len(QUESTIONS[category]))
        score = 0

        for i, question in enumerate(questions):
            correct = ask_question(i + 1, len(questions), question)
            if correct:
                score += 1

        show_results(score, len(questions), category)

        again = input("   Play again? (yes / no): ").strip().lower()
        if again not in ["yes", "y"]:
            print()
            slow_print("   Thanks for playing! Share this with a friend 🌍")
            print_line()
            print()
            break


if __name__ == "__main__":
    main()