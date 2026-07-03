import schedule
import time

from logging_config import log_info, log_error



def weather_update():
    try:
        log_info("Running daily weather update...")
        print("Weather update completed.")
        
    except Exception as e:
        log_error(f"Weather Update Error: {str(e)}")



def aqi_monitor():
    try:
        log_info("Running AQI monitor...")
        print("AQI monitoring completed.")
    except Exception as e:
        log_error(f"AQI Monitor Error: {str(e)}")



def prediction_task():
    try:
        log_info("Generating AI predictions...")
        print("Prediction task completed.")
        # Future: Call your ai_service logic here!
    except Exception as e:
        log_error(f"Prediction Error: {str(e)}")



def excel_backup():
    try:
        log_info("Creating Excel backup...")
        print("Backup completed.")
       
    except Exception as e:
        log_error(f"Backup Error: {str(e)}")



def cleanup_logs():
    try:
        log_info("Cleaning old logs...")
        print("Log cleanup completed.")
    except Exception as e:
        log_error(f"Cleanup Error: {str(e)}")




schedule.every(1).hours.do(weather_update)
schedule.every(2).hours.do(aqi_monitor)
schedule.every(6).hours.do(prediction_task)
schedule.every().day.at("23:00").do(excel_backup)
schedule.every().sunday.at("01:00").do(cleanup_logs)



if __name__ == "__main__":
    log_info("Scheduler started...")
    print("Scheduler is running. Press Ctrl+C to exit.")
    
    while True:
        schedule.run_pending()
        time.sleep(1)