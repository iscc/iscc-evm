"""Compile Vyper contracts to bytecode and create abi files."""
import subprocess
import pathlib
from loguru import logger as log
import io

HERE = pathlib.Path(__file__).parent.absolute()


def build():
    for fp in HERE.glob("*.vy"):
        # compile
        r = subprocess.run(
            ["vyper", fp.as_posix()], capture_output=True, universal_newlines=True
        )
        outpath = fp.parent / (fp.stem + ".bin")
        with io.open(outpath, "wt", newline="\u000A") as outf:
            outf.write(r.stdout)
        log.info(f"built {outpath.name}")

        # export abi
        r = subprocess.run(
            ["vyper", "-f", "abi", fp.as_posix()],
            capture_output=True,
            universal_newlines=True,
        )
        outpath = fp.parent / (fp.stem + ".abi")
        with io.open(outpath, "wt", newline="\u000A") as outf:
            outf.write(r.stdout)
        log.info(f"built {outpath.name}")


if __name__ == "__main__":
    build()
