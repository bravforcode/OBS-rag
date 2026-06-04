import os
import shutil
import hashlib

VAULT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BACKUP_PATH = os.path.join(os.path.dirname(VAULT_PATH), "Backups")
RESTORE_TEMP = os.path.join(os.getcwd(), ".ai", "restore_test")

def calculate_hash(path):
    sha256_hash = hashlib.sha256()
    with open(path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def verify_backup():
    if not os.path.exists(BACKUP_PATH):
        print(f"Backup not found at {BACKUP_PATH}. Skipping simulation.")
        # Create a mock file for demonstration if needed, but per instructions we just write the code.
        return

    print(f"Simulating restore from {BACKUP_PATH} to {RESTORE_TEMP}...")
    
    if os.path.exists(RESTORE_TEMP):
        shutil.rmtree(RESTORE_TEMP)
        
    shutil.copytree(BACKUP_PATH, RESTORE_TEMP)
    
    print("Verifying integrity...")
    mismatches = 0
    
    for root, dirs, files in os.walk(VAULT_PATH):
        for file in files:
            original_file = os.path.join(root, file)
            rel_path = os.path.relpath(original_file, VAULT_PATH)
            restored_file = os.path.join(RESTORE_TEMP, rel_path)
            
            if not os.path.exists(restored_file):
                print(f"[MISSING] {rel_path}")
                mismatches += 1
                continue
                
            if calculate_hash(original_file) != calculate_hash(restored_file):
                print(f"[CORRUPT] {rel_path}")
                mismatches += 1

    if mismatches == 0:
        print("Integrity Check: PASSED")
    else:
        print(f"Integrity Check: FAILED ({mismatches} issues found)")

    # Cleanup
    shutil.rmtree(RESTORE_TEMP)

if __name__ == "__main__":
    verify_backup()
