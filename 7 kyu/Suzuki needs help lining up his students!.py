def lineup_students(string): return sorted(string.split(), key=lambda x: (len(x), x), reverse=True)

s1 = 'Tadashi Takahiro Takao Takashi Takayuki Takehiko Takeo Takeshi Takeshi'
print(lineup_students(s1))

s2 = "Shima Satoshi Naoko Toshi Yuichi Saburo Takahiro Samuru Minori Shinichi Shunichi Shig Tadao Seiji Sadao Takashi Takumi Ryozo Toshihiro Yoshio Michio Yoshihiro Ryozo"
print(lineup_students(s2))
