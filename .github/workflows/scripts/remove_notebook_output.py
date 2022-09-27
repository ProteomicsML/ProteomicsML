"""Generate copies of all notebooks without code output."""

import logging
from glob import glob
from pathlib import Path

from execnb.nbio import read_nb, write_nb
from nbdev import clean
from rich.logging import RichHandler

logging.basicConfig(
    level="INFO", format="%(message)s", handlers=[RichHandler()]
)

def main():
    # Remove existing notebooks copies without output
    for input_path in glob("**/*/_*.ipynb"):
        input_path = Path(input_path)
        logging.info(f"Removing {input_path}")
        input_path.unlink()

    # Generate new notebooks copies without output
    for input_path in glob("**/*/*.ipynb"):
        input_path = Path(input_path)
        logging.info(f"Processing {input_path}")
        copy_path = input_path.with_name("_" + input_path.name)
        nb = read_nb(input_path)

        # Clean notebook, keep outputs; overwrite
        clean.clean_nb(nb, clear_all=False)
        input_path.unlink()
        write_nb(nb, input_path)

        # Clean notebook; remove outputs; write to copy
        clean.clean_nb(nb, clear_all=True)
        write_nb(nb, copy_path)


if __name__ == "__main__":
    main()
