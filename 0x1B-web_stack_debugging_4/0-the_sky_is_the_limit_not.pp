# accept more requests
exec { 'fix web-server':
  command => "sed -i 's/15/4096/' /etc/default/nginx",
  path    => '/usr/local/bin/:/bin/'
}
exec { 'fix -nginx':
  command => "sed -i '6s/768/1024/' /etc/nginx/nginx.conf",
  path    => '/usr/local/bin/:/bin/'
}
service { 'nginx':
  restart  => 'sudo service nginx restart',
}
