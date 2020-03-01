# 1.정의
우선 이 파일을 불러오고
객체를 생성해야 한다

	import sponser
	
	list = Donation()
	
이때 그냥 이렇게 쓰면
영어가 된다.돈 기호는 $ 이고 설명이 영어로 나온다

하지만

	list = Donation("ko")
	
를 써주면
한국어가 된다.돈 단위는 원이고 설명도 한글로 나온다
이와 관련해선 나중에 다루도록 하겠다

# 2.후원자
## 2.1.후원자 추가
우선 후원자를 추가해야 된다.

	list.add("후원자 이름",후원한 양)

난 테스트라는 사람 1000원을 내에게 기부했다고 치겠다
그러면 전체코드가

	import sponser
	
	list = Donation("ko")
	list.add("테스트",1000)

가 된다 하지만 아무 일도 일어나지 않을 것이다
이와 관련해서는 나중에 다루도록 하겠다
## 2.2.후원자 삭제
후원을 받다보면 사기를 치는 사람도 있을 것이다
그럴때 사용하는 코드이다

	list.delete("후원자 이름")

나는 나에게 s1이라는 사람과 s2라는 사람이 각각 1000원를 후원을 했는데
s1이 사기라고 가정하고 전체코드를 작성해 보겠다

	import sponser
	
	list = Donation("ko")
	list.add("s1",1000)
	list.add("s2",1000)
	
	list.delete("s2")

이렇게 하면 된다
하지만 역시 아무것도 나오지 않을것이다
참고로 없는 유저의 을 지우려 하면
그런 유저는 없다는 메시지가 뜬다.
# 3.프린트
앞에서 알려준 예제는 아무것도 나오지 않았다.
그 이유는 뭘까?
왜냐하면 출력을 안했기 때문이다

	list.print()

로 프린트를 할수있지만 역시나
커스터마이징 기능이 있다
앞에서 알려준대로 쓰면

Sponser List------<br>
1.후원자1님 1000원<br>
2.후원자2님 1000원<br>

이렇게 자동으로 뜬다

하지만 

	list.print("후원자 목록------")

으로 하면

후원자 목록------<br>
1.후원자1님 1000원<br>
2.후원자2님 1000원<br>

이 된다.
그리고

	list.print("후원자 목록------","Number")

를 쓰면 아까와 차이가 없이

후원자 목록------<br>
1.후원자1님 1000원<br>
2.후원자2님 1000원<br>

의 형식이 뜰것이다
하지만

list.print("후원자 목록------","")

이렇게 써주면

후원자 목록------<br>
후원자1님 1000원<br>
후원자2님 1000원<br>

이런 형식이 될것이다
그러니까 첫번째 인수는
후원자 목록------ <br>
부분을 바꾸는 것이고

두번째 인수는
1.<br>
부분을 바꾸는 것이다

두번째 인수에서 "Number"
를 넣으면 자동으로
1.<br>
2.<br>
이렇게 붙지만
"I"<br>
이런식으로 해주면

I.<br>
I.<br>

이렇게 된다.
# 4.언어
아까 말했듯이
언어를 정할수 있다
정하는 방법은

	list = Donation()

에서 Donation()
안에 인수를 넣으면 된다
기본적으로 Donation()만 치면
자동으로 en,즉 영어가 된다.
하지만 Donation("ko")
를 쓰면 한국어를 쓸수 있다
물론 Donation("en")
을 쓰면 영어가 된다.

# 5.전체 코드
s1과 s2가 1$씩 후원하였지만 s1이 사기
였고

sponser list------<br>
1.후원자 1$<br>

형식으로 출력

	import sponser
	
	list = Donation("en")
	list.add("s1",1)
	list.add("s2",1)
	list.delete("s1")
	list.print("sponser list------")

1$가 아니라 1000원일때

	import sponser
	
	list = Donation("ko")
	list.add("s1",1000)
	list.add("s2",1000)
	list.delete("s1")
	list.print("sponser list------")

기호를 없애고 싶을때

	import sponser
	
	list = Donation("ko")
	list.add("s1",1000)
	list.add("s2",1000)
	list.delete("s1")
	list.print("sponser list------","")

기호를 * 으로 하고 싶을때

	import sponser
	
	list = Donation("ko")
	list.add("s1",1000)
	list.add("s2",1000)
	list.delete("s1")
	list.print("sponser list------","*)





	
	
