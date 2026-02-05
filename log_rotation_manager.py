import os
import time
import gzip
import shutil

LOG_DIR = "logs"
COMPRESS_AFTER_DAYS = 3
DELETE_AFTER_DAYS = 7

now = time.time()

if not os.path.exists(LOG_DIR):
    print("Log directory not found")
    exit()

print("🔄 Log Rotation Started...\n")

for file in os.listdir(LOG_DIR):
    if file.endswith(".log"):
        file_path = os.path.join(LOG_DIR, file)
        file_age_days = (now - os.path.getmtime(file_path)) / 86400

        # Compress old logs
        if COMPRESS_AFTER_DAYS <= file_age_days < DELETE_AFTER_DAYS:
            gz_path = file_path + ".gz"
            if not os.path.exists(gz_path):
                with open(file_path, 'rb') as f_in, gzip.open(gz_path, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
                print(f"📦 Compressed: {file}")

        # Delete very old logs
        elif file_age_days >= DELETE_AFTER_DAYS:
            os.remove(file_path)
            print(f"🗑️ Deleted: {file}")

print("\n✅ Log Rotation Completed")
