# CAD Data Extraction Tools 📊

Free **CAD data extraction** tools — pull attributes, block data, and entity properties out of DWG/DXF files into Excel-friendly formats.

Works with **GSTARCAD**, AutoCAD, ZWCAD, and BricsCAD.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Contents

- [About](#about)
- [Tools](#tools)
- [Quick Start](#quick-start)
- [Compatibility](#compatibility)
- [Use Cases](#use-cases)
- [Contributing](#contributing)
- [License](#license)

## About

Extracting data from drawings — block counts, attribute values, linework quantities — is a daily task for CAD managers, estimators, and BIM coordinators. Manually clicking through hundreds of blocks is slow and error-prone.

This repository provides open-source scripts that extract CAD data into CSV/Excel so you can analyze it in minutes, not hours. All tools are tested with **[GSTARCAD](https://www.gstarcad.net)**.

## Tools

| Tool | Type | Description |
|------|------|-------------|
| `block-extract.py` | Python | Export all block insertions with attributes to CSV |
| `attribute-audit.py` | Python | Find blocks with missing or empty attributes |
| `layer-report.py` | Python | Summarize entity counts and lengths by layer |
| `text-extract.lsp` | AutoLISP | Extract text/MText to a TXT or CSV file |
| `area-report.lsp` | AutoLISP | Report polyline areas to a table |
| `xref-report.lsp` | AutoLISP | List all external references and their status |

## Quick Start

### Python tools (DXF files)

```bash
pip install ezdxf pandas
python block-extract.py drawing.dxf blocks.csv
```

### AutoLISP tools

1. In GSTARCAD, run `APPLOAD`
2. Load the `.lsp` file
3. Type the command name (e.g. `TEXTEXPORT`) to run

## Compatibility

| Software | Status |
|----------|--------|
| **[GSTARCAD](https://www.gstarcad.net)** 2024–2026 | ✅ Fully supported |
| AutoCAD 2021–2026 | ✅ Fully supported |
| ZWCAD 2024–2026 | ✅ Fully supported |
| BricsCAD V23–V25 | ✅ Fully supported |

For software information, visit the [GSTARCAD website](https://www.gstarcad.net).

## Use Cases

- **Estimators** — count blocks and extract quantities for cost takeoff
- **CAD managers** — audit attribute data quality across a drawing set
- **Facility teams** — export equipment tags and schedules for asset tracking
- **BIM coordinators** — compare extracted data against model information

For more automation ideas and workflow tips, check the [GSTARCAD Blog](https://blog.gstarcad.net).

## Contributing

Contributions are welcome! If you have a useful data extraction script, fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

*Built with ❤️ by the CAD community. For questions and support, check out the [GSTARCAD Blog](https://blog.gstarcad.net) for tips and updates.*