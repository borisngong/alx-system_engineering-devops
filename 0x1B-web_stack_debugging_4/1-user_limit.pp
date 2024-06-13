# Give access to holberton user to access and make modifications

# Increase hard file limit for holberton user
exec { 'increase-hardfile-limit-for-holberton-user':
  command => "sed -i '/^holberton hard/s/5/50000/' /etc/security/limits.conf",
  path    => ['/usr/local/bin', '/bin'],
}

# Increase soft file limit for holberton user
exec { 'increase-soft-limit-for-holberton-user':
  command => "sed -i '/^holberton soft/s/4/50000/' /etc/security/limits.conf",
  path    => ['/usr/local/bin', '/bin'],
}

