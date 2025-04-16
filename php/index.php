<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <title>Bootstrap Slider</title>
</head>
<body>

<div id="dataSlider" class="carousel slide" data-ride="carousel">
    <div class="carousel-inner">
        <?php
        $data = [
            ['title' => 'Data 1', 'description' => 'Description 1'],
            ['title' => 'Data 2', 'description' => 'Description 2'],
            ['title' => 'Data 3', 'description' => 'Description 3'],
            // Add more data as needed
        ];

        $chunks = array_chunk($data, 2); // Split data into chunks of 2

        foreach ($chunks as $index => $chunk) {
            $activeClass = ($index === 0) ? 'active' : '';
            echo "<div class='carousel-item $activeClass'>";
            echo "<div class='row'>";
            foreach ($chunk as $item) {
                echo "<div class='col'>";
                echo "<h5>{$item['title']}</h5>";
                echo "<p>{$item['description']}</p>";
                echo "</div>";
            }
            echo "</div>"; // end of row
            echo "</div>"; // end of carousel-item
        }
        ?>
    </div>

    <a class="carousel-control-prev" href="#dataSlider" role="button" data-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
    </a>
    <a class="carousel-control-next" href="#dataSlider" role="button" data-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
    </a>
</div>

<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
