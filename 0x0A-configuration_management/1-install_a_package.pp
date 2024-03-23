# Puppet manifest to install Flask version 2.1.0

# Ensure Python 3 and pip3 are installed (if not already present)
class { 'python':
  version => '3.x',
}

package { 'python3-pip':
  ensure => installed,
}

# Install Flask using pip3
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

# Ensure that Werkzeug is installed as well (required by Flask)
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
