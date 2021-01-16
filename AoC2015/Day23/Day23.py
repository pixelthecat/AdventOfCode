class Computer:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.pc = 0
        self.memory = []


    def runProgram(self):
        while self.pc >= 0 and self.pc < len(self.memory):
            instr, *ops = self.memory[self.pc].split(' ')

            if instr == 'hlf':
                if ops[0] == 'a':
                    self.a = self.a // 2
                else:
                    self.b = self.b // 2
                self.pc += 1
            elif instr == 'tpl':
                if ops[0] == 'a':
                    self.a = self.a * 3
                else:
                    self.b = self.b * 3
                self.pc += 1
            elif instr == 'inc':
                if ops[0] == 'a':
                    self.a += 1
                else:
                    self.b += 1
                self.pc += 1
            elif instr == 'jmp':
                self.pc += int(ops[0])
            elif instr == 'jie':
                if 'a' in ops[0]:
                    val = self.a
                else:
                    val = self.b

                if val % 2 == 0:
                    self.pc += int(ops[1])
                else:
                    self.pc += 1
            elif instr == 'jio':
                if 'a' in ops[0]:
                    val = self.a
                else:
                    val = self.b

                if val == 1:
                    self.pc += int(ops[1])
                else:
                    self.pc += 1
            else:
                print('INVALID INSTRUCTION ERROR REBOOT RETRY IGNODSFMFSLG')


with open('puzzleinput.txt', 'r') as f:
    text_input = f.readlines()

computer = Computer()

for line in text_input:
    computer.memory.append(line.strip())

computer.runProgram()


print('Part 1: ', computer.b)

computer.pc = 0
computer.a = 1
computer.b = 0

computer.runProgram()


print('Part 2: ', computer.b)
