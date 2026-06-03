from __future__ import annotations

import logging
import sys
from pathlib import Path

from config.settings import settings


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(f"helix_v3.{name}")
    if logger.handlers:
        return logger

    logger.setLevel(getattr(logging, settings.log_level.upper(), logging.INFO))

    fmt = logging.Formatter(
        "[%(asctime)s] %(levelname)-8s %(name)-30s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(fmt)
    logger.addHandler(console)

    log_dir = Path(settings.log_dir)
    log_dir.mkdir(parents=True, exist_ok=True)
    file_handler = logging.FileHandler(log_dir / f"{name}.log")
    file_handler.setFormatter(fmt)
    logger.addHandler(file_handler)

    return logger
