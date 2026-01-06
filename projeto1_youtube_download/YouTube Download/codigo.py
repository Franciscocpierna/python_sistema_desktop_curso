''' from mhyt import yt_download       forma antiga a biblioteca mhyt em desuso

url = "https://www.youtube.com/watch?v=xCe9wnBjIcs"
file = "spyar.mp4"
yt_download(url,file)
'''


import yt_dlp # substituiu a biblioteca, mhyt yt_download

def baixar_video_compativel(url, nome_arquivo):
    # Configurações para garantir compatibilidade com Filmes e TV / Media Player
    ydl_opts = {
        # 'f' força o formato de vídeo h264 (avc1) e áudio m4a (aac)
        # Isso garante que o Windows consiga abrir sem precisar de codecs extras
        'format': 'bestvideo[vcodec^=avc1]+bestaudio[ext=m4a]/best[vcodec^=avc1]/best',
        'outtmpl': nome_arquivo,
        'quiet': False,
        # Garante que o merge dos arquivos resulte em um mp4 real
        'merge_output_format': 'mp4',
    }

    try:
        print(f"Iniciando download compatível: {url}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"\nDownload concluído com sucesso: {nome_arquivo}")
        print("Este arquivo agora deve abrir no 'Filmes e TV' e 'Media Player'.")
    except Exception as e:
        print(f"\nErro no download: {e}")

if __name__ == "__main__":
    # Link do vídeo
    url = "https://www.youtube.com/watch?v=xCe9wnBjIcs"
    # Nome do arquivo de saída
    file = "spyar_compativel.mp4"
    
    baixar_video_compativel(url, file)