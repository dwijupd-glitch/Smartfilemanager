import os
import shutil
import csv
from datetime import datetime

def organize_directory(target_path):
    """
    Core execution pipeline for StorageSentry v1.0:
    1. Validates target directory path.
    2. Scans files and maps extensions to target subfolders[cite: 4, 5, 6].
    3. Moves files using shutil and logs transactions to a persistent CSV[cite: 4, 5, 8].
    4. Computes disk analytics and triggers rule-based alerts.
    """
    # Step 01: Path Validation
    if not os.path.exists(target_path):
        print(f"[Error] Invalid path input: '{target_path}' does not exist[cite: 3, 10].")
        return

    # Extension lookup tables for automatic routing[cite: 4, 6]
    extension_mapping = {
        '.pdf': 'Documents',
        '.docx': 'Documents',
        '.txt': 'Documents',
        '.jpg': 'Images',
        '.png': 'Images',
        '.jpeg': 'Images',
        '.mp4': 'Videos',
        '.mkv': 'Videos',
        '.zip': 'Archives',
        '.rar': 'Archives'
    }

    category_bytes = {}
    total_bytes = 0
    log_records = []

    # Data Persistence Engine Setup (storagesentry_log.csv)
    csv_filename = 'storagesentry_log.csv'
    file_exists = os.path.exists(csv_filename)

    with open(csv_filename, mode='a', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        if not file_exists:
            # Write header if file is newly created
            writer.writerow(['Timestamp', 'File Name', 'Category', 'Size (Bytes)'])

        # Traverse target directory entries[cite: 5, 6]
        for filename in os.listdir(target_path):
            file_path = os.path.join(target_path, filename)

            # Skip subdirectories, process files only
            if os.path.isdir(file_path):
                continue

            # Step 02: Extension Mapping[cite: 5]
            _, ext = os.path.splitext(filename)
            ext = ext.lower()

            # TC-03: Unknown Extension Test -> Route to 'Others' subfolder[cite: 10]
            category = extension_mapping.get(ext, 'Others')

            # Get file size in bytes
            file_size = os.path.getsize(file_path)
            total_bytes += file_size

            # Aggregate category bytes
            category_bytes[category] = category_bytes.get(category, 0) + file_size

            # Step 03: Directory Routing (makedirs and shutil.move)[cite: 4, 5]
            category_dir = os.path.join(target_path, category)
            if not os.path.exists(category_dir):
                os.makedirs(category_dir)

            destination_path = os.path.join(category_dir, filename)
            shutil.move(file_path, destination_path)

            # Step 04: CSV Persistence[cite: 4, 5, 8]
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            writer.writerow([timestamp, filename, category, file_size])
            log_records.append((filename, category, file_size))

    # Step 05: Disk Analytics & Computational Engine[cite: 4, 5, 7]
    print("\n--- STORAGESENTRY v1.0 ANALYTICS REPORT ---")
    if total_bytes == 0:
        print("No files processed or directory is empty.")
        return

    # Size Aggregation Formula (Bytes to Megabytes)
    total_mb = total_bytes / (1024 * 1024)
    print(f"Total Storage Processed: {total_mb:.2f} MB")

    print("\nCategory Percentage Distribution:")
    for cat, b_count in category_bytes.items():
        # Percentage Distribution Formula[cite: 7]
        share_pct = (b_count / total_bytes) * 100
        print(f" * {cat}: {share_pct:.2f}% ({b_count} bytes)")

    # Rule Alert Engine[cite: 4, 7]
    print("\n--- RULE ALERT ENGINE ---")
    
    # Check oversized files (> 50 MB threshold)[cite: 4, 7]
    oversized_threshold = 50 * 1024 * 1024
    for filename, category, f_size in log_records:
        if f_size > oversized_threshold:
            print(f"[ALERT] Oversized File Detected: '{filename}' in '{category}' ({f_size / (1024*1024):.2f} MB > 50 MB)[cite: 4, 7]")

    # Check storage distribution spikes (> 50% category share)[cite: 4, 7]
    for cat, b_count in category_bytes.items():
        share_pct = (b_count / total_bytes) * 100
        if share_pct > 50.0:
            print(f"[ALERT] Storage Spike Warning: Category '{cat}' occupies {share_pct:.2f}% of total storage (> 50%)[cite: 4, 7]")

if __name__ == '__main__':
    user_path = input("Enter target directory path to organize: ")
    organize_directory(user_path)