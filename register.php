<?php
// Проверяем, была ли отправлена форма
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Получаем данные из формы
    $login = $_POST["firstInput"];
    $pass = $_POST["pass"];

    // Подключаемся к базе данных
    $servername = "localhost";
    $username ="root";
    $password = "";
    $dbname = "instagramUser";

    $conn = new mysqli($servername, $username, $password, $dbname);

    // Проверяем соединение с базой данных
    if ($conn->connect_error) {
        die("Ошибка соединения: " . $conn->connect_error);
    }

    // Подготавливаем SQL-запрос и вставляем данные в таблицу
    $sql = "INSERT INTO userstwo (login, pass) VALUES ('$login', '$pass')";

    if ($conn->query($sql) === TRUE) {
        echo "Регистрация прошла успешно!";
    } else {
        echo "Ошибка при регистрации: " . $conn->error;
    }

    // Закрываем соединение с базой данных
    $conn->close();
}
?>
