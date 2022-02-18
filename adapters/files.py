from moviepy.editor import VideoFileClip
from moviepy.video.fx.resize import resize


def files_input_to_list_of_clips(files):
    file_paths = files.split("|")
    return [VideoFileClip(path) for path in file_paths]


def clips_to_youtube_format_friendly(clips):
    resized_clips = map(lambda clip: resize(clip, height=1080, width=1920), clips)
    return list(resized_clips)
