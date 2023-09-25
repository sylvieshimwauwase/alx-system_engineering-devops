# executing killmenoe process
exec { 'kill-killmenow-process':
command => '/usr/bin/pkill killmenow',
onlyif  => '/usr/bin/pgrep killmenow'
}
