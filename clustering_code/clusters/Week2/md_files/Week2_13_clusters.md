#Problem 13

    $coins=random(9,11,1); # number of tosses of the dice

    ## Tossing a coin ##
    A fair coin is tossed [$coins] times.
    o  There is a natural outcome space for the experiment of tossing coins in sequence, where the probability of each outcome is equally likely.  What is the size of this outcome space? [______]{Compute("2^$coins")}
    o  What is the size of the event set for getting exactly [$coins-1] heads?  [______]{Compute("$coins!/($coins-1)!")}
    o  What is the probability of getting exactly [$coins-1] heads? [_________]{Compute("($coins!/($coins-1)!)/2^$coins")}
    o  What is the probability of getting at most [$coins-1] heads? [________]{Compute("1-1/2^$coins")}
    o  What is the probability of getting exactly 6 heads?  [______________]{Compute("($coins!/(6!($coins-6)!))/2^$coins")}



## Part 1

### (292) Mistake Group Digits of size 292




### (6) Mistake Group ['R.1'] of size 6
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|2^10	|4*10	|[('R.1', 10.0, u'10', u'10')]	|
|1	|2^10	|3*10	|[('R.1', 10.0, u'10', u'10')]	|
|2	|2^11	|4^11	|[('R.1', 11.0, u'11', u'11')]	|
|3	|2^9	|8^9	|[('R.1', 9.0, u'9', u'9')]	|




### (5) Mistake Group Fraction of size 5




### (2) Mistake Group ['R.0'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|2^9	|2^81	|[('R.0', 2.0, u'2', u'2')]	|
|1	|2^9	|2^11	|[('R.0', 2.0, u'2', u'2')]	|




### (1) Mistake Group ['R.0', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|2^10	|2*10	|[('R.0', 2.0, u'2', u'2'), ('R.1', 10.0, u'10', u'10')]	|




### (24) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:a8ho

	first_attempt
					2015-10-07 05:49:11
	part1_incorrect_attempt
					('0:00:00', u'10^2')
	part1_correct_attempt
					['0:11:02', u'2^10']

1 Student ID:druble

	first_attempt
					2015-10-08 20:48:25
	part1_incorrect_attempt
					('0:00:00', u'11^2')
	part1_correct_attempt
					['0:00:50', u'2^11']

2 Student ID:jjchung

	first_attempt
					2015-10-08 05:10:39
	part1_incorrect_attempt
					('0:00:00', u'11*11')
					('0:01:08', u'11!')
	part1_correct_attempt
					['1:13:13', u'2^11']

3 Student ID:ssamudra

	first_attempt
					2015-10-08 07:52:33
	part1_incorrect_attempt
					('0:00:00', u'11^11')
	part1_correct_attempt
					['0:00:07', u'2^11']

4 Student ID:abjara

	first_attempt
					2015-10-05 22:29:23
	part1_incorrect_attempt
					('0:00:00', u'11**2')
	part1_correct_attempt
					['0:05:28', u'2**11']

5 Student ID:any027

	first_attempt
					2015-10-03 10:48:59
	part1_incorrect_attempt
					('0:00:00', u'11!')
	part1_correct_attempt
					['0:00:51', u'2^11']

6 Student ID:kthui

	first_attempt
					2015-10-04 06:58:52
	part1_incorrect_attempt
					('0:00:00', u'11!')
					('0:02:52', u'11*11')
	part1_correct_attempt
					['0:05:19', u'2^11']

7 Student ID:vsosnovs

	first_attempt
					2015-10-04 17:38:59
	part1_incorrect_attempt
					('0:00:00', u'9^2')
	part1_correct_attempt
					['0:01:36', u'2^9']

8 Student ID:mbl003

	first_attempt
					2015-10-02 20:51:23
	part1_incorrect_attempt
					('0:00:00', u'10^2')
					('0:04:40', u'10^2')
	part1_correct_attempt
					['10:06:20', u'2^10']

9 Student ID:amquinte

	first_attempt
					2015-10-05 22:17:37
	part1_incorrect_attempt
					('0:00:00', u'11!2')
					('0:01:20', u'11!')
	part1_correct_attempt
					['0:02:11', u'2048']

10 Student ID:mnrahman

	first_attempt
					2015-10-08 02:42:43
	part1_incorrect_attempt
					('0:00:00', u'10!/9!')
					('0:00:51', u'10!/9!')
					('0:01:17', u'10!/9!')
					('0:01:55', u'10!/9!')
					('0:02:08', u'10!/9!')
					('0:02:56', u'10^2')
	part1_correct_attempt
					['0:03:07', u'2^10']

11 Student ID:s6deng

	first_attempt
					2015-10-06 21:01:29
	part1_incorrect_attempt
					('0:00:00', u'10^2')
	part1_correct_attempt
					['0:04:14', u'2^10']

12 Student ID:akhmelni

	first_attempt
					2015-10-08 21:41:09
	part1_incorrect_attempt
					('0:00:00', u'9^2')
	part1_correct_attempt
					['0:01:19', u'2^9']

13 Student ID:jhw015

	first_attempt
					2015-10-04 02:49:52
	part1_incorrect_attempt
					('0:00:00', u'P(9,2)')
	part1_correct_attempt
					['0:03:29', u'2^9']

14 Student ID:hah008

	first_attempt
					2015-10-08 06:27:43
	part1_incorrect_attempt
					('0:00:00', u'9^2')
	part1_correct_attempt
					['0:07:28', u'2^9']

15 Student ID:sayao

	first_attempt
					2015-10-03 00:24:44
	part1_incorrect_attempt
					('0:00:00', u'11^4')
	part1_correct_attempt
					['0:00:20', u'2^11']

16 Student ID:achava

	first_attempt
					2015-10-02 05:03:10
	part1_incorrect_attempt
					('0:00:00', u'11*11')
					('0:00:39', u'11^2')
					('0:00:59', u'11^3')
					('0:02:05', u'11^11')
					('0:04:23', u'11!')
					('0:04:55', u'11!*11!')
	part1_correct_attempt
					['0:06:08', u'2^11']

17 Student ID:hmshah

	first_attempt
					2015-10-06 01:52:02
	part1_incorrect_attempt
					('0:00:00', u'11*11')
	part1_correct_attempt
					['0:00:49', u'2^11']

18 Student ID:wcwhite

	first_attempt
					2015-10-06 19:10:30
	part1_incorrect_attempt
					('0:00:00', u'11^2')
					('0:00:08', u'11*11')
					('0:00:16', u'11+11')
					('0:00:45', u'11!')
					('0:01:02', u'11!/(2!(11-2)!)')
					('0:01:21', u'11!/(4!(11-4)!)')
					('0:00:00', u'11!/2!')
					('0:00:15', u'11!/4!')
					('0:00:20', u'2!')
					('0:00:24', u'11!')
	part1_correct_attempt
					['7:37:30', u'2^11']

19 Student ID:c1wei

	first_attempt
					2015-10-08 07:38:25
	part1_incorrect_attempt
					('0:00:00', u'9^9')
	part1_correct_attempt
					['0:06:10', u'2^9']

20 Student ID:edcole

	first_attempt
					2015-10-04 22:11:06
	part1_incorrect_attempt
					('0:00:00', u'11*2')
	part1_correct_attempt
					['1 day, 19:23:04', u'2^11']

21 Student ID:vasharma

	first_attempt
					2015-10-05 06:20:38
	part1_incorrect_attempt
					('0:00:00', u'10^10')
					('0:00:05', u'10!')
					('0:32:01', u'10!/(10-2)!')
					('0:32:14', u'10!/(10-8)!')
	part1_correct_attempt
					['0:32:38', u'2^10']

22 Student ID:lalacson

	first_attempt
					2015-10-03 15:21:32
	part1_incorrect_attempt
					('0:00:00', u'11!')
					('0:01:33', u'P(11,2)')
					('0:01:54', u'11!/((11-2)!)')
					('0:02:22', u'11*4')
	part1_correct_attempt
					['0:02:41', u'2^11']

23 Student ID:xweng

	first_attempt
					2015-10-07 07:00:24
	part1_incorrect_attempt
					('0:00:00', u'9^2')
	part1_correct_attempt
					['0:00:39', u'2^9']












## Part 2

### (209) Mistake Group Digits of size 209




### (98) Mistake Group Fraction of size 98




### (5) Mistake Group ['R.0'] of size 5
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|11!/(11-1)!	|11!/(4!(11-4)!)	|[('R.0', 39916800, u'11!', u'11!')]	|
|1	|11!/(11-1)!	|11!/10	|[('R.0', 39916800, u'11!', u'11!')]	|
|2	|9!/(9-1)!	|9!/(2!(9-2)!)	|[('R.0', 362880, u'9!', u'9!')]	|
|3	|9!/(9-1)!	|(9!)/((9-2)!)	|[('R.0', 362880, u'9!', u'9!')]	|
|4	|9!/(9-1)!	|(9!)/(2!(9-2)!)	|[('R.0', 362880, u'9!', u'9!')]	|




### (1) Mistake Group Wrong_Sign of size 1




### (1) Mistake Group ['R.0', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|10!/(10-1)!	|10!/9!	|[('R.0', 3628800, u'10!', u'10!'), ('R.1', 362880, u'(10-1)!', u'9!')]	|




### (59) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:a8ho

	first_attempt
					2015-10-07 06:00:13
	part2_incorrect_attempt
					('0:00:32', u'2^10')
					('0:00:38', u'2^9')
	part2_correct_attempt
					['0:11:19', u'10']

1 Student ID:dmn009

	first_attempt
					2015-10-08 09:33:03
	part2_incorrect_attempt
					('0:00:10', u'2^10')

2 Student ID:kew017

	first_attempt
					2015-10-04 19:42:44
	part2_incorrect_attempt
					('0:15:26', u'2*11')
	part2_correct_attempt
					['0:23:37', u'11']

3 Student ID:hmshah

	first_attempt
					2015-10-06 01:52:51
	part2_incorrect_attempt
					('0:12:25', u'10!')
	part2_correct_attempt
					['0:13:31', u'11']

4 Student ID:lpettit

	first_attempt
					2015-10-06 02:52:20
	part2_incorrect_attempt
					('0:28:22', u'2^10')
	part2_correct_attempt
					['0:37:47', u'11']

5 Student ID:agoldsht

	first_attempt
					2015-10-06 23:09:31
	part2_incorrect_attempt
					('0:15:59', u'10!')
	part2_correct_attempt
					['0:19:06', u'(11!/10!)']

6 Student ID:ctroncos

	first_attempt
					2015-10-08 05:42:25
	part2_incorrect_attempt
					('0:01:38', u'10!')
	part2_correct_attempt
					['0:02:53', u'11']

7 Student ID:glcohen

	first_attempt
					2015-10-04 22:55:55
	part2_incorrect_attempt
					('0:02:08', u'2^9')
	part2_correct_attempt
					['0:13:34', u'(10!)/(9!(10-9)!)']

8 Student ID:acvuong

	first_attempt
					2015-10-04 00:17:26
	part2_incorrect_attempt
					('-1 day, 23:57:47', u'2^8')
					('0:00:00', u'C(9,8)')
	part2_correct_attempt
					['0:01:31', u'9']

9 Student ID:any027

	first_attempt
					2015-10-03 10:49:50
	part2_incorrect_attempt
					('0:03:28', u'2^11 - 2^10')
					('0:23:20', u'2^10')
	part2_correct_attempt
					['14:36:10', u'(11!/ (1! * 10!))']

10 Student ID:jjm019

	first_attempt
					2015-10-08 01:43:02
	part2_incorrect_attempt
					('0:02:53', u'2^8')
	part2_correct_attempt
					['0:34:31', u'9']

11 Student ID:sachadal

	first_attempt
					2015-10-05 18:52:40
	part2_incorrect_attempt
					('0:02:14', u'C(10,9)')
	part2_correct_attempt
					['0:07:23', u'10']

12 Student ID:pcdo

	first_attempt
					2015-10-06 19:56:42
	part2_incorrect_attempt
					('0:00:00', u'2^10')
					('0:10:58', u'10!2!')
					('0:12:07', u'C(11,10)')
					('0:21:04', u'10!/10')
					('0:24:40', u'2^11')
					('0:25:32', u'C(11, 10)')
	part2_correct_attempt
					['0:26:04', u'11']

13 Student ID:e9brown

	first_attempt
					2015-10-08 02:09:24
	part2_incorrect_attempt
					('-1 day, 23:58:48', u'C(11,10)')
	part2_correct_attempt
					['-1 day, 23:59:47', u'11']

14 Student ID:vsosnovs

	first_attempt
					2015-10-04 17:40:35
	part2_incorrect_attempt
					('0:02:35', u'(2^9)/(2)')
	part2_correct_attempt
					['0:20:15', u'9!/8!']

15 Student ID:b1green

	first_attempt
					2015-10-08 06:08:57
	part2_incorrect_attempt
					('0:05:35', u'P(11,10)')
	part2_correct_attempt
					['12:59:54', u'11']

16 Student ID:nhn018

	first_attempt
					2015-10-07 03:00:39
	part2_incorrect_attempt
					('0:00:00', u'2^9')
					('0:27:51', u'2^10')
					('0:34:17', u'2^9')
					('0:40:10', u'2^9')
	part2_correct_attempt
					['0:41:48', u'10']

17 Student ID:n2patil

	first_attempt
					2015-10-06 15:47:55
	part2_incorrect_attempt
					('0:00:33', u'2^10')
	part2_correct_attempt
					['1 day, 13:30:58', u'11']

18 Student ID:kthui

	first_attempt
					2015-10-04 07:04:11
	part2_incorrect_attempt
					('0:03:36', u'2^10*11')
					('0:07:04', u'C(11, 10)')
	part2_correct_attempt
					['0:07:22', u'11!/((11-10)!10!)']

19 Student ID:gsrandha

	first_attempt
					2015-10-02 02:24:47
	part2_incorrect_attempt
					('0:00:22', u'2^8')
	part2_correct_attempt
					['0:08:19', u'9']

20 Student ID:ttimmons

	first_attempt
					2015-10-02 19:39:22
	part2_incorrect_attempt
					('0:00:00', u'2^8')
					('0:00:56', u'C(2^9,8)')
					('0:01:37', u'C(9,8)')
	part2_correct_attempt
					['0:02:07', u'[9!]/[8!*(9-8)!]']

21 Student ID:dcastlem

	first_attempt
					2015-10-03 21:42:23
	part2_incorrect_attempt
					('0:17:31', u'9!')
	part2_correct_attempt
					['0:18:33', u'10!/9!']

22 Student ID:rlhagen

	first_attempt
					2015-10-04 22:41:32
	part2_incorrect_attempt
					('0:00:00', u'9!/(9-8)!')
	part2_correct_attempt
					['0:02:03', u'(9!)/8!(9-8)!']

23 Student ID:btn023

	first_attempt
					2015-10-02 01:49:20
	part2_incorrect_attempt
					('0:00:00', u'C(9,8)')
	part2_correct_attempt
					['0:01:01', u'9']

24 Student ID:v3doan

	first_attempt
					2015-10-04 00:02:45
	part2_incorrect_attempt
					('0:00:00', u'2^9')
	part2_correct_attempt
					['0:00:31', u'10']

25 Student ID:ielouaae

	first_attempt
					2015-10-08 23:17:41
	part2_incorrect_attempt
					('0:00:26', u'2^10')
					('0:01:55', u'2^11')
					('0:04:58', u'2^10')
	part2_correct_attempt
					['0:07:20', u'11']

26 Student ID:jcl084

	first_attempt
					2015-10-08 19:25:12
	part2_incorrect_attempt
					('0:00:00', u'2^9')
					('0:00:57', u'2^10 - 2')
	part2_correct_attempt
					['0:02:58', u'10']

27 Student ID:skodigal

	first_attempt
					2015-10-08 00:45:33
	part2_incorrect_attempt
					('0:00:58', u'C(10,9)')
	part2_correct_attempt
					['0:03:11', u'10']

28 Student ID:rraiyyan

	first_attempt
					2015-10-06 06:46:36
	part2_incorrect_attempt
					('0:00:00', u'10!/(2!*8!)')
	part2_correct_attempt
					['0:03:35', u'11!/(10!*1!)']

29 Student ID:hachrist

	first_attempt
					2015-10-02 19:51:04
	part2_incorrect_attempt
					('2 days, 2:22:45', u'2^8')
	part2_correct_attempt
					['2 days, 8:23:35', u'9!/(8!)']

30 Student ID:jhw015

	first_attempt
					2015-10-04 02:53:21
	part2_incorrect_attempt
					('0:07:17', u'8^2')
					('0:08:54', u'2^8')
					('0:10:11', u'8^9')
					('0:12:30', u'C(9,8)')
	part2_correct_attempt
					['0:12:48', u'9']

31 Student ID:dsmonaha

	first_attempt
					2015-10-05 18:33:47
	part2_incorrect_attempt
					('0:06:37', u'9!')
					('0:07:29', u'2^8')
	part2_correct_attempt
					['0:08:03', u'9']

32 Student ID:tcn013

	first_attempt
					2015-10-06 00:57:02
	part2_incorrect_attempt
					('-1 day, 23:59:29', u'2^10')
	part2_correct_attempt
					['0:00:13', u'11']

33 Student ID:kmc012

	first_attempt
					2015-10-05 07:50:52
	part2_incorrect_attempt
					('2 days, 21:56:26', u'2^10')
					('2 days, 21:56:32', u'2^11')
	part2_correct_attempt
					['2 days, 21:57:13', u'11']

34 Student ID:hah008

	first_attempt
					2015-10-08 06:35:11
	part2_incorrect_attempt
					('0:02:12', u'2^8')
					('0:27:32', u'2^8')
	part2_correct_attempt
					['0:47:58', u'9']

35 Student ID:cprafull

	first_attempt
					2015-10-06 19:24:57
	part2_incorrect_attempt
					('0:00:11', u'2^10')
	part2_correct_attempt
					['0:00:38', u'11']

36 Student ID:daw023

	first_attempt
					2015-10-03 08:19:29
	part2_incorrect_attempt
					('0:00:00', u'2^11-2^10-1')
	part2_correct_attempt
					['19:20:57', u'11']

37 Student ID:thwan

	first_attempt
					2015-10-04 00:06:24
	part2_incorrect_attempt
					('0:01:37', u'2^10-1')
					('1 day, 16:12:36', u'1^(9)*2^(1)')
					('1 day, 16:14:15', u'2*9!/8!')
	part2_correct_attempt
					['1 day, 16:21:21', u'10!/9!']

38 Student ID:q3wen

	first_attempt
					2015-10-07 07:23:37
	part2_incorrect_attempt
					('0:00:00', u'2^9')
	part2_correct_attempt
					['0:01:10', u'10']

39 Student ID:lguintu

	first_attempt
					2015-10-06 16:52:34
	part2_incorrect_attempt
					('0:00:00', u'C(10,9)')
	part2_correct_attempt
					['0:00:52', u'10']

40 Student ID:fichoi

	first_attempt
					2015-10-06 21:42:14
	part2_incorrect_attempt
					('0:01:27', u'C(10,9)')
	part2_correct_attempt
					['0:03:40', u'10']

41 Student ID:wcwhite

	first_attempt
					2015-10-07 02:48:00
	part2_incorrect_attempt
					('0:01:11', u'.5*10')
					('0:01:24', u'11!')
	part2_correct_attempt
					['0:05:48', u'11']

42 Student ID:tdurrer

	first_attempt
					2015-10-04 03:04:55
	part2_incorrect_attempt
					('0:00:00', u'C(2048, 10)')
	part2_correct_attempt
					['0:13:40', u'11']

43 Student ID:cstringh

	first_attempt
					2015-10-04 00:02:56
	part2_incorrect_attempt
					('0:01:54', u'2^9+2')
					('0:02:02', u'2^9')
					('0:02:20', u'9+2')
					('0:02:50', u'10!')
					('0:03:00', u'9!')
	part2_correct_attempt
					['0:03:12', u'10']

44 Student ID:edcole

	first_attempt
					2015-10-06 17:34:10
	part2_incorrect_attempt
					('-2 days, 4:35:45', u'11*2')
					('0:00:00', u'2^10')
					('0:02:26', u'2^11')
	part2_correct_attempt
					['0:02:55', u'11']

45 Student ID:rbdoming

	first_attempt
					2015-10-02 21:11:01
	part2_incorrect_attempt
					('0:00:00', u'C(9,8)')
	part2_correct_attempt
					['0:02:26', u'9']

46 Student ID:aurodrig

	first_attempt
					2015-10-07 04:38:05
	part2_incorrect_attempt
					('0:09:40', u'2^8')
	part2_correct_attempt
					['0:38:57', u'9']

47 Student ID:druble

	first_attempt
					2015-10-08 20:49:15
	part2_incorrect_attempt
					('0:18:10', u'C(11, 10)')
	part2_correct_attempt
					['0:27:46', u'11']

48 Student ID:yjshin

	first_attempt
					2015-10-07 07:48:44
	part2_incorrect_attempt
					('-1 day, 23:57:39', u'2^9')
					('-1 day, 23:57:43', u'2^10')
	part2_correct_attempt
					['0:00:37', u'10']

49 Student ID:aportuga

	first_attempt
					2015-10-06 05:36:44
	part2_incorrect_attempt
					('0:01:00', u'2^9')
					('0:02:47', u'2^10')
	part2_correct_attempt
					['0:10:01', u'10']

50 Student ID:arvenega

	first_attempt
					2015-10-08 04:49:12
	part2_incorrect_attempt
					('0:00:11', u'2^10')
	part2_correct_attempt
					['0:07:59', u'11']

51 Student ID:hsc052

	first_attempt
					2015-10-08 04:59:09
	part2_incorrect_attempt
					('0:00:00', u'8!/[1!(8-1)!]')
	part2_correct_attempt
					['0:00:18', u'9!/[1!(9-1)!]']

