if __name__ == '__main__':
    print("Please wait.")
    from RealtimeTTS import TextToAudioStream, CoquiEngine
    import sounddevice, time, logging, sys
    if 'linux' in sys.platform:
        import readline



    #Setup

    engine  = CoquiEngine(
        model_name  = "tts_models/multilingual/multi-dataset/xtts_v2",
        voices_path = "./voice",
        language    = "en",
        voice       = "nicole.wav",
        level=logging.CRITICAL
        )

    stream  = TextToAudioStream(engine)
    running = 1
    
    #Variables

    fast_sentence_fragment = False 
    
    #Main loop

    def dummy_generator(string):
        yield string

    def main():
        while running:
#            print('> ', end='')
            text = input("> ")
            stream.feed(dummy_generator(text))
            stream.play(
                log_synthesized_text=False,
                tokenizer = "nltk",
                context_size = 12,
                force_first_fragment_after_words=20,
                output_wavfile="output.wav")

    print("You may start typing.")

    main()
        

    #Cleanup

    engine.shutdown()
