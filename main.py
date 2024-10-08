class Todo:
    
    def __init__(self):
        self.issue = {}
        self.count = 0
        self.__count_no_complete = 0
        self.__count_transfer = 0
        
    def add_issue(self, issue, clock, complete, transfer):
        self.issue[issue] = [clock, complete, transfer]
        self.count += 1
        
    def delete_issue(self, issue):
        self.issue.pop(issue)
        self.count -= 1
        
    def get_count(self):
        return self.count
    @property
    def  count_no_complete(self):
        return self.__count_no_complete
    @property
    def count_transfer(self):
        return self.__count_transfer
    @count_no_complete.setter
    def count_no_complete(self, count_no_complete):
        self.__count_no_complete = count_no_complete
    @count_transfer.setter    
    def count_transfer(self, count_transfer):
        self.__count_transfer = count_transfer
    
    def change_issue(self, issue):
        temp = self.issue.get(issue)
        temp[1] = True
        self.issue.update({issue:temp})
        
    def change_transfer(self, issue):
        temp = self.issue.get(issue)
        temp[2] = True
        self.issue.update({issue:temp})
        
    def show(self):
        nums = 1
        for key, value in self.issue.items():
            print(f'{nums}.{key} time:{value[0]} {'Выполнено'if value[1] else 'Не выполнено'} {'Перенесено'if value[2] else 'Не перенесено'}')
            nums +=1
            
todo = Todo()
todo.add_issue('Завтрак', '8:30', True, False)
todo.add_issue('Уборка', '10:00', False, False )
todo.add_issue('Корм. кот.', '12:30', False, False)
todo.show()
todo.change_issue('Уборка')
todo.show()



