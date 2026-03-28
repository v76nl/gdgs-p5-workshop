# Level 2 - p5.jsの「フレーム」のしくみ

- setup関数は再生ボタンを押したとき1回だけ実行される
- draw関数はその後1秒間に60回の速度で実行され続ける
- 一度、background()の前の `//` を消して、background関数を有効化しよう
  ```p5.js hl_lines="6"
  function setup() {
    createCanvas(400, 400);
  }

  function draw() {
    background(220);
    circle(mouseX, mouseY, 50)
  }
  ```
     - 円がカーソルに追従する

- 再度background関数をコメントアウトしよう
  ```p5.js hl_lines="6"
  function setup() {
    createCanvas(400, 400);
  }

  function draw() {
    // background(220);
    circle(mouseX, mouseY, 50)
  }
  ```
     - マウスカーソルを動かすと、たくさん円が表示される