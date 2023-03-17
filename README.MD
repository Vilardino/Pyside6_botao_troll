# Pyside6 Botão troll
Este é um pequeno aplicativo que exibe uma janela com uma pergunta e dois botões. Quando um dos botões é clicado, a janela exibe uma nova mensagem. A imagem de fundo e o ícone da janela podem ser personalizados.

# Instalação
Para instalar as dependências listadas em um arquivo _requirements.txt_, você pode usar o comando pip da seguinte forma:

Use
`pip install -r requirements.txt`
para todas as dependências listadas no arquivo requirements.txt em seu ambiente Python atual. Certifique-se de estar no diretório correto onde o arquivo requirements.txt está localizado antes de executar este comando.

# Como personalizar o aplicativo
Se você deseja personalizar o aplicativo, há algumas opções que você pode alterar. Abaixo, seguem algumas instruções sobre como fazer isso.

## Alterar a imagem
A imagem que é exibida na janela é definida no código fonte do aplicativo. Se você deseja alterar a imagem, basta substituir o arquivo files/image.jpg por outro arquivo de imagem. Certifique-se de que o novo arquivo tenha o mesmo nome e a mesma extensão do arquivo original.

## Alterar o ícone
O ícone que é exibido na barra de título da janela é definido no código fonte do aplicativo. Se você deseja alterar o ícone, basta substituir o arquivo files/icone.png por outro arquivo de imagem. Certifique-se de que o novo arquivo tenha o mesmo nome e a mesma extensão do arquivo original.

Alterar a mensagem
A mensagem que é exibida na janela é definida no código fonte do aplicativo. Se você deseja alterar a mensagem, basta modificar a linha que contém o texto da mensagem no arquivo main.py. Por exemplo, se você deseja exibir a mensagem "Bem-vindo ao meu aplicativo!", basta alterar a seguinte linha:

```
self.label.setText('Vamos ficar juntos para sempre?')
```
para:

```
self.label.setText('Bem-vindo ao meu aplicativo!')
```
## Alterar o título da janela
O título que é exibido na barra de título da janela é definido no código fonte do aplicativo. Se você deseja alterar o título, basta modificar a seguinte linha no arquivo main.py:

```
mainwindow.setWindowTitle("Para todo sempre")
```
para:
```
mainwindow.setWindowTitle("Meu aplicativo personalizado")
```
## Como executar o aplicativo
Para executar o aplicativo, abra o terminal e navegue até o diretório do projeto. Em seguida, execute o seguinte comando:

```
python main.py
```
Isso abrirá a janela do aplicativo na tela.

# Gerar executaveis
## Para gerar o arquivo executavel no windows:

```
pyinstaller --name="Para_todo_sempre" --noconfirm --noconsole --onefile --icon='./files/icone.png' --add-data='./files/*;files/' --clean --log-level=WARN main.py
```

## Para gerar o arquivo executavel no linux:

```
pyinstaller --name="Para_todo_sempre" --noconfirm --noconsole --onefile --icon='./files/icone.png' --add-data='./files/*:files/' --clean --log-level=WARN main.py
```