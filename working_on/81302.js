// 거리두기 확인하기

function distance(p1, p2) {
  return Math.abs(p1[0] - p2[0]) + Math.abs(p1[1] - p2[1]);
}

function waiting_room(place) {
  // 먼저 응시자의 위치를 저장합니다.
  p_loc = [];
  for (y = 0; y < 5; y++) {
    for (x = 0; x < 5; x++) {
      if (place[y][x] == "P") {
        p_loc.push([y, x]);
        // console.log(p_loc);
      }
    }
  }

  // console.log("응시자들의 위치", p_loc);

  if (p_loc.length == 0) {
    // 대기실 안에 아무도 없다면,
    return 1;
  }

  // 두 명 사이의 맨해튼 거리를 계산합니다.

  for (i = 0; i < p_loc.length; i++) {
    for (k = i + 1; k < p_loc.length; k++) {
      var p1 = p_loc[i];
      var p2 = p_loc[k];
      // console.log(p1, p2);
      // console.log("거리:", distance(p1, p2));

      if (distance(p1, p2) == 1) {
        return 0;
      }

      if (distance(p1, p2) == 2) {
        //   같은 행에 존재?
        if (p1[0] == p2[0]) {
          // console.log("시발", p1, p2);
          if (place[p1[0]][p1[1] + 1] == "O") {
            return 0;
          }
          //   같은 열에 존재?
        } else if (p1[1] == p2[1]) {
          if (place[p1[0] + 1][p1[1]] == "O") {
            return 0;
          }
        } else {
          // 대각선에 존재!
          // console.log("대각선!", p1, p2);
          //   체크할 칸은 두개.
          spot1 = [p1[0], p2[1]];
          spot2 = [p2[0], p1[1]];

          if (
            place[spot1[0]][spot1[1]] == "O" ||
            place[spot2[0]][spot2[1]] == "O"
          ) {
            return 0;
          }
        }
      } else if (distance(p_loc[i], p_loc[k]) > 2) {
        continue;
      }
    }
  }
  return 1;
}
function solution(places) {
  var answer = [];
  for (place of places) {
    answer.push(waiting_room(place));
  }
  return answer;
}

places = [
  ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
  ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
  ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
  ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
  ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
];

place = ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POPOP"];

// console.log(solution(places));
console.log(waiting_room(place));
