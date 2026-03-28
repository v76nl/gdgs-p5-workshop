# Level 1

- `circle()` を `background()` の下に書いてみよう
    - `circle()` は円を描く指令
        - 今回はこれでずっと遊ぶ
    - 書き方は `circle(x座標, y座標, 直径)`
    - たとえば `circle(100, 150, 50)`

```p5.js hl_lines="7"
function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  circle(100, 150, 50)
}
```

- circle() の括弧の中の値を変えて遊んでみよう
    - 特に2つめの数字
    - 注意: p5.jsでの座標系
        - xは数学と同じく右方向が+だが、yは逆で下方向が+

- `circle()` の括弧の中に `mouseX` と `mouseY` を入れてみよう
    - circle(mouseX, mouseY, 50)

```p5.js hl_lines="7"
function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  circle(mouseX, mouseY, 50)
}
```

- background() の前に `// ` (スラッシュ2つ) を入れてみよう
    - `// background()` とする
    - background関数 が無効化される
    - これをコメントアウトという
    - `//` で始まる行はプログラムとしてみなされず、メモのように扱われる
