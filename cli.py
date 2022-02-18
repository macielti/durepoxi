import adapters.files
import controllers.files
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--files', type=str, required=True)
    parser.add_argument('--output', type=str, required=True)
    args = parser.parse_args()

    clips = adapters.files.files_input_to_list_of_clips(args.files)
    controllers.files.compile_clips(clips, args.output)
