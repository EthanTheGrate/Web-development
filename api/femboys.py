from gtts import gTTS
message = "obama grilled cheese sandwich."
tts = gTTS(message)
tts.save("audio.mp3")