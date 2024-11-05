from youtubesearchpython import ResultMode, VideosSearch
import json
import yt_dlp

musicas = ['drip to hard', 'MajorRD - bonde da rock']
link = ''
for i in musicas:
  videosSearch = VideosSearch(i, limit = 1)
  json_estrutura = videosSearch.result(mode = ResultMode.json)
  dados = json.loads(json_estrutura)
  link += f"{dados["result"][0]["link"]}\n"

link_list = link.split()

for i in link_list:
  ydl_opts = {
    'format': 'bestaudio/best',           
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',      
        'preferredcodec': 'mp3',           
        'preferredquality': '192',         
    }],
    'outtmpl': '%(title)s.%(ext)s',   
  }
  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(i)

