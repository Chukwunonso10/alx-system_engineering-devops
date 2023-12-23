#Using Puppet, install flask from pip3
#
Package { 'flask':
  Ensure   => '2.1.0',
  Provider => 'pip3',
}
