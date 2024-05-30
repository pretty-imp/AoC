symbols, escapes = 0, 0
f = open('task.txt', 'r')
for line in f:
    symbols += len(line.strip())
    escapes += len(eval(line.strip()))
f.close()
print(symbols - escapes)
