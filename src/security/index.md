Companies, universities, and other institutions have mostly failed to protect us
from online threats: nothing happens to them if they don't, and as
[%i "Schneier, Bruce" %]Bruce Schneier[%/i%] has pointed out, their business models
are designed to put the cost of security failures on users
[%b Schneier2021 %]. As a result, much of what we are forced to go through
is [%i "security theater" %][%g security_theater "security theater" %][%/i%]
intended to make us believe something is being done rather than to actually make
us safer: forcing people to change passwords every three months encourages
people to choose memorable (and therefore easy-to-guess) passwords, while all
that random searches of backpacks and bags at the entrance to the subway do is
encourage a would-be attacker to go to another entrance.

It doesn't have to be like this.  As [%b Schneier2019 %] points out, most
security breaches are a result of poor design and rather than Hollywood-style
hacking.  If we think about the threats people actually face, we can build
systems that are safer to use [%b Smalls2021 %].

<div class="callout" markdown="1">
### Privacy is a right

Software doesn't just need to be secure to prevent fraud: it is also an
essential to protecting your [right to privacy][privacy-right], which is
guaranteed by the [Universal Declaration of Human Rights][udhr].  There are many
situations in which governments and law enforcement agencies have legitimate
reasons to violate that right, but we have learned the hard way that the more
access we give them, the more likely that access is to be abused, both by them
and by others.
</div>

## Threat Models

The first step is to realize that digital security is usually not the weakest
link.  At an airport several years ago, I heard a professor of computer science
try to reset an online account over the phone. In just a couple of minutes,
everyone within a few meters knew their full name, their date of birth, their
credit card number (including three-digit verification code on the back), and
what was almost certainly their mother's maiden name.

[%i "social engineering" %][%g social_engineering "Social engineering" %][%/i%] is
far more common than hacking: it is much easier to trick someone into giving you
their password than to break into their devices digitally.  The defense against
this is to pay attention to what's happening and respond accordingly.  However,
being on guard all the time is exhausting; [%i "Snowden, Edward" %]Edward
Snowden[%/i%] and the journalists who worked with him took extraordinary
measures to safeguard themselves against [%g state_level_actor "state-level
actors" %] [%b Snowden2019 %], but most of us aren't involved in issues
of national security and don't need to take those kinds of precautions.
Instead, we typically face one of three kinds of threat:

-   [%i "casual threat" "threat!casual" %][%g casual_threat "Casual threats" %][%/i%]
    are opportunistic. For example, Monica, a professor, is targeted by Mohan,
    an undergraduate who spends hours every day in online echo chambers
    complaining about how "SJW bullshit" is ruining tech. He thinks it would be
    a laugh to make her the target of anonymous abuse online; he is unlikely to
    invest significant effort in his attack, but his attack may be backed up by
    more knowledgeable allies in online forums.

-   [%i "intimate threat" "threat!intimate" %][%g intimate_threat "Intimate threats" %][%/i%] come from people who know their targets' passwords or have a
    chance to install spyware on their targets' devices (which abusers
    frequently do [%b Leitao2019 %]). For example, Elena has ended an
    unhappy relationship and is rebuilding her life.  Her ex, Eric, is obsessed
    with the idea that she left him for someone else and is now stalking her.
    He knows the IDs she uses on social media, some of her old passwords, and
    the PIN for phone.

-   [%i "insider threat" "threat!insider" %][%g insider_threat "Insider threats" %][%/i%] come from people who abuse legitimate access to accounts and
    devices. For example, Boris, a professor, has agreed to serve as an expert
    witness in an upcoming lawsuit; Bethany, a sys admin in his department, has
    been asked by a former colleague to find out what he is going to say in
    order to discredit his testimony.

How can you help counter these threats?

1.  Have and enforce a Code of Conduct ([%x important %]) for any site you
    build so that people who are abusing the system can be shut down quickly.
    Requiring a 24-hour waiting period for creation of new accounts helps as
    well: if casual abusers can't get their kicks right away, many of them will
    move on.

