"""
새로운 마음으로 풀어봤는데

역시 디테일에서 시간이 오래 걸린다

문법은 기본적이
"""

from collections import defaultdict


def solution(genres, plays):
    answer = []

    playlist = defaultdict(list)
    play_cnt = defaultdict(int)

    for idx in range(len(genres)):
        play_cnt[genres[idx]] += plays[idx]
        playlist[genres[idx]].append([plays[idx], idx])

    play_cnt_sorted = sorted(play_cnt.items(), key=lambda x: -int(x[1]))

    for key in playlist.keys():
        playlist[key].sort(key=lambda x: (-int(x[0]), x[1]))

    for genre, cnt in play_cnt_sorted:
        for i in range(min(len(playlist[genre]), 2)):
            answer.append(playlist[genre][i][1])

    return answer