import string
import random

f = open("cabagge.txt", "w+");
g = open("eggplant.txt", "w+");
h = open("potato.txt", "w+");
for i in range(10):
    f.write(random.choice(string.ascii_lowercase));
    g.write(random.choice(string.ascii_lowercase));
    h.write(random.choice(string.ascii_lowercase));
# f.write('\n');
# g.write('\n');
# h.write('\n');
std.write(f);
std.write(g);
std.write(h);
f.close();
g.close();
h.close();
    