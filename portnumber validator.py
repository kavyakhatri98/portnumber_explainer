ports={
    20: "FTP Data Transfer",
    21: "FTP Control",
    22:"SSH (Secure Shell)",
    23:"Telnet",
    25:"SMTP(Simple Mail Transfer Protocol)",
    53:"DNS (Domain Name System)",
    67:"DHCP (Dynamic Host Configuration Protocol) SERVER",
    68:"DHCP (Dynamic Host Configuration Protocol)CLIENT",
    69:"TFTP (Trivial File Transfer Protocol)",
    80:"HTTP(Hypertext Transfer Protocol)WEB TRAFFIC",
    110:"POP3 (Post Office Protocol 3)EMAIL RECEIVING",
    143:"IMAP (Internet Message Access Protocol)EMAIL RECEIVING",
    443:"HTTPS (Hypertext Transfer Protocol Secure)SECURE WEB TRAFFIC",
    3306:"MySQL Database System",
    3389:"RDP (Remote Desktop Protocol)",
    5900:"VNC (Virtual Network Computing)"
}
try:
    port=int(input("Enter the port number: "))
    if 1<=port<=65535:
        if port in ports:
            print("\nPort found!")
            print(f"Port Number: {port}\nService: {ports[port]}")
        else:
            print("\nPort not found in the predefined list. It may be used for other services or applications.")
    else:
        print("\nInvalid port number. Please enter a number between 1 and 65535.")
except ValueError:
    print("\nInvalid input. Please enter a whole number.")