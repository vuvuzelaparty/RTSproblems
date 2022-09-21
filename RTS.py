#!/usr/bin/env python

class RTS:
    def aboveBelow(self, list, compare):
        above=0
        below=0
        for i in list:
            if i > compare:
                above+=1
            if i < compare:
                below+=1
        return { "above" : above, "below" : below }

    def stringRotation(self, str, amount):
        return (str[len(str)-amount:]+str[:len(str)-amount])

def main():
    rts=RTS()
    print(rts.aboveBelow([1,5,2,1,10], 6))
    print(rts.stringRotation("MyString", 10))

if __name__=="__main__":
    main()
