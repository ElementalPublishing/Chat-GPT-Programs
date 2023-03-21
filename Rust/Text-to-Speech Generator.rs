extern crate reqwest;
extern crate serde;
#[macro_use]
extern crate serde_derive;

use std::error::Error;
use std::fs::File;
use std::io::Write;

#[derive(Serialize)]
struct Input {
    text: String,
}

#[derive(Serialize)]
struct Voice {
    language_code: String,
    name: String,
}

#[derive(Serialize)]
struct AudioConfig {
    audio_encoding: String,
    sample_rate_hertz: i32,
}

#[derive(Serialize)]
struct Params {
    input: Input,
    voice: Voice,
    audio_config: AudioConfig,
}

fn main() -> Result<(), Box<dyn Error>> {
    // Replace YOUR_API_KEY with your actual API key
    let api_key = "YOUR_API_KEY";

    // Replace YOUR_RHYME with your actual rhyme
    let rhyme = """
YOUR_RHYME
""";

    // Set the text-to-speech parameters
    let params = Params {
        input: Input {
            text: rhyme.to_string(),
        },
        voice: Voice {
            language_code: "en-US".to_string(),
            name: "en-US-Standard-B".to_string(),
        },
        audio_config: AudioConfig {
            audio_encoding: "LINEAR16".to_string(),
            sample_rate_hertz: 16000,
        },
    };

    // Send the request to the Google Text-to-Speech API
    let client = reqwest::Client::new();
    let response = client
        .post("https://texttospeech.googleapis.com/v1/text:synthesize")
        .json(&params)
        .header("Content-Type", "application/json")
        .header("Authorization", format!("Bearer {}", api_key))
        .send()?;

    // Check the status code of the response
    if !response.status().is_success() {
        return Err(format!("Error: {}", response.status()).into());
    }

    // Parse the JSON response
    let json_response: serde_json::Value = response.json()?;

    // Save the audio data to a .wav file
    let mut wav_file = File::create("rhyme.wav")?;
    wav_file.write_all(json_response["audioContent"].as_str().unwrap().as_bytes())?;

    // Print a message to confirm that the .wav file was saved
    println!("Rhyme saved as rhyme.wav");

    Ok(())
}