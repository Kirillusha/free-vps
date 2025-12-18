from pyrogram import Client

print("--- Генератор сессии Pyrogram ---")

# Using :memory: so we don't create a .session file
with Client(":memory:") as client:
    session_string = client.export_session_string()
    print("\n--- ВАША СТРОКА СЕССИИ (PYROGRAM) ---")
    print(session_string)
    print("\n--- КОНЕЦ ---")
    print("Скопируйте эту строку и вставьте ее в управляющего бота.")
    print("После ввода API ID и Hash, клиент запросит номер телефона, код и пароль (если есть) прямо здесь, в консоли.")
