<?php

    if(isset($_GET["source"])){
        highlight_file(__FILE__);
        die();
    }

    class User{
        public $username;

        public function __construct($username) {
            $this->username = $username;
        }
    }

    function containsForbiddenSubstring(string $username, array $forbidden){
        foreach ($forbidden as $substr) {
            if (str_contains($username, $substr)) {
                return true;
            }
        }
        return false;
    }

    $command = False;
    $welcome_message = "";

    if (isset($_POST["register"])) {
        $username = htmlentities($_POST["username"]);
        $user = new User($username);
        setcookie("user", base64_encode(serialize($user)), time() + 3600, "/");
        header("Location: " . $_SERVER["PHP_SELF"]);
        exit();
    }

    if (isset($_COOKIE["user"])) {
        $data = base64_decode($_COOKIE["user"]);
        $user = unserialize($data);

        $blacklist = ["flag", "nc", "curl", "cat", "wget", "txt", "eval", "more", "less", "bash", "sh", "php", "system", "exec", "shell", "file"];

        if ($user instanceof User) {
            if (!containsForbiddenSubstring($user->username, $blacklist)) {
                $command = "echo 'Welcome, {$user->username}'";
                $welcome_message = "Access granted. Welcome back, agent " . htmlspecialchars($user->username, ENT_QUOTES, 'UTF-8') . ".";
            } else {
                $welcome_message = "Intrusion attempt detected. Access denied for user: " . htmlspecialchars($user->username, ENT_QUOTES, 'UTF-8') . ".";
            }
        } else {
            $welcome_message = "Corrupted data stream. Identity unconfirmed.";
        }
    }
?>

<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Agent 1337</title>
    <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #1a1a2e;
            --primary-text-color: #e0e0e0;
            --neon-cyan: #00ffff;
            --neon-magenta: #ff00ff;
            --accent-color: var(--neon-cyan);
            --input-bg: #2c2c44;
            --border-color: var(--neon-cyan);
            --error-color: #ff4757;
            --terminal-green: #00ff00;
        }

        body {
            background-color: var(--bg-color);
            color: var(--primary-text-color);
            font-family: 'Share Tech Mono', monospace;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            margin: 0;
            padding: 20px;
            box-sizing: border-box;
            text-align: center;
        }

        .container {
            background: rgba(0, 0, 0, 0.3);
            border: 2px solid var(--border-color);
            border-radius: 15px;
            padding: 30px 40px;
            box-shadow: 0 0 15px var(--border-color), inset 0 0 10px rgba(0, 255, 255, 0.2);
            width: 90%;
            max-width: 600px;
            animation: pulseBorder 3s infinite alternate;
        }

        @keyframes pulseBorder {
            0% { border-color: var(--neon-cyan); box-shadow: 0 0 15px var(--neon-cyan), inset 0 0 10px rgba(0, 255, 255, 0.2); }
            50% { border-color: var(--neon-magenta); box-shadow: 0 0 15px var(--neon-magenta), inset 0 0 10px rgba(255, 0, 255, 0.2); }
            100% { border-color: var(--neon-cyan); box-shadow: 0 0 15px var(--neon-cyan), inset 0 0 10px rgba(0, 255, 255, 0.2); }
        }

        h1 {
            color: var(--accent-color);
            text-shadow: 0 0 5px var(--accent-color), 0 0 10px var(--accent-color), 0 0 15px var(--accent-color);
            font-size: 2.5em;
            margin-bottom: 10px;
            letter-spacing: 2px;
        }

        .subtitle {
            color: var(--neon-magenta);
            margin-bottom: 25px;
            font-size: 1.1em;
        }

        .subtitle a {
            color: var(--neon-cyan);
            text-decoration: none;
            transition: color 0.3s, text-shadow 0.3s;
        }

        .subtitle a:hover {
            color: #fff;
            text-shadow: 0 0 8px var(--neon-cyan);
        }

        form {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        input[type="text"] {
            background-color: var(--input-bg);
            color: var(--accent-color);
            border: 1px solid var(--border-color);
            border-radius: 5px;
            padding: 12px 15px;
            margin: 10px 0;
            width: calc(100% - 30px);
            font-family: 'Share Tech Mono', monospace;
            font-size: 1em;
            outline: none;
            transition: box-shadow 0.3s, border-color 0.3s;
        }

        input[type="text"]::placeholder {
            color: rgba(0, 255, 255, 0.5);
        }

        input[type="text"]:focus {
            border-color: var(--neon-magenta);
            box-shadow: 0 0 10px var(--neon-magenta);
        }

        input[type="submit"] {
            background-color: var(--accent-color);
            color: var(--bg-color);
            border: none;
            padding: 12px 25px;
            border-radius: 5px;
            cursor: pointer;
            font-family: 'Share Tech Mono', monospace;
            font-weight: bold;
            font-size: 1.1em;
            text-transform: uppercase;
            transition: background-color 0.3s, box-shadow 0.3s, transform 0.2s;
            margin-top: 10px;
        }

        input[type="submit"]:hover {
            background-color: var(--neon-magenta);
            box-shadow: 0 0 15px var(--neon-magenta);
            transform: translateY(-2px);
        }

        .output-area {
            margin-top: 25px;
            padding: 15px;
            background-color: rgba(0,0,0,0.4);
            border: 1px dashed #444;
            border-radius: 5px;
            color: var(--terminal-green);
            min-height: 2.5em;
            text-align: left;
            white-space: normal;
            word-break: break-all;
        }

        .output-area:not(.empty)::before {
            content: "C:\\Windows\\System32> ";
            display: inline;
            color: var(--terminal-green);
        }

        .output-area.empty::before {
            content: "C:\\Windows\\System32> ";
            display: inline;
            color: var(--terminal-green);
        }

        .output-area.empty::after {
            content: "_";
            display: inline;
            color: var(--terminal-green);
            animation: blinkCursor 1s infinite steps(1, end);
        }

        @keyframes blinkCursor {
            0%, 100% { opacity: 1; }
            50% { opacity: 0; }
        }

        .footer-note {
            margin-top: 30px;
            font-size: 0.8em;
            color: #777;
        }

    </style>
</head>
<body>
    <div class="container">
        <h1>Agent 1337</h1>
        <p class="subtitle">View source <a href="?source" title="View the source code of this challenge">[here]</a>.</p>

        <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="POST">
            <input type="text" name="username" placeholder="Enter Agent ID ..." required>
            <input type="submit" name="register" value="Establish Connection">
        </form>

        <div class="output-area <?php echo empty($welcome_message) ? 'empty' : ''; ?>">
        <?php
            if($command){
                // don't show output, i don't trust u :)
                shell_exec($command);
            }

            if(!empty($welcome_message)){
                 echo htmlspecialchars($welcome_message, ENT_QUOTES, 'UTF-8');
            }
        ?>
        </div>
    </div>

</body>
</html>