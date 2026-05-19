# Level 4 - 変数

- 今、円はマウスに追従するが、これが勝手に動くようにしたい
- 変数を使ってみよう
    - 今までの `mouseX` も変数
    - 変数を自分で作ってみる (定義)
- 一番上に

    ```
    let x = 200;
    let y = 200;
    ```

    と書いてみる

- circleの中の1つめ、2つめを`x, y`にしてみる  
    ※変数の名前と同じ小文字でなければいけない

    ```p5.js hl_lines="1-2 11"
    let x = 200;
    let y = 200;

    function setup() {
      createCanvas(400, 400);
    }

    function draw() {
      // background(220);
      fill(255, 0, 0);
      circle(x, y, random(0, 50));
    }
    ```

    - とりあえず中心に円を表示することに成功！
    - xやyの数字をいじって、円の位置に反映されることを確認してみよう

- でも `circle(200, 200, ...)` でよくない？
    - パラメータを外に置くことでプログラムが見やすくなったり、管理しやすくなったりする

- それで、円をどう動かすの？
    - `y = 0` にしたあと、 `function draw() {` の下に `y = y + 3;` と書く

        ```p5.js hl_lines="2 9"
        let x = 200;
        let y = 0;

        function setup() {
            createCanvas(400, 400);
        }

        function draw() {
            y = y + 3;
            // background(220);
            fill(255, 0, 0);
            circle(x, y, random(0, 50));
        }
        ```

    - どうなっただろうか？
        - 円が勝手に下に行くはず
    - 最初はyが0だが、`draw()` が実行されるたびに +3 されていく
        - 座標については [Level 1](https://v76nl.github.io/gdgs-p5-workshop/level_1/)、draw関数の仕組みについては [Level 2](https://v76nl.github.io/gdgs-p5-workshop/level_2/) を参照

- `y = y + 3` という式は気持ち悪い？
    - 多くのプログラミング言語において、`=` は等しいことではなく「代入」を示す
    - 変数yという箱に対し、yの中身に3を足したものを入れなおす、ということ
    - `y += 3` とも書ける
