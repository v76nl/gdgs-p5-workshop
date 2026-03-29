# EX - 余裕があれば

## Alpha(透明度)
background(220, 220, 220, 20)

## array(配列) - まとめる
x = [100, 200, 300]
呼び出し: x[0]

## for - 繰り返し
for (let i = 0; i < 3; i++) {
    circle(x[i], y, random(0, 50));
}

## Stroke
stroke()
strokeWeight()

## WEBGL - 3D表現
createCanvas(400, 400, WEBGL);

## HSB - RGBとは異なる色表現
Hue, Saturation, Brightness
colorMode(HSB, 1, 1, 1);
fill(0.2, 1, 1);

colorMode(HSB, 360, 1, 1);
fill(frameCount%360, 1, 1);

## noise - randomとは異なる数値

## mouseClicked - マウスクリックに反応
function mouseClicked() {
    
}

## Object