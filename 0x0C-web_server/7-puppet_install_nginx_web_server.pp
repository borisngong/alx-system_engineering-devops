# Puppet Manifest to install and configure Nginx web server with 301 redirections

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Ensure Nginx service is enabled and running
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

# Configure Nginx server block
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => @("END")
    server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        index index.html;

        location / {
            try_files ${uri} ${uri}/ =404;
        }

        location /redirect_me {
            return 301 https://github.com/borisngong;
        }

        error_page 404 /404.html;
        location = /404.html {
            root /usr/share/nginx/html;
            internal;
        }
    }
  END
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Create index.html file with "Hello World!"
file { '/var/www/html/index.html':
  ensure  => file,
  content => "Hello World!\n",
}

# Test Nginx configuration
exec { 'nginx-config-test':
  command     => '/usr/sbin/nginx -t',
  path        => ['/usr/sbin', '/usr/bin', '/bin'],
  refreshonly => true,
  notify      => Service['nginx'],
}


