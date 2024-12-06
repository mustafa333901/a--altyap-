import logging

# --------------------
# 5. Performans ve İzleme
# --------------------
class Monitoring:
    @staticmethod
    def setup_logging(log_file="app.log"):
        """Loglama yapılandırmasını yapar."""
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format='%(asctime)s:%(levelname)s:%(message)s'
        )

    @staticmethod
    def log_message(message):
        """Log kaydını oluşturur."""
        logging.info(message)
