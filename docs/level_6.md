# Level 6 - 配列 (Array)

- `x = [100, 200, 300]`
- 呼び出し: `x[0]`
    - プログラミングでは1番目のことを `[0]` で表す

- 配列を使って円を3つ出すプログラム

    ```p5.js hl_lines="1 15-17"
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
        background(220);
        fill(255, 0, 0);
        circle(x[0], y, 50);
        circle(x[1], y, 50);
        circle(x[2], y, 50);
    }
    ```
