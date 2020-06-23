def response_generation(s,input_question):
    from django.db import connection
    with connection.cursor() as cursor:
        if s=="-1":
            try:
                cursor.execute("INSERT INTO table2(unanswered_query) VALUES(%s)",[input_question])
            except:
                pass
            s2="Sorry, cannot understand the question from provided information."
            return s2
        sql_query=("SELECT response from queries_query WHERE intent=%s")
        cursor.execute(sql_query,[s])
        for x in cursor:
            s1=x
        s2=''.join(s1)
    return s2
