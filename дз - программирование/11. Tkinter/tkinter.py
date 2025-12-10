import tkinter as tk

def start_questionnaire():
    clear_window()
    global current_q, answers
    current_q = 0
    answers = []
    show_question()

def show_question():
    clear_window()
    
    tk.Label(window, text="Первый тест", font=("Arial", 16, "bold")).pack(pady=5)
    
    if current_q < len(questions):
        q = questions[current_q]
        tk.Label(window, text=f"Вопрос {current_q+1}/{len(questions)}", font=("Arial", 14)).pack(pady=10)
        tk.Label(window, text=q["question"], font=("Arial", 12), wraplength=400).pack(pady=10)
        
        global var
        var = tk.StringVar(value="")
        
        for i, option in enumerate(q["options"]):
            tk.Radiobutton(window, text=option, variable=var, value=option, 
                          font=("Arial", 11)).pack(anchor="w", padx=50, pady=2)
        
        tk.Button(window, text="Следующий", command=next_question, 
                 bg="#4CAF50", fg="white", padx=20).pack(pady=20)
        tk.Button(window, text="Выйти", command=window.quit,
                 bg="#f44336", fg="white", padx=20).pack(pady=5)
    else:
        save_results()

def next_question():
    global current_q
    if var.get() == "":
        return
    
    answers.append(var.get())
    current_q += 1
    show_question()

def save_results():
    filename = "анкета_результаты.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("Результаты анкеты по литературе\n")
        f.write("=" * 40 + "\n")
        for i, (q, a) in enumerate(zip(questions, answers)):
            f.write(f"\n{i+1}. {q['question']}\n")
            f.write(f"   Ответ: {a}\n")
    
    clear_window()
    tk.Label(window, text="Первый тест завершен!", font=("Arial", 14)).pack(pady=20)
    tk.Label(window, text="Результаты сохранены в файл:", font=("Arial", 12)).pack(pady=5)
    tk.Label(window, text=filename, font=("Arial", 12, "bold")).pack(pady=5)
    tk.Button(window, text="Начать второй тест", command=start_test, 
             bg="#2196F3", fg="white", padx=20).pack(pady=20)
    tk.Button(window, text="Выйти", command=window.quit,
             bg="#f44336", fg="white", padx=20).pack(pady=5)

def start_test():
    clear_window()
    global test_current_q, score, test_questions
    test_current_q = 0
    score = 0
    test_questions = load_test_questions()
    show_test_question()

def load_test_questions():
    questions = []
    questions = [
        {
            "question": "Кто написал 'Война и мир'?",
            "options": ["Лев Толстой", "Достоевский", "Пушкин"],
            "correct": ["Лев Толстой"]
        },
        {
            "question": "Автор 'Евгений Онегин'?",
            "options": ["Лермонтов", "Пушкин", "Гоголь"],
            "correct": ["Пушкин"]
        },
        {
            "question": "Кто написал 'Преступление и наказание'?",
            "options": ["Толстой", "Достоевский", "Тургенев"],
            "correct": ["Достоевский"]
        },
        {
            "question": "Автор 'Мёртвые души'?",
            "options": ["Гоголь", "Толстой", "Чехов"],
            "correct": ["Гоголь"]
        },
        {
            "question": "Кто написал 'Герой нашего времени'?",
            "options": ["Лермонтов", "Пушкин", "Тургенев"],
            "correct": ["Лермонтов"]
        }
    ]
    
    return questions

def show_test_question():
    clear_window()
    
    tk.Label(window, text="Второй тест", font=("Arial", 16, "bold")).pack(pady=5)
    
    if test_current_q < len(test_questions):
        q = test_questions[test_current_q]
        tk.Label(window, text=f"Вопрос {test_current_q+1}/{len(test_questions)}", 
                font=("Arial", 14)).pack(pady=10)
        tk.Label(window, text=q["question"], font=("Arial", 12), 
                wraplength=400).pack(pady=10)
        
        global test_vars
        test_vars = []
        
        for i, option in enumerate(q["options"]):
            var = tk.BooleanVar()
            test_vars.append(var)
            tk.Checkbutton(window, text=option, variable=var, 
                          font=("Arial", 11)).pack(anchor="w", padx=50, pady=2)
        
        tk.Button(window, text="Ответить", command=check_test_answer, 
                 bg="#2196F3", fg="white", padx=20).pack(pady=20)
        tk.Button(window, text="Выйти", command=window.quit,
                 bg="#f44336", fg="white", padx=20).pack(pady=5)
    else:
        show_test_results()

def check_test_answer():
    global test_current_q, score
    
    q = test_questions[test_current_q]
    selected = [q["options"][i] for i, var in enumerate(test_vars) if var.get()]
    
    if set(selected) == set(q["correct"]):
        score += 1
    
    test_current_q += 1
    show_test_question()

def show_test_results():
    clear_window()
    
    tk.Label(window, text="Второй тест завершен!", font=("Arial", 14)).pack(pady=20)
    tk.Label(window, text=f"Правильных ответов: {score} из {len(test_questions)}", 
            font=("Arial", 12)).pack(pady=10)
    
    tk.Button(window, text="Выйти", command=window.quit,
             bg="#f44336", fg="white", padx=30, pady=10).pack(pady=20)

def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

questions = [
    {
        "question": "Кто ваш любимый русский писатель?",
        "options": ["Лев Толстой", "Фёдор Достоевский", "Александр Пушкин", "Николай Гоголь"]
    },
    {
        "question": "Какое произведение вы читали недавно?",
        "options": ["Война и мир", "Преступление и наказание", "Евгений Онегин", "Мёртвые души"]
    },
    {
        "question": "Какой жанр вам больше нравится?",
        "options": ["Роман", "Поэма", "Рассказ", "Пьеса"]
    },
    {
        "question": "Как часто вы читаете книги?",
        "options": ["Ежедневно", "Несколько раз в неделю", "Раз в месяц", "Редко"]
    },
    {
        "question": "Предпочитаете бумажные или электронные книги?",
        "options": ["Бумажные", "Электронные", "Аудиокниги", "Всё перечисленное"]
    }
]

window = tk.Tk()
window.title("Литературный тест")
window.geometry("500x450")

current_q = 0
answers = []
test_current_q = 0
score = 0
test_questions = []
var = None
test_vars = []

start_questionnaire()
window.mainloop()