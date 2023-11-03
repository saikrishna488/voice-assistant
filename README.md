# Simple Python Voice Assistant

This is a basic Python voice assistant that can perform simple tasks like telling the time, searching on Google, and finding a location. It uses several libraries to enable voice recognition, speech synthesis, and audio playback.

## Features
- Speech recognition to understand your voice commands.
- Uses Google Text-to-Speech (gTTS) for generating speech output.
- Plays audio using the `playsound` library.
- Can provide the current time.
- Can perform Google searches.
- Can find a location based on your query.

## Installation

Make sure you have Python installed on your system. You can install the required libraries using `pip`:

```bash
pip install SpeechRecognition pyaudio gtts playsound
```

## Usage

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/saikrishna488/voice-assistant.git
   ```

2. Navigate to the project directory:

   ```bash
   cd voice-assistant
   ```

3. Run the Python script:

   ```bash
   python main.py
   ```

4. The voice assistant will prompt you to speak a command. You can say commands like:
   - "What time is it?"
   - "Search for OpenAI on Google."
   - "Find a coffee shop near me."

## Dependencies

This project relies on the following Python libraries:
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/): Used for voice recognition.
- [PyAudio](https://pypi.org/project/PyAudio/): Required for working with audio input and output.
- [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/): Used for converting text to speech.
- [playsound](https://pypi.org/project/playsound/): Used for playing audio.

## Customize

You can customize the voice assistant's responses and commands by editing the `voice_assistant.py` script.

## Contributing

Feel free to contribute to this project by adding new features or improving the existing code. You can submit pull requests, report issues, or provide feedback.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Author

- Sai Krishna Reddy
- GitHub: [Your GitHub Profile](https://github.com/saikrishna488)

## Acknowledgments

- Special thanks to the developers of the `SpeechRecognition`, `pyaudio`, `gtts`, and `playsound` libraries for making this project possible.

Enjoy using your Simple Python Voice Assistant! If you have any questions or need assistance, feel free to reach out.
