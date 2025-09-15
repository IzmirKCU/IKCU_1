# General Requirements

## Introduction
### Markdown
What is **Markdown**? Why am I giving you course notes in a Markdown file? (why not use **Microsoft Word** or a simple text file?)

* **Microsoft Word** only runs on Windows/Mac. We could use **LibreOffice** or **ONLYOFFICE** on Linux, but the format generally looks different (usually because the Microsoft fonts are not installed). 

* A text file would be Operating System independent, but would lack any format options. 

**Markdown** sits in between these two options. It accepts rich text format options and is Operating System Independent. The drawback is it takes a little longer to write Markdown files. 




## A Linux based operating system. 

I don't use Windows because it isn't particularly well suited for hard core bioinformatics. I always use Linux, and if you are using High Performance Computing (HPC) or Cloud computing facilities to do your analysis, you will have to use Linux. Moreover, you will have to use the Command Line Inteface (CLI) as you will be accessing the HPC/Cloud system through a CLI terminal.


### Ubuntu vs Mint vs Fedora

It generally doesn't matter so much which version of Linux you are using as there won't be so much difference in the command syntax. the major difference in the distributions (or distros) is how you install software. 

Most people use Ubuntu. I like MINT as it is more 'lightweight' (i.e., it doesn't use so much CPU or memory) so it puts less demand on older computers but you can use any distro you want. If you have a MacBook, I will try to help, but there are no guarantees - MacOS is based on BSD Unix and behaves quite differently from standard Linux distributions. 


          Unix/Linux Family Tree 
          +----------- Unix - - - - - -+ 
          | (modify)           (clone) |  
         BSD                          GNU 
          |      (replace kernel)      | 
     Darwin/OS X                     Linux 


In particular with software installations on MacOS we have run into many problems and in some cases we gave up

### Ubuntu on Windows
If you have a Windows Laptop, you can install Ubuntu for Windows from the Microsoft store
This will give you access to a Ubuntu shell that "sits" on top of Windows. So, you can perform Linux style processing on your files. 

# Required Software/Tools

## Text Editor for viewing code and writing Markdown

You can use whatever you like. I prefer [**Visual Studio Code**](https://code.visualstudio.com/)

## GitHub
We need this to track software changes and to make our code easily available. We will follow the official GitHub tutorial [here](https://docs.github.com/en/get-started/onboarding/getting-started-with-your-github-account) to get setup.




## An Integrated Development Environment (IDE)

I also recommend using an Integrated Development Environment (IDE). You can use Visual Studio Code for this, but in my opinion it lacks the flexibility and power of many of the language specific IDEs. When you are developing more complex software tools a full IDE can aid the development process. Eclipse will handle all the languages we are working with (except R). However, the choice of IDE is really guided by what works best for you- For example, I've never been able to get on with Eclipse and since I primarily develop in Python and Java, I use two different IDEs (PyCharm and IntelliJ).

## Java

We need a Java Runtime Environment (JRE), a Java Development Kit  (JDK) and a Java Virtual Machine (JVM). The JRE provides everything that is needed to run Java programs. The JVM is a subset of the JRE and converts the executable Java code into machine code that can run on a specific system (e.g. Windows versus MacOS) The JDK contains the tools you need to develop Java programs (e.g. a compiler and debugger). If we choose a suitable IDE, we can get the JDK and JRE as part of the package.  


### Eclipse Integrated Development Environment (IDE)

https://www.eclipse.org/downloads/

I installed **IDE 2022-12** 
![sha512bad](images/eclipse/eclipse.png)

and selected Eclipse IDE for Java developers
![sha512bad](images/eclipse/eclipse_install_screen.png)


Need to check the downloaded file is trustworthy

![sha512bad](images/eclipse/eclipse_sha512.png)

To check this, we run the following command from a command window

![sha512bad](images/eclipse/shasum512_eclipse_cli.png)

We'll come back to this after we have finished installing Eclipse

Open a commmand window and change to the folder where you downloaded the installation file

```
(base) simon@minty22:~$ cd Downloads/
```

extract the file

```
(base) simon@minty22:~/Downloads$ tar xvf eclipse-inst-jre-linux64.tar.gz 
eclipse-installer/
eclipse-installer/readme/
eclipse-installer/readme/readme_eclipse.html
eclipse-installer/features/
eclipse-installer/features/org.eclipse.emf.edit
    .
    .
    .
    eclipse-installer/p2/org.eclipse.equinox.p2.engine/profileRegistry/DefaultProfile.profile/1669830388583.profile.gz
```
we now have a new folder `eclipse-installer` 
```    
(base) simon@minty22:~/Downloads$ ls
eclipse-installer  eclipse-inst-jre-linux64.tar.gz  RS_2006-03  RS_2006-03.zst

```
change to this folder and run the installation script
``` 
(base) simon@minty22:~/Downloads$ cd eclipse-installer/
(base) simon@minty22:~/Downloads/eclipse-installer$ ls
artifacts.xml  eclipse-inst      features  p2       readme
configuration  eclipse-inst.ini  icon.xpm  plugins
(base) simon@minty22:~/Downloads/eclipse-installer$ ./eclipse-inst 
``` 

This will open the following window and give a range of different options for the IDE. We are going to use the **Eclipse IDE for Java Developers**






# Perl

As I said in the Introduction, we aren't going to look at Perl in this course as we are using Java, Python and R. 

### Perl 5 vs Perl 6

The only point I will mention is that if you are going to use Perl, it is probably better to stick with Perl5 as Perl5 & 6 seem to represent two different languages and syntaxes. Moreover, BioPerl doesn't seem to be supported in Perl 6 so far.

# Python

You need to be running Python 3, not Python 2

Jupyter notebooks ([https://jupyter.org/install](https://jupyter.org/install))


Command Line Python

Virtual Environments


## R

RStudio



## Docker

### 1. update the software repositories

```
sudo apt update

[sudo] password for simonray:          
Hit:1 http://packages.microsoft.com/repos/code stable InRelease
Hit:2 https://repo.steampowered.com/steam stable InRelease
Hit:3 https://repo.skype.com/deb stable InRelease                              
Hit:4 http://archive.ubuntu.com/ubuntu focal InRelease                                                                      
Hit:5 http://archive.canonical.com/ubuntu focal InRelease                                                                   
Get:6 http://archive.ubuntu.com/ubuntu focal-updates InRelease [114 kB]                                                     
Ign:7 https://ftpmirror1.infania.net/mirror/linuxmint/packages uma InRelease                                                
Hit:8 https://ftpmirror1.infania.net/mirror/linuxmint/packages uma Release                                                  
Get:9 http://security.ubuntu.com/ubuntu focal-security InRelease [114 kB]                               
Get:10 http://archive.ubuntu.com/ubuntu focal-backports InRelease [108 kB]                                          
Hit:12 https://packagecloud.io/slacktechnologies/slack/debian jessie InRelease                                       
Fetched 336 kB in 2s (206 kB/s)
Reading package lists... Done
Building dependency tree       
Reading state information... Done
1 package can be upgraded. Run 'apt list --upgradable' to see it.

``` 


### 2. Install Docker

``` 
sudo apt install docker*
``` 

### 3. System Cleanup

if you are short on disk space you can also do a clean up

```
sudo apt autoremove
```


# Singularity

# SLURM




# Things to Remember

## don't put spaces in directory names

Program Files




