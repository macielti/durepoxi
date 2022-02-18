from moviepy.editor import concatenate_videoclips
import adapters.files


def compile_clips(clips, output):
    youtube_friendly_format_clips = adapters.files.clips_to_youtube_format_friendly(clips)
    concatenated_clips = concatenate_videoclips(youtube_friendly_format_clips, method="compose")
    concatenated_clips.write_videofile(output, codec="libx264", audio_codec="aac")
