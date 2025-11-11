# insert interval

What I needed to realize is that I can guarantee that if I check whether interval[0] in the intervals list is greater than NewInterval[1], and also if interval[1] strictly less than NewInterval[0], as long as I handle the other cases, I can guarantee that I can add the NewInterval (in the first case) or interval in the second case. Merging is basically taking min(x values) and max(y values).
