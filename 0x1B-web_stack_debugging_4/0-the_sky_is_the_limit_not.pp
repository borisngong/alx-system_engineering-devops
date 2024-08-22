# Increase the ULIMIT of the default Nginx file
exec { 'increase-ulimit-for-nginx':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => ['/usr/local/bin/', '/bin/'],
}

# Restart Nginx to apply the changes
exec { 'restart-nginx':
  command => '/etc/init.d/nginx restart',
  path    => ['/etc/init.d/'],
  require => Exec['increase-ulimit-for-nginx'],
}

