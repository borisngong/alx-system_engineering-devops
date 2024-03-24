#!/usr/bin/env bash
# Using Puppet to write a manifest for client configuration file

file { '/etc/ssh/ssh_config':
	ensure  => 'present',
}

file_line { 'disable password authentication':
	path  => '/etc/ssh/ssh_config',
	line  => 'PasswordAuthentication no',
	match => '#PasswordAuthentication',
}

file_line { 'Add Identity file':
	path  => '/etc/ssh/ssh_config',
	line  => 'IdentityFile ~/.ssh/school',
	match => '#IdentityFile',
}