52 Student ID:lcardoso

	first_attempt
					2015-10-08 05:57:54
	part2_incorrect_attempt
					('0:00:00', u'(1^9)*2')
					('0:02:50', u'(1^9)*(1^(10-9))')
	part2_correct_attempt
					['0:20:00', u'10']

53 Student ID:ajvanega

	first_attempt
					2015-10-02 21:17:52
	part2_incorrect_attempt
					('0:01:33', u'2^10')
	part2_correct_attempt
					['0:03:12', u'11']

54 Student ID:hmnaing

	first_attempt
					2015-10-07 02:45:21
	part2_incorrect_attempt
					('16:46:00', u'10* C(2,1)')
					('16:46:29', u'10*( C(2,1))')
	part2_correct_attempt
					['21:20:36', u'11']

55 Student ID:mjethani

	first_attempt
					2015-10-04 23:03:15
	part2_incorrect_attempt
					('0:15:28', u'(2^11)-11')
	part2_correct_attempt
					['0:16:35', u'11']

56 Student ID:syc078

	first_attempt
					2015-10-08 22:37:44
	part2_incorrect_attempt
					('0:16:41', u'2^10')
	part2_correct_attempt
					['0:38:26', u'11']

57 Student ID:whcombs

	first_attempt
					2015-10-07 18:57:17
	part2_incorrect_attempt
					('0:07:22', u'8!/(2!(8-2)!)')
	part2_correct_attempt
					['0:20:10', u'(9!)/(1!(9-1)!)']

58 Student ID:asp025

	first_attempt
					2015-10-08 15:57:20
	part2_incorrect_attempt
					('0:47:36', u'10!')
					('0:47:46', u'9!')
	part2_correct_attempt
					['1:23:52', u'10']












## Part 3

### (86) Mistake Group ['R.1'] of size 86
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|10!/(10-1)!/(2^10)	|9/(2^10)	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|1	|9!/(9-1)!/(2^9)	|2/(2**9)	|[('R.1', 512.0, u'2^9', u'2**9')]	|
|2	|10!/(10-1)!/(2^10)	|2/2^10	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|3	|10!/(10-1)!/(2^10)	|1/2^10	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|4	|9!/(9-1)!/(2^9)	|1/(2^9)	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|5	|11!/(11-1)!/(2^11)	|2/2048	|[('R.1', 2048.0, u'2^11', u'2048')]	|
|6	|10!/(10-1)!/(2^10)	|2/1024	|[('R.1', 1024.0, u'2^10', u'1024')]	|
|7	|9!/(9-1)!/(2^9)	|1/512	|[('R.1', 512.0, u'2^9', u'512')]	|
|8	|9!/(9-1)!/(2^9)	|(2^8)/(2^9)	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|9	|11!/(11-1)!/(2^11)	|2/(2^11)	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|10	|11!/(11-1)!/(2^11)	| (2^11-2^10-1)/2^11	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|11	|10!/(10-1)!/(2^10)	|1/1024	|[('R.1', 1024.0, u'2^10', u'1024')]	|
|12	|11!/(11-1)!/(2^11)	|10/(2^11)	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|13	|11!/(11-1)!/(2^11)	|1/2^11	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|14	|10!/(10-1)!/(2^10)	|9/1024	|[('R.1', 1024.0, u'2^10', u'1024')]	|
|15	|9!/(9-1)!/(2^9)	|1/2^9	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|16	|10!/(10-1)!/(2^10)	|2^9/2^10	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|17	|11!/(11-1)!/(2^11)	|C(2048,10)/2048	|[('R.1', 2048.0, u'2^11', u'2048')]	|
|18	|11!/(11-1)!/(2^11)	|1/(2^11)	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|19	|11!/(11-1)!/(2^11)	|22/(2^11)	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|20	|9!/(9-1)!/(2^9)	|9!/(9-8)!/2^9	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|21	|11!/(11-1)!/(2^11)	|2/2^11	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|22	|9!/(9-1)!/(2^9)	|2/(2^9)	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|23	|10!/(10-1)!/(2^10)	|(1/9)^9/2^10	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|24	|9!/(9-1)!/(2^9)	|8/512	|[('R.1', 512.0, u'2^9', u'512')]	|
|25	|10!/(10-1)!/(2^10)	|1/[2^(10)]	|[('R.1', 1024.0, u'2^10', u'2^(10)')]	|
|26	|10!/(10-1)!/(2^10)	|2/(2^10)	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|27	|11!/(11-1)!/(2^11)	|1/2048	|[('R.1', 2048.0, u'2^11', u'2048')]	|
|28	|9!/(9-1)!/(2^9)	|((2^9)-9)/(2^9)	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|29	|10!/(10-1)!/(2^10)	|1/(2^10)	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|30	|11!/(11-1)!/(2^11)	|(10!/(2!*8!))/(2^11)	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|31	|11!/(11-1)!/(2^11)	|2^10/2^11	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|32	|11!/(11-1)!/(2^11)	|(2^10)/(2^11)	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|33	|9!/(9-1)!/(2^9)	|2/512	|[('R.1', 512.0, u'2^9', u'512')]	|
|34	|9!/(9-1)!/(2^9)	|2/2^9	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|35	|10!/(10-1)!/(2^10)	|18/(2^10)	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|36	|10!/(10-1)!/(2^10)	|10*2^10/2^10	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|37	|11!/(11-1)!/(2^11)	|100/(2^11)	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|38	|9!/(9-1)!/(2^9)	|36/(2^9)	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|39	|9!/(9-1)!/(2^9)	|72/(2^9)	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|40	|9!/(9-1)!/(2^9)	|28/(2^9)	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|41	|11!/(11-1)!/(2^11)	|10/2^11	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|42	|9!/(9-1)!/(2^9)	|8/(2^9)	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|43	|9!/(9-1)!/(2^9)	|((1/2)^8)/(2^9)	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|44	|9!/(9-1)!/(2^9)	|((1/2)*8)/(2^9)	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|45	|9!/(9-1)!/(2^9)	|(1/2)^8/(2^9)	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|46	|10!/(10-1)!/(2^10)	|[(1^9)*(2^(10-9))]/[2^10]	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|47	|9!/(9-1)!/(2^9)	|45/512	|[('R.1', 512.0, u'2^9', u'512')]	|
|48	|10!/(10-1)!/(2^10)	|9/2^10	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|49	|10!/(10-1)!/(2^10)	|10!/2^10	|[('R.1', 1024.0, u'2^10', u'2^10')]	|




### (50) Mistake Group redirect of size 50




### (13) Mistake Group Digits of size 13




### (6) Mistake Group ['R.1.0'] of size 6
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|9!/(9-1)!/(2^9)	|1/(2^8)	|[('R.1.0', 2.0, u'2', u'2')]	|
|1	|11!/(11-1)!/(2^11)	|1/(2^10)	|[('R.1.0', 2.0, u'2', u'2')]	|
|2	|10!/(10-1)!/(2^10)	|18/(2^9)	|[('R.1.0', 2.0, u'2', u'2')]	|
|3	|10!/(10-1)!/(2^10)	|1/(2^9)	|[('R.1.0', 2.0, u'2', u'2')]	|
|4	|10!/(10-1)!/(2^10)	|10/(2^9)	|[('R.1.0', 2.0, u'2', u'2')]	|
|5	|9!/(9-1)!/(2^9)	|1/2^8	|[('R.1.0', 2.0, u'2', u'2')]	|




### (3) Mistake Group ['R.0.0', 'R.1'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|9!/(9-1)!/(2^9)	|((9!)/((8!)(2!)))/(2^9)	|[('R.0.0', 362880, u'9!', u'9!'), ('R.1', 512.0, u'2^9', u'2^9')]	|
|1	|10!/(10-1)!/(2^10)	|((10!)/(9!(10!-9!)))/1024	|[('R.0.0', 3628800, u'10!', u'10!'), ('R.1', 1024.0, u'2^10', u'1024')]	|
|2	|11!/(11-1)!/(2^11)	|(11!/(4!(11-4)!))/2^11	|[('R.0.0', 39916800, u'11!', u'11!'), ('R.1', 2048.0, u'2^11', u'2^11')]	|




### (1) Mistake Group ['R.0.1.0', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|10!/(10-1)!/(2^10)	|10*9^2/2^10	|[('R.0.1.0', 9.0, u'10-1', u'9'), ('R.1', 1024.0, u'2^10', u'2^10')]	|




### (17) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:jtfrankl

	first_attempt
					2015-10-07 23:40:21
	part1_correct_attempt
					['0:00:00', u'2**11']
	part2_correct_attempt
					['0:00:37', u'11']
	part3_incorrect_attempt
					('0:01:03', u'(1/2)**11')
					('0:01:22', u'(1/2)**19')
					('0:01:29', u'(1/2)**10')
	part3_correct_attempt
					['2:55:15', u'11*(1/2)**11']

1 Student ID:msaguiar

	first_attempt
					2015-10-06 04:23:45
	part1_correct_attempt
					['0:00:00', u'(2^9)']
	part2_correct_attempt
					['0:00:30', u'9']
	part3_incorrect_attempt
					('0:02:31', u'9*((1/2)^8)')
	part3_correct_attempt
					['0:21:32', u'9/(2^9)']

2 Student ID:cstringh

	first_attempt
					2015-10-04 00:02:56
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:03:12', u'10']
	part3_incorrect_attempt
					('0:05:36', u'(1/2)^9')
	part3_correct_attempt
					['0:06:43', u'10/(2^10)']

3 Student ID:agoldsht

	first_attempt
					2015-10-06 23:09:31
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:19:06', u'(11!/10!)']
	part3_incorrect_attempt
					('0:21:43', u'11/10')
					('0:21:51', u'11/10!')
	part3_correct_attempt
					['0:22:32', u'11/2^11']

4 Student ID:jag028

	first_attempt
					2015-10-05 06:22:46
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:19:02', u'9']
	part3_incorrect_attempt
					('0:19:20', u'8/9')
	part3_correct_attempt
					['2 days, 16:23:40', u'(9!/(8!*1!))*(1/2)^8*(1/2)^1']

5 Student ID:t2shin

	first_attempt
					2015-10-08 02:00:14
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:00:00', u'10']
	part3_incorrect_attempt
					('0:00:35', u'(1/2)^10')
	part3_correct_attempt
					['0:00:55', u'10/(2^10)']

6 Student ID:ksmurlo

	first_attempt
					2015-10-05 22:14:02
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:00:00', u'10']
	part3_incorrect_attempt
					('1 day, 2:26:07', u'10!/(1!9!)')
	part3_correct_attempt
					['1 day, 2:26:52', u'10/(2^10)']

7 Student ID:c2qiu

	first_attempt
					2015-10-03 18:41:23
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:00:00', u'11']
	part3_incorrect_attempt
					('0:00:00', u'11/(1/2)^11')
	part3_correct_attempt
					['0:05:29', u'11*((1/2)^11)']

8 Student ID:lrlai

	first_attempt
					2015-10-04 23:21:49
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:00:00', u'11']
	part3_incorrect_attempt
					('0:00:00', u'0.5^11')
	part3_correct_attempt
					['0:01:25', u'0.5^11*11']

9 Student ID:kmc012

	first_attempt
					2015-10-05 07:50:52
	part1_correct_attempt
					['0:00:00', u'2^(11)']
	part2_correct_attempt
					['2 days, 21:57:13', u'11']
	part3_incorrect_attempt
					('2 days, 21:57:35', u'C(11,10)')
					('2 days, 22:03:19', u'C(11,10)/(11!)')
					('2 days, 22:04:22', u'11/(11!)')
	part3_correct_attempt
					['2 days, 22:15:32', u'11/(2^11)']

10 Student ID:c1sorian

	first_attempt
					2015-10-08 05:40:36
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:02:09', u'10']
	part3_incorrect_attempt
					('0:02:36', u'10!/(9!)')
	part3_correct_attempt
					['0:04:22', u'10/(2^10)']

11 Student ID:jnatale

	first_attempt
					2015-10-08 00:17:10
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:08:02', u'9']
	part3_incorrect_attempt
					('0:09:58', u'(2^9)/(1/2)^8')
					('0:10:06', u'(1/2)^8')
					('0:10:17', u'((1/2)^8)/9')
					('0:10:24', u'(1/2)*8')
					('0:11:02', u'(1/2)*9')
					('0:11:13', u'(1/2)^9')
					('0:11:18', u'(1/2)*9')
					('0:12:47', u'(2^9)/8')
	part3_correct_attempt
					['0:13:55', u'9/(2^9)']

12 Student ID:jcl084

	first_attempt
					2015-10-08 19:25:12
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:02:58', u'10']
	part3_incorrect_attempt
					('0:07:38', u' 126* ((1/2)^9) * 1/2')
					('0:07:48', u' 126* ((1/2)^9) * (1/2)')
	part3_correct_attempt
					['0:08:31', u'10 * (1/2)^10']

13 Student ID:yil035

	first_attempt
					2015-10-07 06:03:13
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:00:00', u'9']
	part3_incorrect_attempt
					('0:00:00', u'1/256')
	part3_correct_attempt
					['0:01:00', u'9/512']

14 Student ID:edescobe

	first_attempt
					2015-10-04 09:40:33
	part1_correct_attempt
					['0:00:00', u'512']
	part3_incorrect_attempt
					('0:00:00', u'.0175')
	part3_correct_attempt
					['0:00:33', u'.017578']

15 Student ID:mtrafeca

	first_attempt
					2015-10-02 06:02:13
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:00:26', u'10']
	part3_incorrect_attempt
					('0:03:34', u'(.5^9)*2')
					('0:04:01', u'(.5^9)*10')
					('12:29:12', u'(.5^9)')
					('12:29:25', u'(.5^9)*10')
	part3_correct_attempt
					['12:32:46', u'10/(2^10)']

16 Student ID:t2li

	first_attempt
					2015-10-06 03:19:13
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:01:45', u'10']
	part3_incorrect_attempt
					('0:06:15', u'10/100')
	part3_correct_attempt
					['0:06:34', u'10/2^10']












## Part 4

### (102) Mistake Group redirect of size 102




### (83) Mistake Group ['R.1.1'] of size 83
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1-1/(2^11)	|1-(1/(2^11))-(11/(2^11))	|[('R.1.1', 2048.0, u'2^11', u'2^11')]	|
|1	|1-1/(2^11)	|((11!/((1!)*(10!)))/(2^11))*((11!/((2!)*(9!)))/(2^11))*((11!/((3!)*(8!)))/(2^11))*((11!/((4!)*(7!)))/(2^11))*((11!/((5!)*(6!)))/(2^11))*((11!/((6!)*(5!)))/(2^11))*((11!/((7!)*(4!)))/(2^11))*((11!/((8!)*(3!)))/(2^11))*((11!/((9!)*(2!)))/(2^11))*((11!/((10!)*(1!)))/(2^11))	|[('R.1.1', 2048.0, u'2^11', u'2^11')]	|
|2	|1-1/(2^10)	|1-10/(2^10)	|[('R.1.1', 1024.0, u'2^10', u'2^10')]	|
|3	|1-1/(2^10)	|1-(10/(2^10))	|[('R.1.1', 1024.0, u'2^10', u'2^10')]	|
|4	|1-1/(2^10)	|1-(10!/(9!))/(2^10)	|[('R.1.1', 1024.0, u'2^10', u'2^10')]	|
|5	|1-1/(2^9)	|1-(2^8)/(2^9)	|[('R.1.1', 512.0, u'2^9', u'2^9')]	|
|6	|1-1/(2^9)	|1-([9!]/[8!*(9-8)!])/(2^9)	|[('R.1.1', 512.0, u'2^9', u'2^9')]	|
|7	|1-1/(2^9)	|1-([9!]/[8!])/(2^9)	|[('R.1.1', 512.0, u'2^9', u'2^9')]	|
|8	|1-1/(2^11)	|1-(11/(2**11))	|[('R.1.1', 2048.0, u'2^11', u'2**11')]	|
|9	|1-1/(2^11)	|1 - (11! / (2! *9!)) / 2^11	|[('R.1.1', 2048.0, u'2^11', u'2^11')]	|
|10	|1-1/(2^11)	|1 - (11! / (1! *10!)) / 2^11	|[('R.1.1', 2048.0, u'2^11', u'2^11')]	|
|11	|1-1/(2^9)	|1-(9/(2^9))	|[('R.1.1', 512.0, u'2^9', u'2^9')]	|
|12	|1-1/(2^9)	|1-(8/(2^9))	|[('R.1.1', 512.0, u'2^9', u'2^9')]	|
|13	|1-1/(2^11)	|1-(10/(2^11))	|[('R.1.1', 2048.0, u'2^11', u'2^11')]	|
|14	|1-1/(2^11)	|1-(11/(2^11))	|[('R.1.1', 2048.0, u'2^11', u'2^11')]	|
|15	|1-1/(2^11)	|1-(((1^1*1^10)*11)/2^11)	|[('R.1.1', 2048.0, u'2^11', u'2^11')]	|
|16	|1-1/(2^9)	|1-(9/512)	|[('R.1.1', 512.0, u'2^9', u'512')]	|
|17	|1-1/(2^9)	|1-((512-9)/512)	|[('R.1.1', 512.0, u'2^9', u'512')]	|
|18	|1-1/(2^9)	|1 - 9/2^9	|[('R.1.1', 512.0, u'2^9', u'2^9')]	|
|19	|1-1/(2^9)	|1-(10/(2^9))	|[('R.1.1', 512.0, u'2^9', u'2^9')]	|
|20	|1-1/(2^9)	|1 - (10/(2^9))	|[('R.1.1', 512.0, u'2^9', u'2^9')]	|
|21	|1-1/(2^9)	|1 - (9/(2^9))	|[('R.1.1', 512.0, u'2^9', u'2^9')]	|
|22	|1-1/(2^10)	|1 - (11/(2^10))	|[('R.1.1', 1024.0, u'2^10', u'2^10')]	|
|23	|1-1/(2^9)	|1-([(9!)/(8!)]/(2^9))	|[('R.1.1', 512.0, u'2^9', u'2^9')]	|
|24	|1-1/(2^9)	|1-[9/(2^9)]	|[('R.1.1', 512.0, u'2^9', u'2^9')]	|
|25	|1-1/(2^9)	|1 - [10/(2^9)]	|[('R.1.1', 512.0, u'2^9', u'2^9')]	|
|26	|1-1/(2^10)	|1-[10/[2^(10)]]	|[('R.1.1', 1024.0, u'2^10', u'2^(10)')]	|
|27	|1-1/(2^9)	|1-9/2^9	|[('R.1.1', 512.0, u'2^9', u'2^9')]	|
|28	|1-1/(2^9)	|1-8/2^9	|[('R.1.1', 512.0, u'2^9', u'2^9')]	|
|29	|1-1/(2^9)	|1-(46/2^9)	|[('R.1.1', 512.0, u'2^9', u'2^9')]	|
|30	|1-1/(2^10)	|1 - (10/(2^10))	|[('R.1.1', 1024.0, u'2^10', u'2^10')]	|
|31	|1-1/(2^10)	|10 - (10/(2^10))	|[('R.1.1', 1024.0, u'2^10', u'2^10')]	|
|32	|1-1/(2^10)	|(10!/(1(9!))) - (10/(2^10))	|[('R.1.1', 1024.0, u'2^10', u'2^10')]	|
|33	|1-1/(2^11)	|1/(11/2048)	|[('R.1.1', 2048.0, u'2^11', u'2048')]	|
|34	|1-1/(2^9)	|1-9/(2^9)	|[('R.1.1', 512.0, u'2^9', u'2^9')]	|
|35	|1-1/(2^10)	|1-(10/2^10)	|[('R.1.1', 1024.0, u'2^10', u'2^10')]	|
|36	|1-1/(2^9)	|1-(9/2^9)	|[('R.1.1', 512.0, u'2^9', u'2^9')]	|
|37	|1-1/(2^9)	|1-10/[2^9]	|[('R.1.1', 512.0, u'2^9', u'2^9')]	|
|38	|1-1/(2^9)	|1-2/512	|[('R.1.1', 512.0, u'2^9', u'512')]	|
|39	|1-1/(2^11)	|1- (2^10)/(2^11)	|[('R.1.1', 2048.0, u'2^11', u'2^11')]	|
|40	|1-1/(2^11)	|1 - (11/(2^11))	|[('R.1.1', 2048.0, u'2^11', u'2^11')]	|
|41	|1-1/(2^10)	|1-((10+45+120+210+120+45+10)/(2^10))	|[('R.1.1', 1024.0, u'2^10', u'2^10')]	|
|42	|1-1/(2^10)	|1-((10+45+120+210+252+210+120+45+10)/2^10)	|[('R.1.1', 1024.0, u'2^10', u'2^10')]	|
|43	|1-1/(2^10)	|1-((1+10+45+120+210+252+210+120+45+10)/2^10)	|[('R.1.1', 1024.0, u'2^10', u'2^10')]	|
|44	|1-1/(2^11)	|1/(11/(2^11))	|[('R.1.1', 2048.0, u'2^11', u'2^11')]	|
|45	|1-1/(2^11)	|1- (12/(2^11))	|[('R.1.1', 2048.0, u'2^11', u'2^11')]	|
|46	|1-1/(2^10)	|1 - [(10!)/(1!*9!)]/[2^10]	|[('R.1.1', 1024.0, u'2^10', u'2^10')]	|
|47	|1-1/(2^11)	|1-11/2^11	|[('R.1.1', 2048.0, u'2^11', u'2^11')]	|
|48	|1-1/(2^11)	|1-(11/[2^11])	|[('R.1.1', 2048.0, u'2^11', u'2^11')]	|
|49	|1-1/(2^11)	|1-(10/2^11)	|[('R.1.1', 2048.0, u'2^11', u'2^11')]	|
|50	|1-1/(2^11)	|1-(11/2^11)	|[('R.1.1', 2048.0, u'2^11', u'2^11')]	|
|51	|1-1/(2^10)	|(10!/(1!(10-1)!))+(10!/(2!(10-2)!))+(10!/(3!(10-3)!))+(10!/(4!(10-4)!))*2+(5!/(5!(10-5)!))/2**10	|[('R.1.1', 1024.0, u'2^10', u'2**10')]	|
|52	|1-1/(2^10)	|((10!/(1!(10-1)!))+(10!/(2!(10-2)!))+(10!/(3!(10-3)!))+(10!/(4!(10-4)!)))*2+(5!/(5!(10-5)!))/2**10	|[('R.1.1', 1024.0, u'2^10', u'2**10')]	|
|53	|1-1/(2^9)	|1 - (9/512)	|[('R.1.1', 512.0, u'2^9', u'512')]	|
|54	|1-1/(2^9)	|1-(2/(2^9))	|[('R.1.1', 512.0, u'2^9', u'2^9')]	|




