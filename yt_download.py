import yt_dlp
import os
import re

# FFmpeg'in kurulu olduğu yolu buraya yazın
ffmpeg_path = r'C:\ffmpeg\bin\ffmpeg.exe'

def is_playlist(url):
    return 'playlist' in url or 'list=' in url

def get_playlist_title(url):
    ydl_opts = {'quiet': True, 'extract_flat': True, 'skip_download': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return info.get('title', 'Playlist')
    
def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

while True:
    url = input('YouTube playlist veya video URL girin (çıkmak için -1): ')
    
    if url == '-1':
        print('Program sonlandırılıyor...')
        break
    
    if is_playlist(url):
        playlist_title = get_playlist_title(url)
        safe_title = re.sub(r'[\\/:*?"<>|]', '_', playlist_title)
        ensure_dir(safe_title)
        outtmpl = os.path.join(safe_title, '%(title)s.%(ext)s')
    else:
        ensure_dir('download')
        outtmpl = os.path.join('download', '%(title)s.%(ext)s')

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': outtmpl,
        'ffmpeg_location': ffmpeg_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': False if not is_playlist(url) else False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print('İndirme tamamlandı!\n')
    except Exception as e:
        print(f'Hata oluştu: {e}\n')