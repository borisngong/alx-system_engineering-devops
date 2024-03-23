# Using Puppet, install flask version 2.1.0

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