### (29) Mistake Group Digits of size 29




### (26) Mistake Group ['R.1'] of size 26
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1-1/(2^11)	|(2^11) - ((11!/((11!)*(0!)))/(2^11))	|[('R.1', 0.00048828125, u'1/(2^11)', u'(11!/((11!)*(0!)))/(2^11)')]	|
|1	|1-1/(2^10)	|(10!/(9!))/(2^10)+(1/2^10)	|[('R.1', 0.0009765625, u'1/(2^10)', u'1/2^10')]	|
|2	|1-1/(2^9)	|2^9 - (1/2^9)	|[('R.1', 0.001953125, u'1/(2^9)', u'1/2^9')]	|
|3	|1-1/(2^11)	|(2^10)-1/2^11	|[('R.1', 0.00048828125, u'1/(2^11)', u'1/2^11')]	|
|4	|1-1/(2^9)	|(9!)/8!(9-8)/2^9	|[('R.1', 0.001953125, u'1/(2^9)', u'(9-8)/2^9')]	|
|5	|1-1/(2^11)	|0.5^1*0.5^10+0.5^2*0.5^9+0.5^3*0.5^8+0.5^4*0.5^7+0.5^5*0.5^6+0.5^6*0.5^5+0.5^7*0.5^4+0.5^8*0.5^3+0.5^9*0.5^2+0.5^10*0.5^1	|[('R.1', 0.00048828125, u'1/(2^11)', u'0.5^10*0.5^1')]	|
|6	|1-1/(2^9)	|9/(2**9) + 1/(2**9)	|[('R.1', 0.001953125, u'1/(2^9)', u'1/(2**9)')]	|
|7	|1-1/(2^11)	|1/([1/2]^11)	|[('R.1', 0.00048828125, u'1/(2^11)', u'[1/2]^11')]	|
|8	|1-1/(2^10)	|1 - (10/(2^10)) - (1/(2^10))	|[('R.1', 0.0009765625, u'1/(2^10)', u'1/(2^10)')]	|
|9	|1-1/(2^9)	|2^9 - 1 / (2^9)	|[('R.1', 0.001953125, u'1/(2^9)', u'1 / (2^9)')]	|
|10	|1-1/(2^9)	|2^9-1/2^9	|[('R.1', 0.001953125, u'1/(2^9)', u'1/2^9')]	|
|11	|1-1/(2^10)	|(2^10)-1/2^10	|[('R.1', 0.0009765625, u'1/(2^10)', u'1/2^10')]	|
|12	|1-1/(2^11)	|11/(2^11)+(1/2^11)	|[('R.1', 0.00048828125, u'1/(2^11)', u'1/2^11')]	|
|13	|1-1/(2^9)	|8*[1/(2^8)*1/2]	|[('R.1', 0.001953125, u'1/(2^9)', u'1/(2^8)*1/2')]	|
|14	|1-1/(2^9)	|1-9/2^9-1/2^9	|[('R.1', 0.001953125, u'1/(2^9)', u'1/2^9')]	|
|15	|1-1/(2^11)	|(11!/10!)(1/2)^11	|[('R.1', 0.00048828125, u'1/(2^11)', u'(1/2)^11')]	|
|16	|1-1/(2^11)	|11!(1/2)^11	|[('R.1', 0.00048828125, u'1/(2^11)', u'(1/2)^11')]	|
|17	|1-1/(2^11)	|10!(1/2)^11	|[('R.1', 0.00048828125, u'1/(2^11)', u'(1/2)^11')]	|
|18	|1-1/(2^11)	|11*(1/2)**11	|[('R.1', 0.00048828125, u'1/(2^11)', u'(1/2)**11')]	|
|19	|1-1/(2^9)	|(2^9)-(1)/(2^9)	|[('R.1', 0.001953125, u'1/(2^9)', u'(1)/(2^9)')]	|
|20	|1-1/(2^11)	|2^11 - (1/(2^11))	|[('R.1', 0.00048828125, u'1/(2^11)', u'1/(2^11)')]	|
|21	|1-1/(2^10)	|56 * (1/2)^10	|[('R.1', 0.0009765625, u'1/(2^10)', u'(1/2)^10')]	|
|22	|1-1/(2^10)	|10 * (1/2)^10	|[('R.1', 0.0009765625, u'1/(2^10)', u'(1/2)^10')]	|
|23	|1-1/(2^10)	|45 * (1/2)^10	|[('R.1', 0.0009765625, u'1/(2^10)', u'(1/2)^10')]	|
|24	|1-1/(2^11)	|( (11!/(10!*(11-10)!)) /(2^11))+ (11!/(11!*(11-11)!)/(2^11))	|[('R.1', 0.00048828125, u'1/(2^11)', u'11!/(11!*(11-11)!)/(2^11)')]	|




### (17) Mistake Group Wrong_Sign of size 17




### (4) Mistake Group ['R.1.0'] of size 4
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1-1/(2^10)	|10*9*8*7*6*5*4*3*2(1/2)	|[('R.1.0', 1.0, u'1', u'1')]	|
|1	|1-1/(2^10)	|(1/2)(1/2)(1/2)(1/2)(1/2)(1/2)(1/2)(1/2)(1/2)	|[('R.1.0', 1.0, u'1', u'1')]	|
|2	|1-1/(2^10)	|(10!/(1(9!)))	|[('R.1.0', 1.0, u'1', u'1')]	|
|3	|1-1/(2^10)	|(10!/(1!(10-1)!))	|[('R.1.0', 1.0, u'1', u'1!')]	|




### (2) Mistake Group ['R.1.1.0'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1-1/(2^9)	|1-(1/(2^8))	|[('R.1.1.0', 2.0, u'2', u'2')]	|
|1	|1-1/(2^10)	|1- ((1/2^10) + (2/2^10) )	|[('R.1.1.0', 2.0, u'2', u'2')]	|




### (127) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:gthorn

	first_attempt
					2015-10-04 02:24:46
	part1_correct_attempt
					['0:00:00', u'512']
	part2_correct_attempt
					['0:00:00', u'9']
	part3_correct_attempt
					['0:00:00', u'0.017578125']
	part4_incorrect_attempt
					('0:06:06', u'0.99609375')
	part4_correct_attempt
					['0:12:53', u'0.998046875']

1 Student ID:v4zhang

	first_attempt
					2015-10-08 08:01:07
	part1_correct_attempt
					['0:00:00', u'2048']
	part2_correct_attempt
					['0:01:21', u'11']
	part3_correct_attempt
					['0:01:21', u'11/2048']
	part4_incorrect_attempt
					('0:02:10', u'110/2048')
	part4_correct_attempt
					['0:11:28', u'1-1/2048']

2 Student ID:kew060

	first_attempt
					2015-10-08 22:03:58
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:00:00', u'9']
	part3_correct_attempt
					['0:03:22', u'9/(2^9)']
	part4_incorrect_attempt
					('0:03:57', u'9/(2^9)')
					('0:06:46', u'(0.5)^9')
	part4_correct_attempt
					['0:06:58', u'1-(0.5)^9']

3 Student ID:kbielawi

	first_attempt
					2015-10-05 19:36:00
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['-1 day, 23:59:01', u'9']
	part3_correct_attempt
					['0:00:00', u'9/(2^9)']
	part4_incorrect_attempt
					('0:03:41', u'1/2')
					('0:21:47', u'2^9 - 2^8')
					('0:22:36', u'2^8/(2^9)')
	part4_correct_attempt
					['0:23:32', u'1-1/(2^9)']

4 Student ID:jguanzho

	first_attempt
					2015-10-02 07:55:22
	part1_correct_attempt
					['0:00:00', u'2**9']
	part2_correct_attempt
					['0:01:22', u'9']
	part3_correct_attempt
					['0:01:47', u'9/(2**9)']
	part4_incorrect_attempt
					('0:01:47', u'8/(2**9)')
					('0:03:15', u'(9! / (5! * 4!))/(2**9)')
					('0:05:10', u'1/2')
					('0:05:32', u'1/9')
					('0:18:05', u'1/(2**8)')
					('0:20:47', u'8/(2**9)')
					('0:34:51', u'1/(2**8)')
	part4_correct_attempt
					['0:38:11', u'1 - (1/(2**9))']

5 Student ID:alakamsa

	first_attempt
					2015-10-04 19:44:31
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:00:00', u'11']
	part3_correct_attempt
					['0:00:00', u'11/(2^11)']
	part4_incorrect_attempt
					('0:00:00', u'(2^11 - 12)/(2^11)')
	part4_correct_attempt
					['0:00:22', u'(2^11 - 1)/(2^11)']

6 Student ID:jjm019

	first_attempt
					2015-10-08 01:43:02
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:34:31', u'9']
	part3_correct_attempt
					['0:34:55', u'9/(2^9)']
	part4_incorrect_attempt
					('0:44:12', u'(9+36+84+126+126+84+36+9)/(2^9)')
					('0:45:30', u'(9+36+84+126)/(2^9)')
					('0:49:20', u'(1/9)+(2/9)+(3/9)+(4/9)+(5/9)+(6/9)+(7/9)+(8/9)')
					('0:49:41', u'8/9')
					('0:50:10', u'2*(8/9)')
					('1:02:13', u'9+26+84+126+126+84+36+9+1')
					('1:02:40', u'(9+26+84+126+126+84+36+9+1)/512')
					('1:07:01', u'(512-9)/512')
	part4_correct_attempt
					['1:12:11', u'(512-1)/512']

7 Student ID:dan029

	first_attempt
					2015-10-05 00:32:38
	part1_correct_attempt
					['0:00:00', u'2**9']
	part2_correct_attempt
					['0:00:00', u'9']
	part3_correct_attempt
					['0:00:00', u'9/(2**9)']
	part4_incorrect_attempt
					('0:00:18', u'1-(9/(2**9) + 1/(2**9))')
	part4_correct_attempt
					['0:01:27', u'1-1/(2**9)']

8 Student ID:haw081

	first_attempt
					2015-10-04 23:16:06
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:13:36', u'11']
	part3_correct_attempt
					['0:09:13', u'11*0.5^10*0.5^1']
	part4_incorrect_attempt
					('0:19:03', u'11/2^11')
					('0:33:03', u'1132318/2^11')
	part4_correct_attempt
					['0:45:18', u'1-1/2^11']

9 Student ID:jew037

	first_attempt
					2015-10-06 02:20:40
	part1_correct_attempt
					['0:00:00', u'2048']
	part2_correct_attempt
					['0:02:41', u'11']
	part3_correct_attempt
					['0:03:27', u'11/2048']
	part4_incorrect_attempt
					('0:03:38', u'10/2048')
					('0:08:08', u'10/2048')
					('0:08:19', u'9/2048')
					('0:08:24', u'8/2048')
					('0:14:49', u'1013/2048')
	part4_correct_attempt
					['23:24:18', u'2046/2048']

10 Student ID:avasavad

	first_attempt
					2015-10-06 06:11:58
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:00:00', u'11']
	part3_correct_attempt
					['0:00:00', u'11/(2^11)']
	part4_incorrect_attempt
					('2 days, 15:55:06', u'(2^11)-1')
	part4_correct_attempt
					['2 days, 15:55:34', u'[(2^11)-1]/2^11']

11 Student ID:lalacson

	first_attempt
					2015-10-03 15:24:13
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:01:38', u'11']
	part3_correct_attempt
					['0:01:38', u'11/2^11']
	part4_incorrect_attempt
					('0:02:21', u'11^10/2^11')
					('0:03:04', u'11!/2^11')
					('0:09:18', u'2^10/2^11')
					('0:10:35', u'(2^11-11)/2^11')
	part4_correct_attempt
					['0:11:29', u'(2^11-1)/2^11']

12 Student ID:dgunawan

	first_attempt
					2015-10-08 23:24:41
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:00:21', u'10']
	part3_correct_attempt
					['0:00:37', u'10/(2^10)']
	part4_incorrect_attempt
					('0:01:36', u'10/(2^10)')
					('0:03:09', u'1/(2^10)')
					('0:03:43', u'9/(2^10)')
	part4_correct_attempt
					['0:20:47', u'(2^10 - 1)/(2^10)']

13 Student ID:aggouw

	first_attempt
					2015-10-05 06:32:13
	part1_correct_attempt
					['0:00:00', u'2048']
	part2_correct_attempt
					['0:05:46', u'11']
	part3_correct_attempt
					['0:05:58', u'11/2048']
	part4_incorrect_attempt
					('0:07:12', u'11/2048')
					('0:07:55', u'2037/2048')
	part4_correct_attempt
					['1 day, 21:11:35', u'2047/2048']

14 Student ID:tcn013

	first_attempt
					2015-10-06 00:57:02
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:00:13', u'11']
	part3_correct_attempt
					['0:01:44', u'11/(2^11)']
	part4_incorrect_attempt
					('0:01:44', u'12/(2^11)')
					('0:02:10', u'2^10/(2^11)')
	part4_correct_attempt
					['0:03:01', u'(2^11-1)/(2^11)']

15 Student ID:pthsu

	first_attempt
					2015-10-02 04:22:43
	part1_correct_attempt
					['0:00:00', u'(2^11)']
	part2_correct_attempt
					['0:01:20', u'11!/(10!)']
	part3_correct_attempt
					['0:01:34', u'(11!/(10!))/(2^11)']
	part4_incorrect_attempt
					('0:05:03', u'(2^11) - 1')
	part4_correct_attempt
					['0:06:12', u'[(2^11) - 1] / (2^11) ']

16 Student ID:dando

	first_attempt
					2015-10-04 19:57:51
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:00:00', u'11']
	part3_correct_attempt
					['0:00:00', u'11/(2^11)']
	part4_incorrect_attempt
					('0:00:00', u'12/(2^11)')
	part4_correct_attempt
					['0:00:51', u'(2^11-1)/(2^11)']

17 Student ID:dsriniva

	first_attempt
					2015-10-08 17:43:25
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:03:05', u'10']
	part3_correct_attempt
					['0:02:57', u'0.5^10*10']
	part4_incorrect_attempt
					('0:03:36', u'0.5^10*10')
	part4_correct_attempt
					['0:04:16', u'1-0.5^10']

18 Student ID:m4bui

	first_attempt
					2015-10-08 06:08:30
	part1_correct_attempt
					['0:00:00', u'1024']
	part2_correct_attempt
					['0:03:35', u'10']
	part3_correct_attempt
					['0:03:35', u'10/1024']
	part4_incorrect_attempt
					('0:09:10', u'1013/1024')
	part4_correct_attempt
					['0:14:37', u'1023/1024']

19 Student ID:seleon

	first_attempt
					2015-10-07 19:48:38
	part1_correct_attempt
					['0:00:00', u'512']
	part2_correct_attempt
					['0:02:14', u'9']
	part3_correct_attempt
					['0:02:22', u'9/512']
	part4_incorrect_attempt
					('0:02:46', u'9/510')
					('0:02:51', u'9/511')
					('0:04:02', u'9/512')
					('0:04:12', u'510/512')
	part4_correct_attempt
					['0:04:21', u'511/512']

20 Student ID:c1wei

	first_attempt
					2015-10-08 07:44:35
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:10:09', u'9']
	part3_correct_attempt
					['0:10:22', u'9/(2^9)']
	part4_incorrect_attempt
					('0:11:49', u'9/(2^9)')
					('0:12:40', u'((2^9)-2)/(2^9)')
	part4_correct_attempt
					['0:17:09', u'((2^9)-1)/(2^9)']

21 Student ID:starinia

	first_attempt
					2015-10-06 23:47:21
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:00:00', u'10']
	part3_correct_attempt
					['1:46:51', u'10/2^10']
	part4_incorrect_attempt
					('1 day, 1:28:34', u'((10!/(9!1!)) * (10!/(8!2!)) * (10!/(7!3!) )* (10!/(6!4!)) * (10!/(5!5!)) * (10!/(4!6!)) * (10!/(3!7!)) * (10!/(2!8!)) * (10!/(1!9!)))/2^10')
	part4_correct_attempt
					['1 day, 8:22:52', u'511/512']

22 Student ID:m4salaza

	first_attempt
					2015-10-07 03:29:19
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:00:00', u'9']
	part3_correct_attempt
					['0:00:00', u'9/(2^9)']
	part4_incorrect_attempt
					('0:00:45', u'9/(2^9)*8+1')
					('0:10:17', u'9!/(8!*1)/(2^9)')
	part4_correct_attempt
					['0:13:47', u'1-1/(2^9)']

23 Student ID:yos017

	first_attempt
					2015-10-02 11:37:53
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:04:44', u'10']
	part3_correct_attempt
					['0:04:44', u'10/2^10']
	part4_incorrect_attempt
					('0:08:28', u'2/2^10')
					('0:09:25', u'2^9/2^10')
					('0:09:47', u'1014/2^10')
	part4_correct_attempt
					['0:10:58', u'1022/2^10']

24 Student ID:a8ho

	first_attempt
					2015-10-07 06:00:13
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:11:19', u'10']
	part3_correct_attempt
					['0:12:16', u'10/2^10']
	part4_incorrect_attempt
					('0:23:02', u'56/2^10')
					('0:30:08', u'(10*2+45*2+240+420+252*2)/2^10')
	part4_correct_attempt
					['0:45:04', u'(10+45+120+210+252+210+120+45+10)/2^10']

25 Student ID:h4tu

	first_attempt
					2015-10-08 18:54:59
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:00:00', u'9']
	part3_correct_attempt
					['0:00:00', u'9/(2^9)']
	part4_incorrect_attempt
					('0:00:00', u'10/(2^9)')
	part4_correct_attempt
					['0:00:26', u'(2^9-1)/(2^9)']

26 Student ID:jag028

	first_attempt
					2015-10-05 06:22:46
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:19:02', u'9']
	part3_correct_attempt
					['2 days, 16:23:40', u'(9!/(8!*1!))*(1/2)^8*(1/2)^1']
	part4_incorrect_attempt
					('2 days, 16:26:08', u'(9!/(8!*1!))*(1/2)^8*(1/2)^1')
					('3 days, 11:52:48', u'[(9!)/[(8!)(9-8)!]]')
					('3 days, 12:04:26', u'1-(8!/9!)')
					('3 days, 12:04:38', u'1-(8/9)')
					('3 days, 12:05:10', u'1-(9!/(8!*1!))*(1/2)^8*(1/2)^1')
	part4_correct_attempt
					['3 days, 13:38:53', u'1-(1/2)^9']

27 Student ID:asetters

	first_attempt
					2015-10-02 19:56:13
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:00:00', u'9']
	part3_correct_attempt
					['0:00:00', u'9/(2^9)']
	part4_incorrect_attempt
					('0:00:00', u'502/512')
	part4_correct_attempt
					['0:00:16', u'511/512']

28 Student ID:c1sorian

	first_attempt
					2015-10-08 05:40:36
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:02:09', u'10']
	part3_correct_attempt
					['0:04:22', u'10/(2^10)']
	part4_incorrect_attempt
					('0:04:22', u'10!/(2^10)')
					('0:07:15', u'(10+45+120+210+120+45+10)/(2^10)')
	part4_correct_attempt
					['0:13:02', u'1-(1/(2^10))']

29 Student ID:abjara

	first_attempt
					2015-10-05 22:34:51
	part1_correct_attempt
					['0:00:00', u'2**11']
	part2_correct_attempt
					['-1 day, 23:54:09', u'11']
	part3_correct_attempt
					['0:00:00', u'11/2**11']
	part4_incorrect_attempt
					('0:01:51', u'((2**11)-11)/2**11')
	part4_correct_attempt
					['0:29:03', u'[(2^11)-1]/2^11']

30 Student ID:cprafull

	first_attempt
					2015-10-06 19:24:57
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:00:38', u'11']
	part3_correct_attempt
					['0:00:56', u'11/(2^11)']
	part4_incorrect_attempt
					('0:01:57', u'2^11 - 1')
					('0:02:07', u'(2^11) - 1')
					('5:43:44', u'2^11 - 11')
					('5:43:56', u'(2^11) - 11')
					('5:44:24', u'[(2^11) - 11]/(2^11)')
	part4_correct_attempt
					['6:04:23', u'2*[11!/(10!1!) + 11!/(9!2!) + 11!/(8!3!) + 11!/(7!4!) + 11!/(6!5!)]/(2^11)']

31 Student ID:anislam

	first_attempt
					2015-10-08 23:47:23
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:00:00', u'10']
	part3_correct_attempt
					['0:00:00', u'10 / 2 ^ 10']
	part4_incorrect_attempt
					('0:00:00', u'2^10 - 1')
	part4_correct_attempt
					['0:00:56', u'(2^10 - 1) / 2^10']

