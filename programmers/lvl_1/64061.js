// 크레인 인형뽑기 게임

function solution(board, moves) {
  var answer = 0;
  var basket = [];

  moves.forEach((move) => {
    // 인덱스로 바꾸기
    let index = move - 1;
    // console.log(index);

    // 각 층마다 반복
    for (i = 0; i < board.length; i++) {
      // 비어있지 않다면
      if (board[i][index] != 0) {
        // 바구니가 비어있으면 무조건 들어갑니다.
        if (basket.length == 0) {
          basket.push(board[i][index]);
        }
        // 바구니에 무언가가 있다면,
        else {
          // 바구니에 맨 위 아이템이 지금 잡은 아이템과 같다면
          if (board[i][index] == basket[basket.length - 1]) {
            basket.pop();
            answer += 1;
          }
          // 다른 인형이라면
          else {
            basket.push(board[i][index]);
          }
        }
        // console.log(basket);
        console.log(board);
        // 보드안의 그 칸을 비워줍니다
        board[i][index] = 0;
        // 다음 move로 이동!
        break;
      }
    }
  });
  return answer * 2;
}

board = [
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 3],
  [0, 2, 5, 0, 1],
  [4, 2, 4, 4, 2],
  [3, 5, 1, 3, 1],
];

moves = [1, 5, 3, 5, 1, 2, 1, 4];

console.log(solution(board, moves));

// a = [1, 2, 3];
// a[0] = 0;
// console.log(a);

// console.log(board.length);
