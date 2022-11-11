from django.shortcuts import render,redirect
from django.http import HttpResponse
#import Youtube method from pytube Module
from pytube import YouTube
#to download video to client side
from django.http import FileResponse
from io import BytesIO
import os
from wsgiref.util import FileWrapper
from requests import request
# Create your views here.
def index(request):
    context={}
    global url
    if request.POST.get('load'):
        url = request.POST['link']
        video = YouTube(url)
        vidTitle,vidThumbnail = video.title,video.thumbnail_url
        qual,stream = [],[]
        for vid in video.streams.filter(progressive=True):
            qual.append(vid.resolution)
            stream.append(vid)
        context = {'vidTitle':vidTitle,'vidThumbnail':vidThumbnail,
                        'qual':qual,'stream':stream,
                        'url':url}
    elif request.POST.get('download-video'):
        homedir = os.path.expanduser("~")
        dirs = homedir + '/Downloads/'
        yt = YouTube(url)
        choosen_quality = request.POST.get('Resolutions')
        video = yt.streams.get_by_itag(choosen_quality)
        video.download(output_path = dirs, filename = "video.mp4")
        file = FileWrapper(open(f'{dirs}/video.mp4', 'rb'))
        response = HttpResponse(file, content_type = 'application/vnd.mp4')
        response['Content-Disposition'] = 'attachment; filename = "video.mp4"'
        os.remove(f'{dirs}/video.mp4')
        return response
    return render(request,'index.html',context)