32 Student ID:tpmach

	first_attempt
					2015-10-03 21:40:56
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:03:24', u'9!/[8!(9-8)!]']
	part3_correct_attempt
					['0:03:36', u'9/2^9']
	part4_incorrect_attempt
					('0:05:49', u'2^9-(9!/[1!(9-1)!])-1')
					('0:10:22', u'(2^9-1-9!/[1!(9-1)!])/2^9')
					('0:17:24', u'504/512')
					('0:30:54', u'(2^9-10)/2^9')
					('0:35:09', u'2^9-1')
					('0:35:43', u'2^9-2')
	part4_correct_attempt
					['0:36:08', u'(2^9-1)/2^9']

33 Student ID:t2li

	first_attempt
					2015-10-06 03:19:13
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:01:45', u'10']
	part3_correct_attempt
					['0:06:34', u'10/2^10']
	part4_incorrect_attempt
					('0:07:02', u'(2^10-10)/2^10')
					('0:07:22', u'(2^10-10-1)/2^10')
	part4_correct_attempt
					['0:15:03', u'(2^10-1)/2^10']

34 Student ID:dis003

	first_attempt
					2015-10-08 07:13:16
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:03:55', u'11']
	part3_correct_attempt
					['0:05:04', u'11/2^11']
	part4_incorrect_attempt
					('0:05:04', u'(2^11-11)/2^11')
					('0:07:26', u'(2^11-11-11)/2^11')
	part4_correct_attempt
					['0:08:32', u'(2^11-1)/2^11']

35 Student ID:rraiyyan

	first_attempt
					2015-10-06 06:46:36
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:03:35', u'11!/(10!*1!)']
	part3_correct_attempt
					['0:03:35', u'11/(2^11)']
	part4_incorrect_attempt
					('0:03:35', u'(11!/(10!*1!)+11!/(2!*9!)+11!/(3!*8!)+11!/(4!*7!)+11!/(5!*6!))/(2^11)')
	part4_correct_attempt
					['0:04:51', u'2*(11!/(10!*1!)+11!/(2!*9!)+11!/(3!*8!)+11!/(4!*7!)+11!/(5!*6!))/(2^11)']

36 Student ID:jhw015

	first_attempt
					2015-10-04 02:53:21
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:12:48', u'9']
	part3_correct_attempt
					['0:16:59', u'9/ 2^9']
	part4_incorrect_attempt
					('2 days, 12:39:24', u'9!/2^9')
	part4_correct_attempt
					['4 days, 1:34:30', u'511/512']

37 Student ID:dsmonaha

	first_attempt
					2015-10-05 18:33:47
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:08:03', u'9']
	part3_correct_attempt
					['0:08:30', u'9/512']
	part4_incorrect_attempt
					('0:09:03', u'9/512')
					('0:16:16', u'(8!)^2')
					('0:16:23', u'(8!)')
					('0:16:39', u'((8!)^2)/512')
					('0:16:59', u'(8!)/512')
	part4_correct_attempt
					['1 day, 22:38:58', u'511/512']

38 Student ID:hmnaing

	first_attempt
					2015-10-07 02:45:21
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['21:20:36', u'11']
	part3_correct_attempt
					['21:20:36', u'11/(2^11)']
	part4_incorrect_attempt
					('21:21:11', u'11/(2^11)')
					('21:24:07', u'(2^10)/(2^11)')
					('21:28:41', u'1/(2^11)')
					('21:31:08', u'10/(2^11)')
					('21:31:22', u'11/(2^11)')
	part4_correct_attempt
					['21:35:00', u'1-(1/(2^11))']

39 Student ID:edescobe

	first_attempt
					2015-10-04 09:40:33
	part1_correct_attempt
					['0:00:00', u'512']
	part3_correct_attempt
					['0:00:33', u'.017578']
	part4_incorrect_attempt
					('0:03:06', u'.99069')
	part4_correct_attempt
					['0:03:45', u'.998046']

40 Student ID:ctroncos

	first_attempt
					2015-10-08 05:42:25
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:02:53', u'11']
	part3_correct_attempt
					['0:03:29', u'11/(2^11)']
	part4_incorrect_attempt
					('17:44:41', u'66/(2^11)')
					('17:45:06', u'55/(2^11)')
					('17:47:43', u'(C(11,10) + C(11,11))/(2^11)')

41 Student ID:muy002

	first_attempt
					2015-10-07 21:36:23
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:02:15', u'11']
	part3_correct_attempt
					['0:02:41', u'11/2^11']
	part4_incorrect_attempt
					('0:02:57', u'10/2^11')
					('0:03:28', u'11/2^11')
					('0:05:23', u'(11!/(10!*1!))/2^11')
					('0:05:55', u'11!/10!')
					('0:06:20', u'(11!/10!)/2^11')
					('0:07:05', u'10!/2^11')
					('0:22:53', u'(11!/10)/2^11')
					('0:23:08', u'(11/10!)/2^11')
					('0:23:19', u'(11/10)/2^11')
					('0:23:45', u'(11!/(10!*(11-10)!))/2^11')
					('1:56:01', u'(11!/10!)/2^10')
					('1:56:41', u'(11!/10!)/2^11')
					('22:13:24', u'(11!/(2!*9!))/2^11')
					('22:14:16', u'1/2^11')
	part4_correct_attempt
					['22:14:33', u'1-(1/2^11)']

42 Student ID:jtfrankl

	first_attempt
					2015-10-07 23:40:21
	part1_correct_attempt
					['0:00:00', u'2**11']
	part2_correct_attempt
					['0:00:37', u'11']
	part3_correct_attempt
					['2:55:15', u'11*(1/2)**11']
	part4_incorrect_attempt
					('3:00:51', u'11!/(10!)')
					('3:00:58', u'11!/(10!1!)')
					('3:02:13', u'.5')
					('3:03:01', u'11!/1!')
					('3:03:06', u'11!/10!')
					('3:03:21', u'1.2')
	part4_correct_attempt
					['3:07:03', u'1-(1/2)^11']

43 Student ID:cstringh

	first_attempt
					2015-10-04 00:02:56
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:03:12', u'10']
	part3_correct_attempt
					['0:06:43', u'10/(2^10)']
	part4_incorrect_attempt
					('2 days, 21:42:55', u'10!')
					('2 days, 21:47:04', u'(11/(2^10)) - (10/(2^10))')
					('2 days, 21:47:19', u'(10/(2^10)) - (10/(2^10))')
	part4_correct_attempt
					['2 days, 22:05:57', u'1- (1/2)^10']

44 Student ID:j5phung

	first_attempt
					2015-10-02 17:08:28
	part1_correct_attempt
					['0:00:00', u'2048']
	part2_correct_attempt
					['0:01:01', u'11']
	part3_correct_attempt
					['0:01:01', u'11/2048']
	part4_incorrect_attempt
					('0:02:38', u'2042/2048')
					('0:05:35', u'2037/2048')
	part4_correct_attempt
					['0:12:51', u'2047/2048']

45 Student ID:eshung

	first_attempt
					2015-10-08 18:29:05
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:00:00', u'9']
	part3_correct_attempt
					['0:00:00', u'9/(2^9)']
	part4_incorrect_attempt
					('0:02:10', u'(C(9,2)+C(9,3)+C(9,4)+C(9,5)+C(9,6)+C(9,7)+9)/(2^9)')
					('0:03:16', u'510/(2^9)')
					('0:09:45', u'510/(2^9)')
	part4_correct_attempt
					['0:11:55', u'511/(2^9)']

46 Student ID:rbdoming

	first_attempt
					2015-10-02 21:11:01
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:02:26', u'9']
	part3_correct_attempt
					['0:02:40', u'9/2^9']
	part4_incorrect_attempt
					('0:02:40', u'9/2^9')
					('0:07:49', u'(2^9) -1')
	part4_correct_attempt
					['0:11:16', u'511/512']

47 Student ID:ralhadda

	first_attempt
					2015-10-08 17:31:19
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:05:25', u'10']
	part3_correct_attempt
					['0:06:43', u'10/(2^10)']
	part4_incorrect_attempt
					('0:07:03', u'10/(2^10)')
					('0:11:28', u'10/(2^10)')
					('0:11:45', u'9/(2^10)')
					('0:11:50', u'8/(2^10)')
					('0:11:56', u'7/(2^10)')
					('0:12:02', u'6/(2^10)')
					('0:12:07', u'5/(2^10)')
					('0:12:12', u'4/(2^10)')
					('0:12:17', u'3/(2^10)')
					('0:12:22', u'2/(2^10)')
					('0:12:28', u'1/(2^10)')
					('0:12:40', u'100/(2^10)')

48 Student ID:yjshin

	first_attempt
					2015-10-07 07:48:44
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:00:37', u'10']
	part3_correct_attempt
					['0:01:02', u'10/1024']
	part4_incorrect_attempt
					('0:01:51', u'1013/1024')
					('0:02:19', u'1004/1024')
					('0:31:47', u'1014/1024')
					('0:32:06', u'1004/1024')
					('0:34:17', u'1013/1024')
	part4_correct_attempt
					['0:36:06', u'1022/1024']

49 Student ID:aportuga

	first_attempt
					2015-10-06 05:36:44
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:10:01', u'10']
	part3_correct_attempt
					['0:10:19', u'10/(2^10)']
	part4_incorrect_attempt
					('0:10:49', u'((2^10)-10)/(2^10)')
					('0:11:15', u'10!/(2^10)')
	part4_correct_attempt
					['0:53:16', u'1-(1/(2^10))']

50 Student ID:bpandayk

	first_attempt
					2015-10-08 15:23:40
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:00:21', u'10']
	part3_correct_attempt
					['0:00:48', u'10/1024']
	part4_incorrect_attempt
					('0:01:19', u'9!/1024')
	part4_correct_attempt
					['0:16:02', u'1022/1024']

51 Student ID:bkoli

	first_attempt
					2015-10-08 08:26:36
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:01:18', u'11']
	part3_correct_attempt
					['0:01:55', u'11/(2^11)']
	part4_incorrect_attempt
					('8:09:41', u'2^11 - 2^10')
					('8:10:52', u'(2^11 - 10)/2^11')
					('8:11:27', u'(2^11 - 11)/2^11')
					('8:12:18', u'2^11 - (11/(2^11))')
					('8:13:14', u'2^11 - 1')
					('8:15:05', u'2^11 - 2')
	part4_correct_attempt
					['8:18:29', u'(2^11 - 2)/2^11']

52 Student ID:dac064

	first_attempt
					2015-10-08 21:38:33
	part1_correct_attempt
					['0:00:00', u'2048']
	part2_correct_attempt
					['0:00:00', u'11']
	part3_correct_attempt
					['0:00:00', u'11/2048']
	part4_incorrect_attempt
					('0:00:00', u'22/2048')
	part4_correct_attempt
					['0:03:01', u'2047/2048']

53 Student ID:sghouse

	first_attempt
					2015-10-04 18:47:47
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:00:00', u'9']
	part3_correct_attempt
					['0:00:00', u'9/2^9']
	part4_incorrect_attempt
					('0:00:00', u'(2^9-9)/2^9')
	part4_correct_attempt
					['0:03:21', u'(2^9-1)/2^9']

54 Student ID:msaguiar

	first_attempt
					2015-10-06 04:23:45
	part1_correct_attempt
					['0:00:00', u'(2^9)']
	part2_correct_attempt
					['0:00:30', u'9']
	part3_correct_attempt
					['0:21:32', u'9/(2^9)']
	part4_incorrect_attempt
					('0:23:17', u'((2^9)-9)/(2^9)')
	part4_correct_attempt
					['0:23:38', u'((2^9)-1)/(2^9)']

55 Student ID:jyc018

	first_attempt
					2015-10-05 15:59:34
	part1_correct_attempt
					['0:00:00', u'2**11']
	part2_correct_attempt
					['0:00:00', u'11']
	part3_correct_attempt
					['0:00:00', u'11/2**11']
	part4_incorrect_attempt
					('0:00:00', u'2**11-1-11')
					('0:01:59', u'2**11-1')
					('0:02:12', u'2**11-2')
					('0:03:53', u'11+C(11,2)+C(11,3)+C(11,4)+C(11,5)+C(11,6)+C(11,7)+C(11,8)+C(11,9)+C(11,10)')
					('0:04:13', u'C(11,2)')
	part4_correct_attempt
					['0:09:48', u'2046/2**11']

56 Student ID:b3hwang

	first_attempt
					2015-10-08 23:36:30
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:00:00', u'10']
	part3_correct_attempt
					['0:00:00', u'10/(2^10)']
	part4_incorrect_attempt
					('0:06:35', u'(2^10) - 1')
	part4_correct_attempt
					['0:07:12', u'((2^10) -1)/(2^10)']

57 Student ID:lywong

	first_attempt
					2015-10-05 23:28:10
	part1_correct_attempt
					['0:00:00', u'1024']
	part2_correct_attempt
					['15:21:31', u'10']
	part3_correct_attempt
					['15:23:35', u'10/1024']
	part4_incorrect_attempt
					('15:23:35', u'1014/1024')
	part4_correct_attempt
					['15:24:05', u'1023/1024']

58 Student ID:hkhodada

	first_attempt
					2015-10-02 18:49:54
	part1_correct_attempt
					['0:00:00', u'512']
	part2_correct_attempt
					['0:15:04', u'9']
	part3_correct_attempt
					['0:15:20', u'9/512']
	part4_incorrect_attempt
					('10:48:29', u'9/512')
	part4_correct_attempt
					['11:42:43', u'511/512']

59 Student ID:glcohen

	first_attempt
					2015-10-04 22:55:55
	part1_correct_attempt
					['0:00:00', u'1024']
	part2_correct_attempt
					['0:13:34', u'(10!)/(9!(10-9)!)']
	part3_correct_attempt
					['0:12:30', u'((10!)/(9!))/1024']
	part4_incorrect_attempt
					('0:13:34', u'(10!)/(9!(10-9)!)')
					('0:14:34', u'5/1024')
	part4_correct_attempt
					['0:15:13', u'1023/1024']

60 Student ID:achava

	first_attempt
					2015-10-02 05:09:18
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:07:10', u'(11!/((10!)*(1!)))']
	part3_correct_attempt
					['0:07:23', u'(11!/((10!)*(1!)))/(2^11)']
	part4_incorrect_attempt
					('0:08:24', u'(11!/((10!)*(1!)))/(2^11)')
					('0:14:43', u'(11!/((1!)*(10!)))*(11!/((2!)*(9!)))*(11!/((3!)*(8!)))*(11!/((4!)*(7!)))*(11!/((5!)*(6!)))*(11!/((6!)*(5!)))*(11!/((7!)*(4!)))*(11!/((8!)*(3!)))*(11!/((9!)*(2!)))*(11!/((10!)*(1!)))')
					('0:15:08', u'((11!/((1!)*(10!)))*(11!/((2!)*(9!)))*(11!/((3!)*(8!)))*(11!/((4!)*(7!)))*(11!/((5!)*(6!)))*(11!/((6!)*(5!)))*(11!/((7!)*(4!)))*(11!/((8!)*(3!)))*(11!/((9!)*(2!)))*(11!/((10!)*(1!))))*2^11')
					('0:16:27', u'((11!/((1!)+(10!)))+(11!/((2!)+(9!)))+(11!/((3!)+(8!)))+(11!/((4!)+(7!)))+(11!/((5!)+(6!)))+(11!/((6!)+(5!)))+(11!/((7!)+(4!)))+(11!/((8!)+(3!)))+(11!/((9!)+(2!)))+(11!/((10!)+(1!))))*2^11')
					('0:18:18', u'(10!/((10!)*(1!)))/(2^11)')
					('0:18:26', u'(10!/((10!)*(1!)))/(2^10)')
					('0:18:35', u'(11!/((10!)*(1!)))/(2^10)')
					('0:19:18', u'(10!/((10!)*(1!)))/(2^11)')
					('0:19:37', u'(10!/((9!)*(1!)))/(2^11)')
					('0:20:42', u'(10!/((10!)*(1!)))/(2^11)')
					('0:29:02', u'(2^11)-((11!/((10!)*(1!)))/(2^11))')
					('0:34:38', u'(2^11) - ((2^11) - ((11!/((10!)*(1!)))/(2^11)))')
	part4_correct_attempt
					['0:37:03', u'((2^11) - ((11!/((11!)*(0!)))/(2^11)))/(2^11)']

61 Student ID:ffhaddad

	first_attempt
					2015-10-03 00:06:40
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:05:43', u'9']
	part3_correct_attempt
					['0:06:01', u'9/2^9']
	part4_incorrect_attempt
					('0:10:41', u'((2^9)-2)/2^9')
	part4_correct_attempt
					['0:12:53', u'((2^9)-1)/2^9']

62 Student ID:awollner

	first_attempt
					2015-10-06 15:40:09
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:00:00', u'11']
	part3_correct_attempt
					['0:00:00', u'11/2^11']
	part4_incorrect_attempt
					('0:00:00', u'2^11-1')
	part4_correct_attempt
					['0:02:38', u'2047/2048']

63 Student ID:dcrume

	first_attempt
					2015-10-08 17:32:07
	part1_correct_attempt
					['0:00:00', u'2^(11)']
	part2_correct_attempt
					['0:00:43', u'11']
	part3_correct_attempt
					['0:00:00', u'11/(2^11)']
	part4_incorrect_attempt
					('0:03:10', u'2^(10)/2^(11)')

64 Student ID:pvl001

	first_attempt
					2015-10-03 15:48:09
	part1_correct_attempt
					['0:00:00', u'1024']
	part2_correct_attempt
					['0:01:26', u'10']
	part3_correct_attempt
					['0:01:26', u'10/1024']
	part4_incorrect_attempt
					('0:01:26', u'11/1024')
	part4_correct_attempt
					['0:02:22', u'1023/1024']

65 Student ID:mrchin

	first_attempt
					2015-10-05 20:49:34
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:00:42', u'10']
	part3_correct_attempt
					['0:00:47', u'10/(2^10)']
	part4_incorrect_attempt
					('0:00:57', u'(2^10) - 10')
					('0:01:12', u'((2^10) - 10)/2^10')
	part4_correct_attempt
					['2:14:20', u'((2^10) - 1)/2^10']

66 Student ID:agoldsht

	first_attempt
					2015-10-06 23:09:31
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:19:06', u'(11!/10!)']
	part3_correct_attempt
					['0:22:32', u'11/2^11']
	part4_incorrect_attempt
					('0:22:53', u'11!/2^11')
					('0:26:15', u'(11+10+9+8+7+6+5+4+3+2+1)/2^11')
					('1:47:15', u'1-(1/2^11 + 11/2^11)')
	part4_correct_attempt
					['1:59:16', u'(2^11 - 1) / (2^11)']

67 Student ID:n2patil

	first_attempt
					2015-10-06 15:47:55
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['1 day, 13:30:58', u'11']
	part3_correct_attempt
					['1 day, 13:33:19', u'11/(2^11)']
	part4_incorrect_attempt
					('1 day, 14:07:32', u'(11/(2^11))/1')
					('1 day, 14:16:03', u'((2^11)-12)/(2^11)')
	part4_correct_attempt
					['1 day, 14:20:24', u'1-(1/2^11)']

68 Student ID:ttimmons

	first_attempt
					2015-10-02 19:39:22
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:02:07', u'[9!]/[8!*(9-8)!]']
	part3_correct_attempt
					['0:07:23', u'([9!]/[8!(9-8)!])/(2^9)']
	part4_incorrect_attempt
					('0:08:03', u'([8!]/[7!])/(2^9)')
					('0:08:31', u'([8!])/(2^9)')
	part4_correct_attempt
					['1 day, 4:18:37', u'1-(1/[2^9])']

69 Student ID:jeqin

	first_attempt
					2015-10-02 20:22:54
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:00:00', u'10']
	part3_correct_attempt
					['0:00:00', u'10/(2^10)']
	part4_incorrect_attempt
					('0:00:25', u'1/(2^10)')
	part4_correct_attempt
					['1:39:14', u'[(2^10)-1]/(2^10)']

70 Student ID:jnatale

	first_attempt
					2015-10-08 00:17:10
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:08:02', u'9']
	part3_correct_attempt
					['0:13:55', u'9/(2^9)']
	part4_incorrect_attempt
					('0:16:26', u'8/(2^9)')
					('0:16:43', u'7/(2^9)')
					('0:16:56', u'6/(2^9)')
					('2:42:44', u'9/4')
					('2:44:33', u'(1/2)^2')
					('2:45:15', u'(1/2)^8')
					('2:45:28', u'9/(2^9)')
					('2:45:42', u'8/9')
	part4_correct_attempt
					['3:58:41', u'1-((1/2)^9)']

71 Student ID:jblynch

	first_attempt
					2015-10-05 04:20:47
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:02:39', u'10']
	part3_correct_attempt
					['0:07:04', u'10/2^10']
	part4_incorrect_attempt
					('0:11:52', u'(10*45*120*210*252*210*120*45*10)/2^10')
	part4_correct_attempt
					['0:12:32', u'(10+45+120+210+252+210+120+45+10)/2^10']

72 Student ID:smohiman

	first_attempt
					2015-10-02 21:05:12
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:00:00', u'9!/(1!*8!)']
	part3_correct_attempt
					['0:00:00', u'9/(2^9)']
	part4_incorrect_attempt
					('0:00:00', u'(2^9)-(9/(2^9))')
					('0:04:27', u'(2^9)-1')
					('0:08:28', u'(2^9)-9')
					('0:08:37', u'(2^9)-8')
					('0:12:41', u'2^9')
					('0:12:58', u'(2^9)-1')
					('0:14:21', u'(2^9)-(9/(2^9))-1')
	part4_correct_attempt
					['0:16:53', u'((2^9)-1)/(2^9)']

73 Student ID:nnh002

	first_attempt
					2015-10-07 00:34:05
	part1_correct_attempt
					['0:00:00', u'2048']
	part2_correct_attempt
					['0:00:00', u'11']
	part3_correct_attempt
					['0:00:00', u'11/2048']
	part4_incorrect_attempt
					('0:00:00', u'2036/2048')
	part4_correct_attempt
					['0:03:33', u'2047/2048']

