from manager import start_runner

if __name__ == "__main__":
    try:
        start_runner()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
