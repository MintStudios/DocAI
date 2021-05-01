from speech_rec import background_listening, adjust_mic, recognize
import config


def main():
    adjust_mic()

    while True:
        if not config.is_active and config.background_first_time:
            config.background_first_time = False
            background_listening(5)

        if config.is_active:
            config.background_first_time = True
            recognize()


if __name__ == "__main__":
    main()