74 Student ID:sthapa

	first_attempt
					2015-10-06 06:38:14
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:02:06', u'9!/(8!)']
	part3_correct_attempt
					['0:02:43', u'(9!/(8!))/(2^9)']
	part4_incorrect_attempt
					('0:03:57', u'7!/(2^9)')
					('0:04:02', u'8!/(2^9)')
					('0:06:12', u'(2!*3!*4!*5!*6!*7!*8!)/(2^9)')
					('0:06:31', u'8!/(2^9)')
					('0:09:29', u'2^9 - 9')
	part4_correct_attempt
					['0:15:31', u'511/(2^9)']

75 Student ID:tol003

	first_attempt
					2015-10-06 23:33:00
	part1_correct_attempt
					['0:00:00', u'2048']
	part2_correct_attempt
					['0:00:00', u'11']
	part3_correct_attempt
					['0:00:00', u'11/2048']
	part4_incorrect_attempt
					('0:00:00', u'66/2048')
					('0:01:55', u'65/2048')
					('0:03:23', u'67/2048')
					('0:05:57', u'2037/2048')
					('0:19:53', u'1024/2048')
					('0:20:45', u'1013/2048')
					('0:27:02', u'2037/2048')
					('0:33:04', u'11/2048')
					('0:33:54', u'2036/2048')
					('0:35:29', u'2038/2048')
	part4_correct_attempt
					['0:38:31', u'2047/2048']

76 Student ID:aakumar

	first_attempt
					2015-10-03 22:23:21
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['-1 day, 23:59:44', u'10']
	part3_correct_attempt
					['0:01:55', u'10/1024']
	part4_incorrect_attempt
					('0:01:55', u'11023/1024')
	part4_correct_attempt
					['0:02:01', u'1023/1024']

77 Student ID:wcwhite

	first_attempt
					2015-10-07 02:48:00
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:05:48', u'11']
	part3_correct_attempt
					['18:12:44', u'11/2^11']
	part4_incorrect_attempt
					('18:14:40', u'1/2^11')
					('18:15:21', u'121/2^11')
					('18:21:04', u'1-0.00537109')
					('18:21:17', u'1/(1-0.00537109)')
					('18:23:56', u'11!/10!')
					('18:24:08', u'10!/11!')
					('1 day, 16:09:20', u'11!(10!(11-10)!)')
					('1 day, 16:09:30', u'11!/(10!(11-10)!)')
	part4_correct_attempt
					['1 day, 16:09:49', u'1']

78 Student ID:arvenega

	first_attempt
					2015-10-08 04:49:12
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:07:59', u'11']
	part3_correct_attempt
					['0:01:03', u'11/(2^11)']
	part4_incorrect_attempt
					('0:12:25', u'.9946')
					('0:12:38', u'.99462891')
	part4_correct_attempt
					['0:17:16', u'1-(1/(2^11))']

79 Student ID:csl030

	first_attempt
					2015-10-04 21:44:22
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:00:00', u'9']
	part3_correct_attempt
					['0:00:00', u'9/2^9']
	part4_incorrect_attempt
					('0:01:45', u'1 - (1- 9/2^9)')
					('0:05:15', u'2^8 / 2 ^ 9')
	part4_correct_attempt
					['0:06:24', u'1 - (1/2)^9']

80 Student ID:r2fisher

	first_attempt
					2015-10-05 16:26:17
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:00:18', u'11']
	part3_correct_attempt
					['0:00:26', u'11/(2^11)']
	part4_incorrect_attempt
					('0:00:26', u'(2^11-11)/(2^11)')
	part4_correct_attempt
					['0:00:36', u'(2^11-1)/(2^11)']

81 Student ID:volim

	first_attempt
					2015-10-03 18:48:40
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:00:00', u'(11!)/(10!)']
	part3_correct_attempt
					['0:00:00', u'11/(2^11)']
	part4_incorrect_attempt
					('0:00:00', u'(2^11)-1')
	part4_correct_attempt
					['0:01:28', u'[(2^11)-1]/(2^11)']

82 Student ID:aurodrig

	first_attempt
					2015-10-07 04:38:05
	part1_correct_attempt
					['0:00:00', u'512']
	part2_correct_attempt
					['0:38:57', u'9']
	part3_correct_attempt
					['0:39:11', u'9/512']
	part4_incorrect_attempt
					('0:51:04', u'56/512')
					('0:57:52', u'1/512')
					('0:57:59', u'17/512')
					('1:09:56', u'1/512')
					('1:10:03', u'.99/512')
					('1:12:04', u'8/512')
	part4_correct_attempt
					['1:12:16', u'511/512']

83 Student ID:ytc012

	first_attempt
					2015-10-06 09:44:37
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:00:34', u'9']
	part3_correct_attempt
					['0:00:54', u'9/2^9']
	part4_incorrect_attempt
					('0:01:40', u'2^9-1')
	part4_correct_attempt
					['0:02:06', u'(2^9-1)/2^9']

84 Student ID:tjke

	first_attempt
					2015-10-03 23:29:08
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:00:00', u'11']
	part3_correct_attempt
					['0:00:00', u'11/2^11']
	part4_incorrect_attempt
					('0:00:00', u'(11+1)/2^11')
	part4_correct_attempt
					['0:00:25', u'(2^11-1)/2^11']

85 Student ID:asp025

	first_attempt
					2015-10-08 15:57:20
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['1:23:52', u'10']
	part3_correct_attempt
					['1:16:39', u'10/2^10']
	part4_incorrect_attempt
					('1:24:24', u'9!/2^10')
	part4_correct_attempt
					['1:55:21', u'1022/2^10']

86 Student ID:dlgoldbe

	first_attempt
					2015-10-08 04:52:01
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:00:49', u'9']
	part3_correct_attempt
					['0:00:49', u'9/(2^9)']
	part4_incorrect_attempt
					('0:02:39', u'9!/(2^9)')
					('0:03:50', u'(9+8+7+6+5+4+3+2)/(2^9)')
					('0:09:00', u'(2^9) - 1')
	part4_correct_attempt
					['0:09:17', u'((2^9) - 1)/(2^9)']

87 Student ID:fichoi

	first_attempt
					2015-10-06 21:42:14
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:03:40', u'10']
	part3_correct_attempt
					['0:05:25', u'10/1024']
	part4_incorrect_attempt
					('0:05:25', u'10/1024')
					('0:25:37', u'45/512')
					('0:27:30', u'23/256')
					('0:47:50', u'10/1024')
	part4_correct_attempt
					['0:55:35', u'1023/1024']

88 Student ID:kquong

	first_attempt
					2015-10-03 21:26:11
	part1_correct_attempt
					['0:00:00', u'512']
	part2_correct_attempt
					['0:00:00', u'9']
	part3_correct_attempt
					['0:00:00', u'9/512']
	part4_incorrect_attempt
					('0:00:00', u'(512-9-1)/512')
	part4_correct_attempt
					['0:01:15', u'(512-1)/512']

89 Student ID:jfalcone

	first_attempt
					2015-10-07 03:37:38
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:00:00', u'9']
	part3_correct_attempt
					['0:00:13', u'9/(2^9)']
	part4_incorrect_attempt
					('0:00:59', u'((2^8)*9)/(2^9)')
	part4_correct_attempt
					['0:06:37', u'((2^9)-1)/(2^9)']

90 Student ID:vsamant

	first_attempt
					2015-10-02 17:03:06
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['-1 day, 23:57:54', u'9']
	part3_correct_attempt
					['0:06:24', u'((9!)/((8!)(1!)))/(2^9)']
	part4_incorrect_attempt
					('0:06:24', u'(1-(9!/(9!)))/(2^9)')
					('1 day, 9:46:17', u'1/256')
					('1 day, 23:53:03', u'(2^9-(1/512))/(2^9)')
	part4_correct_attempt
					['1 day, 23:56:00', u'1-1/(2^9)']

91 Student ID:dcastlem

	first_attempt
					2015-10-03 21:42:23
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:18:33', u'10!/9!']
	part3_correct_attempt
					['0:18:56', u'10/1024']
	part4_incorrect_attempt
					('0:19:06', u'10/1024')
					('0:21:57', u'9!/1024')
					('1:05:27', u'9/1024')
					('1:05:46', u'11/1024')
	part4_correct_attempt
					['1:09:38', u'1023/1024']

92 Student ID:ppanourg

	first_attempt
					2015-10-07 23:44:44
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:01:09', u'9']
	part3_correct_attempt
					['0:02:47', u'9/(2^9)']
	part4_incorrect_attempt
					('0:02:47', u'9/(2^9)')
	part4_correct_attempt
					['6:35:41', u'1-(1/(2^9))']

93 Student ID:spw006

	first_attempt
					2015-10-04 05:55:21
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:00:47', u'10']
	part3_correct_attempt
					['0:01:24', u'10/1024']
	part4_incorrect_attempt
					('0:02:21', u'1/2')
					('13:11:03', u'1/512')
	part4_correct_attempt
					['13:11:24', u'1-(1/512)']

94 Student ID:pcdo

	first_attempt
					2015-10-06 19:56:42
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:26:04', u'11']
	part3_correct_attempt
					['0:26:30', u'11(1/(2^11))']
	part4_incorrect_attempt
					('0:27:15', u'1 - (11(1/(2^11)))')
	part4_correct_attempt
					['0:31:52', u'1 - (1(1/(2^11)) - 2/(2^11))']

95 Student ID:vsosnovs

	first_attempt
					2015-10-04 17:40:35
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:20:15', u'9!/8!']
	part3_correct_attempt
					['0:20:45', u'9/512']
	part4_incorrect_attempt
					('0:42:00', u'512-9')
					('0:47:13', u'512-18')
	part4_correct_attempt
					['0:47:47', u'511/512']

96 Student ID:k5law

	first_attempt
					2015-10-05 01:55:27
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:06:23', u'(9!)/(8!)']
	part3_correct_attempt
					['0:06:23', u'((9!)/(8!))/2^9']
	part4_incorrect_attempt
					('0:10:29', u'1-((9!)/(9!))')
					('0:36:11', u'(1-((9!)/(9!)))/2^9')
					('0:40:10', u'1/(2^9)')
	part4_correct_attempt
					['0:50:09', u'1-(1/(2^9))']

97 Student ID:p4kumar

	first_attempt
					2015-10-08 19:05:26
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:00:00', u'10']
	part3_correct_attempt
					['0:00:00', u'10/(2^10)']
	part4_incorrect_attempt
					('0:00:00', u'857/(2^10)')
					('0:01:06', u'1014/(2^10)')
					('0:20:59', u'(1024 - 11)/(2^10)')
	part4_correct_attempt
					['0:23:12', u'1022/(2^10)']

98 Student ID:amquinte

	first_attempt
					2015-10-05 22:19:48
	part1_correct_attempt
					['0:00:00', u'2048']
	part2_correct_attempt
					['0:04:04', u'11']
	part3_correct_attempt
					['0:04:04', u'11/2048']
	part4_incorrect_attempt
					('0:04:04', u'12376/2048')
	part4_correct_attempt
					['0:12:09', u'1-(1/2048)']

99 Student ID:jmiclat

	first_attempt
					2015-10-08 00:00:28
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['20:11:38', u'11']
	part3_correct_attempt
					['20:11:48', u'11/2^11']
	part4_incorrect_attempt
					('20:15:41', u'11 * 11!/10')
					('20:18:12', u'C(11,10)')
	part4_correct_attempt
					['20:19:46', u'(2^11 - 1)/2^11']

100 Student ID:bmilton

	first_attempt
					2015-10-04 01:42:25
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:01:06', u'10']
	part3_correct_attempt
					['0:02:50', u'10/1024']
	part4_incorrect_attempt
					('0:05:14', u'10/1024')
					('0:06:17', u'C(10,1)*(1/2)^9')
					('0:06:34', u'(1/2)^9 * 10')
					('0:12:56', u'1014/1024')
	part4_correct_attempt
					['0:18:07', u'1023/1024']

101 Student ID:jhc010

	first_attempt
					2015-10-08 14:26:02
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:00:00', u'9']
	part3_correct_attempt
					['0:00:00', u'9/2^9']
	part4_incorrect_attempt
					('0:00:00', u'2^9-1')
					('0:00:16', u'2^9-2')
	part4_correct_attempt
					['0:01:10', u'(2^9-1)/(2^9)']

102 Student ID:rsmurlo

	first_attempt
					2015-10-08 01:54:38
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:00:51', u'9']
	part3_correct_attempt
					['0:00:00', u'9/2^9']
	part4_incorrect_attempt
					('0:02:29', u'(2^9-9)/2^9')
	part4_correct_attempt
					['0:04:13', u'(2^9-1)/2^9']

103 Student ID:dkostins

	first_attempt
					2015-10-05 21:07:11
	part1_correct_attempt
					['0:00:00', u'2048']
	part2_correct_attempt
					['0:01:59', u'11']
	part3_correct_attempt
					['0:06:07', u'11/2048']
	part4_incorrect_attempt
					('0:07:25', u'(11+10+9+8+7+6+5+4+3+2+1)/2048')
					('0:08:10', u'(11!)/2048')
					('0:08:16', u'(10!)/2048')
	part4_correct_attempt
					['4:38:27', u'2046/2048']

104 Student ID:agarango

	first_attempt
					2015-10-08 20:23:20
	part1_correct_attempt
					['0:00:00', u'2048']
	part2_correct_attempt
					['0:00:00', u'11']
	part3_correct_attempt
					['0:00:00', u'11/2048']
	part4_incorrect_attempt
					('2:13:00', u'2037/2048')
					('2:13:07', u'2038/2048')
	part4_correct_attempt
					['2:13:16', u'2046/2048']

105 Student ID:twsalim

	first_attempt
					2015-10-04 00:20:29
	part1_correct_attempt
					['0:00:00', u'2048']
	part2_correct_attempt
					['0:00:00', u'11']
	part3_correct_attempt
					['0:00:00', u'0.00537']
	part4_incorrect_attempt
					('0:00:00', u'0.9946')
					('0:03:36', u'99.994')
					('0:13:34', u'0.99463')
	part4_correct_attempt
					['0:15:09', u'0.99951']

106 Student ID:s6deng

	first_attempt
					2015-10-06 21:05:43
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:00:00', u'10']
	part3_correct_attempt
					['0:03:59', u'10/(2^10)']
	part4_incorrect_attempt
					('0:03:59', u'[(10!)(10!)*(10!/2!)*(10!/3!)*(10!/4!)*(10!/5!)*(10!/6!)*(10!/7!)*(10!/8!)*10]/(2^10)')
					('0:06:03', u'[(10!/10!)(10!/9!)*(10!/(8!2!))*(10!/(7!3!))*(10!/(6!4!))*(10!/(5!5!))*(10!/(6!4!))*(10!/(7!3!))*(10!/(8!2!))*10]/(2^10)')
					('0:08:00', u'[10*(10!/(2!8!))*(10!/(3!7!))*(10!/(4!6!))*(10!/(5!5!))]/(2^10)')
					('0:08:46', u'[10*(10!/(2!8!))*(10!/(3!7!))*(10!/(4!6!))*(10!/(5!5!))*(10!/(6!/4!))*(10!/(7!3!))*(10!/(8!2!))*10]/(2^10)')
					('0:12:32', u'[10+(10!/(2!8!))+(10!/(3!7!))+(10!/(4!6!))+(10!/(5!5!))+(10!/(6!/4!))+(10!/(7!3!))+(10!/(8!2!))+10]/(2^10)')
					('0:13:06', u'[(10!/(0!10!))+(10!/(1!9!))+(10!/(2!8!))+(10!/(3!7!))+(10!/(4!6!))+(10!/(5!5!))+(10!/(6!/4!))+(10!/(7!3!))+(10!/(8!2!))+10]/(2^10)')
					('0:13:19', u'[(10!/(0!10!))+(10!/(1!9!))+(10!/(2!8!))+(10!/(3!7!))+(10!/(4!6!))+(10!/(5!5!))+(10!/(6!/4!))+(10!/(7!3!))+(10!/(8!2!))+10]*(2^10)')
					('0:13:47', u'[(10!/(0!10!))+(10!/(1!9!))+(10!/(2!8!))+(10!/(3!7!))+(10!/(4!6!))+(10!/(5!5!))+(10!/(6!4!))+(10!/(7!3!))+(10!/(8!2!))+10]*(2^10)')
	part4_correct_attempt
					['0:14:05', u'[(10!/(0!10!))+(10!/(1!9!))+(10!/(2!8!))+(10!/(3!7!))+(10!/(4!6!))+(10!/(5!5!))+(10!/(6!4!))+(10!/(7!3!))+(10!/(8!2!))+10]/(2^10)']

107 Student ID:achinn

	first_attempt
					2015-10-06 19:28:30
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:00:00', u'10']
	part3_correct_attempt
					['0:00:00', u'10/(2^10)']
	part4_incorrect_attempt
					('0:00:00', u'(2^10)-1')
	part4_correct_attempt
					['0:02:06', u'((2^10)-1)/2^10']

108 Student ID:kalang

	first_attempt
					2015-10-05 22:33:36
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:02:01', u'9']
	part3_correct_attempt
					['0:01:35', u'1/(2^9)*9']
	part4_incorrect_attempt
					('0:02:46', u'1/(2^9)*2^8')
					('0:03:30', u'8/9')
					('0:06:29', u'2^8/2^9')
					('0:11:18', u'9!/(8!*1!)')
					('0:12:28', u'9/2^9')
					('0:26:54', u'1-(1/2^9)*(9/2^9)*(36/2^9)')
	part4_correct_attempt
					['0:28:48', u'1-(1/2^9)']

109 Student ID:jcl084

	first_attempt
					2015-10-08 19:25:12
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:02:58', u'10']
	part3_correct_attempt
					['0:08:31', u'10 * (1/2)^10']
	part4_incorrect_attempt
					('0:09:49', u'10 * (1/2)^10 /2')
					('0:14:56', u'1/10')
					('0:15:47', u'C(10,1)')
					('0:21:31', u'1- (10 * (1/2)^10 )')
	part4_correct_attempt
					['0:23:53', u'1-(1/(2^10))']

110 Student ID:mcatozzi

	first_attempt
					2015-10-06 23:18:51
	part1_correct_attempt
					['0:00:00', u'512']
	part2_correct_attempt
					['0:00:56', u'9']
	part3_correct_attempt
					['0:02:23', u'9/512']
	part4_incorrect_attempt
					('0:02:45', u'503/512')
					('0:16:55', u'502/512')
					('0:32:44', u'426/512')
					('0:32:58', u'427/512')
					('0:36:45', u'503/512')
					('0:45:07', u'510/512')
	part4_correct_attempt
					['0:52:44', u'511/512']

111 Student ID:aadhakal

	first_attempt
					2015-10-05 07:24:25
	part1_correct_attempt
					['0:00:00', u'1024']
	part2_correct_attempt
					['-1 day, 23:57:19', u'10']
	part3_correct_attempt
					['0:08:17', u'10/1024']
	part4_incorrect_attempt
					('0:08:17', u'11/1024')
					('0:09:35', u'1013/1024')
					('0:11:58', u'372400/1024')
	part4_correct_attempt
					['12:52:14', u'1023/1024']

112 Student ID:jnn015

	first_attempt
					2015-10-03 20:45:32
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:02:15', u'11']
	part3_correct_attempt
					['0:02:15', u'11/2^11']
	part4_incorrect_attempt
					('0:02:15', u'(2^11 - 11)/2^11')
	part4_correct_attempt
					['0:03:24', u'(2^11 - 1)/2^11']

113 Student ID:dpereira

	first_attempt
					2015-10-03 20:57:44
	part4_incorrect_attempt
					('0:00:00', u'(2^10 - 10)/(2^10)')
	part4_correct_attempt
					['0:01:49', u'1 - (1/(2^10))']

114 Student ID:hmshah

	first_attempt
					2015-10-06 01:52:51
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:13:31', u'11']
	part3_correct_attempt
					['0:13:49', u'11/2048']
	part4_incorrect_attempt
					('0:16:55', u'(2048-11)/2048')
					('0:17:01', u'(2048-10)/2048')

115 Student ID:dtea

	first_attempt
					2015-10-08 18:56:06
	part1_correct_attempt
					['0:00:00', u'2**10']
	part2_correct_attempt
					['0:02:04', u'10']
	part3_correct_attempt
					['2:29:34', u'10/2**10']
	part4_incorrect_attempt
					('2:29:46', u'(2*(10!))/2**10')
					('2:43:39', u'(((10!/(1!(10-1)!))+(10!/(2!(10-2)!))+(10!/(3!(10-3)!))+(10!/(4!(10-4)!)))*2+(5!/(5!(10-5)!)))/2**10')
	part4_correct_attempt
					['2:43:54', u'(((10!/(1!(10-1)!))+(10!/(2!(10-2)!))+(10!/(3!(10-3)!))+(10!/(4!(10-4)!)))*2+(10!/(5!(10-5)!)))/2**10']

116 Student ID:lahawkin

	first_attempt
					2015-10-03 17:54:16
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:05:04', u'9']
	part3_correct_attempt
					['0:06:10', u'9/(2^9)']
	part4_incorrect_attempt
					('5 days, 5:14:42', u'8/(2^9)')
					('5 days, 5:15:13', u'2/(2^9)')
	part4_correct_attempt
					['5 days, 5:24:29', u'1-(1/(2^9))']

117 Student ID:yig015

	first_attempt
					2015-10-08 07:11:22
	part1_correct_attempt
					['0:00:00', u'1024']
	part2_correct_attempt
					['0:00:00', u'10']
	part3_correct_attempt
					['0:00:00', u'10/1024']
	part4_incorrect_attempt
					('0:00:00', u'1014/1024')
	part4_correct_attempt
					['0:42:23', u'1023/1024']

