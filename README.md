# 📬 MBOX Splitter

A fast and efficient Python tool for splitting large .mbox email archive files into smaller chunks. Designed to prevent issues with oversized mailbox files and improve email management.

## 🚀 Features

✅ Splits large .mbox files into smaller parts based on size (MB)  
✅ Preserves email integrity and format  
✅ Real-time progress tracking with a dynamic progress bar  
✅ Automatically names output files sequentially (file_1.mbox, file_2.mbox, etc.)  
✅ Works efficiently with large .mbox files

## 📌 Requirements

Make sure you have Python 3.x installed. Additionally, install the required dependencies:

`pip install tqdm`

## 📥 Installation

Clone the repository and navigate to the project folder:

`git clone https://github.com/gray-area/mbox-splitter.git
cd mbox-splitter`

## 🔧 Usage

Move .mbox file into MBOX Splitter folder

Run the script with the following command:

`python splitter.py <filename.mbox> <size_in_MB>`

## 📌 Example

Splitting a backup.mbox file into 50MB chunks:

`python splitter.py backup.mbox 50`

## 📤 Output

The tool will generate new .mbox files in the same directory:

`backup_1.mbox (≈ 50MB)
backup_2.mbox (≈ 50MB)
backup_3.mbox (remaining size)`

## ⏳ Progress bar

For example if the input mbox file is 11GB and the output chucks are of 1024 MB = 1GB.

```text
Splitting `backup.mbox` into chunks of 1024 MB...

Processing Data:   9%|█▊                  | 1.07G/11.7G [00:53<08:09, 21.7MB/s]Created file `backup_1.mbox`, size=1025MB, approx messages=1749.
Processing Data:  18%|███▋                | 2.15G/11.7G [01:54<06:22, 24.9MB/s]Created file `backup_2.mbox`, size=1026MB, approx messages=1746.
Processing Data:  28%|█████▌              | 3.23G/11.7G [02:43<05:53, 23.9MB/s]Created file `backup_3.mbox`, size=1025MB, approx messages=2070.
Processing Data:  37%|███████▎            | 4.30G/11.7G [03:40<04:05, 30.1MB/s]Created file `backup_4.mbox`, size=1025MB, approx messages=1686.
...
Created file `backup_11.mbox`, size=868MB, approx messages=3083.

Done.
```

## 🛠️ How It Works

1. Reads the .mbox file message by message.

2. Calculates each email’s size in bytes.

3. Writes messages into a new .mbox file until it reaches the specified size.

4. Creates a new .mbox file and continues processing.

## 🐍 Compatibility

✅ Python 3.x  
✅ Works on Windows, macOS, and Linux

## 🏆 Contributing

Feel free to fork this repo and submit a pull request! Any contributions, suggestions, or improvements are welcome.

## 📜 License

MIT License. See LICENSE for details.

## 📧 Contact

For questions or support, open an issue on GitHub.

## 🚀 Enjoy hassle-free .mbox splitting! 🎯
