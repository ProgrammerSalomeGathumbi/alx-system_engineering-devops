# create a file in /tmp.
file {'/tmp/school':
  content => "I love Puppet\n",
  mode    => '0744',
  group   => 'www-data',
  owner   => 'www-data',
}
