# Setup client ssh config

file {'/etc/ssh/ssh_config':
  content => 'Host *
	PasswordAuthentication no
	IdentityFile ~/.ssh/school'
}
