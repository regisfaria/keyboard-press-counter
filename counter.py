from keyboard import *
import sys

recorded = record(until=sys.argv[1])

totalPressed = 0
for keyPressed in recorded:
  totalPressed += 1

print('Total keyboard strokes: {}'.format(totalPressed))