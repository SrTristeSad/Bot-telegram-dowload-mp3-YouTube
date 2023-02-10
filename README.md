# Bot-telegram-dowload-mp3-YouTube 

# como instalar na vps 

1° Instalar o Python na VPS:

` sudo apt-get update `

` sudo apt-get install python3.7 `

2° Instalar o pip:

` sudo apt-get install python3-pip `

3° Instalar as dependências necessárias para o funcionamento do bot:

` pip3 install aiogram youtube-dl ffmpeg `

4° Carregar o código-fonte do bot na VPS:

Você pode fazer isso usando o comando ` scp ` ou copiando e colando o código em um editor de texto na VPS.

5° Executar o bot:

` python3 bot.py `



Observe que você precisará substituir "BOT_TOKEN_HERE" no código pelo token de seu bot do Telegram. Além disso, certifique-se de que as bibliotecas youtube-dl e ffmpeg estejam instaladas e funcionando corretamente na VPS.
