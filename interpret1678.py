command = "G()(al)"

command = command.replace("()","o") # 先檢查字串中是否有"()"，有就替換成"o"
command = command.replace('(al)','al') # 再把修改過的字串檢查是否有"(al)"，有就替換成"al"
print(command) #最後印出修改完的字串
 

