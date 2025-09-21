<?php
    $flag = @file_get_contents("/flag.txt");

    $db_host = getenv("DB_HOST") ?: "db";
    $db_name = getenv("DB_NAME") ?: "imgdb";
    $db_user = getenv("DB_USER") ?: "imguser";
    $db_pass = getenv("DB_PASS") ?: "imgpass";

    $dsn = "mysql:host={$db_host};dbname={$db_name};charset=utf8mb4";
    $options = [
        PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES   => false,
    ];

    function getDbConnection($dsn, $db_user, $db_pass, $options) {
        try {
            $pdo = new PDO($dsn, $db_user, $db_pass, $options);
            return $pdo;
        } catch (PDOException $e) {
            error_log("Database connection failed: " . $e->getMessage());
            return null;
        }
    }

    $pdo = getDbConnection($dsn, $db_user, $db_pass, $options);
    if (!$pdo) {
        die("Error: Could not establish database connection.");
    }

    if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST["id"])) {
        $image_id = $_POST["id"];
        $image_id = str_replace("'", "\\'", $image_id);
        $image_id = str_replace('"', '\\"', $image_id);
        $image_id = str_replace(" ", "", $image_id);

        $banned_keywords = ["UNION", "SELECT", "FROM", "WHERE", "AND", "OR", "INSERT", "UPDATE", "DELETE", "DROP", "TABLE", "DATABASE", "SCHEMA", "COLUMN", "ALTER", "CREATE", "INDEX", "TRIGGER", "VIEW", "SLEEP", "BENCHMARK", "LOAD_FILE"];
        
        foreach ($banned_keywords as $keyword) {
            $image_id = str_ireplace($keyword, "", $image_id);
        }

        $sql = "SELECT url_image FROM images WHERE id_image = '" . $image_id . "' LIMIT 1";
        
        try {
            $stmt = $pdo->query($sql);
            $url_image = $stmt->fetchColumn();

            if ($url_image === false) {
                die("Image ID not found :(");
            } else if (strpos($url_image, "flag.txt") !== false){
                die("Forbitten");
            } else {
                if (strpos($flag, $url_image) === 0) {
                    die("You can't steal my flag brody :)");
                }
            }
            
            $content = @file_get_contents($url_image);

            if ($content) {
                header("Content-Type: image/jpg");
                echo $content;
            }else{
                die("Image not found :(");
            }

        } catch (PDOException $e) {
            die("SQL Error: Execution failed.");
        }

    } else {
        $stmt = $pdo->query("SELECT id_image, url_image FROM images ORDER BY CAST(id_image AS UNSIGNED)");
        $images = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>

        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Cat Gallery</title>
            <style>
                body { font-family: Arial; background: #f0f2f5; margin: 0; padding: 0; }
                .gallery { padding: 30px; display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 20px; }
                .image-card { background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 5px rgba(0,0,0,0.1); text-align: center; }
                .image-card img { width: 100%; height: 160px; object-fit: cover; }
                .image-card form { margin: 0; padding: 10px; }
                .image-card button { padding: 8px 12px; background: #4267B2; color: white; border: none; border-radius: 4px; cursor: pointer; }
            </style>
        </head>
        <body>
            <h1 style="text-align: center; background: #4267B2; color: white; padding: 20px;">Cat Gallery</h1>
            <div class="gallery">
                <?php $catNames = ["Gaspare", "Pino er soldato", "Ernesto", "Pasquale", "Gino", "Ermenegildo", "Gesualdo", "Carmine", "Pancrazio", "Calogero"];
                foreach ($images as $index => $image): ?>
                    <div class="image-card">
                        <img src="<?php echo $image["url_image"]; ?>" alt="Cat">
                        <form method="POST" action="">
                            <input type="hidden" name="id" value="<?php echo htmlspecialchars($image["id_image"]); ?>">
                            <p><?php echo $catNames[$index]; ?></p>
                            <button type="submit">View</button>
                        </form>
                    </div>
                <?php endforeach; }?>
            </div>
        </body>
        </html>
