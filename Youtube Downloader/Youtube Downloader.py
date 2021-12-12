from pytube import YouTube
from pytube import Playlist

print("Download a video or a playlist : ")
result = input("your option is : ").lower()
if result == "video":
    # link = 'https://www.youtube.com/watch?v=FVq6TYw9WjE&list=PLuXY3ddo_8nzCVqXcTFqwcM5R0gZiMRiW&index=4&t=11s'
    video_link = input("Please enter the video url: ")
    output_video = input("Please enter out put path: ")
    video = YouTube(video_link)


    def finish():
        print("download done")


    video.streams.get_lowest_resolution().download(output_path=output_video)
    video.register_on_complete_callback(finish())

elif result == "playlist":
    playlist_link = input("Please enter the playlist link :")
    output_playlist = input("Please enter output path: ")
    playlist = Playlist(playlist_link)
    for video in playlist.videos:
        video.streams.get_lowest_resolution().download(output_path=output_playlist)


    def finish():
        print("download done")


    video.register_on_complete_callback(finish())
