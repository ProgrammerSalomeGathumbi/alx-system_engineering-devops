#  Install flask from pip3. 
package {'flask':
  ensure   => 'installed',
  provider => 'pip3',
  name     => 'flask==2.1.0'
}
