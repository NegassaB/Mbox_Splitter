import os
import sys
from contextlib import ExitStack

from tqdm import tqdm

if len(sys.argv) != 3:
    print("\nUsage: python mbox-splitter.py filename.mbox size")
    print("       where `size` is a positive integer in MB\n")
    sys.exit()

filename = sys.argv[1]
if not os.path.exists(filename):
    print(f"File `{filename}` does not exist.")
    sys.exit()

try:
    split_size = int(sys.argv[2]) * 1024 * 1024  # Convert MB to Bytes
except ValueError:
    print("Size must be a positive number")
    sys.exit()

if split_size < 1:
    print("Size must be a positive number")
    sys.exit()

print(f"Splitting `{filename}` into chunks of {sys.argv[2]} MB...\n")

# Use a progress bar based on the total file size
file_size = os.path.getsize(filename)
pbar = tqdm(total=file_size, unit="B", unit_scale=True, desc="Processing Data")

chunk_count = 1
output_template = filename.replace(".mbox", "_{}.mbox")
current_output_name = output_template.format(chunk_count)

current_chunk_size = 0
message_count = 0

# Use ExitStack to safely manage dynamic file opening
with open(filename, "rb") as infile, ExitStack() as stack:
    # Enter the first output file into the context stack
    outfile = stack.enter_context(open(current_output_name, "wb"))

    for line in infile:
        line_len = len(line)

        # Look for the standard binary signature of a new email block
        # It must start with b'From ' and we must already be over our target size
        if line.startswith(b"From ") and current_chunk_size >= split_size:
            # Clear previous file context (closes the old file safely)
            stack.pop_all().close()
            print(
                f"Created file `{current_output_name}`, size={current_chunk_size // (1024 * 1024)}MB, approx messages={message_count}."
            )

            chunk_count += 1
            current_output_name = output_template.format(chunk_count)
            # Safely open the next file under the context manager
            outfile = stack.enter_context(open(current_output_name, "wb"))
            current_chunk_size = 0
            message_count = 0

        if line.startswith(b"From "):
            message_count += 1

        outfile.write(line)
        current_chunk_size += line_len
        pbar.update(line_len)

    pbar.close()

# The last file block automatically closes when exiting the `with` block above
print(
    f"Created file `{current_output_name}`, size={current_chunk_size // (1024 * 1024)}MB, approx messages={message_count}."
)
print("\nDone.")
