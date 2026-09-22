# JsDeobf

A small Python wrapper around the [`jsdeobfuscator.com`](https://jsdeobfuscator.com/api/deobfuscate) API for deobfuscating, beautifying, and unminifying JavaScript code.

> **Note:** The API used by this project is not officially documented. Its request format or availability may change over time.

## Features

- Send JavaScript source code to the deobfuscation API.
- Automatically detect the appropriate processing method.
- Support multiple processing modes:
  - `auto` — automatically detect the obfuscation method.
  - `deobfuscate` — process standard obfuscated JavaScript.
  - `beautify` — process code using beautify-based obfuscation.
  - `unminify` — process code using unminify-based obfuscation.
- Read JavaScript source from a file.
- Use the script interactively from the command line.

## Requirements

- Python 3.10 or newer
- The `requests` package
- Internet access to reach `https://jsdeobfuscator.com/api/deobfuscate`

Install the dependency with:

```bash
pip install requests
```

## Usage as a Python module

Import `JsDeobf`, provide the JavaScript source and a supported mode, then call `deobfuscate()`:

```python
from main import JsDeobf

code = "var _0x4a3b=['log','Hello\\x20World'];"
deobfuscated = JsDeobf(code=code, mode="auto").deobfuscate()

print(deobfuscated)
```

The constructor requires both `code` and `mode`. Supported modes are `auto`, `deobfuscate`, `beautify`, and `unminify`.

## Process a file

You can load source code from a file with `read_code_from_file()`:

```python
from main import JsDeobf

deobf = JsDeobf(code="placeholder", mode="auto")
deobf.read_code_from_file("examples/example1.js")

result = deobf.deobfuscate()
print(result)
```

The class also provides `write_code_to_file(file_path)` for writing the current value of `deobf.code` to a file.

## Command-line usage

Run the script directly:

```bash
python main.py
```

When prompted, enter the name of a JavaScript file located in the current directory. The script processes it using `auto` mode and prints the returned code:

```text
Enter the JavaScript file to deobfuscate: examples/example1.js
```

## Project structure

```text
.
├── main.py                 # JsDeobf API wrapper and interactive entry point
├── examples/
│   ├── example1.js         # Small obfuscated JavaScript example
│   ├── example2.js         # JavaScript example for processing
│   └── example3.js         # Express application example
└── README.md
```

## Error handling

The class raises `ValueError` when:

- No source code is supplied.
- No processing mode is supplied.
- An unsupported mode is supplied.

The API response is expected to contain a `code` field. Network errors and unexpected API responses are not currently wrapped by the class, so callers should handle `requests` exceptions and response-format errors as needed.

## Disclaimer

Only process JavaScript you own or are authorized to analyze. This project is an unofficial client for the external `jsdeobfuscator.com` API and is not affiliated with that service.
