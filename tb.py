from pytube import YouTube

YouTube('http://youtube.com/watch?v=9bZkp7q19f0').streams.first().download()
yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0').streams.all()
