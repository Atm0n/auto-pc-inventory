<?php

$config = array();

$config['mysql']['host'] = '192.168.56.101';
$config['mysql']['user'] = 'clients';
$config['mysql']['pass'] = 'inventory';
$config['mysql']['name'] = 'inventory';

$db = mysqli_connect($config['mysql']['host'], $config['mysql']['user'], $config['mysql']['pass'], $config['mysql']['name']);

if (!$db) {
    die('La connecció ha fallat ' . mysqli_connect_error());
} 



?>