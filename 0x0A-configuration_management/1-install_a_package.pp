# installation of flask 2.1.0  using  script
package { 'flusk-2.1.0':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3'
}