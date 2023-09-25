# installing flask using puppet
package { 'install-flask':
  ensure   => '2.1.0',
  provider => pip3,
}
