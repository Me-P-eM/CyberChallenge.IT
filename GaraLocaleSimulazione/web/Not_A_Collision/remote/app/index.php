<?php
    if(isset($_GET["source"])){
        highlight_file(__FILE__);
        die();
    }

    $collision = false;

    if(isset($_POST["collision"])){
        $input1 = $_POST["input1"];

        if($input1 == md5($input1)){
            $collision = true;
        }
    }
?>

<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
</head>
<body style="font-family: Arial, sans-serif; background-color: #f4f4f4; text-align: center; padding: 20px;">
    <h1 style="color: #333;">NOT A COLLISION</h1>
    <p style="color: #666;">Give me a collision pls. If you want you can view the source code <a href="?source">here</a>.</p>

    <div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1); display: inline-block; margin-top: 20px;">
        <form action="" method="POST">
            <input type="text" name="input1" placeholder="input" required style="width: 80%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 5px;">
            <input type="submit" name="collision" value="click" style="background-color: #007bff; color: white; border: none; padding: 10px 15px; border-radius: 5px; cursor: pointer; transition: 0.3s;">
        </form>
        <br>
        <p>
            <?php
                if($collision){
                    define('ACCESS_GRANTED', true);
                    $home = $_GET["page"] ?? "home.php";
                    include($home);
                }
            ?>
        </p>
    </div>

</body>
</html>
