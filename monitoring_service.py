
# monitoring_service/monitoring_service.py
from prometheus_client import start_http_server
import logging

class MonitoringService:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def run(self):
        """Start the monitoring service."""
        start_http_server(8005)  # Expose metrics on port 8005
        self.logger.info("Monitoring service started.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    service = MonitoringService()
    service.run()