1.  Notify a device's owner when you send data from their device to someone
    else. (Doing this should be required by law for the same reason that
    everyone who manufactures packaged food is required to list its
    ingredients.)

1.  Keep a [%i "logging!for security" %]log[%/i%] of every administrative
    action ([%x errors %]) so that there will be a record if someone uses
    their privileges inappropriately. They might be able to delete that record,
    but if it is [%i "digital signature!for activity logs" %][%g digital_signature "digitally signed" %][%/i%] there will still be evidence of tampering.

1.  Do code reviews to ensure that programmers aren't inserting
    [%i "code review!for security" %][%g back_door "back doors" %][%/i%] in software
    [%b Sharma2021 %] or accidentally leaving access points intended
    solely for testing.

## Authentication

Using a weak password is a good way to ensure that your account will eventually
be compromised, in part because [%i "dictionary attack" %][%g dictionary_attack "dictionary attacks" %][%/i%] can be run offline against stored passwords to
find ones that match common patterns. Using a clever password scheme, such as
the name of the site plus a word only you know, does not make you more secure:
whatever scheme you have thought of, attackers have seen before.  And since
people are often identified on multiple sites by the same email address, as soon
as one site where you've used that scheme is compromised, attackers can guess
the scheme and use it elsewhere.

As a programmer, you should therefore require users to create strong passwords.
This does *not* mean requiring upper-case letters, digits, punctuation
characters, Egyptian hieroglyphics, and emoji; as [this XKCD
cartoon][xkcd-passwords] points out, a phrase containing four random words is
more secure and easier to remember.

Another solution is to use a password manager that generates strong passwords
and saves them all under a master passphrase (which again should be several
words long and hard to forget).  Doing this does create a single point of
attack, but is still safer than choosing passwords yourself.  In addition,
password managers aren't fooled by sites with names like `paypaI.com`.

<div class="callout" markdown="1">
### I know how to do that

Writing passwords down and keeping them in your wallet is not necessarily a bad
practice—it depends on who is doing it. For example, an elderly person who
finds tech confusing might well choose simple, easy-to-guess passwords for their
accounts if they have to be remembered. On the other hand, they have a lifetime
of practice keeping track of bits of paper, and will probably notice if their
purse or wallet is stolen.
</div>

Passwords are just one form of [%i "authentication" %]authentication[%/i%].
In general, proving your identity relies on something you know (like a
password), something you have (like a swipe card), or something you are (like
your fingerprints).  [%i "two-factor authentication" "authentication!two-factor" %][%g 2fa "Two-factor authentication" %][%/i%] (2FA) requires two
of these together to establish your identity, e.g., a password (which can be
stolen electronically) plus a random code generated by an app on your phone
(which means attackers need access to you).

It is more secure to use an app for 2FA instead of text messages or email, but
either is a big advance on single-factor authentication.  Many security experts
now recommend using a physical 2FA key such as a
[%i "YubiKey" %]YubiKey[%/i%] that fits on a keychain and plugs into a standard USB
port.  Sites like [%i "Tech Solidarity" %][Tech Solidarity][tech-solidarity][%/i%]
have easy-to-follow instructions explaining
how to set them up for a range of popular social networking sites.

What you should *never* do is share a confirmation code, since a common attack
is to trigger a password reset and then call the victim pretending to be from
the IT department and ask them to read the code back to "verify" your
account. As soon as you do this, the attacker can change your password and get
into your account.

The advice above leads directly to some recommendations for developers:

1.  Require strong passwords, but don't require people to change them
    frequently.

1.  Support two-factor authentication. (Use a library rather than building
    it yourself.)

1.  Include a health warning with every confirmation code you send to your
    users telling them not to share the code with anyone, ever.

## Don't Open That

