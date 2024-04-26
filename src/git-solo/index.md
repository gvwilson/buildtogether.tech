---
title: Using Git On Your Own
---

[%i "version control!reasons to use" %]Version control[%/i%] is the
collective memory of the project. It's what lets you move files from one machine
to another without clobbering stuff you just spent three hours writing and
without worrying about whether you forgot something important.  It also lets you
undo your mistakes: if you spend an hour or two going down the wrong path, and
want to get back to where you were, version control lets you do it reliably with
a single command. And if all that wasn't enough, version control keeps track of
who did what so that you know who to turn to with questions.

Dozens of [%i "version control!systems" %]version control[%/i%] systems
exist. [%i "version control!CVS" "CVS (version control)" %][CVS][cvs][%/i%]
was the workhorse of the open source world for many years; it was replaced by
[%i "version control!Subversion" "Subversion (version
control)" %][Subversion][subversion][%/i%], which fixed many of its predecessor's
flaws while introducing a few minor ones of its own.
Both of these were [%i "version control!centralized" %][%g centralized_system "centralized systems" %][%/i%]:

1.  One [%i "version control!repository" "repository (version control)" %][%g repository "repository" %][%/i%]
    stored the definitive copy of the project's files.

1.  Nobody ever edited the contents of the main repository directly. Instead,
    everyone worked in a local copy.

1.  In order to share files with other people (or to create a backup, which is
    really just a way to share files with your future self) people would [%g push_git "push" %]
    the contents of their copy to the main repository.
    To get other people's work, they would [%g pull_git "pull" %]
    changes from the main repository and combine them with their own work.

Centralized version control systems have largely been replaced by
[%i "version control!decentralized" %][%g decentralized_system "decentralized" %][%/i%]
ones, and in particular by [%i "version control!Git" "Git" %][Git][git][%/i%].
In theory, Git doesn't need a main
repository: developers can merge the contents of any repository into any other.
In practice, almost every project designates one repository as the master copy
so that people know where to look to find the current state of the project.

Unfortunately, Git has a needlessly complicated interface.
[%b PerezDeRosso2013 %] found that even experienced users have
a [%i "mental model!Git" %][%g mental_model "mental model" %][%/i%] of how it works that
contradicts its actual operation in important ways, and each of those
contradictions produces a steady stream of "what the hell?"  moments. Other
distributed version control systems like [%i "version control!Mercurial" "Mercurial (version control)" %][Mercurial][mercurial][%/i%]
are proof that this
complexity and pain are unnecessary.  The fact that most people don't
immediately realize that [the random Git manual page
generator][git-man-page-generator] is a [%i "Git!interface
(indistinguishable from hoax)" %]hoax[%/i%] says a lot as well.

So why do people keep using [%i "Git!reasons for popularity" %]Git[%/i%]? The
answer these days is, "Because it's the tax they have to pay in order to use
[GitHub][github]." At the time of writing, GitHub has over 40 million users and
hosts over 28 million public repositories, including those for many well-known
open source projects. It is easily the most popular
[%i "software portal!GitHub" %][%g software_portal "software portal" %][%/i%] in existence, and
offers all of the tools a small software team needs. Other portals exist, such
as [%i "Bitbucket" "software portal!Bitbucket" %][Bitbucket][bitbucket][%/i%]
and [%i "GitLab" "software portal!GitLab" %][GitLab][gitlab][%/i%], but
GitHub's share of the educational market is even larger than its share
among professional developers.  If you're using anything in class, you're almost
certainly using it, and it's probably helping you become a better programmer
[%b Hsing2019 %].

<div class="callout" markdown="1">
### Why can't we fix it?

If Git's interface is a problem, why can't we build a new one?
[%b PerezDeRosso2016 %] tried, but as they report, the gravity of the
existing interface is simply too powerful: as soon as people run into a problem
and start searching online for solutions, they're thrown back into the world of
original Git.
</div>

This chapter won't try to teach you Git from scratch: [GitHub's
guides][github-guides] and [the Atlassian Git tutorial][atlassian-git] do an
excellent job of that, as does [the Carpentries lesson on Git][carpentries-git].
Instead, we will review the basics that we hope you have learned previously,
then look at how to use Git and GitHub to collaborate in [%x git-team %].
We will show the commands as if you were running them in the Unix shell, but we
recommend that you use a [%i "Git!graphical interface" %]graphical
interface[%/i%] like [GitKraken][gitkraken], [SourceTree][sourcetree], or the
one that comes with your [%i "IDE" %]IDE[%/i%] ([%x tooling %]). These
are layered on top of the commands we are going to discuss, so they (should) all
work the same way.

