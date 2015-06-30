__author__ = 'timmcatee'

'''the query will expect a dictionary of responses from the survey form using the django ORM.
This script parses the results, then feeds them into a SQL db filter of the cars database. '''

import mysql.connector

def cars_db_filter(q1,q2,q9,q10,q13,q14,q15,q16,q17):
    filtered_list = []
    q1 = parse_q1(q1)
    q2 = parse_q2(q2)
    q9 = parse_q9(q9)
    q10 = parse_q10(q10)
    q13 = parse_q13(q13)
    q14 = parse_q14(q14)
    q15 = parse_q15(q15)
    q16 = parse_q16(q16)
    q17low, q17high = parse_q17(q17)
    cnx = mysql.connector.connect(user='root',database='django_survey')
    cursor = cnx.cursor()
    # query built with a combination of connector syntax and python
    # cool thing about python is that if we don't need a filter, it's blank
    query = ("SELECT vname FROM cars WHERE (cityMPG BETWEEN %s AND %s)"
             +q1+q2+q9+q10+q13+q14+q15+q16)
    cursor.execute(query, (q17low,q17high))
    for vname in cursor:
        filtered_list.append(vname[0])
    cursor.close()
    cnx.close()
    print query
    return filtered_list

#added parsing questions since the cars db doesn't match question answers exactly
def parse_q1(q1):
    if q1 == "NO Type (returns all options)":
        q1 = ""
    elif q1 == "":
        q1 = ""
    else:
        q1 = (" AND (vtype='%s')" % q1)
    return q1

def parse_q2(q2):
    if q2 == "NO Sub-Type (returns all options)":
        q2 = ""
    elif q2 == "Crossover (a.k.a. Normal)":
        q2 = " AND (crossover='TRUE') "
    elif q2 == "Luxury":
        q2 = " AND (luxury='TRUE')"
    elif q2 == "Diesel":
        q2 = " AND (diesel='TRUE')"
    elif q2 == "Hybrid":
        q2 = " AND (hybrid='TRUE')"
    elif q2 == "Flexfuel":
        q2 = " AND (flexfuel='TRUE')"
    elif q2 == "Electric":
        q2 = " AND (electric='TRUE')"
    elif q2 == "Performance":
        q2 = " AND (performance='TRUE')"
    elif q2 == "Hatchback":
        q2 = " AND (hatchback='TRUE')"
    elif q2 == "Exotic":
        q2 = " AND (exotic='TRUE')"
    elif q2 == "Factory Tuner":
        q2 = " AND (factorytuner='TRUE')"
    else:
        q2 = ""
    return q2

def parse_q9(q9):
    if q9 == "Automatic":
        q9 = " AND (drivetype='Automatic') "
    elif q9 == "Automated Manual":
        q9 = " AND (drivetype='Automated Manual')"
    elif q9 == "Manual (stick shift)":
        q9 = " AND (drivetype='Manual')"
    elif q9 == "Direct Drive (Electric Vehicles)":
        q9 = " AND (drivetype='Direct Drive')"
    else:
        q9 = ""
    return q9

def parse_q10(q10):
    if q10 == "Yes - Only see vehicles with high consumer ratings":
        q10 = " AND (highrating>3) "
    elif q10 == "No - See all vehicles":
        q10 = ""
    else:
        q10 = ""
    return q10

def parse_q13(q13):
    if q13 == "ANY Price":
        q13 = ""
    elif q13 == "$11000 to $22499":
        q13 = " AND (pricerange='11000to22499') "
    elif q13 == "$22500 to $26499":
        q13 = " AND (pricerange='22500to26499') "
    elif q13 == "$26500 to $29999":
        q13 = " AND (pricerange='26500to29999') "
    elif q13 == "$30000 to $33499":
        q13 = " AND (pricerange='30000to33499') "
    elif q13 == "$33500 to $36799":
        q13 = " AND (pricerange='33500to36799') "
    elif q13 == "$36800 to $40499":
        q13 = " AND (pricerange='36800to40499') "
    elif q13 == "$40500 to $44799":
        q13 = " AND (pricerange='40500to44799') "
    elif q13 == "$44800 to $51299":
        q13 = " AND (pricerange='44800to51299') "
    elif q13 == "$51300 to $69999":
        q13 = " AND (pricerange='51300to69999') "
    elif q13 == "$70000 to $999999":
        q13 = " AND (pricerange='70000to999999') "
    else:
        q13 = ""
    return q13

def parse_q14(q14):
    if q14 == "Important (Above average)":
        q14 = " AND (hpimportance='Above')"
    elif q14 == "Not Important (Below average)":
        q14 = " AND (hpimportance='Below')"
    else:
        q14 = ""
    return q14

def parse_q15(q15):
    if q15 == "Important (Above average)":
        q15 = " AND (torqueimportance='Above')"
    elif q15 == "Not Important (Below average)":
        q15 = " AND (torqueimportance='Below')"
    else:
        q15 = ""
    return q15

def parse_q16(q16):
    if q16 == "Important (Above average)":
        q16 = " AND (resaleimportance='Above')"
    elif q16 == "Not Important (Below average)":
        q16 = " AND (resaleimportance='Below')"
    else:
        q16 = ""
    return q16

def parse_q17(q17):
    if q17 == "Electric cars only":
        q17low = 61
        q17high = 1000
    elif q17 == "35-60 MPG City":
        q17low = 35
        q17high = 60
    elif q17 == "20-34 MPG City":
        q17low = 20
        q17high = 34
    elif q17 == "< 20 MPG City":
        q17low = 1
        q17high = 19
    else:
        q17low = 0
        q17high = 1000
    return q17low, q17high

#UNIT TESTS

#debug fake answers to test cars_db_filter

def debug_cars():
    q1 = "NO Type (returns all options)"
    q2 = "Luxury"
    q9 = "Automatic"
    q10 = "Yes - Only see vehicles with high consumer ratings"
    q13 = "$40500 to $44799"
    q14 = "Important (Above average)"
    q15 = "Important (Above Average)"
    q16 = "Important (Above average)"
    q17 = "20-34 MPG City"

    print cars_db_filter(q1,q2,q9,q10,q13,q14,q15,q16,q17)

if __name__=="__main__":
    debug_cars()



