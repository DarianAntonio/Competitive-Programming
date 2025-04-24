guest_name = str(input())
residence_host = str(input())
letters_pile = str(input())
if sorted(guest_name+residence_host) == sorted(letters_pile):
    print("YES")
else:
    print("NO")