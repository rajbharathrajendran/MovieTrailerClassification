import csv
#from _future_ import absolute_import, unicode_literals
import youtube_dl as yd

def Download_Video(url_list,quiet=False):
    name=r"results/"+"%(id)s--%(title)s.mp4"
    ydl_opts = {'ignoreerrors':True,'writeautomaticsub':True,
                'outtmpl':name,
                "quiet":quiet}
    ydl=yd.YoutubeDL(ydl_opts)
    ydl.download(url_list)

with open("../youtube_ids.txt") as f:
    youtube_ids = f.readlines()
with open("../movies_list.txt") as f:
    movie_ids = f.readlines()
with open("../metadata/Genre.txt") as f:
    genre = f.readlines()

genre_list = [(genre[i].strip().split(",")) for i in range(0,len(genre))]
trailer_data = [("https://www.youtube.com/watch?v="+youtube_ids[i].strip(), movie_ids[i].strip(), genre_list[i][0], genre_list[i][1], genre_list[i][2], genre_list[i][3], genre_list[i][4], genre_list[i][5], genre_list[i][6], genre_list[i][7], genre_list[i][8], genre_list[i][9]) for i in range(0,len(youtube_ids))]

with open('../trailer_data.csv', 'wb') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(trailer_data)

with open("../trailer_data.csv","r") as file:
    lines=file.readlines()
urls=[l.split(",")[0] for l in lines[1:]]
Download_Video(urls)
