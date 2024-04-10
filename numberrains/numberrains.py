<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>黑客帝国字母雨</title>
</head>

<body onselectstart="false">

    <canvas id="canvas" height="100%" width="100%"></canvas>

    <style type="text/css">
        html,
        body {
            margin: 0;
            padding: 0;
            overflow: hidden;
        }
    </style>

    <script type="text/javascript">

        var canvas = document.getElementById('canvas');
        var ctx = canvas.getContext('2d');

        canvas.height = window.innerHeight;
        canvas.width = window.innerWidth;

        var texts = 'abcdefghigklmnopqrstuvwxyz'.split('');
        var fontSize = 16;
        var columns = canvas.width / fontSize;
        var drops = [];

        for (var x = 0; x < columns; x++) {
            drops[x] = 1;
        }

        function draw() {

            ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            ctx.fillStyle = randColor();
            ctx.font = fontSize + 'px Microsoft YaHei';

            for (var i = 0; i < drops.length; i++) {
                var text = texts[Math.floor(Math.random() * texts.length)];
                ctx.fillText(text, i * fontSize, drops[i] * fontSize);

                if (drops[i] * fontSize > canvas.height || Math.random() > 0.95) {
                    drops[i] = 0;
                }

                drops[i]++;
            }
        }

        function randColor() {
            var r = Math.floor(Math.random() * 256);
            var g = Math.floor(Math.random() * 256);
            var b = Math.floor(Math.random() * 256);
            return "rgb(" + r + "," + g + "," + b + ")";
        }

        setInterval(draw, 50); 
    </script>

</body>

</html>
