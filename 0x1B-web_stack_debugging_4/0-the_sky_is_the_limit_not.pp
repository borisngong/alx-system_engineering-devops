#increses the ULIMIT of the default file
exec { 'fix-for-nginx':
  # Change ULIMIT value
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  # Path for sed command
  path    => ['/usr/local/bin', '/bin'],
}

# To apply changes, restart nginx
exec { 'nginx-restart':
  # Restart nginx
  command => '/etc/init.d/nginx restart',
  # Path for init script
  path    => ['/etc/init.d'],
  require => Exec['fix-for-nginx'],
}

