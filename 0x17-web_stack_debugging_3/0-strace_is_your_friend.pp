# fix apache error 500 for wordpress site
exec { 'fix-error':
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
  path    => '/usr/local/bin/:/bin/'
}
