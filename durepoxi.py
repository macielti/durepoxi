import adapters.files
import controllers.files
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--files', type=str, required=True, help='Path to files separated by "|". Example: '
                                                                 '"0e4f7545-3503-4d8b-af3c-039b4ede241b.mp4|2f6f5e25'
                                                                 '-e86f-4b35-86a1-592e15fff5eb.mp4|20eb1ad5-e92d-4f7c'
                                                                 '-a860-f0e62490afc4.mp4"', )
    parser.add_argument('--output', type=str, required=True,
                        help='Directory path to file where the file will be saved. Example: "/tmp/result.mp4"')
    args = parser.parse_args()

    clips = adapters.files.files_input_to_list_of_clips(args.files)
    controllers.files.compile_clips(clips, args.output)
