Vim�UnDo� Rv�N�#�p�/�	=��i���G�,<����                     <       <   <   <    X�=�    _�                             ����                                                                                                                                                                                                                                                                                                                                                             X�;�     �               mselect a.cuisine from Dish a join Ingredients b on a.food=b.food where b.ingredient='cumin' group by cuisine;5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             X�;�     �               qsql=select a.cuisine from Dish a join Ingredients b on a.food=b.food where b.ingredient='cumin' group by cuisine;5�_�                       r    ����                                                                                                                                                                                                                                                                                                                                                             X�;�     �               rsql="select a.cuisine from Dish a join Ingredients b on a.food=b.food where b.ingredient='cumin' group by cuisine;5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             X�;�     �               cursor.execute5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             X�;�     �               cursor.execute(sql)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             X�;�     �               results=cursor.fetchall5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             X�;�     �               results=cursor.fetchall()5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                             X�;�     �               print5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                             X�;�     �               print()5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                             X�;�     �               print('b.answer: {}'.format)5�_�   
                    #    ����                                                                                                                                                                                                                                                                                                                                                             X�;�     �               %print('b.answer: {}'.format(results))5�_�                       $    ����                                                                                                                                                                                                                                                                                                                                                             X�;�    �               %print('b.answer: {}'.format(results))5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             X�;�     �                �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             X�;�     �                5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             X�;�     �               sqlList=5�_�                       	    ����                                                                                                                                                                                                                                                                                                                                                             X�;�     �               
sqlList=[]5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             X�;�     �                   cursor.execute5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             X�;�     �                   cursor.execute(sql)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             X�;�     �                   results=cursor.fetchall5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             X�;�     �                   results=cursor.fetchall()5�_�                       	    ����                                                                                                                                                                                                                                                                                                                                                             X�;�     �               	    print5�_�                       
    ����                                                                                                                                                                                                                                                                                                                                                             X�;�     �                   print()5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             X�;�     �               !    print('{}.answer: {}'.format)5�_�                       !    ����                                                                                                                                                                                                                                                                                                                                                             X�;�     �               #    print('{}.answer: {}'.format())5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             X�;�    �                   results=cursor.fetchall()5�_�                       
    ����                                                                                                                                                                                                                                                                                                                                                             X�=     �               
sqlList=[]5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             X�=     �               QNo=ord5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             X�=     �               	QNo=ord()5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             X�=      �               for sql in sqlList:�               QNo=ord('a')5�_�                       !    ����                                                                                                                                                                                                                                                                                                                                                             X�=*     �               #    print('{}.answer: {}'.format())5�_�                        $    ����                                                                                                                                                                                                                                                                                                                                                             X�=+     �               &    print('{}.answer: {}'.format(chr))5�_�      !                  &    ����                                                                                                                                                                                                                                                                                                                                                             X�=+     �               )    print('{}.answer: {}'.format(chr(i)))5�_�       "           !      (    ����                                                                                                                                                                                                                                                                                                                                                             X�=0     �               *    print('{}.answer: {}'.format(chr(QNo))5�_�   !   #           "      1    ����                                                                                                                                                                                                                                                                                                                                                             X�=7     �               2    print('{}.answer: {}'.format(chr(QNo),results)5�_�   "   $           #          ����                                                                                                                                                                                                                                                                                                                                                             X�=C     �                   inc5�_�   #   %           $          ����                                                                                                                                                                                                                                                                                                                                                             X�=E    �                   inc(QNo)5�_�   $   &           %      	    ����                                                                                                                                                                                                                                                                                                                                         P       v���    X�=k     �               
sqlList=[]5�_�   %   '           &           ����                                                                                                                                                                                                                                                                                                                                         P       v���    X�=o     �                   �             5�_�   &   (           '          ����                                                                                                                                                                                                                                                                                                                                         P       v���    X�=s     �                   �             5�_�   '   )           (          ����                                                                                                                                                                                                                                                                                                                                         P       v���    X�=z     �               M    select food from Ingredients where ingredient='butter' and quantity>16'''5�_�   (   *           )      N    ����                                                                                                                                                                                                                                                                                                                                         P       v���    X�=}     �               N    "select food from Ingredients where ingredient='butter' and quantity>16'''5�_�   )   +           *          ����                                                                                                                                                                                                                                                                                                                                         P       v���    X�=�     �               	sqlList=[5�_�   *   ,           +           ����                                                                                                                                                                                                                                                                                                                                         r       v���    X�=�     �                �             5�_�   +   -           ,           ����                                                                                                                                                                                                                                                                                                                                         r       v���    X�=�     �               n"select a.cuisine from Dish a join Ingredients b on a.food=b.food where b.ingredient='cumin' group by cuisine"5�_�   ,   .           -           ����                                                                                                                                                                                                                                                                                                                                         r       v���    X�=�     �                 5�_�   -   /           .           ����                                                                                                                                                                                                                                                                                                                                         r       v���    X�=�    �                 5�_�   .   0           /           ����                                                                                                                                                                                                                                                                                                                                         r       v���    X�=�     �                    inc(QNo)5�_�   /   1           0           ����                                                                                                                                                                                                                                                                                                                                         r       v���    X�=�     �                �             5�_�   0   2           1           ����                                                                                                                                                                                                                                                                                                                                         r       v���    X�=�    �                5�_�   1   3           2           ����                                                                                                                                                                                                                                                                                                                                         r       v���    X�=�     �                Psql='''select food from Ingredients where ingredient='butter' and quantity>16'''5�_�   2   4           3           ����                                                                                                                                                                                                                                                                                                                                         r       v���    X�=�     �                cursor.execute(sql)5�_�   3   5           4           ����                                                                                                                                                                                                                                                                                                                            
          
   r       v���    X�=�     �                results=cursor.fetchall()5�_�   4   6           5           ����                                                                                                                                                                                                                                                                                                                            	          	   r       v���    X�=�     �                %print('a.answer: {}'.format(results))5�_�   5   7           6           ����                                                                                                                                                                                                                                                                                                                                         r       v���    X�=�     �                 5�_�   6   8           7           ����                                                                                                                                                                                                                                                                                                                                         r       v���    X�=�     �                rsql="select a.cuisine from Dish a join Ingredients b on a.food=b.food where b.ingredient='cumin' group by cuisine"5�_�   7   9           8           ����                                                                                                                                                                                                                                                                                                                                         r       v���    X�=�     �                cursor.execute(sql)5�_�   8   :           9           ����                                                                                                                                                                                                                                                                                                                                         r       v���    X�=�     �                results=cursor.fetchall()5�_�   9   ;           :           ����                                                                                                                                                                                                                                                                                                                                         r       v���    X�=�     �                %print('b.answer: {}'.format(results))5�_�   :   <           ;           ����                                                                                                                                                                                                                                                                                                                                         r       v���    X�=�     �                 5�_�   ;               <           ����                                                                                                                                                                                                                                                                                                                                         r       v���    X�=�    �                 5��