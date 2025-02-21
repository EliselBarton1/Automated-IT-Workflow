🚀 Automated IT Workflow - Cleanup Script

📄 Project Description

This project features a Python script (cleanup_temp.py) designed to automate the cleanup of temporary files in a specified directory. The script identifies and deletes files older than 7 days, enhancing system organization and freeing up storage space.

🛠 Features

Automatically deletes files older than 7 days in the specified folder.

Displays messages indicating which files are being deleted.

Includes error handling for improved stability.

🚧 Setup Instructions

1. Clone the Repository

git clone https://github.com/YOUR_USERNAME/Automated-IT-Workflow.git
cd Automated-IT-Workflow/Python_Clean_Up

2. Ensure Dependencies are Installed

Python 3.x (Verify using python3 --version)

VS Code (Optional for code editing)

3. Prepare the Temp Directory

mkdir ~/Temp
touch ~/Temp/testfile1.txt
touch ~/Temp/testfile2.log

4. Run the Script

python3 cleanup_temp.py

🟢 Expected Output

Deleting testfile1.txt...
Deleting testfile2.log...

🚀 Optional: Automate with Cron Job

Open the crontab editor:

crontab -e

Add the following line to run the script daily at 12 PM:

0 12 * * * /usr/bin/python3 /home/ebarton/projects/Automated-IT-Workflow/Python_Clean_Up/cleanup_temp.py

📝 Troubleshooting

No files deleted: Check if files are older than 7 days.

Permission errors: Ensure the script has appropriate permissions (chmod +x cleanup_temp.py).

Python not found: Verify Python installation using python3 --version.

💡 Future Enhancements

Implement a cron job for scheduled automation.

Add logging to track deleted files in a log file (cleanup.log).

Enable configurable settings for folder path and file age threshold.

📂 Project Structure

Automated-IT-Workflow/
│
├─ Python_Clean_Up/
│    ├─ cleanup_temp.py          # Main script for cleaning up old files
│    ├─ com.ellie.cleanup.plist  # (Optional) Automation script for macOS
│    ├─ README.md                # Project documentation
│    └─ .gitignore               # Files/folders to exclude from version control
│
└─ Temp/                         # Directory containing temporary files

👥 Contributors

Elisel Barton - Project Development and Testing

📄 License

This project is licensed under the MIT License.