<?php
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['email'])) {
    $to = 'info@mdgtlab.com'; // Cambiar al correo electrónico de destino
    $subject = 'New Subscription';
    $message = 'You have a new subscriber with the following email: ' . $_POST['email'];
    $headers = 'From: noreply@yourdomain.com' . "\r\n" . // Asegúrate de cambiar esto a una dirección válida en tu dominio
               'Reply-To: noreply@yourdomain.com' . "\r\n" .
               'X-Mailer: PHP/' . phpversion();

    mail($to, $subject, $message, $headers);

    echo "Thank you for subscribing!";
}
?>
