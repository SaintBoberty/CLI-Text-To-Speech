import argparse
import asyncio
import os
import subprocess
import sys
import edge_tts

# Expanded library of high-quality neural voices
VOICES = {
    # --- Hyper-Realistic / Multilingual (Top Tier) ---
    "ava": "en-US-AvaMultilingualNeural",
    "andrew": "en-US-AndrewMultilingualNeural",
    "brian": "en-US-BrianMultilingualNeural",
    "emma": "en-US-EmmaMultilingualNeural",

    # --- US Accents ---
    "us-aria": "en-US-AriaNeural",          # Expressive / Conversational
    "us-guy": "en-US-GuyNeural",            # Deep / Casual
    "us-jenny": "en-US-JennyNeural",        # Natural / Narrative
    "us-chris": "en-US-ChristopherNeural",  # Energetic
    "us-steffan": "en-US-SteffanNeural",    # Storyteller / Smooth

    # --- UK Accents ---
    "uk-ryan": "en-GB-RyanNeural",          # Clear / Professional
    "uk-sonia": "en-GB-SoniaNeural",        # Calm / Warm
    "uk-thomas": "en-GB-ThomasNeural",      # Deep British
    "uk-maisie": "en-GB-MaisieNeural",      # Casual British

    # --- Australian Accents ---
    "au-natasha": "en-AU-NatashaNeural",
    "au-william": "en-AU-WilliamNeural",

    # --- Canadian Accents ---
    "ca-clara": "en-CA-ClaraNeural",
    "ca-liam": "en-CA-LiamNeural",

    # --- Irish & South African ---
    "ie-emily": "en-IE-EmilyNeural",
    "ie-connor": "en-IE-ConnorNeural",
    "za-leah": "en-ZA-LeahNeural",

    # --- Indian English ---
    "in-neerja": "en-IN-NeerjaNeural",
    "in-prabhat": "en-IN-PrabhatNeural",
}

async def generate_speech(text, voice_id, output_file, rate="+0%"):
    """Generates audio asynchronously using edge-tts."""
    try:
        communicate = edge_tts.Communicate(text, voice_id, rate=rate)
        await communicate.save(output_file)
        subprocess.run(["xdg-open", output_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"Error generating audio: {e}")

async def interactive_mode(voice_id, rate):
    """Live interactive prompt to talk directly from the terminal."""
    print(f"\n--- Interactive Mode Enabled ({voice_id}) ---")
    print("Type your text and hit Enter. Type 'exit', 'quit', or 'close' to leave.\n")

    count = 1
    while True:
        try:
            text = input("Say > ").strip()
            if text.lower() in ["exit", "quit", "close"]:
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

    parser.add_argument(
        "-v",
        "--voice",
        default="ava",
        help=f"Select preset ({', '.join(VOICES.keys())}) or pass raw voice string"
    )
    parser.add_argument("-r", "--rate", type=str, default="+0%", help="Speed modification (e.g., '+20%' or '-10%')")
    parser.add_argument("-o", "--output", type=str, default="output.mp3", help="Output filename")

    args = parser.parse_args()

    selected_voice = VOICES.get(args.voice, args.voice)

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