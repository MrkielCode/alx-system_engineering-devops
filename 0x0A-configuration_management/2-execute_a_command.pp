# To kill a filename "killmenow" using exec
exec { 'kill process':
  command  => 'pkill killmenow',
  path     => '/usr/bin',
  provider => shell
}
