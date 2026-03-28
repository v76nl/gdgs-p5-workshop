# Level 1
- circle() を background() の下に書いてみよう
    - 書き方は circle(x座標, y座標, 直径)
    - たとえば circle(100, 150, 50)
    - 値を変えて遊んでみよう
```p5.js hl_lines="7"
function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  circle(100, 150, 50)
}
```
- circle() の中に `mouseX` と `mouseY` を入れてみよう
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
    - // background() とする
    - background() が無効化される
    - これをコメントアウトという
    - // で始まる行はプログラムとしてみなされず、メモのように扱われる
