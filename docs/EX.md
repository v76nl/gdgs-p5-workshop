# EX - 余裕があれば

## Alpha(透明度)

- 色を指定するとき4番目に値を入力すると、それは透明度と解釈される
- 例： `background(220, 220, 220, 20)`
- 範囲は0~255で、0が完全な透明、255が完全な不透明

```p5.js hl_lines="6 14"
let x = 200;
let y = 0;

function setup() {
    createCanvas(400, 400);
    background(220, 220, 220);
}

function draw() {
    y = y + 3;
    if (y > 400) {
        y = 0;
    }
    background(220, 220, 220, 20);
    fill(255, 0, 0)
    circle(x, y, random(0, 50))
}
```

## HSB - RGBとは異なる色表現

- HSB: Hue, Saturation, Brightness
    - つまり、色合い、鮮やかさ、明るさの3つで色を指定する
        - 三原色の混合で色を指定するRGBとは異なるやり方
- `colorMode(HSB, 数値, 数値, 数値)` で有効化する

    ```
    colorMode(HSB, 1, 1, 1);
    fill(0.2, 1, 1);
    ```

    - HSBにするとRGBは使えなくなるので注意

```
let frames = 0;

function setup() {
    createCanvas(400, 400);
    background(220);
}

function draw() {
    colorMode(HSB, 360, 1, 1);
    background(0, 0, 0);
    fill(frames, 1, 1);
    circle(200, 200, 50);
  
    frames = frames + 1;
  
    if (frames > 359) {
        frames = 0;
    }
}
```

## mouseClicked - マウスクリックに反応

- これを書くと、マウスクリックに反応して処理を行える

    ```
    function mouseClicked() {
        やりたい処理
    }
    ```

```
let fill_color = 0;

function setup() {
    createCanvas(400, 400);
    background(220);
}

function draw() {
    background(200);
    fill(fill_color);
    circle(200, 200, 50);
}

function mouseClicked() {
    fill_color = 255;
}
```

- マウスクリックを離したり、再度クリックしたときにも色が変わるようにしてみよう

## Stroke

- `stroke()` で図形の輪郭線の色を変えられる
- `strokeWeight()` で図形の輪郭線の太さを変えられる
- 図形を描画するより前の処理に書く必要がある

```p5.js hl_lines="1 11 21"
let stroke_weight = 10;
let is_reversed = 1

function setup() {
    createCanvas(400, 400);
}

function draw() {
    background(220);
    fill(100, 100, 100, 50);
    stroke(100, 100, 100);
    
    stroke_weight = stroke_weight + 0.2 * is_reversed
    if (stroke_weight > 20) {
      is_reversed = is_reversed * -1;
    }
    if (stroke_weight < 10){
      is_reversed = is_reversed * -1;
    }
  
    strokeWeight(stroke_weight);
    circle(200, 200, 80);
}
```

## テキスト

- `text("文字", x座標, y座標)` で文字を表示できる  
    `text("GDGoC Chuo", 20, 200);`
- `textSize(数字)` を `text()` より前に行うことで大きさを変えられる

```
function setup() {
    createCanvas(400, 400);
    background(220);
}

function draw() {
    textSize(60);
    text("GDGoC Chuo", 20, 200);
}
```

## noise - randomとは異なる柔らかなランダム性

- 詳細割愛 (難しいため)

```
let frames = 0;
let x = 0;

function setup() {
    createCanvas(400, 400);
    background(220);
}

function draw() {
    background(200);
  
    noise_value = noise(frames * 0.1);
    y = 150 + noise_value * 100;
  
    // y = 150 + random(100)
  
    circle(x, y, 50);
  
    frames = frames + 1;
    x = x + 3;
    if (x > 400) { 
        x = 0
    }
}
```

## WEBGL - 3D表現

- `createCanvas()` の中の3番目の値に `WEBGL` と入れると、3Dモードになる
- 例
    `createCanvas(400, 400, WEBGL);`

```p5.js
function setup() {
    createCanvas(400, 400, WEBGL);
    orbitControl();
}

function draw() {
    background(220);
    rotateX(frameCount * 0.01);
    rotateY(frameCount * 0.01);
    fill(0, 100, 0, 50);
    box(100);
}
```

## Object

- 詳細割愛 (難しいため)

## おまけ

- [Level 1](https://v76nl.github.io/gdgs-p5-workshop/level_0/) の画像のプログラム  
ここからでも → [p5.js Web Editor | p5.js Lesson 2026 March](https://editor.p5js.org/v76nl/sketches/2BarazSA3)

```
// 
let x = [100, 200, 300];
let y = 0;

function setup() {
  createCanvas(400, 400);
}

function draw() {
  y = y + 3;
  
  if (y > 400) {
    y = 0;
  }
  
  background(0, 0, 0, 10);
  fill(random(0, 255), 200, 200);
  stroke(200, 100, 100);
  strokeWeight(5)
  
  for (let i = 0; i < 3; i++){
    circle(x[i], y, random(0, 50));
  }
}
```