118 Student ID:hpc001

	first_attempt
					2015-10-03 00:07:11
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:00:00', u'9']
	part3_correct_attempt
					['-1 day, 23:57:24', u'9/512']
	part4_incorrect_attempt
					('0:05:49', u'56/512')
					('0:06:23', u'456/512')
	part4_correct_attempt
					['0:06:55', u'511/512']

119 Student ID:kosung

	first_attempt
					2015-10-07 06:17:44
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:00:31', u'11']
	part3_correct_attempt
					['0:00:31', u'11/2^11']
	part4_incorrect_attempt
					('0:00:31', u'12/2^11')
	part4_correct_attempt
					['0:01:59', u'(2^11-1)/2^11']

120 Student ID:s2chaudh

	first_attempt
					2015-10-08 06:12:52
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:04:27', u'9']
	part3_correct_attempt
					['0:02:41', u'9/512']
	part4_incorrect_attempt
					('0:16:27', u'(9+36+84+126+126+84+36+9)/512')
	part4_correct_attempt
					['0:16:54', u'(9+36+84+126+126+84+36+9+1)/512']

121 Student ID:c3chung

	first_attempt
					2015-10-07 23:22:29
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:00:00', u'10']
	part3_correct_attempt
					['0:00:00', u'10/(2^10)']
	part4_incorrect_attempt
					('0:00:00', u'(2^10)-1')
	part4_correct_attempt
					['0:04:50', u'[(2^10)-1]/(2^10)']

122 Student ID:ajvanega

	first_attempt
					2015-10-02 21:17:52
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:03:12', u'11']
	part3_correct_attempt
					['0:03:56', u'11/(2^11)']
	part4_incorrect_attempt
					('0:06:04', u'2^10/2^11')
					('0:07:24', u'((2^10)-1)/2^11')
					('0:26:45', u'10/(2^11)')
					('0:38:20', u'(2^9)/(2^11)')
					('0:38:32', u'(2^10)/(2^11)')
					('4 days, 4:26:41', u'10/11')
					('4 days, 4:30:55', u'2^10/(2^11)')
					('4 days, 5:03:36', u'11/(2^11)')
					('4 days, 5:12:23', u'1-(11/(2^11)+(1/2^11))')
	part4_correct_attempt
					['4 days, 5:23:34', u'1-(1/(2^11))']

123 Student ID:mtrafeca

	first_attempt
					2015-10-02 06:02:13
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:00:26', u'10']
	part3_correct_attempt
					['12:32:46', u'10/(2^10)']
	part4_incorrect_attempt
					('12:43:18', u'(10!/(9!))/(2^10)')
					('12:44:19', u'C(10,9)')
	part4_correct_attempt
					['6 days, 13:29:10', u'1-(1/2^10)']

124 Student ID:kgrozav

	first_attempt
					2015-10-02 21:09:10
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:02:13', u'11']
	part3_correct_attempt
					['0:02:41', u'11/(2^11)']
	part4_incorrect_attempt
					('0:05:05', u'11/(2^11)')
					('0:23:23', u'11!/(2^11)')
					('0:30:36', u'121/(2^11)')

125 Student ID:whcombs

	first_attempt
					2015-10-07 18:57:17
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:20:10', u'(9!)/(1!(9-1)!)']
	part3_correct_attempt
					['0:21:39', u'9/(2^9)']
	part4_incorrect_attempt
					('0:23:03', u'((9!)/(8!(9-8)!))/2^9')
					('0:27:09', u'9!/(8!(9-8)!)/(2^9)')
					('0:35:40', u'510/(2^9)')
					('0:37:42', u'9!/(2!(9-2)!)/(2^9)')
					('0:46:08', u'510/(2^9)')
					('0:47:07', u'501/(2^9)')
	part4_correct_attempt
					['0:48:56', u'511/(2^9)']

126 Student ID:j2phung

	first_attempt
					2015-10-06 18:58:26
	part1_correct_attempt
					['0:00:00', u'1024']
	part2_correct_attempt
					['0:07:01', u'10']
	part3_correct_attempt
					['0:07:01', u'10/1024']
	part4_incorrect_attempt
					('0:07:01', u'1013/1024')
					('0:08:03', u'1014/1024')
	part4_correct_attempt
					['0:09:31', u'1023/1024']












## Part 5

### (251) Mistake Group ['R.1'] of size 251
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|9!/[6!*(9-6)!]/(2^9)	|4/(2**9)	|[('R.1', 512.0, u'2^9', u'2**9')]	|
|1	|9!/[6!*(9-6)!]/(2^9)	|6/(2**9)	|[('R.1', 512.0, u'2^9', u'2**9')]	|
|2	|10!/[6!*(10-6)!]/(2^10)	|2^4/2^10	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|3	|9!/[6!*(9-6)!]/(2^9)	|1/(2^9)	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|4	|11!/[6!*(11-6)!]/(2^11)	|32/2048	|[('R.1', 2048.0, u'2^11', u'2048')]	|
|5	|10!/[6!*(10-6)!]/(2^10)	|6/(2^10)	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|6	|10!/[6!*(10-6)!]/(2^10)	|10*4/(2^10)	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|7	|10!/[6!*(10-6)!]/(2^10)	|10*6/(2^10)	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|8	|10!/[6!*(10-6)!]/(2^10)	|10*9*8*7/(2^10)	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|9	|10!/[6!*(10-6)!]/(2^10)	|60/(2^10)	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|10	|9!/[6!*(9-6)!]/(2^9)	|1/512	|[('R.1', 512.0, u'2^9', u'512')]	|
|11	|9!/[6!*(9-6)!]/(2^9)	|148/512	|[('R.1', 512.0, u'2^9', u'512')]	|
|12	|9!/[6!*(9-6)!]/(2^9)	|(2^6)/(2^9)	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|13	|9!/[6!*(9-6)!]/(2^9)	|6/(2^9)	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|14	|11!/[6!*(11-6)!]/(2^11)	|6/(2^11)	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|15	|11!/[6!*(11-6)!]/(2^11)	|7/(2^11)	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|16	|11!/[6!*(11-6)!]/(2^11)	|11/(2^11)	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|17	|9!/[6!*(9-6)!]/(2^9)	|9/2^9	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|18	|11!/[6!*(11-6)!]/(2^11)	|30/(2^11)	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|19	|11!/[6!*(11-6)!]/(2^11)	|35/(2^11)	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|20	|10!/[6!*(10-6)!]/(2^10)	|[10!/6!4!]/[2^10]	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|21	|11!/[6!*(11-6)!]/(2^11)	|5^6/(2^11)	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|22	|11!/[6!*(11-6)!]/(2^11)	|31/(2^11)	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|23	|11!/[6!*(11-6)!]/(2^11)	|36/2^11	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|24	|11!/[6!*(11-6)!]/(2^11)	|35/2^11	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|25	|11!/[6!*(11-6)!]/(2^11)	|(6+5+4+3+2+1)/2^11	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|26	|11!/[6!*(11-6)!]/(2^11)	|(6!)/2^11	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|27	|9!/[6!*(9-6)!]/(2^9)	|168/512	|[('R.1', 512.0, u'2^9', u'512')]	|
|28	|10!/[6!*(10-6)!]/(2^10)	|10/(2^10)	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|29	|11!/[6!*(11-6)!]/(2^11)	|(11! / 6! * 5!) / 2^11	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|30	|11!/[6!*(11-6)!]/(2^11)	|11/2^11	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|31	|11!/[6!*(11-6)!]/(2^11)	|(C(11,6)/2)/2^11	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|32	|10!/[6!*(10-6)!]/(2^10)	|1/1024	|[('R.1', 1024.0, u'2^10', u'1024')]	|
|33	|11!/[6!*(11-6)!]/(2^11)	|[(11!)/(6!)(11!-6!)]/(2^11)	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|34	|9!/[6!*(9-6)!]/(2^9)	|9/512	|[('R.1', 512.0, u'2^9', u'512')]	|
|35	|9!/[6!*(9-6)!]/(2^9)	|27/512	|[('R.1', 512.0, u'2^9', u'512')]	|
|36	|9!/[6!*(9-6)!]/(2^9)	|36/512	|[('R.1', 512.0, u'2^9', u'512')]	|
|37	|9!/[6!*(9-6)!]/(2^9)	|6!/512	|[('R.1', 512.0, u'2^9', u'512')]	|
|38	|9!/[6!*(9-6)!]/(2^9)	|3!/512	|[('R.1', 512.0, u'2^9', u'512')]	|
|39	|11!/[6!*(11-6)!]/(2^11)	|1/2^11	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|40	|11!/[6!*(11-6)!]/(2^11)	|(1/2^11)	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|41	|11!/[6!*(11-6)!]/(2^11)	|12!/2^11	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|42	|10!/[6!*(10-6)!]/(2^10)	|4!/1024	|[('R.1', 1024.0, u'2^10', u'1024')]	|
|43	|10!/[6!*(10-6)!]/(2^10)	|6!/1024	|[('R.1', 1024.0, u'2^10', u'1024')]	|
|44	|11!/[6!*(11-6)!]/(2^11)	|12!/6!/6!/2^11	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|45	|10!/[6!*(10-6)!]/(2^10)	|6/1024	|[('R.1', 1024.0, u'2^10', u'1024')]	|
|46	|11!/[6!*(11-6)!]/(2^11)	|64/2048	|[('R.1', 2048.0, u'2^11', u'2048')]	|
|47	|11!/[6!*(11-6)!]/(2^11)	|1/2048	|[('R.1', 2048.0, u'2^11', u'2048')]	|
|48	|10!/[6!*(10-6)!]/(2^10)	|10 * 9 * 8 * 7/ 2^10	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|49	|10!/[6!*(10-6)!]/(2^10)	|10 * 9 * 8 * 7 / 6!/ 2^10	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|50	|10!/[6!*(10-6)!]/(2^10)	|10 * 9 * 8 * 7 / 2^10	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|51	|10!/[6!*(10-6)!]/(2^10)	|10 * 9 * 8 * 7 * 6* 5/ 2^10	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|52	|11!/[6!*(11-6)!]/(2^11)	|(11*10*9*8*7)/(2^11)	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|53	|10!/[6!*(10-6)!]/(2^10)	|P(10,4)/1024	|[('R.1', 1024.0, u'2^10', u'1024')]	|
|54	|10!/[6!*(10-6)!]/(2^10)	|10*9*8*7/1024	|[('R.1', 1024.0, u'2^10', u'1024')]	|
|55	|10!/[6!*(10-6)!]/(2^10)	|10*9*8*7*6*5/1024	|[('R.1', 1024.0, u'2^10', u'1024')]	|
|56	|9!/[6!*(9-6)!]/(2^9)	|6/ 2 ^9	|[('R.1', 512.0, u'2^9', u'2 ^9')]	|
|57	|9!/[6!*(9-6)!]/(2^9)	|6/2^9	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|58	|11!/[6!*(11-6)!]/(2^11)	|16/2048	|[('R.1', 2048.0, u'2^11', u'2048')]	|
|59	|9!/[6!*(9-6)!]/(2^9)	|(9*8*7)/512	|[('R.1', 512.0, u'2^9', u'512')]	|
|60	|9!/[6!*(9-6)!]/(2^9)	|9*8*7*6/(4*3*2)/2^9	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|61	|11!/[6!*(11-6)!]/(2^11)	|[11!/4!*7!]/[2^11]	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|62	|11!/[6!*(11-6)!]/(2^11)	|2^6/2^11	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|63	|9!/[6!*(9-6)!]/(2^9)	|(9!/6!* 3!)/2^9	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|64	|11!/[6!*(11-6)!]/(2^11)	|4/2^11	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|65	|9!/[6!*(9-6)!]/(2^9)	|9/(2^9)	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|66	|10!/[6!*(10-6)!]/(2^10)	|(1/9)^6/2^10	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|67	|9!/[6!*(9-6)!]/(2^9)	|7/512	|[('R.1', 512.0, u'2^9', u'512')]	|
|68	|9!/[6!*(9-6)!]/(2^9)	|6/512	|[('R.1', 512.0, u'2^9', u'512')]	|
|69	|10!/[6!*(10-6)!]/(2^10)	|5040/1024	|[('R.1', 1024.0, u'2^10', u'1024')]	|
|70	|11!/[6!*(11-6)!]/(2^11)	|1/(2^11)	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|71	|11!/[6!*(11-6)!]/(2^11)	|(11*10*9*8*7*6)/(2^11)	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|72	|9!/[6!*(9-6)!]/(2^9)	|7/(2^9)	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|73	|10!/[6!*(10-6)!]/(2^10)	|2/(2^10)	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|74	|10!/[6!*(10-6)!]/(2^10)	|7/1024	|[('R.1', 1024.0, u'2^10', u'1024')]	|
|75	|10!/[6!*(10-6)!]/(2^10)	|(2^6)/(2^10)	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|76	|10!/[6!*(10-6)!]/(2^10)	|840/1024	|[('R.1', 1024.0, u'2^10', u'1024')]	|
|77	|10!/[6!*(10-6)!]/(2^10)	|10/1024	|[('R.1', 1024.0, u'2^10', u'1024')]	|
|78	|9!/[6!*(9-6)!]/(2^9)	|(9*8*7) / (2^9)	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|79	|9!/[6!*(9-6)!]/(2^9)	|(9!/6!3!) / (2^9)	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|80	|11!/[6!*(11-6)!]/(2^11)	|6/2**11	|[('R.1', 2048.0, u'2^11', u'2**11')]	|
|81	|11!/[6!*(11-6)!]/(2^11)	|11/2**11	|[('R.1', 2048.0, u'2^11', u'2**11')]	|
|82	|11!/[6!*(11-6)!]/(2^11)	|7/2**11	|[('R.1', 2048.0, u'2^11', u'2**11')]	|
|83	|11!/[6!*(11-6)!]/(2^11)	|(6!/(11-6)!)/2^11	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|84	|9!/[6!*(9-6)!]/(2^9)	|(9*8*7)/2^9	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|85	|9!/[6!*(9-6)!]/(2^9)	|(9!/3!6!)/2^9	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|86	|11!/[6!*(11-6)!]/(2^11)	|(11!/6!(11-6)!)/2^11	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|87	|11!/[6!*(11-6)!]/(2^11)	|11/2048	|[('R.1', 2048.0, u'2^11', u'2048')]	|
|88	|11!/[6!*(11-6)!]/(2^11)	|55/2048	|[('R.1', 2048.0, u'2^11', u'2048')]	|
|89	|11!/[6!*(11-6)!]/(2^11)	|(6!)/2048	|[('R.1', 2048.0, u'2^11', u'2048')]	|
|90	|9!/[6!*(9-6)!]/(2^9)	|2/(2^9)	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|91	|10!/[6!*(10-6)!]/(2^10)	|(10-6)!/(2^10)	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|92	|10!/[6!*(10-6)!]/(2^10)	|210 * (.5^4) *(.5^6)/(2^10)	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|93	|11!/[6!*(11-6)!]/(2^11)	|P(11,5)/(2^11)	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|94	|11!/[6!*(11-6)!]/(2^11)	|(11!/6!5!)/2^11	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|95	|11!/[6!*(11-6)!]/(2^11)	|(11!/6!5!)/(2**11)	|[('R.1', 2048.0, u'2^11', u'2**11')]	|
|96	|11!/[6!*(11-6)!]/(2^11)	|6!/(2!*4!)/(2^11)	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|97	|10!/[6!*(10-6)!]/(2^10)	|4!/2^10	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|98	|11!/[6!*(11-6)!]/(2^11)	|6/2^11	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|99	|11!/[6!*(11-6)!]/(2^11)	|6!/2^11	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|100	|11!/[6!*(11-6)!]/(2^11)	|66/2^11	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|101	|11!/[6!*(11-6)!]/(2^11)	|6*5/2^11	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|102	|11!/[6!*(11-6)!]/(2^11)	|6!*5/2^11	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|103	|11!/[6!*(11-6)!]/(2^11)	|6!*5!/2^11	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|104	|11!/[6!*(11-6)!]/(2^11)	|(6!/(6*(11-6)))/2^11	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|105	|10!/[6!*(10-6)!]/(2^10)	|7/(2^10)	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|106	|9!/[6!*(9-6)!]/(2^9)	|4/512	|[('R.1', 512.0, u'2^9', u'512')]	|
|107	|11!/[6!*(11-6)!]/(2^11)	|P(11,6)/2048	|[('R.1', 2048.0, u'2^11', u'2048')]	|
|108	|11!/[6!*(11-6)!]/(2^11)	|(11!/5!6!)/2048	|[('R.1', 2048.0, u'2^11', u'2048')]	|
|109	|11!/[6!*(11-6)!]/(2^11)	|(11*10*9*8*7)/((2^11))	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|110	|10!/[6!*(10-6)!]/(2^10)	|10/2^10	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|111	|11!/[6!*(11-6)!]/(2^11)	|5/(2^11)	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|112	|11!/[6!*(11-6)!]/(2^11)	|6/2048	|[('R.1', 2048.0, u'2^11', u'2048')]	|
|113	|11!/[6!*(11-6)!]/(2^11)	|5/2048	|[('R.1', 2048.0, u'2^11', u'2048')]	|
|114	|11!/[6!*(11-6)!]/(2^11)	|2/2048	|[('R.1', 2048.0, u'2^11', u'2048')]	|
|115	|11!/[6!*(11-6)!]/(2^11)	|3/2048	|[('R.1', 2048.0, u'2^11', u'2048')]	|
|116	|11!/[6!*(11-6)!]/(2^11)	|4/2048	|[('R.1', 2048.0, u'2^11', u'2048')]	|
|117	|11!/[6!*(11-6)!]/(2^11)	|7/2048	|[('R.1', 2048.0, u'2^11', u'2048')]	|
|118	|11!/[6!*(11-6)!]/(2^11)	|8/2048	|[('R.1', 2048.0, u'2^11', u'2048')]	|
|119	|11!/[6!*(11-6)!]/(2^11)	|9/2048	|[('R.1', 2048.0, u'2^11', u'2048')]	|
|120	|11!/[6!*(11-6)!]/(2^11)	|6!/2048	|[('R.1', 2048.0, u'2^11', u'2048')]	|
|121	|11!/[6!*(11-6)!]/(2^11)	|6/11/2048	|[('R.1', 2048.0, u'2^11', u'2048')]	|
|122	|9!/[6!*(9-6)!]/(2^9)	|(2^3)/(2^9)	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|123	|9!/[6!*(9-6)!]/(2^9)	|8/512	|[('R.1', 512.0, u'2^9', u'512')]	|
|124	|9!/[6!*(9-6)!]/(2^9)	|12/512	|[('R.1', 512.0, u'2^9', u'512')]	|
|125	|10!/[6!*(10-6)!]/(2^10)	|10*9*8*7/2^10	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|126	|9!/[6!*(9-6)!]/(2^9)	|9^3/2^9	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|127	|9!/[6!*(9-6)!]/(2^9)	|27/2^9	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|128	|9!/[6!*(9-6)!]/(2^9)	|18/2^9	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|129	|9!/[6!*(9-6)!]/(2^9)	|(9!/6!3!)/2^9	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|130	|10!/[6!*(10-6)!]/(2^10)	|35/(2^10)	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|131	|10!/[6!*(10-6)!]/(2^10)	|75/(2^10)	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|132	|11!/[6!*(11-6)!]/(2^11)	|(11!/(6!)*(5!))/(2^11)	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|133	|9!/[6!*(9-6)!]/(2^9)	|3/(2^9)	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|134	|11!/[6!*(11-6)!]/(2^11)	|55440/(2^11)	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|135	|11!/[6!*(11-6)!]/(2^11)	|(55440/430)/(2^11)	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|136	|11!/[6!*(11-6)!]/(2^11)	|17/(2^11)	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|137	|10!/[6!*(10-6)!]/(2^10)	|[(1^6)*(2^(10-6))]/[2^10]	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|138	|10!/[6!*(10-6)!]/(2^10)	|[(1^6)*(1^(10-6))]/[2^10]	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|139	|11!/[6!*(11-6)!]/(2^11)	|(462/(6!))/(2^11)	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|140	|11!/[6!*(11-6)!]/(2^11)	|(11*5)/(2^11)	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|141	|10!/[6!*(10-6)!]/(2^10)	|370/1024	|[('R.1', 1024.0, u'2^10', u'1024')]	|
|142	|11!/[6!*(11-6)!]/(2^11)	|(2^5)/(2^11)	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|143	|11!/[6!*(11-6)!]/(2^11)	|(6*2^5)/(2^11)	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|144	|11!/[6!*(11-6)!]/(2^11)	|(C(11,6)*2^5)/(2^11)	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|145	|11!/[6!*(11-6)!]/(2^11)	|(6*5^2)/(2^11)	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|146	|11!/[6!*(11-6)!]/(2^11)	|2^5/2^11	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|147	|11!/[6!*(11-6)!]/(2^11)	|11* 10 * 9 * 8 * 7/2^11	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|148	|11!/[6!*(11-6)!]/(2^11)	|[11*10*9*8*7]/2048	|[('R.1', 2048.0, u'2^11', u'2048')]	|
|149	|11!/[6!*(11-6)!]/(2^11)	|[11*10*9*8*7*6]/2048	|[('R.1', 2048.0, u'2^11', u'2048')]	|
|150	|9!/[6!*(9-6)!]/(2^9)	|126/2^9	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|151	|10!/[6!*(10-6)!]/(2^10)	|1/2^10	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|152	|10!/[6!*(10-6)!]/(2^10)	|(10 6)/1024	|[('R.1', 1024.0, u'2^10', u'1024')]	|
|153	|10!/[6!*(10-6)!]/(2^10)	|(10*9*8*7)/2^10	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|154	|10!/[6!*(10-6)!]/(2^10)	|6/2^10	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|155	|10!/[6!*(10-6)!]/(2^10)	|(10*9*8*7*6*5)/2^10	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|156	|10!/[6!*(10-6)!]/(2^10)	|(10*7)/2^10	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|157	|10!/[6!*(10-6)!]/(2^10)	|204.8/1024	|[('R.1', 1024.0, u'2^10', u'1024')]	|
|158	|10!/[6!*(10-6)!]/(2^10)	|102.4/1024	|[('R.1', 1024.0, u'2^10', u'1024')]	|
|159	|10!/[6!*(10-6)!]/(2^10)	|(1024/11)/1024	|[('R.1', 1024.0, u'2^10', u'1024')]	|
|160	|9!/[6!*(9-6)!]/(2^9)	|(9*8*7)/(2^9)	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|161	|10!/[6!*(10-6)!]/(2^10)	|10/2**10	|[('R.1', 1024.0, u'2^10', u'2**10')]	|
|162	|9!/[6!*(9-6)!]/(2^9)	|(8*7*6)/(2^9)	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|163	|9!/[6!*(9-6)!]/(2^9)	|18/512	|[('R.1', 512.0, u'2^9', u'512')]	|
|164	|11!/[6!*(11-6)!]/(2^11)	|(462*6!)/(2^11)	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|165	|9!/[6!*(9-6)!]/(2^9)	|24/512	|[('R.1', 512.0, u'2^9', u'512')]	|
|166	|9!/[6!*(9-6)!]/(2^9)	|23/512	|[('R.1', 512.0, u'2^9', u'512')]	|
|167	|9!/[6!*(9-6)!]/(2^9)	|52/512	|[('R.1', 512.0, u'2^9', u'512')]	|
|168	|10!/[6!*(10-6)!]/(2^10)	|(6!)/2**10	|[('R.1', 1024.0, u'2^10', u'2**10')]	|
|169	|11!/[6!*(11-6)!]/(2^11)	|14784/2048	|[('R.1', 2048.0, u'2^11', u'2048')]	|
|170	|10!/[6!*(10-6)!]/(2^10)	|(10!/6!(10-6)!)/2**10	|[('R.1', 1024.0, u'2^10', u'2**10')]	|
|171	|9!/[6!*(9-6)!]/(2^9)	|21/(2^9)	|[('R.1', 512.0, u'2^9', u'2^9')]	|
|172	|10!/[6!*(10-6)!]/(2^10)	|12/(2^10)	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|173	|10!/[6!*(10-6)!]/(2^10)	|8/(2^10)	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|174	|10!/[6!*(10-6)!]/(2^10)	|5/(2^10)	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|175	|11!/[6!*(11-6)!]/(2^11)	|55440/2^11	|[('R.1', 2048.0, u'2^11', u'2^11')]	|
|176	|10!/[6!*(10-6)!]/(2^10)	|1/(2^10)	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|177	|10!/[6!*(10-6)!]/(2^10)	|120/(2^10)	|[('R.1', 1024.0, u'2^10', u'2^10')]	|
|178	|10!/[6!*(10-6)!]/(2^10)	|40 / 2^10	|[('R.1', 1024.0, u'2^10', u'2^10')]	|




