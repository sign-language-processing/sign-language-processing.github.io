import os
import re
import argparse
import imageio

# Create argument parser
parser = argparse.ArgumentParser(description='Fix GIFs in LaTeX document for use with animategraphics.')
parser.add_argument('input_file', metavar='input_file', type=str, help='path to the input LaTeX file')
parser.add_argument('output_file', metavar='output_file', type=str, help='path to the output LaTeX file')
args = parser.parse_args()


def get_gif_framerate(gif_path):
    # Load the GIF using imageio
    with imageio.get_reader(gif_path) as reader:
        # Get the framerate from the file metadata
        metadata = reader.get_meta_data()
        fps = int(1000/reader.get_meta_data()['duration'])
    # Return the framerate as an integer
    return int(fps)


# Regular expression to match \includegraphics commands
include_graphics_pattern = re.compile(r"\\includegraphics(\[[^\]]*\])?\{([^\}]+\.gif)\}")

# Read the entire input file into a string
with open(args.input_file, "r") as f:
    input_str = f.read()

# Find all \includegraphics commands in the input string
include_graphics_cmds = include_graphics_pattern.findall(input_str)

# # Loop through each \includegraphics command and replace the file path with animategraphics code
# for cmd in include_graphics_cmds:
#     # Get the full path of the .gif file
#     base_dir = os.path.dirname(args.input_file)
#     gif_path = os.path.join(os.path.dirname(args.input_file), cmd[1])
#     # Convert the .gif file to an animated PDF using ImageMagick
#     pdf_path = gif_path.replace('.gif', '.pdf')
#
#     if not os.path.exists(pdf_path):
#         os.system(f"convert {gif_path} -coalesce -density 300 -dispose previous -loop 0 {pdf_path}")
#         print(f"Converted {gif_path} to {pdf_path}")
#
#     # Replace the file path with animategraphics code, preserving the optional arguments
#     graphics_arguments = cmd[0][1:-1]
#     framerate = get_gif_framerate(gif_path)
#     pdf_path = pdf_path[len(base_dir)+1:]
#     animate_graphics_code = f"\\animategraphics[autoplay,loop,{graphics_arguments}]{{{framerate}}}{{{pdf_path}}}{{0}}{{}}"
#     input_str = input_str.replace(f"\\includegraphics{cmd[0]}{{{cmd[1]}}}", animate_graphics_code)

# Convert the middle frame of the .gif file to a JPEG using ImageMagick
for cmd in include_graphics_cmds:
    base_dir = os.path.dirname(args.input_file)
    gif_path = os.path.join(os.path.dirname(args.input_file), cmd[1])
    file_ext = gif_path.split('.')[-1]
    png_path = gif_path.replace('.' + file_ext, '.png')

    if not os.path.exists(png_path):
        num_frames = int(os.popen(f"identify -format \"%n \" {gif_path}").read().split(" ")[0])
        os.system(f"convert {gif_path} -coalesce -delete 0-{num_frames//2},{num_frames//2 + 2}-99999 {png_path}")
        # print(f"Converted {gif_path} to {png_path}")

    # Replace the file path with animategraphics code, preserving the optional arguments
    graphics_arguments = cmd[0][1:-1]
    pdf_path = png_path[len(base_dir)+1:]
    animate_graphics_code = f"\\includegraphics[{graphics_arguments}]{{{pdf_path}}}"
    input_str = input_str.replace(f"\\includegraphics{cmd[0]}{{{cmd[1]}}}", animate_graphics_code)

# Write the updated LaTeX file
with open(args.output_file, "w") as f:
    f.write(input_str)

print(f"Updated LaTeX file written to {args.output_file}")
