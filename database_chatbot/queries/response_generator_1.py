def response_generation(s,input_question):
    from django.db import connection
    with connection.cursor() as cursor:
        if s==-1:
            cursor.execute("SELECT * FROM table2")
            for x in cursor:
                if x[0]==input_question:
                    s2="Sorry, cannot understand the question from provided information."
                    return s2
            try:
                cursor.execute("INSERT INTO Unanswered_query(unanswered_query) VALUES(%s)",[input_question])
            except:
                pass
            s2="Sorry, cannot understand the question from provided information."
            return s2
        sql_query=("SELECT response from Query WHERE intent=%s")
        cursor.execute(sql_query,[s])
        for x in cursor:
            print(x)
            s1=x
        s2=''.join(s1)
    return s2
