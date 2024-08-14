# Corrects a typo in the WordPress configuration file `wp-settings.php`
#by replacing incorrect `phpp` extensions with `php`

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
