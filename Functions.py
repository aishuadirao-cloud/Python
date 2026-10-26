class trainingFunctions():
    def subfields():
        fields=['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        print("Sub-fields in AI are:")
        for i in fields:
            print(i)
        
    def oddeven(num):
        if(num%2==0):
            return "Even"
        else:
            return "Odd"    
    
    def eligibility(gender,age):
        if(gender=="M" and age>=21):
            return("Eligible")
        elif(gender=="F" and age>=18):
            return("Eligible")
        else:
            return("Not Eligible")  

    def calcPercentage(listMarks):
        sum=0
        for i,marks in enumerate(listMarks):
            print("Subject",i+1,":",marks)
            sum=sum+marks
        print("Total:",sum)
        return((sum/500)*100)

    def triangle():
        height=float(input("Enter the height of the triangle"))
        breath=float(input("Enter the breath of the triangle"))
        print("Area formula: (Height*Breadth)/2")
        print("Area of the triangle:",(height*breath)/2)
        side1=float(input("Enter the side1 length of the triangle"))
        side2=float(input("Enter the side2 length of the triangle"))
        print("Perimeter formula: side1+side2+breath")
        print("Perimeter of the triangle",side1+side2+breath)

    
    