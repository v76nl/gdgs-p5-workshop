# Level 3

- circleの直径を `random(0, 50)` にしてみよう
  ```p5.js hl_lines="7"
  function setup() {
    createCanvas(400, 400);
  }

  function draw() {
    // background(220);
    circle(mouseX, mouseY, random(0, 50))
  }
  ```
    - `random(0, 50)` は0から50までのランダムな数字を作る

## 円の色を変えてみる
- circle() の上に `fill(255, 0, 0)` と書いてみよう
  ```p5.js hl_lines="7"
  function setup() {
    createCanvas(400, 400);
  }

  function draw() {
    // background(220);
    fill(255, 0, 0)
    circle(mouseX, mouseY, random(0, 50))
  }
  ```
  - 色が変わった！
  - RGBについて
    - RGBは光の三原色Red, Green, Blueのこと
    - それぞれの値は0~255
  - 好きに色をいじってみよう

## ここで休憩
- ヒマだったらパラメーターをいじってみよう
