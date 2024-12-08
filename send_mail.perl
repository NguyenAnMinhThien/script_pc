#!/usr/bin/perl
 
# Details for email
$to = 'nguyenanminhthien97@gmail.com';
$from = 'thien.nguyen.ct@renesas.com';
$subject = 'Sending mail using perl';
$message = 'There is pass';
 
open(MAIL, "|/usr/sbin/sendmail -t");
 
# Email Header
print MAIL "To: $to\n";
print MAIL "From: $from\n";
print MAIL "Subject: $subject\n\n";
 
# Email Body
print MAIL $message;
 
$result = close(MAIL);
if($result) 
{ 
    print "Email Sent, Bro!\n";
} 
else
{ 
    print "There was a problem, Bro!\n";
}

