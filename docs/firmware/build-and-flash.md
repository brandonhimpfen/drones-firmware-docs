# Build and Flash Documentation

Build and flash instructions must be exact enough for a new engineer or field technician to reproduce the process.

## Required information

- Supported operating systems
- Toolchain versions
- Python version
- Compiler version
- Board target names
- Required environment variables
- Build commands
- Flash commands
- Expected output
- Troubleshooting steps

## Example structure

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
make board_name_default
make board_name_upload
```

## Flash safety notes

- Confirm hardware target before flashing.
- Remove propellers before bench flashing or motor tests.
- Use stable power during firmware update.
- Validate firmware version after flashing.
- Keep rollback firmware available.
