#include <iostream>
#include <fstream>
#include <string>
#include <cpprest/http_client.h>
#include <rapidjson/document.h>

using namespace std;
using namespace web;
using namespace web::http;
using namespace web::http::client;

int main() {
    // Replace YOUR_API_KEY with your actual API key
    string api_key = "YOUR_API_KEY";

    // Replace YOUR_RHYME with your actual rhyme
    string rhyme = """
YOUR_RHYME
""";

    // Create the HTTP client and set the authorization header
    http_client client(U("https://texttospeech.googleapis.com"));
    client.default_request_headers().add(U("Authorization"), U("Bearer " + api_key));

    // Set the text-to-speech parameters in a JSON object
    rapidjson::Document params;
    params.SetObject();
    rapidjson::Value input(rapidjson::kObjectType);
    input.AddMember("text", rhyme, params.GetAllocator());
    params.AddMember("input", input, params.GetAllocator());
    rapidjson::Value voice(rapidjson::kObjectType);
    voice.AddMember("languageCode", "en-US", params.GetAllocator());
    voice.AddMember("name", "en-US-Standard-B", params.GetAllocator());
    params.AddMember("voice", voice, params.GetAllocator());
    rapidjson::Value audio_config(rapidjson::kObjectType);
    audio_config.AddMember("audioEncoding", "LINEAR16", params.GetAllocator());
    audio_config.AddMember("sampleRateHertz", 16000, params.GetAllocator());
    params.AddMember("audioConfig", audio_config, params.GetAllocator());

    // Send the request to the Google Text-to-Speech API
    http_response response = client.request(methods::POST, U("/v1/text:synthesize"), params).get();

    // Check the status code of the response
    if (response.status_code() != 200) {
        cout << "Error: " << response.status_code() << endl;
        return 1;
    }

    // Parse the JSON response
    rapidjson::Document json_response;
    json_response.Parse(response.extract_string().get().c_str());

    // Save the audio data to a .wav file
    ofstream wav_file("rhyme.wav", ios::binary);
    wav_file.write(json_response["audioContent"].GetString(), json_response["audioContent"].GetStringLength());
    wav_file.close();

    // Print a message to confirm that the .wav file was saved
    cout << "Rhyme saved as rhyme.wav" << endl;

    return 0;
}