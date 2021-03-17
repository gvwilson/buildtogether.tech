---
---

Which of these do you believe is true?

1.  As a student, you own every piece of software you write for course
    assignments.  If the university wants to use that software in any way other
    than for giving you a grade, they need your permission: you can say "no" or
    ask for payment.

1.  You own the software you write for course assignments *as long as you do
    the work on your own computer*. If you use a university's machines, they
    have an equal right to the software: you can continue developing it or
    sell it if you want, but they can too, and they don't need your permission.

1.  If you are an undergraduate and paying fees to attend a university, you
    own the software you produce. If you are a graduate student being paid a
    stipend, on the other hand, the university owns what you produce.

1.  If you a graduate student then you, your supervisor, and your university
    all have a right to what you produce.

The answer is, "It depends where you are."  Different schools can have very
different rules, even if they are in the same legal jurisdiction (i.e., the same
country, state, or province). In fact, some universities' rules depend not only
on who you are but on which faculty you are in.

The rules in industry are less complex---anything you do on company time or with
company resources belongs to the company---but there are many gray areas. For
example, I wrote some of the first drafts of this book on a company laptop while
traveling for work. Does that mean I owe my former employer a share of the
royalties?

Who owns what is just one of the rights that societies recognize.  Others
guaranteed by the [Universal Declaration of Human Rights][udhr] include the
right to say what you want, the right to live free from fear, and the right to
be treated the same way as everyone else regardless of your race, sex,
orientation, religion, or disability.  Most countries have signed this
declaration, meaning that in theory at least, it has the force of law.

However, the phrase "in theory" in the previous paragraph is doing a lot of
work.  In practice, most societies still treat people unequally and unfairly;
the question is, do we acknowledge that and try to fix it, or ignore it in the
hope that when bad things happen, they'll only happen to other people?  What's
more, all of our rights have been profoundly affected by what software engineers
have built. If the first rule of being compassionate is to do no harm, the first
step in becoming a compassionate programmer is to learn what rights people have
so that you don't violate them.

## Intellectual Property

<span g="intellectual_property">Intellectual property</span> (IP) is a catch-all
term that covers four separate kinds of rights: copyrights, patents, trade
secrets, and trademarks. Each of these has evolved over several centuries to
address the economic and moral concerns of people powerful enough to influence
law-making. What ties them together is that, compared with physical goods,
information is expensive to produce but cheap to copy. IP exists to ensure that
creators can earn enough from producing intangible goods that they can keep
doing it. Each kind of IP therefore gives its holder some kind of limited
monopoly over some kind of information.

<span g="copyright">Copyrights</span> apply to any original expression that
anyone creates. While people can't (yet) own facts, they *can* own any
representation of those facts that contains an element of creativity.  As a
result of this broad scope, there are several exceptions to copyright, making it
the weakest protection available. When placed in the proper context, however,
copyright is a powerful tool for IP protection.

<span g="patent">Patents</span> apply to inventions, technological improvements,
certain designs, business methods, and a few other things. They grant a
monopoly---the right to exclude others from using the patented idea---for a
fixed period of time (usually twenty years).  Since the right is stronger, the
requirements for obtaining a patent are more stringent: it can take years,
hundreds of pages of paperwork, and thousands of dollars to secure one.

Patents are intended to be a bargain between the inventor and the public: the
inventor discloses how the invention works (so that other people can learn from)
and in exchange society ensures that she is the only one who can profit from it
for a reasonable time. If an inventor doesn't want anyone to know how her
invention works she can treat it as a <span g="trade_secret">trade
secret</span>.  This isn't a property right as such, but rather the practice of
relying on things like <span g="non_disclosure_agreement">non-disclosure
agreements</span> to keep something secret. There is less risk of someone being
inspired by your idea to create something better, but if the idea *does* leak,
the inventor has less legal protection.

Finally, <span g="trademark">trademarks</span> allow people to tell whether a
product is authentic or not. Given that everyone has limited time in which to
make decisions, a brand name acts as a form of mental shorthand: if company XYZ
has a reputation for high quality or low prices, or if a particular medication
has been proven to be effective against an ailment like heart disease, the name
itself has commercial value.

## Software Licenses

A <span g="license">license</span> dictates how project materials can be used
and redistributed.  If the license or a publication agreement makes it difficult
for people to contribute, the project is less likely to attract new members, so
the choice of license is crucial to the project's long-term sustainability.

Every creative work has some sort of license; the only question is whether
authors and users know what it is and choose to enforce it.  Choosing a license
for a project can be complex, not least because the law hasn't kept up with
everyday practice.  (<cite>Lindberg2008</cite> is a good exploration of these
issues if you want details.)  Depending on country, institution, and job role,
most creative works are automatically eligible for intellectual property
protection.  However, members of the team may have different levels of copyright
protection.  For example, students and faculty may have a copyright on the
research work they produce, but university staff members may not, since their
employment agreement may state that what they create on the job belongs to their
employer.

