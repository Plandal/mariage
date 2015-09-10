<?php 
	/* SECTION I - CONFIGURATION */

$receiver_mail = 'bivol@red-sky.pl';
$mail_title = ( ! empty( $_POST[ 'name' ] )) ? ' from ' . $_POST[ 'name' ]  : ' from [WebSite]';

/* SECTION II - CODE */
$result = 'Nothing Happened';
if ( ! empty( $_POST [ 'e-mail' ] ) && ! empty( $_POST [ 'message' ] ) ) {
 $email = $_POST[ 'e-mail' ];
 $message = $_POST[ 'message' ];
 $message = wordwrap( $message, 70, "\r\n" );
 $subject = $mail_title;
// $header = 'From: ' . $_POST[ 'name' ] . "\r\n";
 $header = 'Reply-To: ' . $email;
 if ( mail( $receiver_mail, $subject, $message, $header ) )
  $result = 'Message successfully sent.';
 else
  $result = 'Message could not be sent.';
} else {
 $result = 'Please fill all the fields.';
}
echo $result;