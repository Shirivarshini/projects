import os
import shutil

# Use Windows Downloads from WSL
TARGET_FOLDER = "/mnt/c/Users/Your_Name/Downloads"

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Programs": [".py", ".java", ".cpp", ".exe"],
}

def safe_move(src, dest):
    if not os.path.exists(dest):
        shutil.move(src, dest)
    else:
        base, ext = os.path.splitext(dest)
        i = 1
        while os.path.exists(f"{base}_{i}{ext}"):
            i += 1
        shutil.move(src, f"{base}_{i}{ext}")

def organize_files():
    print("📂 Organizing files in:")
    print(f"➡️  {TARGET_FOLDER}\n")

    if not os.path.exists(TARGET_FOLDER):
        print("❌ Target folder does not exist!")
        return

    for file in os.listdir(TARGET_FOLDER):
        file_path = os.path.join(TARGET_FOLDER, file)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        file_ext = os.path.splitext(file)[1].lower()
        moved = False

        for folder, extensions in FILE_TYPES.items():
            if file_ext in extensions:
                folder_path = os.path.join(TARGET_FOLDER, folder)
                os.makedirs(folder_path, exist_ok=True)
                safe_move(file_path, os.path.join(folder_path, file))
                print(f"✅ {file} → {folder}/")
                moved = True
                break

        if not moved:
            other_path = os.path.join(TARGET_FOLDER, "Others")
            os.makedirs(other_path, exist_ok=True)
            safe_move(file_path, os.path.join(other_path, file))
            print(f"📦 {file} → Others/")

    print("\n🎉 File organization completed successfully!")

if __name__ == "__main__":
    organize_files()