## A Review of the Basics

When I am working on a solo project or in a small team, [%i "Git!basic
commands" %]seven commands[%/i%] account for roughly 85% of my Git
activity. Adding two more commands to set things up produces a toolkit that uses
Git as a file backup system.

The first step is to make sure that [%i "Git!configuring" %]Git knows who
we[%/i%] are by telling it our name and email address:

[%inc git_config.sh %]

Breaking this down:

-   Git commands are written as <code>git <em>verb</em></code>, where
    <code><em>verb</em></code> is a sub-command telling Git exactly what we want
    to do.

-   The `--global` option is used to specify a value for the command in the same
    way that parameters are used to pass values to functions. In this case,
    we're telling Git that we want to configure things globally (i.e., for every
    project we have on this computer). We can also configure things
    repository-by-repository if we want to have a different name or email
    address for different projects.

-   `user.name` is the thing we want to configure. There are a lot of these;
    `git config --list` displays them all.

-   Finally, we specify the values we want `user.name` and `user.email` to
    have. We wrap these in quotes because they contain spaces and the `@`
    symbol, which might otherwise confuse the shell.

Now that Git knows who we are, let's [%i "Git!creating project" %]set up a
project[%/i%].  If we are starting from scratch, we create a directory, go into
it, and run `git init`. This may or may not print out some messages depending on
what version of Git you have and how much of its output your GUI shows (if
you're using one). Either way, this command creates a sub-directory called
`.git` inside your project directory. That special sub-directory is what makes
something a project: it stores the data Git uses to keep track of what files you
have and how they've changed.

<div class="callout" markdown="1">
### Don't mess

Don't edit the files in your `.git` directory yourself—it will have the same
unfortunate effect as editing a spreadsheet or an image as if it was a text
file. If you'd like to know more about what they're for and how Git uses them,
please see [%b Chacon2014 %] or [%b Cook2019 %].
</div>

If your instructor or one of your teammates has already created a project, you
won't use `git init`. Instead, you will use `git clone` followed by the
project's URL to get a local copy called a [%i "Git!cloning project" %][%g clone_git "clone" %][%/i%].
For example, if you want a clone of this book, you can do
this:

[%inc git_clone.sh %]

This will create a directory with the same name as the project, create a `.git`
sub-directory inside it, and download the project's history so that you can
start work.

Regardless of how you create your repository, you can use `git log` to look at
its [%i "Git!history" %]history[%/i%]. If I run this command right now for
this book, I get:

[%inc git_log.sh %]
[%inc git_log.out %]

Each entry has:

-   A line labeled `commit` followed by a large hexadecimal number.  This number
    is a unique [%i "Git!commit ID" %]label[%/i%] for the state of the
    project's files at that point in time.  if we want to refer to a particular
    version of our project, we can use this or its first half-dozen digits (such
    as `6e30bd`) so long as the latter is unambiguous.

-   Two lines showing who saved the state of the project and when. The name and
    email address in the `Author` field are the ones we set up with `git
    config`; the [%i "timestamp!of Git commit" %][%g timestamp "timestamp" %][%/i%] is accurate to the second, and includes time zone
    information like the `-0500` showing that I'm in Eastern time so that anyone
    in the world can tell exactly when these files were saved.

-   A short comment called a [%i "commit message (version control)" "Git!commit message" %][%g commit_message "commit message" %][%/i%] that tells us what this
    change is all about. We will take a look in [%x git-team %] at how to
    write a good commit message; for now, just remember that if you and your
    teammates have made a hundred changes to the project over the course of ten
    or twelve weeks, you're going to want something more informative than "Fixed
    stuff."

All right: what are [%i "commit (version control)" "Git!commit" %][%g commit "commits" %][%/i%] and where do they come from? A commit is a snapshot
of the project at a particular moment in time; we create them using a command
like:

[%inc git_commit_with_message.sh %]

Here, `commit` is the verb and the `-m` (short for "message") option is followed
by the comment we want to save in the log.

<div class="callout" markdown="1">
### The most popular question on Stack Overflow

If you use Git on the command line and you *don't* provide a message using the
`-m` option, it will launch an editor so that you can write a longer message.
This is a good thing, except that the default editor on most Unix systems is
something called [%i "Vim editor!exiting" %]Vim[%/i%], whose interface is no
more intuitive than Git's. (In fact, one of the most frequently-viewed questions
on [Stack Overflow][stack-overflow] is "[How do I exit the Vim
editor?][so-exit-vim]". Unsurprisingly, another
[%i "Git!configuring" %]frequently-viewed question[%/i%] on Stack Overflow is
"[How do I make Git use the editor of my choice for my commits?][so-configure-git-editor]"
One of the many reasons you should interact with Git through a GUI is to avoid this issue.
</div>

