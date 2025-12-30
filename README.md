Python File Organizer

A Python-based automation tool that organizes files in a directory by categorizing them into folders based on file extensions. This project simplifies file management and improves productivity by reducing manual sorting.


## Features

* Automatically categorizes files by type (Images, Documents, Videos, etc.)
* Creates folders dynamically if they don’t exist
* Safely moves files without overwriting existing ones
* Displays real-time logs of file movements
* Works seamlessly on **Windows (via WSL)** and **Linux**


## Tech Stack

* **Language:** Python 3
* **Modules Used:** `os`, `shutil`


## Folder Categories

| Category  | File Extensions                  |
| --------- | -------------------------------- |
| Images    | `.jpg`, `.jpeg`, `.png`, `.gif`  |
| Documents | `.pdf`, `.docx`, `.txt`, `.pptx` |
| Videos    | `.mp4`, `.mkv`, `.avi`           |
| Music     | `.mp3`, `.wav`                   |
| Programs  | `.py`, `.java`, `.cpp`, `.exe`   |
| Others    | All uncategorized files          |


## Example Output Structure

```
Downloads/
├── Images/
├── Documents/
├── Videos/
├── Music/
├── Programs/
└── Others/
```


## How It Works

1. Scans all files in the target directory
2. Identifies file extensions
3. Matches extensions with predefined categories
4. Creates required folders automatically
5. Moves files safely into respective folders


## How to Run

### 1.Clone the Repository

```bash
git clone https://github.com/your-username/python-file-organizer.git
cd python-file-organizer
```

### 2.Update Target Directory

In `file_organizer.py`, set the folder you want to organize:

```python
TARGET_FOLDER = "/mnt/c/Users/Shirivarshini A/Downloads"
```

> If using Windows + WSL, always use `/mnt/c/` path format.


### 3.Run the Script

```bash
python file_organizer.py
```


## Sample Output

```
📂 Organizing files in:
➡️  /mnt/c/Users/Shirivarshini A/Downloads

✅ resume.pdf → Documents/
✅ image.png → Images/
📦 random.xyz → Others/

🎉 File organization completed successfully!
```


## Safety Handling

* Prevents overwriting files with the same name
* Renames duplicates automatically (e.g., `file_1.txt`)
* Skips existing directories


## Future Enhancements

* Command-line arguments support
* GUI version using `tkinter`
* Date-wise or size-based organization
* Config file for custom extensions
* Auto-run using task scheduler / cron jobs


## Use Cases

* Organizing Downloads folder
* Cleaning project directories
* Automating file management tasks
* Beginner-friendly Python automation project


## License

This project is open-source and free to use for learning and personal projects.


## Author

**Shirivarshini A**
Python Developer | Tech Enthusiast 


### If you like this project, don’t forget to star the repo!


