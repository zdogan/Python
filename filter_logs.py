# This script reads a log file, filters the lines based on a keyword, and prints the relevant lines.
import re # module is used for regular expression operations.

def filter_security_logs(log_file_path, keyword):
    # Open the log file in read mode
    with open(log_file_path, 'r') as file:
        logs = file.readlines()
    
    # Filter logs that contain the keyword (case-insensitive)
    relevant_logs = [log for log in logs if re.search(keyword, log, re.IGNORECASE)]
    
    return relevant_logs

# Example usage
if __name__ == "__main__":  #ensure it runs only when the script is executed directly
    log_file_path = 'security_logs.txt'
    keyword = 'error'
    filtered_logs = filter_security_logs(log_file_path, keyword)

    # Print each filtered log
    for log in filtered_logs:
        print(log)