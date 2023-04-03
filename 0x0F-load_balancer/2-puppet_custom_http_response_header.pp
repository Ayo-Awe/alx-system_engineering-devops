# install and configure nginx on an ubuntu server

package { 'nginx':
  ensure   => installed,
  provider => 'apt'
}

file { '/var/www/html/':
  ensure => 'directory',
  before => Service['nginx']
}

file { '/etc/nginx/sites-enabled/default':
  ensure  => 'file',
  content => 'server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;

        server_name _;
        add_header X-Served-By $hostname always;

        location / {
                try_files $uri $uri/ =404;
        }
  }',
  require => Package['nginx'],
  before  => Service['nginx']

}

service { 'nginx':
  ensure  => 'running',
  require => Package['nginx']
}
