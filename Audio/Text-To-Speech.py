import argparse
import asyncio
import os
import subprocess
import sys
import edge_tts

# Quick preset map for popular high-quality neural voices
VOICES = {
    "gb-male": "en-GB-RyanNeural",
    "gb-female": "en-GB-SoniaNeural",
    "us-male": "en-US-AndrewNeural",
    "us-female": "en-US-AvaNeural",
    "au-male": "en-AU-WilliamNeural",
}

async def generate_speech(text, voice_id, output_file, rate="+0%"):
    """Generates audio asynchronously using edge-tts."""
    try:
        communicate = edge_tts.Communicate(text, voice_id, rate=rate)
        await communicate.save(output_file)
        # Suppress output from xdg-open to keep the terminal clean
        subprocess.run(["xdg-open", output_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"Error generating audio: {e}")

async def interactive_mode(voice_id, rate):
    """Live interactive prompt to talk directly from the terminal."""
    print(f"\n--- Interactive Mode Enabled ({voice_id}) ---")
    print("Type your text and hit Enter. Type 'exit' , 'quit' or 'close' to leave.\n")

    count = 1
    while True:
        try:
            text = input("Say > ").strip()
            if text.lower() in ["exit", "quit","close"]:
                print("Exiting interactive mode.")
                break
            if not text:
                continue

            temp_file = f"temp_speech_{count}.mp3"
            await generate_speech(text, voice_id, temp_file, rate)
            count += 1
        except (KeyboardInterrupt, EOFError):
            break

def main():
    parser = argparse.ArgumentParser(description="Text-to-Speech CLI")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-t", "--text", type=str, help="Single text string to convert")
    group.add_argument("-f", "--file", type=str, help="Path to a text file")
    group.add_argument("-i", "--interactive", action="store_true", help="Launch live terminal typing mode")

    parser.add_argument("-v", "--voice", choices=VOICES.keys(), default="gb-male", help="Select voice preset (default: gb-male)")
    parser.add_argument("-r", "--rate", type=str, default="+0%", help="Speed modification (e.g., '+20%%' or '-10%%')")
    parser.add_argument("-o", "--output", type=str, default="output.mp3", help="Output filename")

    args = parser.parse_args()

    selected_voice = VOICES[args.voice]

    if args.interactive:
        asyncio.run(interactive_mode(selected_voice, args.rate))
    elif args.file:
        if os.path.exists(args.file):
            with open(args.file, "r", encoding="utf-8") as f:
                content = f.read()
            asyncio.run(generate_speech(content, selected_voice, args.output, args.rate))
        else:
            print(f"Error: File '{args.file}' not found.")
    elif args.text:
        asyncio.run(generate_speech(args.text, selected_voice, args.output, args.rate))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

