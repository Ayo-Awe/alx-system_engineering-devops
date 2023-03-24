# create a flle in /tmp directory

file {'/tmp/school':
  mode    => '0744',
  content => 'I love Puppet',
  group   => 'www-data',
  owner   => 'www-data'
}
