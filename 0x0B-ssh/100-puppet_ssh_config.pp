# Setup client ssh config

file {'/home/ubuntu/.ssh/config':
  content => 'Host *
	PasswordAuthentication no
	IdentityFile ~/.ssh/school'
}
