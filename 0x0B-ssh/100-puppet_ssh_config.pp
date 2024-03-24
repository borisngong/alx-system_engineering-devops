#!/usr/bin/env bash
# Using Puppet to write a manifest for client configuration file

file { 'etc/ssh/ssh_config':
	ensure  => 'present',
	content => "

	# configuration of ~/.ssh/school

	host *
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",
}
