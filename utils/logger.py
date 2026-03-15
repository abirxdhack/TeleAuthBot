import logging
import sys

_handler = logging.StreamHandler(sys.stdout)
_handler.setLevel(logging.INFO)
_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"))

logger = logging.getLogger("TeleAuthBot")
logger.setLevel(logging.INFO)
logger.addHandler(_handler)

logging.getLogger("telethon").setLevel(logging.WARNING)
logging.getLogger("pyrogram").setLevel(logging.WARNING)