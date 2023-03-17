# Para gerar o arquivo executavel no windows:

```
pyinstaller --name="Para_todo_sempre" --noconfirm --noconsole --onefile --icon='./files/icone.png' --add-data='./files/*;files/' --clean --log-level=WARN main.py
```
