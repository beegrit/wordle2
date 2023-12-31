from guesslist import guesslist

numlet = {
  "e": { "yellow": [2,919,929,937,941], "green": [3, 5, 7, 11, 13] },
  "s": { "yellow": [17,947,953,967,971], "green": [19, 23, 29, 31, 37] },
  "a": { "yellow": [41,977,983,991,997], "green": [43, 47, 53, 59, 61] },
  "o": { "yellow": [67,1009,1013,1019,1021], "green": [71, 73, 79, 83, 89] },
  "r": { "yellow": [97,1031,1033,1039,1049], "green": [101, 103, 107, 109, 113] },
  "i": { "yellow": [127,1051,1061,1063,1069], "green": [131, 137, 139, 149, 151] },
  "l": { "yellow": [157,1087,1091,1093,1097], "green": [163, 167, 173, 179, 181] },
  "t": { "yellow": [191,1103,1109,1117,1123], "green": [193, 197, 199, 211, 223] },
  "n": { "yellow": [227,1129,1151,1153,1163], "green": [229, 233, 239, 241, 251] },
  "u": { "yellow": [257,1171,1181,1187,1193], "green": [263, 269, 271, 277, 281] },
  "d": { "yellow": [283,1201,1213,1217,1223], "green": [293, 307, 311, 313, 317] },
  "y": { "yellow": [331,1229,1231,1237,1249], "green": [337, 347, 349, 353, 359] },
  "c": { "yellow": [367,1259,1277,1279,1283], "green": [373, 379, 383, 389, 397] },
  "p": { "yellow": [401,1289,1291,1297,1301], "green": [409, 419, 421, 431, 433] },
  "m": { "yellow": [439,1303,1307,1319,1321], "green": [443, 449, 457, 461, 463] },
  "h": { "yellow": [467,1327,1361,1367,1373], "green": [479, 487, 491, 499, 503] },
  "g": { "yellow": [509,1381,1399,1409,1423], "green": [521, 523, 541, 547, 557] },
  "b": { "yellow": [563,1427,1429,1433,1439], "green": [569, 571, 577, 587, 593] },
  "k": { "yellow": [599,1447,1451,1453,1459], "green": [601, 607, 613, 617, 619] },
  "f": { "yellow": [631,1471,1481,1483,1487], "green": [641, 643, 647, 653, 659] },
  "w": { "yellow": [661,1489,1493,1499,1511], "green": [673, 677, 683, 691, 701] },
  "v": { "yellow": [709,1523,1531,1543,1549], "green": [719, 727, 733, 739, 743] },
  "z": { "yellow": [751,1553,1559,1567,1571], "green": [757, 761, 769, 773, 787] },
  "j": { "yellow": [797,1579,1583,1597,1601], "green": [809, 811, 821, 823, 827] },
  "x": { "yellow": [829,1607,1609,1613,1619], "green": [839, 853, 857, 859, 863] },
  "q": { "yellow": [877,1621,1627,1637,1657], "green": [881, 883, 887, 907, 911] }
}
wordnum = {} #every word with their coresponding number
for word in guesslist:
  pword = 1
  for x,letter in enumerate(list(word)):
    pword *= numlet[letter]["green"][x]
    for let in list(word):
      if let != letter:
        pword *= numlet[let]["yellow"][x]
  
  wordnum[pword] = word