### (46) Mistake Group redirect of size 46




### (37) Mistake Group Digits of size 37




### (24) Mistake Group ['R.0.0', 'R.1'] of size 24
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|10!/[6!*(10-6)!]/(2^10)	|[10!/4!]/[2^10]	|[('R.0.0', 3628800, u'10!', u'10!'), ('R.1', 1024.0, u'2^10', u'2^10')]	|
|1	|11!/[6!*(11-6)!]/(2^11)	|[(11!)/(6!)]/(2^11)	|[('R.0.0', 39916800, u'11!', u'11!'), ('R.1', 2048.0, u'2^11', u'2^11')]	|
|2	|11!/[6!*(11-6)!]/(2^11)	|[11!/(4!*7!)]/[2^11]	|[('R.0.0', 39916800, u'11!', u'11!'), ('R.1', 2048.0, u'2^11', u'2^11')]	|
|3	|9!/[6!*(9-6)!]/(2^9)	|9!/(9-6)!/2^9	|[('R.0.0', 362880, u'9!', u'9!'), ('R.1', 512.0, u'2^9', u'2^9')]	|
|4	|10!/[6!*(10-6)!]/(2^10)	|((10!)/(9!(10!-9!)))/1024	|[('R.0.0', 3628800, u'10!', u'10!'), ('R.1', 1024.0, u'2^10', u'1024')]	|
|5	|9!/[6!*(9-6)!]/(2^9)	|((9!)/(2!*6!))/2^9	|[('R.0.0', 362880, u'9!', u'9!'), ('R.1', 512.0, u'2^9', u'2^9')]	|
|6	|10!/[6!*(10-6)!]/(2^10)	|[10!/(10!-6!)]/[2^(10)]	|[('R.0.0', 3628800, u'10!', u'10!'), ('R.1', 1024.0, u'2^10', u'2^(10)')]	|
|7	|11!/[6!*(11-6)!]/(2^11)	|(11!/6!)/(2^11)	|[('R.0.0', 39916800, u'11!', u'11!'), ('R.1', 2048.0, u'2^11', u'2^11')]	|
|8	|10!/[6!*(10-6)!]/(2^10)	|(10!/4!)/1024	|[('R.0.0', 3628800, u'10!', u'10!'), ('R.1', 1024.0, u'2^10', u'1024')]	|
|9	|10!/[6!*(10-6)!]/(2^10)	|(10!/6!)/1024	|[('R.0.0', 3628800, u'10!', u'10!'), ('R.1', 1024.0, u'2^10', u'1024')]	|
|10	|11!/[6!*(11-6)!]/(2^11)	|(11!/(11-6)!)/2^11	|[('R.0.0', 39916800, u'11!', u'11!'), ('R.1', 2048.0, u'2^11', u'2^11')]	|
|11	|11!/[6!*(11-6)!]/(2^11)	|(11!/(6!))/(2^11)	|[('R.0.0', 39916800, u'11!', u'11!'), ('R.1', 2048.0, u'2^11', u'2^11')]	|
|12	|10!/[6!*(10-6)!]/(2^10)	|(10!/4!)/(2^10)	|[('R.0.0', 3628800, u'10!', u'10!'), ('R.1', 1024.0, u'2^10', u'2^10')]	|
|13	|11!/[6!*(11-6)!]/(2^11)	|(11!/5!)/2048	|[('R.0.0', 39916800, u'11!', u'11!'), ('R.1', 2048.0, u'2^11', u'2048')]	|
|14	|10!/[6!*(10-6)!]/(2^10)	|[(10!)/(6!)]/(2^10)	|[('R.0.0', 3628800, u'10!', u'10!'), ('R.1', 1024.0, u'2^10', u'2^10')]	|
|15	|11!/[6!*(11-6)!]/(2^11)	|(11!/6!)/2^11	|[('R.0.0', 39916800, u'11!', u'11!'), ('R.1', 2048.0, u'2^11', u'2^11')]	|
|16	|9!/[6!*(9-6)!]/(2^9)	|(9!/3!)/(2^9)	|[('R.0.0', 362880, u'9!', u'9!'), ('R.1', 512.0, u'2^9', u'2^9')]	|
|17	|9!/[6!*(9-6)!]/(2^9)	|((9!)/(2!(9-2)!))/2^9	|[('R.0.0', 362880, u'9!', u'9!'), ('R.1', 512.0, u'2^9', u'2^9')]	|
|18	|11!/[6!*(11-6)!]/(2^11)	|((11!)/(5!))/(2^11)	|[('R.0.0', 39916800, u'11!', u'11!'), ('R.1', 2048.0, u'2^11', u'2^11')]	|
|19	|11!/[6!*(11-6)!]/(2^11)	|((11!)/((11-6)!))/(2^11)	|[('R.0.0', 39916800, u'11!', u'11!'), ('R.1', 2048.0, u'2^11', u'2^11')]	|
|20	|10!/[6!*(10-6)!]/(2^10)	|(10!/(3!*6!))/2^10	|[('R.0.0', 3628800, u'10!', u'10!'), ('R.1', 1024.0, u'2^10', u'2^10')]	|
|21	|10!/[6!*(10-6)!]/(2^10)	|(10!/6!)/2**10	|[('R.0.0', 3628800, u'10!', u'10!'), ('R.1', 1024.0, u'2^10', u'2**10')]	|
|22	|9!/[6!*(9-6)!]/(2^9)	|(9!/(3!*(9-3)))/(2^9)	|[('R.0.0', 362880, u'9!', u'9!'), ('R.1', 512.0, u'2^9', u'2^9')]	|




### (14) Mistake Group ['R.1.0'] of size 14
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|11!/[6!*(11-6)!]/(2^11)	|1/2^6	|[('R.1.0', 2.0, u'2', u'2')]	|
|1	|11!/[6!*(11-6)!]/(2^11)	|6!/2^6	|[('R.1.0', 2.0, u'2', u'2')]	|
|2	|11!/[6!*(11-6)!]/(2^11)	|6/2^6	|[('R.1.0', 2.0, u'2', u'2')]	|
|3	|11!/[6!*(11-6)!]/(2^11)	|11/(2^6)	|[('R.1.0', 2.0, u'2', u'2')]	|
|4	|9!/[6!*(9-6)!]/(2^9)	|1/(2^6)	|[('R.1.0', 2.0, u'2', u'2')]	|
|5	|9!/[6!*(9-6)!]/(2^9)	|6/(2^6)	|[('R.1.0', 2.0, u'2', u'2')]	|
|6	|9!/[6!*(9-6)!]/(2^9)	|9/(2^6)	|[('R.1.0', 2.0, u'2', u'2')]	|
|7	|9!/[6!*(9-6)!]/(2^9)	|1/(2^9)*2^6	|[('R.1.0', 2.0, u'2', u'2')]	|
|8	|10!/[6!*(10-6)!]/(2^10)	|6/(2^9)	|[('R.1.0', 2.0, u'2', u'2')]	|
|9	|11!/[6!*(11-6)!]/(2^11)	|11/2^6	|[('R.1.0', 2.0, u'2', u'2')]	|




### (8) Mistake Group ['R.0.0', 'R.0.1.0', 'R.1'] of size 8
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.0.1.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|11!/[6!*(11-6)!]/(2^11)	|(11!/(6!6!))/(2^11)	|[('R.0.0', 39916800, u'11!', u'11!'), ('R.0.1.0', 720, u'6!', u'6!'), ('R.1', 2048.0, u'2^11', u'2^11')]	|
|1	|11!/[6!*(11-6)!]/(2^11)	|(11!/(6!4!))/2^11	|[('R.0.0', 39916800, u'11!', u'11!'), ('R.0.1.0', 720, u'6!', u'6!'), ('R.1', 2048.0, u'2^11', u'2^11')]	|
|2	|11!/[6!*(11-6)!]/(2^11)	|[(11!)/[(6!)(11!-6!)]]/(2^11)	|[('R.0.0', 39916800, u'11!', u'11!'), ('R.0.1.0', 720, u'6!', u'6!'), ('R.1', 2048.0, u'2^11', u'2^11')]	|
|3	|11!/[6!*(11-6)!]/(2^11)	|[(11!)/[(6!)(4!)]]/(2^11)	|[('R.0.0', 39916800, u'11!', u'11!'), ('R.0.1.0', 720, u'6!', u'6!'), ('R.1', 2048.0, u'2^11', u'2^11')]	|
|4	|9!/[6!*(9-6)!]/(2^9)	|(9!/(6!(9-6)))/2^9	|[('R.0.0', 362880, u'9!', u'9!'), ('R.0.1.0', 720, u'6!', u'6!'), ('R.1', 512.0, u'2^9', u'2^9')]	|
|5	|9!/[6!*(9-6)!]/(2^9)	|(9!/(6!*2!))/(2^9)	|[('R.0.0', 362880, u'9!', u'9!'), ('R.0.1.0', 720, u'6!', u'6!'), ('R.1', 512.0, u'2^9', u'2^9')]	|
|6	|10!/[6!*(10-6)!]/(2^10)	|10!/(6!*3!)(2^10)	|[('R.0.0', 3628800, u'10!', u'10!'), ('R.0.1.0', 720, u'6!', u'6!'), ('R.1', 1024.0, u'2^10', u'2^10')]	|
|7	|10!/[6!*(10-6)!]/(2^10)	|10!/(6!*3!)/(2^10)	|[('R.0.0', 3628800, u'10!', u'10!'), ('R.0.1.0', 720, u'6!', u'6!'), ('R.1', 1024.0, u'2^10', u'2^10')]	|




### (7) Mistake Group ['R.0.0'] of size 7
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|11!/[6!*(11-6)!]/(2^11)	|(11!/6!) * (1/2^11)	|[('R.0.0', 39916800, u'11!', u'11!')]	|
|1	|9!/[6!*(9-6)!]/(2^9)	|(9!)/6!(9-6)/2^9	|[('R.0.0', 362880, u'9!', u'9!')]	|
|2	|10!/[6!*(10-6)!]/(2^10)	|10!/(2^10)(6!)	|[('R.0.0', 3628800, u'10!', u'10!')]	|
|3	|10!/[6!*(10-6)!]/(2^10)	|10!/(2^10)(4!)	|[('R.0.0', 3628800, u'10!', u'10!')]	|
|4	|11!/[6!*(11-6)!]/(2^11)	|11!/6!5!	|[('R.0.0', 39916800, u'11!', u'11!')]	|
|5	|11!/[6!*(11-6)!]/(2^11)	|11!/(6!)(5!)	|[('R.0.0', 39916800, u'11!', u'11!')]	|
|6	|9!/[6!*(9-6)!]/(2^9)	|(9!/3!)*[1/(2^9)]	|[('R.0.0', 362880, u'9!', u'9!')]	|




### (4) Mistake Group ['R.0', 'R.1'] of size 4
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|10!/[6!*(10-6)!]/(2^10)	|[10!/(6!4!)][2^10]	|[('R.0', 210.0, u'10!/[6!*(10-6)!]', u'10!/(6!4!)'), ('R.1', 1024.0, u'2^10', u'2^10')]	|
|1	|9!/[6!*(9-6)!]/(2^9)	|(9*8*7) / 6*(2^9)	|[('R.0', 84.0, u'9!/[6!*(9-6)!]', u'(9*8*7) / 6'), ('R.1', 512.0, u'2^9', u'2^9')]	|
|2	|11!/[6!*(11-6)!]/(2^11)	|11* 10 * 9 * 8 * 7/(5*4*3*2)(2^11)	|[('R.0', 462.0, u'11!/[6!*(11-6)!]', u'11* 10 * 9 * 8 * 7/(5*4*3*2)'), ('R.1', 2048.0, u'2^11', u'2^11')]	|
|3	|9!/[6!*(9-6)!]/(2^9)	|(12*7)(2^9)	|[('R.0', 84.0, u'9!/[6!*(9-6)!]', u'12*7'), ('R.1', 512.0, u'2^9', u'2^9')]	|




### (2) Mistake Group ['R.0'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|11!/[6!*(11-6)!]/(2^11)	|C(11,6)*((1/2)^6)	|[('R.0', 462.0, u'11!/[6!*(11-6)!]', u'C(11,6)')]	|
|1	|11!/[6!*(11-6)!]/(2^11)	|C(11,6)*6!	|[('R.0', 462.0, u'11!/[6!*(11-6)!]', u'C(11,6)')]	|




### (2) Mistake Group Wrong_Sign of size 2




### (2) Mistake Group ['R.0.1', 'R.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|11!/[6!*(11-6)!]/(2^11)	|12!/(6!*5!)/2^11	|[('R.0.1', 86400.0, u'6!*(11-6)!', u'6!*5!'), ('R.1', 2048.0, u'2^11', u'2^11')]	|
|1	|11!/[6!*(11-6)!]/(2^11)	|(6!/(6!*(11-6)!))/2^11	|[('R.0.1', 86400.0, u'6!*(11-6)!', u'6!*(11-6)!'), ('R.1', 2048.0, u'2^11', u'2^11')]	|




### (1) Mistake Group ['R.0.0', 'R.0.1', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.0.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|11!/[6!*(11-6)!]/(2^11)	|(11!(5!*6!))/2^11	|[('R.0.0', 39916800, u'11!', u'11!'), ('R.0.1', 86400.0, u'6!*(11-6)!', u'5!*6!'), ('R.1', 2048.0, u'2^11', u'2^11')]	|




### (1) Mistake Group ['R.0.1.1', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|10!/[6!*(10-6)!]/(2^10)	|(10!/6!)/1024 * (10!/4!)/1024	|[('R.0.1.1', 24, u'(10-6)!', u'4!'), ('R.1', 1024.0, u'2^10', u'1024')]	|




### (1) Mistake Group ['R.0.1.0', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|11!/[6!*(11-6)!]/(2^11)	|12!/(6!*6!)/2^11	|[('R.0.1.0', 720, u'6!', u'6!'), ('R.1', 2048.0, u'2^11', u'2^11')]	|




### (62) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:gthorn

	first_attempt
					2015-10-04 02:24:46
	part1_correct_attempt
					['0:00:00', u'512']
	part2_correct_attempt
					['0:00:00', u'9']
	part3_correct_attempt
					['0:00:00', u'0.017578125']
	part5_incorrect_attempt
					('0:07:15', u'0.01171875')
	part5_correct_attempt
					['0:10:51', u'0.1640625']

1 Student ID:dlgoldbe

	first_attempt
					2015-10-08 04:52:01
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:00:49', u'9']
	part3_correct_attempt
					['0:00:49', u'9/(2^9)']
	part5_incorrect_attempt
					('0:07:40', u'(9!)/(3!*6!)')
	part5_correct_attempt
					['0:07:56', u'((9!)/(3!*6!))/(2^9)']

2 Student ID:lpettit

	first_attempt
					2015-10-06 02:52:20
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:37:47', u'11']
	part3_correct_attempt
					['0:38:21', u'11/2048']
	part5_incorrect_attempt
					('0:40:55', u'(11!)/(6!*(5!))')
	part5_correct_attempt
					['0:41:37', u'((11!)/(6!*(5!)))/2048']

3 Student ID:agoldsht

	first_attempt
					2015-10-06 23:09:31
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:19:06', u'(11!/10!)']
	part3_correct_attempt
					['0:22:32', u'11/2^11']
	part5_incorrect_attempt
					('2:03:03', u'11!/(5!6!)')
	part5_correct_attempt
					['2:03:52', u'11!/(5!*6!*2^11)']

4 Student ID:v4zhang

	first_attempt
					2015-10-08 08:01:07
	part1_correct_attempt
					['0:00:00', u'2048']
	part2_correct_attempt
					['0:01:21', u'11']
	part3_correct_attempt
					['0:01:21', u'11/2048']
	part5_incorrect_attempt
					('0:19:33', u'1-[(2^6)/2048]')
	part5_correct_attempt
					['0:25:22', u'462/2048']

5 Student ID:kebao

	first_attempt
					2015-10-03 17:50:44
	part1_correct_attempt
					['0:00:00', u'2048']
	part2_correct_attempt
					['0:08:16', u'11']
	part3_correct_attempt
					['0:08:39', u'11/2048']
	part5_incorrect_attempt
					('0:09:12', u'6!')
	part5_correct_attempt
					['0:15:37', u'(11!/(6!*5!))/2048']

6 Student ID:glcohen

	first_attempt
					2015-10-04 22:55:55
	part1_correct_attempt
					['0:00:00', u'1024']
	part2_correct_attempt
					['0:13:34', u'(10!)/(9!(10-9)!)']
	part3_correct_attempt
					['0:12:30', u'((10!)/(9!))/1024']
	part5_incorrect_attempt
					('0:15:13', u'(10!)/(6!(10-6)!)')
	part5_correct_attempt
					['0:15:29', u'(10!)/(6!(10-6)!)/1024']

7 Student ID:ppanourg

	first_attempt
					2015-10-07 23:44:44
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:01:09', u'9']
	part3_correct_attempt
					['0:02:47', u'9/(2^9)']
	part5_incorrect_attempt
					('0:02:47', u'(9*8*7)/(3!)')
	part5_correct_attempt
					['6:35:41', u'((9*8*7)/6)/(2^9)']

8 Student ID:ewbrenna

	first_attempt
					2015-10-04 04:13:31
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:00:00', u'9']
	part3_correct_attempt
					['0:00:00', u'9/(2^9)']
	part5_incorrect_attempt
					('0:49:22', u'9!/(6!*(3!))')
	part5_correct_attempt
					['0:49:49', u'(9!/(6!*(3!)))/512']

9 Student ID:msaguiar

	first_attempt
					2015-10-06 04:23:45
	part1_correct_attempt
					['0:00:00', u'(2^9)']
	part2_correct_attempt
					['0:00:30', u'9']
	part3_correct_attempt
					['0:21:32', u'9/(2^9)']
	part5_incorrect_attempt
					('0:25:34', u'9!/((6!)(3!))')
	part5_correct_attempt
					['0:25:58', u'(9!/((6!)(3!)))/2^9']

10 Student ID:spw006

	first_attempt
					2015-10-04 05:55:21
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:00:47', u'10']
	part3_correct_attempt
					['0:01:24', u'10/1024']
	part5_incorrect_attempt
					('13:30:37', u'(10*9*8*7)(1/64)(1/16)')
	part5_correct_attempt
					['13:31:25', u'(10*9*8*7/4!)(1/64)(1/16)']

11 Student ID:cprafull

	first_attempt
					2015-10-06 19:24:57
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:00:38', u'11']
	part3_correct_attempt
					['0:00:56', u'11/(2^11)']
	part5_incorrect_attempt
					('5:59:49', u'11!/[(6!)(5!)]')
	part5_correct_attempt
					['6:00:12', u'(11!/[(6!)(5!)])/(2^11)']