To avoid legal messiness, every project should include an explicit license.
This license should be chosen early, since changing a license can be
complicated.  For example, each collaborator may hold copyright on their work
and therefore need to be asked for approval when a license is changed.
Similarly, changing a license does not change it retroactively, so different
users may wind up operating under different licensing structures.

<div class="callout" markdown="1">

### Leave it to the professionals

Don't write your own license.  Legalese is a highly technical language, and
words don't mean what you think they do.  What's more, it's often hard to
understand the interactions between multiple licenses on different kinds of
material <cite>Almeida2017</cite>.

</div>

Just as the project's Code of Conduct is usually placed in a root-level file
called `CONDUCT.md` (<span x="project"></span>), its license is usually put in a
file called `LICENSE.md` that is also in the project's root directory.  To make
license selection for code as easy as possible, GitHub allows us to select one
of several common software licenses when creating a repository.  Unfortunately,
their list does not include common licenses for data or written works like
papers and reports.

The Open Source Initiative maintains [a list][osi-license-list] of <span
g="open_license">open licenses</span>, and [choosealicense.com][choose-license]
will help us find a license that suits our needs.  In order to choose the right
one, we need to understand the difference between two kinds of license.  The
<span g="mit_license">MIT License</span> and its close sibling the <span
g="bsd_license">BSD License</span> say that people can do whatever they want to
with the software as long as they cite the original source, and that the authors
accept no responsibility if things go wrong.  The <span g="gpl">GNU Public
License</span> (GPL) gives people similar rights, but requires them to share
their own work on the same terms:

<blockquote markdown="1">

You may copy, distribute and modify the software as long as you track
changes/dates in source files.  Any modifications to or software including
(via compiler) GPL-licensed code must also be made available under the GPL
along with build and install instructions.

--- [tl;dr][tldr-gpl]

</blockquote>

In other words, if someone modifies GPL-licensed software or incorporates it
into their own project, and then distributes what they have created, they have
to distribute the source code for their own work as well.

The GPL was created to prevent companies from taking advantage of open software
without contributing anything back.  The last thirty years have shown that this
restriction isn't necessary: many projects have survived and thrived without
this safeguard.  We therefore recommend that projects choose the MIT license, as
it places the fewest restrictions on future action.

The [Hippocratic License][hippocratic-license] is a newer license that is
quickly becoming popular.  Where the GPL requires people to share their work,
the Hippocratic License requires them to do no harm.  More precisely, it forbids
people from using the software in ways that violate the Universal Declaration of
Human Rights.  We have learned the hard way that software and science can be
mis-used; adopting the Hippocratic License is a small step toward preventing
this.

## Creative Commons Licenses

The MIT license, the GPL, and the Hippocratic License are intended for use with
software.  When it comes to data and reports, the most widely used family of
licenses are those produced by [Creative Commons][creative-commons].  These have
been written and checked by lawyers and are well understood by the community.

The most liberal option is referred to as <span g="cc0">CC0</span> where the "0"
stands for "zero restrictions".  This puts work in the public domain, i.e.,
allows anyone who wants to use it to do so however they want with no
restrictions.  CC-0 is usually the best choice for data, since it simplifies
aggregate analysis involving datasets from different sources.  It does not
negate the scholarly tradition and requirement of citing sources; it just
doesn't make it a legal requirement.

The next step up from CC-0 is the Creative Commons--Attribution license, usually
referred to as <span g="cc_by">CC-BY</span>. This allows people to do whatever
they want to with the work as long as they cite the original source.  This is
the best license to use for manuscripts: we want people to share them widely but
also want to get credit for our work.

Other Creative Commons licenses incorporate various restrictions, and are
usually referred two using the two-letter abbreviations listed below:

-   ND (no derivative works) prevents people from creating modified versions of
    our work.  Unfortunately, this also inhibits translation and reformatting.

-   SA (share-alike) requires people to share work that incorporates ours on the
    same terms that we used.  Again, it is fine in principle but in practice
    makes aggregation and recombination difficult.

-   NC (no commercial use) does *not* mean that people cannot charge money for
    something that includes our work, though some publishers still try to imply
    that in order to scare people away from open licensing.  Instead, the NC
    clause means that people cannot charge for something that uses our work
    without our explicit permission, which we can give under whatever terms we
    want.

<div class="callout" markdown="1">

### Why be open?

<cite>Hippel2006</cite> reports that 85% of all interesting innovations in all
industries come not from the suppliers but from the users.  The more open work
is, the better able users are to tinker with it and do things that the first
contributors would never have thought of trying.

</div>
