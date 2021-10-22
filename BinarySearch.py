class searcha:
    limit=mid=key=0
    item=0
    mlist=[]
    def reads(self):
        global limit
        global item
        global mlist
        mlist=[]
        limit=int(input("enter the number of elements \n "))
        for i in range(limit):
            item=int(input("enter the number \n"))
            mlist.append(item)
            mlist.sort()
    def bisearch(self):
        global limit
        global mid,key
        key=int(input("enter the element to find: \n"))
        lb=0
        ub=len(mlist)
        while lb<=ub:
            mid=(lb+ub)/2
            mid=int(mid)
            if mlist[mid]==key:
                self.prints()
                print("element {} is found at index {}!".format(key,mid))
                print(">>note: index starts from 0<<")
                exit(0)
            elif key>mlist[mid]:
                lb=mid+1
            else:
                ub=mid-1
        self.prints()
        print("element {} not found!".format(key))
    def prints(self):
         global mid,key,mlist
         print("the list is :",mlist)
         print("the element to find:",key)

o1=searcha()
o1.reads()
o1.bisearch()