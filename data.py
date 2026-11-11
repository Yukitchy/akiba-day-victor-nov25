"""Single source of truth for page (build.py) and PDF (mkpdf.py). Times, shops, tastes live ONLY here."""
URL = 'https://yukitchy.github.io/akiba-day-victor-nov25/'
DATE_LONG = 'Wednesday, November 25'
# n: (short, lat, lon, full name, JP name, time, hours, photo)
STOPS = {
 1: ('Meet', 35.69881, 139.77237, 'Vie de France, BiTO AKIBA 1F', 'ヴィ・ド・フランス', '10:00', 'Bakery cafe, Akihabara Electric Town exit', 'hero.jpg'),
 2: ('Radio Kaikan', 35.697674, 139.771881, 'Akihabara Radio Kaikan + BIG MAGIC', '秋葉原ラジオ会館 / BIG MAGIC 9F', '10:10', 'Building 10:00 to 20:00', 'radio-kaikan.jpg'),
 3: ('TRADER', 35.700104, 139.771637, 'TRADER Akihabara main store', 'トレーダー 秋葉原本店', '11:00', 'Open 11:00 to 20:00', 'trader.jpg'),
 4: ('Animate', 35.700531, 139.771683, 'Animate Akihabara', 'アニメイト秋葉原', '11:30', 'Open 10:00 to 21:00', 'animate.jpg'),
 5: ('Gachapon Kaikan', 35.701856, 139.771250, 'Akihabara Gachapon Kaikan', '秋葉原ガチャポン会館', '11:55', 'Opens 11:00', 'gachapon.jpg'),
 6: ('Lunch', 35.69880, 139.77191, 'Lunch, you pick one of six', '', '12:25', 'All near the station', 'kamadoka.jpg'),
}
DONE = '13:00'
# letter, name, JP, genre, hours, where, map query, photo
LUNCH = [
 ('a', 'Yakiniku Toraji', '焼肉トラジ 秋葉原店', 'Yakiniku', 'Lunch 11:00 to 15:00', '1 min from the station', 'Yakiniku Toraji Akihabara', 'toraji-akiba.jpg'),
 ('b', 'Kamadoka', 'かまどか 秋葉原店', 'Chicken, rice pots', 'Open 11:00 to 23:00', 'BiTO AKIBA 6F', 'Kamadoka Akihabara', 'kamadoka.jpg'),
 ('c', 'Juke Steak', 'ジュークステーキ 秋葉原', 'Steak lunch', 'Lunch 11:30 to 14:30', '3 min from the station', 'Juke Steak Akihabara', 'juke-steak.jpg'),
 ('d', 'Ootoya', '大戸屋ごはん処 秋葉原駅前店', 'Set meals', 'Open 11:00 to 23:00', 'BiTO AKIBA 4F', 'Ootoya Akihabara Ekimae', 'ootoya.jpg'),
 ('e', 'Showa Shokudo', '昭和食堂 秋葉原駅前店', 'Diner set meals', 'Open until 23:00', '3 min, cash only', 'Showa Shokudo Akihabara', 'showa-shokudo.jpg'),
 ('f', 'Kanda Tamagoken', '神田たまごけん 秋葉原店', 'Omurice', 'Open 11:00 to 21:15', '5 min from the station', 'Kanda Tamagoken Akihabara', 'kanda-tamagoken-akiba.jpg'),
]
TASTES = ['ONE PIECE · Garp', 'Frieren · Stark', 'Black Clover · Yami', 'Pokémon cards']
# timeline band (time, label)
BAND = [('10:00', 'Meet, Vie de France'), ('10:10', 'Radio Kaikan + BIG MAGIC'), ('11:00', 'TRADER'), ('11:30', 'Animate'),
        ('11:55', 'Gachapon Kaikan'), ('12:25', 'Lunch, pick one of six'), ('13:00', 'Done, at the station')]
# per-stop pitch tied to tastes (page + must match PDF only in time/shop/taste)
PITCH = {
 2: 'A tall building full of small shops. One Piece figures on the figure floors, and BIG MAGIC on the 9th floor for Pokémon cards. We pick the floors that match your favourites.',
 3: 'Three floors of second-hand figures sorted by series, so One Piece and other shonen series are easy to find, above floors of games. It opens at 11:00, so we come here after Radio Kaikan.',
 4: 'Several floors of new anime and manga goods. The stop for new Frieren and Black Clover goods, with plenty of One Piece and Pokémon too.',
 5: 'Hundreds of capsule toy machines. There are always Pokémon machines in the rows. Try a few and keep what comes out.',
}
SWAP = 'Want only Pokémon cards? Swap in Hareruya 2 (Pokémon cards, 3 min away). Want manga? Book Off is one minute from the station.'
