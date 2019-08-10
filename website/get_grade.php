<?php
$username = $_POST['username'];
$password = $_POST['password'];
$location = '/.../get_grade.py';

$command = 'python3 ' . $location . ' ' . $username . ' ' . $password;
$new_command = escapeshellcmd($command);
$output = shell_exec($new_command);
echo json_encode($output);
