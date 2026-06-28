import logging
import os

# ==========================================
# Create Logs Folder
# ==========================================

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "weather_intelligence.log")

# ==========================================
# Configure Logging
# ==========================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

# ==========================================
# Create Logger
# ==========================================

logger = logging.getLogger("WeatherIntelligencePro")


# ==========================================
# Helper Functions
# ==========================================

def log_info(message):
    logger.info(message)


def log_warning(message):
    logger.warning(message)


def log_error(message):
    logger.error(message)


def log_critical(message):
    logger.critical(message)