Much of the software we use was designed in more innocent times, and since
companies are almost never held liable for the damage caused by their software,
they have consistently prioritized convenience for the many over harm to the
few. One common example is documents that contain code that automatically runs
when the document is opened. Used for good, these [%i "macro" %]macros[%/i%]
can check that an address field has been filled in correctly. Used for evil, it
can email everyone in your address book, or send a copy of it to anyone in the
world.  Microsoft Word and various game mods are particularly notorious for this
vulnerability.

Attempts to get you to open an email attachment, click on a link, install
software, or log into a website are called [%i "phishing" %][%g phishing "phishing" %][%/i%] attacks.  The strongest defense is to never do
these things, but that would make most work impossible. The second-best defense
is to invest in a [%i "virus scanner" %]virus scanner[%/i%] to check email
attachments and downloads before you open them.

Similarly, don't click links in emails without checking them first: instead,
hover over the link and see if it matches the site it claims to be.  You can
also log into the site manually rather than following the provided link: it may
take a few extra seconds, but is still faster than fixing your credit rating.
And when you go to a web site, check the real domain name in the URL:
`paypaI.com` with an upper-case "I" instead of a lower-case "l" is not the site
it pretends to be, and `wwwpaypal.com` is a different domain than
`www.paypal.com`.

<div class="callout" markdown="1">
### Trained to do the wrong thing

Many sites send an email with a random URL to confirm your identity when you are
resetting your password. On the one hand, this means that an attacker has to get
access to your email in order to break into your account. On the other hand,
random URLs are hard to type in, so these emails encourage us to click on links
in emails. If you are not expecting a password reset email, *don't click on the
link*, even if it includes your name or other details:
[%i "spearphishing" %][%g spearphishing "spearphishing" %][%/i%] uses data harvested
from previous victims to attack specific targets.

Similarly, if someone from your bank calls you up and asks for information to
confirm your identity, you should ask *them* for information to confirm theirs,
such as, "What were the dates of my last two transactions?"  If they say they're
unable to answer because that's another department, end the conversation and
then call your bank directly to either complete the operation or report the
attack.
</div>

How can you support these safety rules with software?

1.  I really want to say, "Don't send attachments," but that's not practical.
    What you *can* do is send email telling people that there's a document for
    them to download, then require them to log in to your site in order to
    download it.

1.  Notify people immediately of any data breaches so that they can warn others.
    Don't wait until a breach happens before figuring out how to do this: build
    an emergency notification system directly into your product.

## Delete Before Discarding

Moving files into the trash and then emptying it does not actually erase the
data: it just tells the computer that the space is available for reuse. (This is
why reporters and private investigators regularly go [%i "dumpster diving" %][%g dumpster_diving "dumpster diving" %][%/i%].) The best way to address this
problem is to encrypt your hard drive, which is a quick setup option for all
major operating systems these days.

Even with that, you should act as if any device you throw away might fall into
unfriendly hands.  (The odds of this happening by accident are low, but it won't
be by accident: attackers have been known to get jobs in electronics recycling
depots in order to collect the raw material for attacks.)  Use a [%i "secure
deletion tool" %]secure deletion tool[%/i%] like [BleachBit][bleachbit] (for
Linux or Windows) or [FileShredder][fileshredder] (for MacOS) before selling,
recycling, or discarding your hardware, but keep in mind that this doesn't
affect backups or files stored online on sites like [Dropbox][dropbox]. And keep
in mind that it is practically impossible to truly delete data from social
networking sites: in most cases, their "delete" usually means "don't show any
more" rather than "erase all past record of".

That brings us to the fact that many tech companies who offer free products and
services make money by selling targeted advertising to you using the data they
have about you, or by selling the data you've given them to third parties.  (As
they saying goes, if you're not paying for the service, you are probably the
product.)  Companies do give users some control over personal data, but they
frequently change their terms of service in opaque ways. Seemingly-innocuous
information can give attackers valuable clues: restaurant "likes" reveal where
you were at specific times, while funny stories about childhood birthday parties
reveal likely answers to security questions. Again, it's a good practice to get
into the habit of checking your privacy settings every time you do some other
regular task.

