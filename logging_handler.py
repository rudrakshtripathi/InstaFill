import logging

# Configure logging
logging.basicConfig(
    filename="application_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def log_failed_application(internship_details, error):
    logging.error(f"Failed to apply for {internship_details}. Error: {error}")

def log_successful_application(internship_details):
    logging.info(f"Successfully applied for: {internship_details}")

def view_application_history():
    """Returns past internship applications as a list."""
    history = []
    try:
        with open("data/applied_history.csv", mode="r") as file:
            reader = csv.reader(file)
            history = list(reader)

        return history if history else [["No applications found", "", ""]]

    except Exception as e:
        return [["Could not load history", str(e), ""]]

def retry_failed_applications(progress_bar):
    """Retries failed applications from log."""
    failed_list = []
    try:
        with open("data/failed_applications.csv", mode="r") as file:
            reader = csv.reader(file)
            failed_list = list(reader)

        if not failed_list:
            print("No failed applications to retry.")
            return

        for row in failed_list:
            title, link, _ = row
            print(f"Retrying {title} ({link})...")
            # Modify function to accept link-based application
            # apply_for_multiple_internships(1, False, "", "", "", progress_bar)

    except Exception as e:
        print(f"Could not retry applications: {e}")
