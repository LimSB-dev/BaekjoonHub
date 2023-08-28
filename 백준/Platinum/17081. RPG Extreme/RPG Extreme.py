import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]
commands = list(input().strip())

delta = {
    'U': lambda x, y: (x-1, y),
    'D': lambda x, y: (x+1, y),
    'L': lambda x, y: (x, y-1),
    'R': lambda x, y: (x, y+1),
}


class Player:
    first_pos = (0, 0)
    past_situation = '@'
    x = 0
    y = 0
    turn = 0
    level = 1
    max_health = 20
    cur_health = 20
    power = 2
    armor = 2
    exp = 0

    weapon = {
        'W': 0,
        'A': 0,
        'O': []
    }

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.first_pos = (x, y)

    def move(self, cmd):
        self.turn += 1
        nx, ny = delta[cmd](self.x, self.y)

        if 0 > nx or nx >= n or 0 > ny or ny >= m or grid[nx][ny] == '#':
            if self.past_situation == '^':
                self.spike_trap()
            return

        if self.past_situation == '^':
            grid[self.x][self.y] = '^'
        else:
            grid[self.x][self.y] = '.'

        self.x, self.y = nx, ny
        self.past_situation = grid[self.x][self.y]

        if self.past_situation == 'M' or self.past_situation == '&':
            self.attack((self.x, self.y))
        elif self.past_situation == 'B':
            self.open_box((self.x, self.y))
        elif self.past_situation == '^':
            self.spike_trap()

        grid[self.x][self.y] = '@'

    def attack(self, pos):
        name = monster[pos].get('name')
        power = monster[pos].get('power')
        armor = monster[pos].get('armor')
        max_health = monster[pos].get('health')
        cur_health = monster[pos].get('health')
        exp = monster[pos].get('exp')

        if 'CO' in self.weapon['O']:
            if 'DX' in self.weapon['O']:
                cur_health -= max(1, (self.power +
                                  self.weapon['W']) * 3 - armor)
            else:
                cur_health -= max(1, (self.power +
                                  self.weapon['W']) * 2 - armor)
        else:
            cur_health -= max(1, self.power + self.weapon['W'] - armor)

        if 'HU' in self.weapon['O'] and self.past_situation == 'M':
            self.cur_health = self.max_health

        if cur_health <= 0:
            self.kill(exp)
        else:
            cnt = 0
            while True:
                if cnt != 0 or 'HU' not in self.weapon['O'] or self.past_situation != 'M':
                    self.cur_health -= max(1, power -
                                           self.armor - self.weapon['A'])
                    if self.cur_health <= 0:
                        if 'RE' in self.weapon['O']:
                            self.weapon['O'].remove('RE')
                            cur_health = max_health
                            self.cur_health = self.max_health
                            self.x, self.y = self.first_pos
                            self.past_situation = '@'
                            grid[self.x][self.y] = '@'
                            break
                        else:
                            self.cur_health = 0
                            self.game_over('monster', name)
                            exit()

                cur_health -= max(1, self.power + self.weapon['W'] - armor)
                if cur_health <= 0:
                    self.kill(exp)
                    break

                cnt += 1

    def kill(self, exp):
        if 'EX' in self.weapon['O']:
            self.exp += int(exp * 1.2)
        else:
            self.exp += exp

        if 'HR' in self.weapon['O']:
            self.cur_health = min(self.cur_health + 3, self.max_health)

        if self.exp >= 5 * self.level:
            self.level_up()

        if self.past_situation == 'M':
            grid[self.x][self.y] = '@'
            self.game_over('win')
            exit()

    def level_up(self):
        self.level += 1
        self.max_health += 5
        self.cur_health = self.max_health
        self.power += 2
        self.armor += 2
        self.exp = 0

    def open_box(self, pos):
        type = item[pos].get('type')
        effect = item[pos].get('effect')

        if type == 'W' or type == 'A':
            self.weapon[type] = effect
        else:
            if effect in self.weapon[type]:
                return

            if len(self.weapon[type]) < 4:
                self.weapon[type].append(effect)

    def spike_trap(self):
        if 'DX' in self.weapon['O']:
            self.cur_health -= 1
        else:
            self.cur_health -= 5

        if self.cur_health <= 0:
            if 'RE' in self.weapon['O']:
                self.weapon['O'].remove('RE')
                self.cur_health = self.max_health
                grid[self.x][self.y] = '^'
                self.x, self.y = self.first_pos
                self.past_situation = '@'
                grid[self.x][self.y] = '@'
            else:
                self.cur_health = 0
                grid[self.x][self.y] = '^'
                self.game_over('spike')
                exit()

    def game_over(self, reason, name=''):
        print('\n'.join(''.join(row) for row in grid))
        print(f'Passed Turns : {self.turn}')
        print(f'LV : {self.level}')
        print(f'HP : {self.cur_health}/{self.max_health}')
        print(f'ATT : {self.power}+{self.weapon["W"]}')
        print(f'DEF : {self.armor}+{self.weapon["A"]}')
        print(f'EXP : {self.exp}/{5 * self.level}')

        if reason == 'win':
            print('YOU WIN!')
        elif reason == 'monster':
            print(f'YOU HAVE BEEN KILLED BY {name}..')
        elif reason == 'spike':
            print('YOU HAVE BEEN KILLED BY SPIKE TRAP..')
        elif reason == 'turn':
            print('Press any key to continue.')


k, l = 0, 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == '@':
            player = Player(i, j)
        elif grid[i][j] == 'M' or grid[i][j] == '&':
            k += 1
        if grid[i][j] == 'B':
            l += 1

monster = {}
for _ in range(k):
    r, c, s, w, a, h, e = input().split()
    monster[(int(r) - 1, int(c) - 1)] = {
        'name': s,
        'power': int(w),
        'armor': int(a),
        'health': int(h),
        'exp': int(e),
    }

item = {}
for _ in range(l):
    r, c, t, s = input().split()
    item[(int(r) - 1, int(c) - 1)] = {
        'type': t,
        'effect': s if t == 'O' else int(s),
    }

for cmd in commands:
    player.move(cmd)

player.game_over('turn')
