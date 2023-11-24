# installation of flask 2.1.0 script

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
