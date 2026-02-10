mysql> SHOW DATABASES;

+--------------------+

| Database           |

+--------------------+

| information\_schema |

| mysql              |

| performance\_schema |

| sage               |

| sys                |

+--------------------+

5 rows in set (0.500 sec)



mysql> USE SAGE;

Database changed





mysql> SHOW TABLES

&nbsp;   -> ;

+----------------+

| Tables\_in\_sage |

+----------------+

| emp            |

+----------------+

1 row in set (0.482 sec)



mysql> SELECT\*FROM emp;

+------+----------+-------+----------+------+--------+---------+--------+---------+

| eNO  | NAME     | E\_ADD | MOBILE   | D\_NO | D\_NAME | SALARY  | JOB\_ID | ADDRESS |

+------+----------+-------+----------+------+--------+---------+--------+---------+

|    1 | ROHIT    |   198 | 82994322 |    3 | CSE    | 1000000 |     67 | NULL    |

|    2 | KRISH    |   103 |  6888798 |    3 | CSE    | 5000000 |     69 | NULL    |

|    3 | KIRTI    |   125 |  7309031 |    3 | CSE    | 3000000 |     68 | NULL    |

|    4 | DEEPTESH |    83 | 85218166 |    3 | CSE    | 4000000 |     70 | NULL    |

+------+----------+-------+----------+------+--------+---------+--------+---------+

4 rows in set (0.675 sec)



mysql> INSERT INTO emp(ADDRESS)

&nbsp;   -> VALUES ('BHOPAL');

Query OK, 1 row affected (0.481 sec)



mysql> SELECT\*FROM emp;

+------+----------+-------+----------+------+--------+---------+--------+---------+

| eNO  | NAME     | E\_ADD | MOBILE   | D\_NO | D\_NAME | SALARY  | JOB\_ID | ADDRESS |

+------+----------+-------+----------+------+--------+---------+--------+---------+

|    1 | ROHIT    |   198 | 82994322 |    3 | CSE    | 1000000 |     67 | NULL    |

|    2 | KRISH    |   103 |  6888798 |    3 | CSE    | 5000000 |     69 | NULL    |

|    3 | KIRTI    |   125 |  7309031 |    3 | CSE    | 3000000 |     68 | NULL    |

|    4 | DEEPTESH |    83 | 85218166 |    3 | CSE    | 4000000 |     70 | NULL    |

| NULL | NULL     |  NULL |     NULL | NULL | NULL   |    NULL |   NULL | BHOPAL  |

+------+----------+-------+----------+------+--------+---------+--------+---------+

5 rows in set (0.009 sec)



### USE OF UPDATE

mysql> UPDATE emp

&nbsp;   -> SET ADDRESS = 'BHOPAL';

Query OK, 4 rows affected (0.475 sec)

Rows matched: 5  Changed: 4  Warnings: 0



mysql> SELECT\*FROM emp;

+------+----------+-------+----------+------+--------+---------+--------+---------+

| eNO  | NAME     | E\_ADD | MOBILE   | D\_NO | D\_NAME | SALARY  | JOB\_ID | ADDRESS |

+------+----------+-------+----------+------+--------+---------+--------+---------+

|    1 | ROHIT    |   198 | 82994322 |    3 | CSE    | 1000000 |     67 | BHOPAL  |

|    2 | KRISH    |   103 |  6888798 |    3 | CSE    | 5000000 |     69 | BHOPAL  |

|    3 | KIRTI    |   125 |  7309031 |    3 | CSE    | 3000000 |     68 | BHOPAL  |

|    4 | DEEPTESH |    83 | 85218166 |    3 | CSE    | 4000000 |     70 | BHOPAL  |

| NULL | NULL     |  NULL |     NULL | NULL | NULL   |    NULL |   NULL | BHOPAL  |

+------+----------+-------+----------+------+--------+---------+--------+---------+

5 rows in set (0.007 sec)



mysql> DELETE FROM emp

&nbsp;   -> WHERE eNO IS NULL;

Query OK, 1 row affected (0.441 sec)



mysql> SELECT\*FROM emp;

+------+----------+-------+----------+------+--------+---------+--------+---------+

| eNO  | NAME     | E\_ADD | MOBILE   | D\_NO | D\_NAME | SALARY  | JOB\_ID | ADDRESS |

+------+----------+-------+----------+------+--------+---------+--------+---------+

|    1 | ROHIT    |   198 | 82994322 |    3 | CSE    | 1000000 |     67 | BHOPAL  |

|    2 | KRISH    |   103 |  6888798 |    3 | CSE    | 5000000 |     69 | BHOPAL  |

|    3 | KIRTI    |   125 |  7309031 |    3 | CSE    | 3000000 |     68 | BHOPAL  |

|    4 | DEEPTESH |    83 | 85218166 |    3 | CSE    | 4000000 |     70 | BHOPAL  |

+------+----------+-------+----------+------+--------+---------+--------+---------+

4 rows in set (0.007 sec)



### USE OF AVG to find average of values in a column



mysql> SELECT AVG(SALARY) AS Average\_Salary

&nbsp;   -> FROM emp;

+----------------+

| Average\_Salary |

+----------------+

|   3250000.0000 |

+----------------+

1 row in set (0.420 sec)



#### MAXIMUM SALARY

mysql> SELECT MAX(SALARY) AS Highest\_Salary FROM emp;

+----------------+

| Highest\_Salary |

+----------------+

|        5000000 |

+----------------+

1 row in set (0.010 sec)



#### MINIMUM SALARY

mysql> SELECT MIN(SALARY) AS Lowest\_Salary FROM emp;

+---------------+

| Lowest\_Salary |

+---------------+

|       1000000 |

+---------------+

1 row in set (0.009 sec)



#### TOTAL SALARY

mysql> SELECT SUM(SALARY) AS Total\_Salary FROM emp;

+--------------+

| Total\_Salary |

+--------------+

|     13000000 |

+--------------+

1 row in set (0.007 sec)



#### EMPLOYEE WITH SALARY MORE THAN AVERAGE

*MISTAKE*

mysql> SELECT NAME,SALARY

&nbsp;   -> FROM emp

&nbsp;   -> WHERE SALARY > (SALARY AVG(SALARY) FROM emp);

ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'AVG(SALARY) FROM emp)' at line 3



*CORRECT*

mysql> SELECT NAME,SALARY

&nbsp;   -> FROM emp

&nbsp;   -> WHERE SALARY > (SELECT AVG(SALARY) FROM emp);

+----------+---------+

| NAME     | SALARY  |

+----------+---------+

| KRISH    | 5000000 |

| DEEPTESH | 4000000 |

+----------+---------+

2 rows in set (0.403 sec)



