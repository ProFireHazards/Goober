import msvcrt

while True:
    key = msvcrt.getch()
    print(f'{key}')

    # Exit the loop if the user presses the Esc key
    if f"{key}" == "b'e'":
        break