# DISCLAIMER
## Script is meant to be for League of Legends .rofl files, if you need to parse other games rofl files, contact me to provide further updates.

# JSON-like Data Extractor and Parser for .ROFL Files

This Python project provides tools to extract and parse JSON-like data from `.rofl` files, which are often used in applications to store data in a somewhat structured format that resembles JSON. Specifically, this project targets extracting gameplay data, decoding it, and parsing the complex structure within to produce human-readable summaries of the game.

## Features

- **Extract JSON-like Data**: Extracts a segment of JSON-like data from binary `.rofl` files, handling encoding issues gracefully.
- **Parse Complex JSON Strings**: Parses complex, nested JSON strings that may not strictly adhere to JSON standards, using a robust method to handle unknown structures.
- **Generate Game Summaries**: Produces detailed summaries of gameplay, including time played, player stats (KDA, gold earned, minions killed, etc.), and other relevant information.

## Usage

1. **Setup**: Ensure you have Python installed on your system.

2. **Extract and Parse Data**:
   - Replace `'your_file_path_here'` with the actual path to your `.rofl` file in the script.
   - Run the script. It will extract JSON-like data from the file, parse it, and print out a game summary including each player's performance.

3. **Output**:
   - The script outputs the total game time in `MM:SS` format.
   - For each player, it prints their unique identifier, skin, KDA ratio, minions killed, gold earned, role, vision score, and win status.

## Dependencies

This project uses the `json` module from Python's standard library, requiring no external dependencies.

## Limitations

- The script is designed to work with `.rofl` files that contain specific patterns of JSON-like data. It may require adjustments for other file types or structures.

- Error handling is basic, focusing on the most common issues encountered with file reading and JSON parsing. Further refinement may be necessary for broader use cases.

## Contributing

Contributions are welcome! If you have improvements or encounter issues, please feel free to open an issue or submit a pull request.

