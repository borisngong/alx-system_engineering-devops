# Puppet Manifest to increase file limits for the 'holberton' user

# Increase the hard file limit for the 'holberton' user
exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/^holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => ['/usr/local/bin/', '/bin/'],
}

# Increase the soft file limit for the 'holberton' user
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/^holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => ['/usr/local/bin/', '/bin/'],
}

