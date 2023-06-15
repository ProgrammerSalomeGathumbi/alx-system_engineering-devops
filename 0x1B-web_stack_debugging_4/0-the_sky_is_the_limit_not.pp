# accept more requests
exec { 'fix web-server':
  command => "sed -i 's/15/4096/' /etc/default/nginx",
  path    => '/usr/local/bin/:/bin/'
  notify  => Exec['restart nginx']
}
exec { 'restart nginx':
  command     => 'nginx restart',
  refreshonly => 'true'
  path        => '/etc/init.d'
}
