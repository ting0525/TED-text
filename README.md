# VTT to Markdown Converter

A desktop application that converts VTT subtitle files to Markdown format with customizable headers.

![Application Screenshot](assets/screenshot.png)

## Features

- Download VTT files from URLs
- Convert VTT subtitles to Markdown format
- Add custom header formatting (### prefix)
- Customize output filename
- User-friendly GUI interface
- Progress tracking
- Error handling and status updates

## Installation

### Option 1: Run from Source

1. Clone the repository:
```bash
git clone https://github.com/yourusername/vtt-converter.git
cd vtt-converter
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

### Option 2: Use Executable (Windows)

1. Download the latest release from the Releases page
2. Extract the ZIP file
3. Run `VTTConverter.exe`

## Building from Source

To create your own executable:

1. Install cx_Freeze:
```bash
pip install cx_Freeze
```

2. Run the build script:
```bash
python build.py build
```

The executable will be created in the `build` directory.

## Usage

1. Launch the application
2. Enter the VTT file URL in the URL field
3. (Optional) Enter a custom filename for the output
4. Choose an output folder or use the default
5. Click "Process VTT" to start conversion
6. Monitor progress in the status window

## Requirements

- Python 3.7 or higher
- Required packages:
  - requests
  - tkinter (usually comes with Python)
  - cx_Freeze (for building executable)

## Development

### Project Structure
```
vtt_converter/
├── src/
│   ├── gui/          # GUI related modules
│   ├── processors/   # Core processing logic
│   ├── utils/        # Utility functions
│   └── config/       # Configuration files
├── assets/           # Icons and resources
└── main.py          # Application entry point
```

### Adding New Features

1. For GUI changes: Modify files in `src/gui/`
2. For processing logic: Update `src/processors/`
3. For utility functions: Add to `src/utils/`

## License

[MIT License](LICENSE)

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## Troubleshooting

### Common Issues

1. **URL Error**: Ensure the URL ends with .vtt
2. **Download Failed**: Check your internet connection
3. **Conversion Error**: Verify the VTT file format
4. **Permission Error**: Run as administrator or check folder permissions

## Contact

For support or suggestions, please open an issue in the GitHub repository.