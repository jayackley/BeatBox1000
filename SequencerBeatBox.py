# Circuit Playground 808 Drum machine
import time
import board
import neopixel
import digitalio
import random

from audiocore import WaveFile
from audioio import AudioOut

playing = True
threefour = False

bpm = 200  # Beats per minute, change this to suit your tempo
brightness = 5

# Enable the speaker
speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.direction = digitalio.Direction.OUTPUT
speaker_enable.value = True
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)

buttonPads = (digitalio.DigitalInOut(board.A3), digitalio.DigitalInOut(board.A2),
              digitalio.DigitalInOut(board.A1), digitalio.DigitalInOut(board.A5),
              digitalio.DigitalInOut(board.TX), digitalio.DigitalInOut(board.A6),
              digitalio.DigitalInOut(board.A4))

for i in range(7):
    buttonPads[i].direction = digitalio.Direction.INPUT
    buttonPads[i].pull = digitalio.Pull.UP

zero = False
one = False
two = False
three = False
four = False
five = False
six = False

numbers = [zero, one, two, three, four, five, six]

# The seven files assigned to the buttonPads
audiofiles = ("bd_zome.wav", "bd_tek.wav", "bass_hit_c.wav",
              "hihat.wav",  "eggshake.wav", "elec_hi_snare.wav",
              "elec_cymbal.wav", "blank.wav")

audio = AudioOut(board.SPEAKER)


def play_file(filename, pixelnum):
    pixels[pixelnum] = (random.randrange(1, brightness, 1),
                        random.randrange(1, brightness, 1),
                        random.randrange(1, brightness, 1))
    pixels.show()
    print("playing file " + filename)
    file = open(filename, "rb")
    wave = WaveFile(file)
    audio.play(wave)
    time.sleep(bpm / 960)
    pixels.fill((0, 0, 0))
    pixels.show()


buttonA = digitalio.DigitalInOut(board.BUTTON_A)
buttonA.switch_to_input(pull=digitalio.Pull.DOWN)

buttonB = digitalio.DigitalInOut(board.BUTTON_B)
buttonB.switch_to_input(pull=digitalio.Pull.DOWN)

switch = digitalio.DigitalInOut(board.SLIDE_SWITCH)
switch.switch_to_input(pull=digitalio.Pull.UP)



while True:
    # Turning the contemporaneous button pushes into on/off switches
    for i in range(7):
        if buttonPads[i].value is False:
            if numbers[i] is False:
                numbers[i] = True
                print(str(i) + ' = True')
                pixels[i] = (random.randrange(1, brightness*2, 1),
                             random.randrange(1, brightness*2, 1),
                             random.randrange(1, brightness*2, 1))
                pixels.show()
            elif numbers[i] is True:
                numbers[i] = False
                print(str(i) + ' = False')

    if playing is True:

        # Three Four Time~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if threefour is True:
            # First Hit in the grid
            if numbers[0] is True:
                play_file(audiofiles[0], 0)
            elif numbers[4] is True:
                play_file(audiofiles[4], 4)
            else:
                play_file(audiofiles[7], 7)

            # Second Hit in the grid
            if numbers[3] is True:
                play_file(audiofiles[3], 3)
            else:
                play_file(audiofiles[7], 7)

            # third hit in the grid
            if numbers[1] is True:
                play_file(audiofiles[1], 1)
            elif numbers[4] is True:
                play_file(audiofiles[4], 4)
            else:
                play_file(audiofiles[7], 7)

            # fourth hit in the grid
            if numbers[3] is True:
                play_file(audiofiles[3], 3)
            else:
                play_file(audiofiles[7], 7)

            # fifth hit in the grid
            if numbers[2] is True:
                play_file(audiofiles[2], 2)
            elif numbers[5] is True:
                play_file(audiofiles[5], 5)
            elif numbers[4] is True:
                play_file(audiofiles[4], 4)
            else:
                play_file(audiofiles[7], 7)

            # sixth hit in the grid
            if numbers[6] is True:
                play_file(audiofiles[6], 6)
            elif numbers[3] is True:
                play_file(audiofiles[3], 3)
            else:
                play_file(audiofiles[7], 7)

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~FourFour Time
        if threefour is False:
            # First Hit
            if numbers[0] is True:
                play_file(audiofiles[0], 0)
            elif numbers[1] is True:
                play_file(audiofiles[1], 1)
            else:
                play_file(audiofiles[7], 7)
            # Second Hit
            if numbers[2] is True:
                play_file(audiofiles[2],2)
            elif numbers[3] is True:
                play_file(audiofiles[3], 3)
            else:
                play_file(audiofiles[7], 7)
            # Third Hit
            if numbers[4] is True:
                play_file(audiofiles[4], 4)
            else:
                play_file(audiofiles[7], 7)
            # Fourth Hit
            if numbers[3] is True:
                play_file(audiofiles[3], 3)
            else:
                play_file(audiofiles[7], 7)
            # Fifth Hit
            if numbers [5] is True:
                play_file(audiofiles[5], 5)
            elif numbers[4] is True:
                play_file(audiofiles[4], 4)
            else:
                play_file(audiofiles[7], 7)
            # Sixth Hit
            if numbers[3] is True:
                play_file(audiofiles[3], 3)
            else:
                play_file(audiofiles[7], 7)
            # Seventh Hit
            if numbers[1] is True:
                play_file(audiofiles[1], 1)
            elif numbers[4] is True:
                play_file(audiofiles[4], 4)
            else:
                play_file(audiofiles[7], 7)
            # Eighth Hit
            if numbers [6] is True:
                play_file(audiofiles[6], 6)
            elif numbers[3] is True:
                play_file(audiofiles[3], 3)
            else:
                play_file(audiofiles[7], 7)
# set the BPM
        if buttonA.value and bpm < 900:
            bpm = bpm + 50
        elif buttonB.value and bpm > 40:
            bpm = bpm - 50

    if buttonPads[0].value is False and buttonPads[6].value is False:
        if threefour is False:
            threefour = True
            print('TimeSwap3/4')
            time.sleep(bpm / 430)
        elif threefour is True:
            threefour = False
            print('FourFour')
            time.sleep(bpm / 430)

    if buttonA.value and buttonB.value and playing is False:
        playing = True
        print('playing!')
        pixels[9] = (100, 100, 100)
        pixels.show()
        time.sleep(bpm / 430)
        pixels[9] = (0, 0, 0)
        pixels.show()
    if buttonA.value and buttonB.value and playing is True:
        playing = False
        print('not playing!')
        pixels[9] = (100, 100, 100)
        pixels.show()
        time.sleep(bpm / 430)
        pixels[9] = (0, 0, 0)
        pixels.show()
