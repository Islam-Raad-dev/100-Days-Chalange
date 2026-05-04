def Check_Spam(Email_Text):
    Spam_Words = ["مجاني", "جائزة", "ربح", "اضغط هنا"]
     
    for word in Spam_Words:
        if word in Email_Text:
            return "spam"
    
    return "Inbox"

print (Check_Spam("اضغط هنا"))
print (Check_Spam("ربح"))
print (Check_Spam("جائزة"))
print (Check_Spam("مجاني"))
