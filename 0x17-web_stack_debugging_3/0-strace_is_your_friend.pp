# This Puppet exec resource fixes the 'phpp' extension to 'php'
# within the WordPress configuration file wp-settings.php located at
#/var/www/html/wp-settings.php.

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}