Before we run `git commit`, though, we need to tell Git which files we want to
save in the commit, which we do using `git add`:

[%inc git_add.sh %]

[%i "Git!difference between add and commit" %]One way to think about
this[%/i%] is that `git add` puts things in a box to be shipped, while `git
commit` actually sends the package. Git requires us to do this in two steps
because we might change our mind about what we want to store: for example, we
might `git add` a file, then realize we need to make a few more edits, `git add`
it again, and then `git commit`. Alternatively, we might add a bunch of files,
then realize that some of them (like editor backup files or temporary files
created by the compiler) shouldn't be saved, so we take them out before
committing.

<div class="callout" markdown="1">
### Teach us to care and not to care

You can tell Git to [%i "Git!ignoring files" %]ignore certain kinds of
files[%/i%] by putting their names, or patterns that match multiple names, in a
file called `.gitignore`.  For example, the `.gitignore` file for this project
includes:

[%inc git_ignore.txt %]

Be careful not to put files containing passwords or [%g api_key "API
keys" %] for web services into version control: even if the repository is
private now, it might be public in future, or the team might grow to include
someone who shouldn't have access ([%x security %]).
</div>

We can keep track of which changes haven't yet been added and which ones have
using [%i "Git!showing status" %]`git status`[%/i%]. If I run this command
right now in this book's project I get:

[%inc git_status.sh %]
[%inc git_status.out %]

The first paragraph titled "Changes to be committed" tells me which files I have
asked Git to save using `git add`. The second paragraph, "Changes not staged for
commit", shows that I have modified `version-control.md` (this chapter) since I
last asked Git to save a snapshot. Both paragraphs tell me that I can use `git
restore` with or without the `--staged` option to put a file back the way it was
if I decide I don't want to save the changes I've made.

I can use [%i "Git!recovering old files" %]`git restore`[%/i%] to recover an
old version of a file from any previous commit. Being able to do this was the
original motivation for version control systems, and is still one of the main
reasons people use them. For example, if I want to get the version of this file
from two days ago, I can use `git log` to find the commit ID `2be70844`, and
then run:

[%inc git_restore.sh %]

I can also count backward from where I am now.  The most recent commit has the
special [%i "Git!HEAD" %]symbolic name `HEAD`[%/i%]; the expression `HEAD~1`
means "the one before it", while `HEAD~2` goes back two commits and so
on. Regardless of how I specify what I want, restoring an old version doesn't
erase any of the ones I have saved since then: the project's history stays
intact.

Finally, I should make sure there's a second physical copy of my work so that if
my drive fails or my laptop is stolen I don't lose everything I've done. If I
created the repository by cloning something on GitHub, then Git will
automatically have created a bookmark called a
[%i "Git!remote" "remote (in Git)" %][%g remote_git "remote" %][%/i%] that points
at the original repository. I can get a list of remotes like this:

[%inc git_remote.sh %]
[%inc git_remote.out %]

The `-v` option (short for "verbose") tells Git to print more than just the
remote's name. The remote itself is called `origin`, and Git lists two URLs for
it because in theory you can download (or "fetch") from one and upload (or
"push") to another. (I have been using Git for sixteen years, and have never
once needed this feature.)

One of the differences between a version control system like Git and a file
backup tool like [Dropbox][dropbox] is that Git *doesn't* automatically
synchronize local changes to the remote repository.  If I want to [%i "Git!saving changes remotely" %]save[%/i%] everything I've done locally on
GitHub, I have to push them explicitly:

[%inc git_push_origin_main.sh %]

The verb is `push`; the word `origin` identifies where I want to send things,
and the word `main` identifies the branch I'm on.  We'll discuss branches in the
next section, but for now, you can run `git branch` to see which ones you have
and which one you're working in.

The counterpart of `git push` is `git pull`. It downloads changes from the
remote repository and merges them into your local copy:

[%inc git_pull_origin_main.sh %]

Pushing and pulling changes allows you and your teammates to synchronize your
work. They're also very useful operations if you're working on your own and
using two or more computers (such as a personal laptop and your school's
servers).

<div class="callout" markdown="1">
### Clean and build

Many instructors require learners to submit work by committing it to a Git
repository. One way to check that what works for you will work for whoever is
grading it is to clone a fresh copy of the project in a temporary directory and
make sure that everything builds and runs there. Doing that will tell you if you
or one of your teammates has forgotten to commit a key file. In an advanced
course, you might be asked to do this automatically every time someone commits
changes; we'll explore this in [%x tooling %].
</div>

## A Branch-Based Workflow

So far we have only used a sequential timeline with Git: each change builds on
the one before, and *only* on the one before.  However, there are times when we
want to work on several things at once.  To do this, we can use
[%i "branch (in Git)" "Git!branch" %][%g branch_git "branches" %][%/i%] to work on
separate tasks in parallel.  Each branch is like a parallel timeline: changes made
to one branch have no effect on other branches unless and until we explicitly merge
them.

We can see what branches exist in a repository like this:

[%inc git_branch.sh %]
[%inc git_branch.out %]

When we initialize a repository, Git automatically creates a branch called
`master`; most people now rename this to `main` by running:

[%inc git_branch_rename.sh %]

immediately after running `git init`.  The [%i "Git!branch names" %]`main`
branch[%/i%] is usually considered the "official" version of the repository,
i.e., the version of the project that should be graded or published for other
people to use.  The asterisk `*` indicates that it is currently active, i.e.,
that all changes we make will take place in this branch by default.

To create a new branch called `homework3` we run:

[%inc git_branch_create.sh %]

The name of the branch should indicate what it's for, just like the names of
files and variables.  We can check that the branch exists by running `git
branch` again:

[%inc git_branch_2.sh %]
[%inc git_branch_2.out %]

Our branch is there, but the `*` shows that we are still in the `main` branch.
To switch to our new branch we use the `checkout` command:

[%inc git_checkout.sh %]
[%inc git_checkout.out %]

We haven't made any changes since switching to the `homework3` branch, so at
this point `main` and `homework3` are at the same point in the repository's
history.  Commands like `ls` and `git log` therefore show that the files and
history haven't changed.

<div class="callout" markdown="1">
### Where branches are saved

Git saves every version of every file in the repository's `.git` directory.
When we switch from one branch to another, it copies files out of there and
rearranges directories to restore that state of the world.
</div>

Why go to all this trouble?  Because it allows us to work on several things at
once without stepping on our own toes, just as putting variables inside objects
and classes allows us to ignore the details of *this* when we're working on
*that*. For example, if we are close to finishing homework 3 but want to get an
early start on homework 4, we can create a new branch from `main` called
`homework4` and start setting things up in there.

When we are done, we can [%i "merge (in Git)" "Git!merge" %][%g merge_git "merge" %][%/i%] the state of one branch back into another. Merging
doesn't change the source branch, but once it's done, all of the changes made
there are in the destination branch.

To see what the differences are between two branches, we use [%i "Git!viewing differences" %]`git diff`[%/i%] with those branches' names:

[%inc git_diff_branch.sh %]

More generally, we can use `git diff` to compare any two states of the
repository, including old versions with current ones:

[%inc git_diff_head.sh %]
[%inc git_diff_head.out %]

The output marks additions with a `+` and deletions with a `-`. A line that has
changed is shown as a deletion followed by an addition, and the lines marked
with `@@` show where in the file the change occurred.

<div class="callout" markdown="1">
### See the difference

You have to be a bit of a masochist to read diffs like this; it's a lot easier
using a [%i "Git!graphical interface" %]GUI[%/i%] like
[DiffMerge][diffmerge].  You can [use other tools to view diffs][git-difftool]
between files that aren't plain text, but only if such tools exist. They don't
for many common file formats: for example, there isn't an easy way to see the
differences between two version of an SVG diagram or between two spreadsheets.
If you are looking for projects to work on that people will actually use, these
would be good ones.
</div>

Once we're sure we actually want to merge changes, we do so like this:

[%inc git_merge.sh %]

Git automatically creates a new commit to represent the merge.  If we now run
`git diff main..homework3`, Git doesn't print anything because there aren't any
differences to show.

After we merge the changes from `homework3` into `main` there is no need to keep
the `homework3` branch, so we can delete it:

[%inc git_branch_delete.sh %]
[%inc git_branch_delete.out %]

Merging `homework3` into `main` went smoothly, but if we are going to use
branches, we must learn how to merge [%i "conflict (in Git)" "Git!conflict" %][%g conflict_git "conflicts" %][%/i%].  These occur when a line has been changed
in different ways in two branches or when a file has been deleted in one branch
but edited in the other.

If the file `README.md` has been changed in both `main` and `homework4`,
`git diff` will show the conflict:

[%inc git_diff_conflict.sh %]

When we try to merge `homework4` into `main`, Git doesn't know which of these
changes to keep:

[%inc git_merge_conflict.sh %]

After we run this command, Git has put both sets of changes into `README.md`,
but has marked which came from where:

[%inc cat_readme.sh %]

The lines from `<<<<<<< HEAD` to `=======` are what was in `main`, while the
lines from there to `>>>>>>> docs` show what was in `homework4`.  If there were
several conflicting regions in the same file, Git would mark each one this way.
Once again, you have to hate yourself a little to view these conflicts as raw
text files; even legacy text editors like [Emacs][emacs] will highlight them,
and Git GUIs will help you view and edit these regions.

We have to decide what to do next: keep the `main` changes, keep those from
`homework4`, edit this part of the file to combine them, or write something new.
Whatever we do, we must remove the `>>>`, `===`, and `<<<` markers.  Once we are
done, we can add the file and commit the change like we would any other edit:

[%inc git_resolve.sh %]

Our branch's history will now show a single sequence of commits with the `main`
changes on top of the earlier `homework4` changes:

[%inc git_log_oneline.sh %]

If we want to see what happened, we can add the `--graph` option to `git log`:

[%inc git_log_graph.sh %]

At this point we can delete the `homework` branch or switch back to it and do
some more work.  Each time we switch to it, we merge changes *from* `main`
*into* `homework4`, do our editing (while switching back to `main` or other
branches as needed to work on the code), and then merge *from* `homework4` *to*
`main` once the documentation is updated.

<div class="callout" markdown="1">
### Rebasing

One way to make the history of a repository easier to read is to squash several
consecutive commits into one.  This is called
[%i "Git!rebase; rebasing (in version control)" %][%g "rebase_git" "rebasing" %][%/i%],
and can be done using:

[%inc git_rebase.sh %]

where `START` identifies the commit *before* the ones you want to start merging
(i.e., the last one *not* to modify). Rebasing can go wrong in a lot of
confusing ways, particularly if you have merged changes from another branch into
the one you're squashing, so we recommend that you avoid it for schoolwork.
</div>

Branches can be confused, but this [%i "Git!workflow" "workflow (in
Git)" %]workflow[%/i%] will help you keep track of what you are doing:

1.  `git checkout main` to make sure you are in the `main` branch.

2.  `git checkout -b name-of-feature` to create a new branch.  *Always* create a
    branch when making changes, since you never know what else might come up.
    The branch name should be as descriptive as a variable name or filename
    would be.

3.  Make your changes.  If something occurs to you along the way—for example,
    if we are writing a new function and realize that the documentation for some
    other function should be updated—*don't* do that work in this branch.
    Instead, commit our changes, switch back to `main`, and create a new branch
    for the other work.

4.  When the new feature is complete, use `git merge` to get any changes you
    merged into `main` after creating `name-of-feature` and resolve any
    conflicts.  This is an important step: you want to test that everything
    works while you are in your feature branch, not in `main`.

5.  Finally, switch back to `main` and `git merge name-of-feature main` to merge
    your changes into `main`.  You should not have any conflicts, and all of
    your tests should pass.

Most developers use this [%g branch_per_feature_workflow "branch-per-feature workflow" %], but what
exactly is a "feature"?  These rules make sense for small projects:

1.  Anything cosmetic that is only one or two lines long can be done in `main`
    and committed right away.  "Cosmetic" means changes to comments or
    documentation: nothing that affects how code runs, not even a simple
    variable renaming.

2.  A pure addition that doesn't change anything else is a feature and goes into
    a branch.  For example, if you are adding a feature to the user interfaces,
    that should be done on its own branch because it might take several tries to
    get right, and you might interrupt yourself to fix things you discover along
    the way.

3.  Every bug fix is also done in a separate branch

The hardest thing about using a branch-per-feature workflow is sticking to it
for small changes.  As the first point in the list above suggests, most people
are pragmatic about this on small projects; on large ones, where dozens of
people might be committing, even the smallest and most innocuous change needs to
be in its own branch so that it can be reviewed (which we discuss below).