Unfortunately, even if you do this, information may leak through other
means. For example, attackers can friend your friends in an attempt to get
information about you, such as the name of your first school. And as bad as
social media sites are for social engineering in this way, cell phone apps are
often worse. If a game wants access to your camera and address book, you should
probably find a different game to play.

Since social media is a fact of life for most of us, you should check your
settings periodically, just as you would take your car in for an oil change. (I
do these things at the same time in order to remember both.) Turn off everything
you can and then use a tracking blocker such as [Ghostery][ghostery] to reduce
information leakage.

Here are some things you can do as a developer to support these rules:

1.  Don't store any information you don't have to, or only store it in encrypted
    form [%b Wayner2009 %].

1.  Charge people for your software or the service you provide rather than
    relying on ads or selling their data. You won't see the kind of growth that
    Facebook did in its early days, but on the other hand, you won't be [fueling
    genocide][facebook-rohingya].

1.  Make your terms of service as clear as possible, and provide a translation
    into everyday language. For example, look up the license for your favorite
    social media site on [TLDRlegal][tldr-legal] and compare the legal language
    to the plain English description.

1.  Allow people to actually delete personal information.

The last of these rules shows why security is hard. On the one hand, people
should be able to erase themselves from your records. On the other, abusers will
use this to cover their tracks. You may not get to decide how to balance these
two needs: legislation like the EU's [%i "General Data Protection Regulation
(GDPR)" %][General Data Protection Regulation][gdpr][%/i%] (GDPR) includes a
[right to be forgotten][gdpr-forgotten].

<div class="callout" markdown="1">
### When you travel

Many experts recommend using separate devices or accounts for work and personal
life, but this is unrealistic for most people: everyone checks their personal
email from their work device eventually, and everyone uses their personal phone
for 2FA. However, you should consider getting a second phone for international
travel: the legalities around who can take your devices and/or force you to
unlock them are complicated and frequently overstepped, so you should assume
that anything on or connected to the devices you are traveling with will be
compromised.
</div>

## Fighting Back

Casual attackers may eventually get bored and move on, but like all bullies,
they will sometimes revisit previous victims.  Even if they don't, they are
likely to pick new ones.  It's unjust to ask the victim of an attack to do extra
work, but please consider taking these four steps:

Do not engage directly.
:   Casual attackers are often seeking attention, so a direct response often
    encourages further attacks (and can draw attention from like-minded
    attackers).

Find support.
:   Being targeted is frightening and wearying, particularly if you belong to one
    of the many groups that are targeted in real life as well as online. Let
    family, friends, and colleagues know what is happening so that they can
    support you. They may also be able to offer advice if they have been in
    similar situations.

Use anti-harassment apps like [Block Party][block-party].
:   And document everything: save emails and take screenshots of sites like
    Facebook and Twitter in case attackers delete or alter material.

