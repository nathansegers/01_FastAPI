from database import db, start_db, check_seeded
import logging
from seeder import start_seeding
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
import os
from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed

max_tries = 60 * 5  # 5 minutes
wait_seconds = 1

@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
def init() -> None:
    try:
        # Try to create session to check if DB is awake
        db.execute("SELECT 1")
    except Exception as e:
        logger.error(e)
        raise e

def main() -> None:
    logger.info("Initializing service")
    init()
    logger.info("Service finished initializing")

    start_db()
    seeded = check_seeded()
    logging.info(f"Database is seeded: {seeded}")
    if not seeded:
        logging.info("""
        ----------------------------------------------------------------\n
        Start seeding database...\n
        ----------------------------------------------------------------\n
        """)
        start_seeding()
    else:
        logging.info("No need to seed!")


if __name__ == "__main__":
    main()


