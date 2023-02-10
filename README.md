# Bot-telegram-dowload-mp3-YouTube 

um script Python para um bot do Telegram que permite baixar vídeos do YouTube e convertê-los para o formato MP3. O bot usa a biblioteca Aiogram para lidar com a API Telegram Bot e lidar com as interações do usuário.


O comando ` /start ` envia uma mensagem ao usuário com instruções de como usar o bot.

O comando ` /help ` envia uma mensagem ao usuário explicando o que o bot faz.

O comando ` /download ` envia uma mensagem ao usuário solicitando a URL do vídeo do YouTube que deseja baixar e o converte em um arquivo MP3. O arquivo MP3 é então enviado de volta ao usuário.

O bot usa os utilitários "youtube-dl" e "ffmpeg" para baixar e converter os vídeos. O vídeo é primeiro baixado para o sistema de arquivos local e depois convertido para o formato MP3. Por fim, o arquivo MP3 é enviado de volta ao usuário.

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