12 Student ID:anislam

	first_attempt
					2015-10-08 23:47:23
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:00:00', u'10']
	part3_correct_attempt
					['0:00:00', u'10 / 2 ^ 10']
	part5_incorrect_attempt
					('0:00:00', u'10 * 9 * 8 * 7')
					('0:02:07', u'10 * 9 * 8 * 7 / 10!')
	part5_correct_attempt
					['0:08:13', u'(10! / (6! * 4!)) * (1/2)^6 * (1/2)^4']

13 Student ID:aadhakal

	first_attempt
					2015-10-05 07:24:25
	part1_correct_attempt
					['0:00:00', u'1024']
	part2_correct_attempt
					['-1 day, 23:57:19', u'10']
	part3_correct_attempt
					['0:08:17', u'10/1024']
	part5_incorrect_attempt
					('12:52:14', u'1/7')
	part5_correct_attempt
					['13:44:41', u'210/1024']

14 Student ID:l5han

	first_attempt
					2015-10-05 01:51:13
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:00:00', u'11']
	part3_correct_attempt
					['0:00:00', u'11/(2^11)']
	part5_incorrect_attempt
					('1 day, 16:28:53', u'11!/(5!*6!)')
	part5_correct_attempt
					['1 day, 16:29:51', u'[11!/(5!*6!)]/2^11']

15 Student ID:pvl001

	first_attempt
					2015-10-03 15:48:09
	part1_correct_attempt
					['0:00:00', u'1024']
	part2_correct_attempt
					['0:01:26', u'10']
	part3_correct_attempt
					['0:01:26', u'10/1024']
	part5_incorrect_attempt
					('0:01:26', u'1/210')
	part5_correct_attempt
					['0:02:22', u'210/1024']

16 Student ID:vsosnovs

	first_attempt
					2015-10-04 17:40:35
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:20:15', u'9!/8!']
	part3_correct_attempt
					['0:20:45', u'9/512']
	part5_incorrect_attempt
					('0:23:02', u'9!/(6!(3!))')
					('0:23:17', u'9!/(6!3!)')
	part5_correct_attempt
					['0:25:41', u'84/512']

17 Student ID:b1green

	first_attempt
					2015-10-08 06:08:57
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['12:59:54', u'11']
	part3_correct_attempt
					['13:00:45', u'11/(2^11)']
	part5_incorrect_attempt
					('13:04:41', u'P(11,6)')
	part5_correct_attempt
					['13:23:41', u'462/(2^11)']

18 Student ID:b3hwang

	first_attempt
					2015-10-08 23:36:30
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:00:00', u'10']
	part3_correct_attempt
					['0:00:00', u'10/(2^10)']
	part5_incorrect_attempt
					('0:01:39', u'(.5)^10')
	part5_correct_attempt
					['0:03:17', u'210/(2^10)']

19 Student ID:tpmach

	first_attempt
					2015-10-03 21:40:56
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:03:24', u'9!/[8!(9-8)!]']
	part3_correct_attempt
					['0:03:36', u'9/2^9']
	part5_incorrect_attempt
					('0:08:35', u'9!/[6!(9-6)!]')
	part5_correct_attempt
					['0:09:02', u'(9!/[6!(9-6)!])/2^9']

20 Student ID:syc078

	first_attempt
					2015-10-08 22:37:44
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:38:26', u'11']
	part3_correct_attempt
					['0:38:26', u'11/(2^11)']
	part5_incorrect_attempt
					('0:38:26', u'C(11, 5)')
					('0:39:03', u'11/((6!)(5!))')
					('0:39:38', u'(11!)/((6!)(5!))')
					('0:40:04', u'(11!) / ( (6!) (5!) )')
	part5_correct_attempt
					['0:40:48', u'((11!) / ( (6!) (5!) )) / (2^11)']

21 Student ID:ctroncos

	first_attempt
					2015-10-08 05:42:25
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:02:53', u'11']
	part3_correct_attempt
					['0:03:29', u'11/(2^11)']
	part5_incorrect_attempt
					('17:57:27', u'(11!/(11!*5!))(0.5^6)(0.5)^5')
	part5_correct_attempt
					['17:59:52', u'(11!/(6!*5!))(0.5^6)(0.5)^5']

22 Student ID:bmilton

	first_attempt
					2015-10-04 01:42:25
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:01:06', u'10']
	part3_correct_attempt
					['0:02:50', u'10/1024']
	part5_incorrect_attempt
					('0:04:12', u'1/2(10*9*8*7)/1024')
					('0:04:25', u'(1/2)^6')
					('0:04:32', u'(1/2)^10')
	part5_correct_attempt
					['0:20:08', u'210/1024']

23 Student ID:dcgriffi

	first_attempt
					2015-10-08 03:55:58
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:00:00', u'11']
	part3_correct_attempt
					['0:00:00', u'11/(2^11)']
	part5_incorrect_attempt
					('0:07:42', u'11^5')
					('0:07:58', u'11*5')
					('0:35:45', u'(11!)/(6!)')
					('2:25:32', u'(11!)/(5!)')
	part5_correct_attempt
					['2:35:04', u'((11!)/((6!)*(5!)))/(2^11)']

24 Student ID:rsmurlo

	first_attempt
					2015-10-08 01:54:38
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:00:51', u'9']
	part3_correct_attempt
					['0:00:00', u'9/2^9']
	part5_incorrect_attempt
					('0:33:07', u'9!/(3!6!)')
	part5_correct_attempt
					['0:33:46', u'(9!/(3!6!))/2^9']

25 Student ID:jnatale

	first_attempt
					2015-10-08 00:17:10
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:08:02', u'9']
	part3_correct_attempt
					['0:13:55', u'9/(2^9)']
	part5_incorrect_attempt
					('0:14:41', u'6/(2^9) + 4/(2^9)')
					('0:14:46', u'6/(2^9) + 3/(2^9)')
	part5_correct_attempt
					['2:38:01', u'21/128']

26 Student ID:avasavad

	first_attempt
					2015-10-06 06:11:58
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:00:00', u'11']
	part3_correct_attempt
					['0:00:00', u'11/(2^11)']
	part5_incorrect_attempt
					('0:19:36', u'6!(5!*6!)')
					('0:21:23', u'4* 6!(5!*6!)')
	part5_correct_attempt
					['2 days, 16:39:24', u'(11!/[6!5!])/2^11']

27 Student ID:mrchin

	first_attempt
					2015-10-05 20:49:34
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:00:42', u'10']
	part3_correct_attempt
					['0:00:47', u'10/(2^10)']
	part5_incorrect_attempt
					('0:08:03', u'[(2^10)/6]*[(1/2)^6]*[1-(1/2)]^4')
	part5_correct_attempt
					['0:09:54', u'[(10*9*8*7)/(4*3*2)]*[(1/2)^6]*[1-(1/2)]^4']

28 Student ID:twsalim

	first_attempt
					2015-10-04 00:20:29
	part1_correct_attempt
					['0:00:00', u'2048']
	part2_correct_attempt
					['0:00:00', u'11']
	part3_correct_attempt
					['0:00:00', u'0.00537']
	part5_incorrect_attempt
					('0:00:00', u'0.225')
	part5_correct_attempt
					['0:17:19', u'0.22558']

29 Student ID:achinn

	first_attempt
					2015-10-06 19:28:30
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:00:00', u'10']
	part3_correct_attempt
					['0:00:00', u'10/(2^10)']
	part5_incorrect_attempt
					('0:00:00', u'10!/((6!)*(4!))')
	part5_correct_attempt
					['0:01:55', u'(10!/((6!)*(4!)))/2^10']

30 Student ID:jap009

	first_attempt
					2015-10-08 22:38:05
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:00:56', u'11']
	part3_correct_attempt
					['0:01:44', u'11/2^11']
	part5_incorrect_attempt
					('0:06:37', u'1/2')
	part5_correct_attempt
					['0:20:06', u'231/1024']

31 Student ID:kalang

	first_attempt
					2015-10-05 22:33:36
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:02:01', u'9']
	part3_correct_attempt
					['0:01:35', u'1/(2^9)*9']
	part5_incorrect_attempt
					('0:04:03', u'1/(2^9)*9^3')
	part5_correct_attempt
					['0:23:51', u'(9!/(6!*3!))/2^9']

32 Student ID:jcl084

	first_attempt
					2015-10-08 19:25:12
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:02:58', u'10']
	part3_correct_attempt
					['0:08:31', u'10 * (1/2)^10']
	part5_incorrect_attempt
					('0:17:48', u'90 * (1/2)^10')
					('0:18:02', u'90 * (1/2)^7')
	part5_correct_attempt
					['0:19:32', u'210 * (1/2)^10']

33 Student ID:aalhaida

	first_attempt
					2015-10-08 11:46:36
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:16:09', u'10']
	part3_correct_attempt
					['0:16:09', u'10/2^10']
	part5_incorrect_attempt
					('0:22:46', u'10!/(3!*6!*2^10)')
	part5_correct_attempt
					['0:25:29', u'(10!/(6!*4!))/2^10']

34 Student ID:ctgraves

	first_attempt
					2015-10-06 00:21:53
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:00:00', u'11']
	part3_correct_attempt
					['0:00:00', u'11/(2^11)']
	part5_incorrect_attempt
					('0:00:58', u'6!/(11-6)!')
					('0:04:59', u'(11!)/(6!  * (11-6)!)')
	part5_correct_attempt
					['0:05:06', u'(11!)/(6! * (11-6)!)/2^11']

35 Student ID:dsmonaha

	first_attempt
					2015-10-05 18:33:47
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:08:03', u'9']
	part3_correct_attempt
					['0:08:30', u'9/512']
	part5_incorrect_attempt
					('1 day, 22:40:25', u'1-(C(9,6)/(2^9))')
	part5_correct_attempt
					['1 day, 22:43:27', u'84/2^9']

36 Student ID:ajabasa

	first_attempt
					2015-10-05 21:18:45
	part1_correct_attempt
					['0:00:00', u'1024']
	part2_correct_attempt
					['0:01:48', u'10']
	part3_correct_attempt
					['0:01:48', u'10/1024']
	part5_incorrect_attempt
					('0:07:42', u'(10!/6!)/1024 + (10!/4!)/1024')
	part5_correct_attempt
					['0:11:27', u'(10!/(6!*4!))/1024']

37 Student ID:tstevens

	first_attempt
					2015-10-07 12:14:07
	part1_correct_attempt
					['0:00:00', u'1024']
	part2_correct_attempt
					['0:00:00', u'10']
	part3_correct_attempt
					['0:00:00', u'10/1024']
	part5_incorrect_attempt
					('0:00:59', u'.5^.6')
	part5_correct_attempt
					['1 day, 5:28:04', u'0.205078125']

38 Student ID:jtfrankl

	first_attempt
					2015-10-07 23:40:21
	part1_correct_attempt
					['0:00:00', u'2**11']
	part2_correct_attempt
					['0:00:37', u'11']
	part3_correct_attempt
					['2:55:15', u'11*(1/2)**11']
	part5_incorrect_attempt
					('2:56:30', u'6*(1/2)**11')
	part5_correct_attempt
					['3:05:24', u'(11!/(5!6!))/(2**11)']

39 Student ID:jcj006

	first_attempt
					2015-10-08 00:18:54
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:00:00', u'9']
	part3_correct_attempt
					['0:00:00', u'9/(2^9)']
	part5_incorrect_attempt
					('0:05:46', u'7!*6!*5!*4!*3!*2')
					('0:07:32', u'7+6*2+5*3+4*4+3*5+2*6+7')
					('0:08:28', u'1/(7+6*2+5*3+4*4+3*5+2*6+7)')
					('0:09:03', u'1/(2^9 - (7+6*2+5*3+4*4+3*5+2*6+7))')
	part5_correct_attempt
					['0:09:24', u'(7+6*2+5*3+4*4+3*5+2*6+7)/2^9']

40 Student ID:sippolit

	first_attempt
					2015-10-03 20:02:36
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:01:40', u'9']
	part3_correct_attempt
					['0:01:40', u'9/512']
	part5_incorrect_attempt
					('0:19:40', u'6!/(6!*4!)')
	part5_correct_attempt
					['0:24:07', u'(9!/(6!*3!))/512']

41 Student ID:eaherman

	first_attempt
					2015-10-03 20:58:35
	part1_correct_attempt
					['0:00:00', u'2^(10)']
	part2_correct_attempt
					['0:01:17', u'10']
	part3_correct_attempt
					['0:02:10', u'10/1024']
	part5_incorrect_attempt
					('0:03:55', u'[10!]/[(6!)(4!)]')
					('0:05:16', u'6!')
					('0:05:23', u'4!')
	part5_correct_attempt
					['0:07:21', u'[(10!)/((6!)(4!))]/1024']

42 Student ID:sayao

	first_attempt
					2015-10-03 00:25:04
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:00:57', u'11']
	part3_correct_attempt
					['0:01:13', u'11/2^11']
	part5_incorrect_attempt
					('0:02:26', u'C(11,6)')
					('0:08:07', u'11!/5!')
					('0:08:24', u'2^6')
					('0:12:42', u'C(11,5)')
	part5_correct_attempt
					['0:15:12', u'11!/(5! * 6!)/2^11']

43 Student ID:anvan

	first_attempt
					2015-10-03 07:47:33
	part1_correct_attempt
					['0:00:00', u'2^(11)']
	part2_correct_attempt
					['0:00:29', u'11']
	part3_correct_attempt
					['0:01:06', u'11 * (1/2)^11']
	part5_incorrect_attempt
					('0:01:06', u'11 * (1/2)^11')
	part5_correct_attempt
					['0:01:48', u'11!/(6!5!) * (1/2)^11']

44 Student ID:jnn015

	first_attempt
					2015-10-03 20:45:32
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:02:15', u'11']
	part3_correct_attempt
					['0:02:15', u'11/2^11']
	part5_incorrect_attempt
					('0:34:29', u'12!/6!/6!')
	part5_correct_attempt
					['0:36:58', u'11!/6!/5!/2^11']

45 Student ID:csl030

	first_attempt
					2015-10-04 21:44:22
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:00:00', u'9']
	part3_correct_attempt
					['0:00:00', u'9/2^9']
	part5_incorrect_attempt
					('0:07:25', u'(1/2)^6 * 2 * 2 * 2')
					('0:08:49', u'(1/2)^6')
					('0:09:03', u'(1/2)^9')
					('0:11:35', u'C(9, 6)')
					('0:12:16', u'C(9,6)')
	part5_correct_attempt
					['0:13:55', u'(9!/(6!* 3!))/2^9']

46 Student ID:jjchung

	first_attempt
					2015-10-08 06:23:52
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:00:50', u'11']
	part3_correct_attempt
					['0:02:03', u'11/(2^11)']
	part5_incorrect_attempt
					('0:06:11', u'(11!/6!*5!)*(.5^6)*(.5^5)')
	part5_correct_attempt
					['0:06:25', u'(11!/(6!*5!))*(.5^6)*(.5^5)']

47 Student ID:wcwhite

	first_attempt
					2015-10-07 02:48:00
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:05:48', u'11']
	part3_correct_attempt
					['18:12:44', u'11/2^11']
	part5_incorrect_attempt
					('1 day, 16:10:13', u'11!/(6!(11-6)!)')
					('1 day, 16:11:10', u'11!/(6!5!)')
					('1 day, 16:11:19', u'11!/30!')
					('1 day, 16:12:20', u'1/2')
	part5_correct_attempt
					['1 day, 16:20:21', u'(11!/(6!(11-6)!))*(.5^6)*(.5^5)']

48 Student ID:tdurrer

	first_attempt
					2015-10-04 03:04:55
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:13:40', u'11']
	part3_correct_attempt
					['0:14:56', u'11/2048']
	part5_incorrect_attempt
					('0:14:56', u'(11!)/((6!)(5!))')
	part5_correct_attempt
					['0:15:24', u'[(11!)/((6!)(5!))]/2048']

49 Student ID:cstringh

	first_attempt
					2015-10-04 00:02:56
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:03:12', u'10']
	part3_correct_attempt
					['0:06:43', u'10/(2^10)']
	part5_incorrect_attempt
					('2 days, 21:51:37', u'(1/2)^6')
					('2 days, 21:56:27', u'(10!)/(6!(10-6)!)')
					('2 days, 21:56:56', u'(10!)/(6!(10-6)!)* (1/2)^6*(1/2)4')
	part5_correct_attempt
					['2 days, 21:57:10', u'(10!)/(6!(10-6)!)* (1/2)^6*(1/2)^4']

50 Student ID:ksrijong

	first_attempt
					2015-10-08 08:03:24
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:04:03', u'11']
	part3_correct_attempt
					['0:04:36', u'11/2^11']
	part5_incorrect_attempt
					('0:05:55', u'(11*10*9*8*7*6)/(6!)')
	part5_correct_attempt
					['0:09:57', u'[(11*10*9*8*7*6)/(6!)]/2^11']

51 Student ID:v4sharma

	first_attempt
					2015-10-05 01:23:58
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:00:37', u'10']
	part3_correct_attempt
					['0:00:59', u'10/(2^10)']
	part5_incorrect_attempt
					('0:32:09', u'10!/(2^10)(6!)(4!)')
					('0:59:42', u'10!/(2^10)(6!)(4!)(6!)')
	part5_correct_attempt
					['1:01:05', u'10!/((2^10)(4!)(6!))']

52 Student ID:r2fisher

	first_attempt
					2015-10-05 16:26:17
	part1_correct_attempt
					['0:00:00', u'2^11']
	part2_correct_attempt
					['0:00:18', u'11']
	part3_correct_attempt
					['0:00:26', u'11/(2^11)']
	part5_incorrect_attempt
					('0:01:53', u'11!/(6!*5!)')
					('0:02:10', u'11!/(6!)')
					('0:02:15', u'11!/(5!)')
					('0:03:56', u'11!/(6!*5!)')
					('0:04:33', u'11*10*9*8*7')
					('4:20:00', u'11!/(6!*5!)')
	part5_correct_attempt
					['4:20:14', u'(11!/(6!*5!))/(2^11)']

53 Student ID:aportuga

	first_attempt
					2015-10-06 05:36:44
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:10:01', u'10']
	part3_correct_attempt
					['0:10:19', u'10/(2^10)']
	part5_incorrect_attempt
					('0:15:33', u'10!/((10-6)!6!)')
	part5_correct_attempt
					['0:50:48', u'((10!/4!)/6!)/(2^10)']

54 Student ID:xweng

	first_attempt
					2015-10-07 07:01:03
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:00:12', u'9']
	part3_correct_attempt
					['0:00:26', u'9/2^9']
	part5_incorrect_attempt
					('0:03:03', u'1-27/2^9')
	part5_correct_attempt
					['0:34:35', u'84/2^9']

55 Student ID:c4du

	first_attempt
					2015-10-07 06:43:50
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['0:00:00', u'9']
	part3_correct_attempt
					['0:00:00', u'9/2^9']
	part5_incorrect_attempt
					('0:02:39', u'C(9,6)')
	part5_correct_attempt
					['0:15:19', u'84/2^9']

56 Student ID:yypan

	first_attempt
					2015-10-02 04:53:04
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:01:10', u'10']
	part3_correct_attempt
					['0:04:22', u'10/(2^10)']
	part5_incorrect_attempt
					('0:10:02', u'10!/(6!*4!)')
	part5_correct_attempt
					['0:10:40', u'[10!/(6!*4!)]/(2^10)']

57 Student ID:rohan

	first_attempt
					2015-10-08 22:59:07
	part1_correct_attempt
					['0:00:00', u'1024']
	part2_correct_attempt
					['0:00:00', u'10']
	part3_correct_attempt
					['0:00:00', u'10/1024']
	part5_incorrect_attempt
					('0:00:24', u'7/128')
					('0:03:22', u'1.025')
					('0:33:36', u'13.125')
					('0:34:55', u'.0205')
	part5_correct_attempt
					['0:36:52', u'210(((1/2)^6)((1/2)^4))']

58 Student ID:v3doan

	first_attempt
					2015-10-04 00:02:45
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:00:31', u'10']
	part3_correct_attempt
					['0:00:31', u'10/2^10']
	part5_incorrect_attempt
					('0:00:51', u'C(10,6)')
					('0:01:00', u'P(10,6)')
					('0:01:40', u'C(10,6)')
	part5_correct_attempt
					['0:07:32', u'10! / (6! 4!)/ 2^10']

59 Student ID:zig006

	first_attempt
					2015-10-06 00:44:46
	part1_correct_attempt
					['0:00:00', u'2^9']
	part2_correct_attempt
					['-1 day, 23:57:44', u'9']
	part3_correct_attempt
					['-1 day, 23:57:44', u'9/2^9']
	part5_incorrect_attempt
					('0:01:06', u'1-(9*8*7)/2^9')
					('0:02:42', u'9*8*7/9!')
	part5_correct_attempt
					['0:15:37', u'(9!/(3!6!))/2^9']

60 Student ID:zhw110

	first_attempt
					2015-10-08 04:34:27
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:00:00', u'10']
	part3_correct_attempt
					['0:00:00', u'10/(2^10)']
	part5_incorrect_attempt
					('0:02:07', u'10*9*8*7/(2^10 * 6!)')
	part5_correct_attempt
					['0:02:32', u'10*9*8*7*6*5/(2^10 * 6!)']

61 Student ID:jit002

	first_attempt
					2015-10-08 15:53:44
	part1_correct_attempt
					['0:00:00', u'2048']
	part2_correct_attempt
					['0:00:00', u'11']
	part3_correct_attempt
					['0:00:00', u'11/2048']
	part5_incorrect_attempt
					('0:00:00', u'C(11,6)')
	part5_correct_attempt
					['0:01:25', u'462/2048']











