from pytube import YouTube
from pytube import Playlist

print("Download a video or a playlist : ")
result = input("your option is : ").lower()
if result == "video":
    # link = 'https://www.youtube.com/watch?v=FVq6TYw9WjE&list=PLuXY3ddo_8nzCVqXcTFqwcM5R0gZiMRiW&index=4&t=11s'
    video_link = input("Please enter the video url: ")
    output_video = input("Please enter out put path: ")
    video = YouTube(video_link)


    # print(f"The video title is :\n{video.title}\n---------------------")
    # print(f"The video description is :\n{video.description}\n---------------------")
    # print(f"The video views is :\n{video.views}\n---------------------")
    # print(f"The video rating is :\n{video.rating}\n---------------------")
    # print(f"The video duration is :\n{video.length/60} minutes \n---------------------")
    # print(video.streams)
    # for stream in video.streams:
    #     print(stream)

    # for stream in video.streams.filter(progressive=True, resolution="720p"):
    #     print(stream)

    # for stream in video.streams.filter(subtype="mp4"):
    #     print(stream)

    # print(video.streams.get_highest_resolution())

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
