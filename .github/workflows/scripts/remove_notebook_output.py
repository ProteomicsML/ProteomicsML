"""Generate copies of all notebooks without code output."""

import subprocess
from glob import glob
from pathlib import Path


def main():
    for input_path in glob("**/*/*.ipynb"):
        input_path = Path(input_path)
        if input_path.stem.startswith("_"):
            # Remove existing notebooks copies without output
            input_path.unlink()
        else:
            # Generate new notebooks copies without output
            output_name = f"_{input_path.stem}"
            subprocess.run(
                ["jupyter", "nbconvert", "--clear-output", "--to", "notebook", "--output", str(output_name), str(input_path)],
                check=True,
            )


if __name__ == "__main__":
    main()