Report the attack.
:   Social media sites have done everything they can to avoid legal
    accountability for online attacks, but companies and universities will
    usually (eventually) take what steps they can once they know there is a
    problem. They are more inclined to take real action against the attacker if
    they believe that you might speak publicly about what has happened and
    thereby damage their reputation, so never agree to a [%i "non-disclosure
    agreement!abuse of" %]non-disclosure agreement[%/i%] that would prevent you
    from doing so ([%x fairness %]).

Above all, remember that it's not just about you. We don't just wear masks to
prevent ourselves from becoming infected: we also wear them so that we will not
infect others. Similarly, if you do not take precautions with online security
then you are putting others at risk.  Simple steps like putting passwords on
PDFs that contain sensitive information can go a long way to deter attackers, in
the same way that a sturdy-looking bike lock encourages would-be thieves to go
after some other bike.

The only long-term way to improve everyone's online safety is to pressure
politicians to strengthen legislation so that companies, universities, and other
institutions have real incentives to take meaningful action. Cars and drugs are
as safe as they are because their manufacturers are liable for negligence and
harm. The sooner software companies and social media sites are liable as well,
the safer all of us will be. As a programmer, you can push for this:

1.  The next time there is an election in your area, ask the candidates whether
    they support meaningful liability for privacy breaches and online abuse.  In
    my experience, if three people ask about something in quick succession,
    candidates will decide that they need to have some sort of answer.

1.  The next time your college or university is updating its curriculum,
    petition for a full-semester course on computer security—one that focuses
    on common exploits rather than the minutiae of cryptography.

1.  Add your voice to campaigns to get companies to clean up their act, and if
    you have a choice, don't work for the worst of them ([%x fairness %]).

> If you are currently in…an undergraduate software engineering or
> computer science course, the first thing you need to understand is
> that you will spend your career working alongside equally competent
> professionals who had a completely different educational pathway from
> yours. They may have come to development from another field entirely;
> they may have come to development through a focused educational
> experience such as a code academy; and they may have fallen into
> development for the fun of it with no formal web education whatsoever…
>
> So if you're assuming that there will be a common set of knowledge of
> practices, procedures, and processes regarding privacy for you to draw
> upon throughout your career, you need to adjust your expectations…
> Don't look towards your management and leadership either, as they're
> none the wiser. If privacy is a factor in your future workplaces, it's
> likely to be driven by the legal department as a strictly reactive,
> scary, and deeply resented legal compliance obligation whose purpose
> is to cover your company's backside rather than protect the people in
> your data.
>
> All of that means that someone in your workplaces, and on your career
> journeys, needs to show leadership in privacy, and it might as well be
> you.
>
> — [%i "Burns, Heather" %][Heather Burns][burns-privacy-quote][%/i%]

## An Example Attack

Dozens of books have been written about the mechanics of computer security
[%b Easttom2019 McDonald2020 Seitz2021 %].  We won't try to cover all of
that here, but it wouldn't feel right to wrap up this chapter without showing
you at least one software exploit that's unfortunately still quite common.

Suppose your application lets the user type in their ID, then uses that to look
up their account details in a database:

```py
def get_account(database_connection):
    username = input('Username:')
    query = 'select * from User where username="{}";'.format(username)
    result = database_connection.run(query)
    return result
```

It's simple, and the programmer has even remembered to wrap the username in
quotes. But suppose a malicious user enters this as their username:

```txt
"; drop table User; select "
```

<!-- continue -->
Once this is inserted, the query becomes:

```py
select * from User where username=""; drop table User; select "";'
```

<!-- continue -->
which looks up a user without a name, erases all of the data in the `User`
table, and then returns an empty string (the final `select`).  This is called an
[%i "SQL injection attack" %][%g sql_injection "SQL injection attack" %][%/i%],
and with a few modifications, it can be used to [%i "exfiltrate" %]exfiltrate[%/i%] data rather than delete it.

You defend against this by always [%i "sanitizing data" %][%g sanitizing_data "sanitizing user input" %][%/i%] before using it. In this case, the query can
be written as:

```py
    query = 'select * from User where username=?;'
    result = database_connection.run(query, username)
```

<!-- continue -->
The database connection library will escape special characters like the quotes
and semi-colons in the user's input and then use the result in place of the
question mark `?` in the query.

A [%g xss "cross-site scripting" %] attack works in the same way.
Suppose an online chat system displays whatever the user types as a message.  If
the user types in something that looks like a `<script>` tag containing some
JavaScript, then whoever views the message will run that JavaScript in their
browser. Again, the defense is to sanitize input; as with SQL, use a well-tested
library (preferably one whose source code you can check) rather than trying to
figure out the details yourself.
