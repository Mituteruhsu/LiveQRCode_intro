def pharse_str(inp_str,style):
    readline=len(style)
    CurrentStrNum=len(inp_str)
    CheckStrNum=0  #noStrptr
    while CurrentStrNum>=readline:
        
        for i in range(readline):
            if not (bool(ord('0')<=inp_str[CheckStrNum+i] <=ord('9')) ^ bool(style[i]=="1")):#is alpha or is number use Nxor gate 
                pass
            else:#check error
                CheckStrNum+=1
                CurrentStrNum=len(inp_str)-CheckStrNum
                break
            if i==readline-1:
                print(f"Find it : {inp_str[CheckStrNum:CheckStrNum+i+1]}")
                return inp_str[CheckStrNum:CheckStrNum+i+1]
    print("not found")
    return ""