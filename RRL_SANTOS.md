RRL STUFF
Phishing Awareness Campaign
A study by E.B. Blancaflor et al., deals with how users are vulnerable to smishing, email phishing and social media phishing. The study shows that phishing attacks can be done with minimal effort. To achieve this, the researchers created two fake webpages, one named Shop Mug Manila where there is a survey that asks users for their contact information, and a disclaimer page that asks the user about their awareness of such attacks. The study also made use of Google’s Tag Manager and Analytics tools, and GoPhish, which is an open-source phishing framework. They also used a Bitly URL shortener to hide its real URL from unsuspecting victims. 

The researchers used a variety of approaches to demonstrate the vulnerability of unwary users:
•	Smishing – They used shortened links to 24 targeted users.
•	Social Media Phishing  - Through messenger, they distributed the link to the website to 46 targeted users.
•	Email Phishing  - The researchers made a fake gmail account posing as the website and have sent it to 37 targeted users.

Out of all the techniques that are used in the study, social media phishing is proven to be the most effective of them all, with a 52.17% success rate. Making this the most effective platform to attack users. It is suggested that the best way of mitigating the risk of attacks is to understand the concept of phishing. Targeted users must also look for the destination URL of the sent link before clicking, even if it is from someone they know. Another important note is that the use of Google’s Tag Manager and Analytics can bypass Facebook messenger’s error detection, and the security standards of Google Mail, making it a dangerous tool if used maliciously, specially when storing sensitive information.  

SMS-based OTP
A study by A.R. Reyes et al., demonstrates a novel approach to secure an SMS-based OTP. An OTP (One Time Password) is a code of password that is only useable within a single session or transaction. It is widely used for authentication because it only needs a mobile number to be effective. It starts with a  generated code by the user to identify if the username and password is actually coming from them. Once the correct OTP has been filled, the user can now proceed with logging in.



SMS-based OTP however is still vulnerable to smishing attacks. With social engineering, users can be fooled into giving their OTP to gain access to their accounts. And other threats such as:

•	Keylogging – captures user keystrokes, and sends them to the attacker.
•	Screencapturing – capturing of the screen
•	Shoulder surfing – looking at someone’s keyboard whenever they are entering sensitive information, and copying from it.

Using a web-based application and end-user mobile application, both use an algorithm named Blowfish-128, which is an improved version of the blowfish algorithm supporting the 128-bits block size. The algorithm implements a dynamic selection encryption method, while reducing the execution times of the cipher function in randomly determined rounds. The algorithm also improved its performance, security, complexity, and execution time. The code will then be sent to the SMS, which was designed to expire at a specific time. If incorrect information has been received or the OTP expires, you will have to retry again. To combat against smishing and eavesdropping, the OTP sent by the web app will not be displayed on the interface of the mobile app for protection. After confirmation in the phone, another otp will be generated from the received verification of the user,  which will then be verified by the web app, creating another layer of protection between the mobile app, web app, and the user. As a result, the solution OTP is safer from attacks and is safer from smishing, eavesdropping and other related vulnerabilities that are likewise present in a normal OTP setting.





References

[1] 	E. B. Blancaflor, A. B. Alfonso, K. N. U. Banganay, G. A. B. Dela Cruz, K. E. Fernandez and S. A. M. Santos, "Let's Go Phishing: A Phishing Awareness Campaign Using Smishing, Email Phishing, and Social Media Phishing Tools," in 11th Annual International Conference on Industrial Engineering and Operations Management, Singapore, 2021. 

[2] 	A. R. L. Reyes, E. D. Festijo and R. P. Medina, "Enhanced Multi-factor Out-of-band Authentication En Route to Securing SMS-based OTP," International Journal of Engineering and Technology Innovation, vol. 9, no. 2, pp. 145-154, 1 April 2019. 


