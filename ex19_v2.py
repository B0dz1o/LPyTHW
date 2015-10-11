from sys import argv

def write_repeat(repeats, symbol='.'):
    print symbol * repeats
    repeats += 3

script, repeats_argv = argv
repeats_argv = int(repeats_argv)
   
write_repeat(1)
write_repeat(4 / 2)
write_repeat(int(raw_input("Write how many repeats -> ")))

repeats = 1
write_repeat(repeats)
#print repeats
write_repeat(repeats + repeats)
#print repeats
write_repeat(repeats * 3)

write_repeat(repeats_argv, script)
write_repeat(repeats_argv + repeats, script)
write_repeat(int('5'), '5')
write_repeat(int('5'))
