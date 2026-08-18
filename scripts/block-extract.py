#!/usr/bin/env python3
"""Export all block insertions with attributes to CSV."""
import argparse

try:
    import ezdxf
except ImportError:
    raise SystemExit("pip install ezdxf")


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract blocks to CSV")
    parser.add_argument("dxf", help="Input DXF file")
    parser.add_argument("csv", help="Output CSV file")
    args = parser.parse_args()

    doc = ezdxf.readfile(args.dxf)
    msp = doc.modelspace()

    with open(args.csv, "w", encoding="utf-8") as fh:
        fh.write("block_name,insert_x,insert_y,rotation,attributes\n")
        for insert in msp.query("INSERT"):
            attrs = ";".join(
                f"{tag}={value}" for tag, value in insert.attribs_text()
            )
            fh.write(
                f"{insert.dxf.name},{insert.dxf.insert.x:.3f},"
                f"{insert.dxf.insert.y:.3f},{insert.dxf.rotation:.2f},"
                f"{attrs}\n"
            )

    print(f"Exported block data to {args.csv}")


if __name__ == "__main__":
    main()