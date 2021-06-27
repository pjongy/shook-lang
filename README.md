# 슉-랭 (Shook lang)

## (주의) 욕설이 섞인 밈입니다. [Namuwiki](https://namu.wiki/w/%EC%8A%88%EC%8A%89%20%EC%8A%88%EC%88%99.%20%EC%8A%89.%20%EC%8B%9C.%20%EC%8B%9C%EB%B0%9C%EB%9F%BC%EC%95%84.?from=%EC%8A%89%20%EC%8A%88%EC%8A%89)
실용적인 프로젝트가 아닙니다. (Inspired by [umjunsik-lang](https://github.com/rycont/umjunsik-lang/))


## 슈슉 슈숙. 슉. 시. 시발럼아.
![Shoo-Shook](./assets/shook.png)


## 키워드
```
슉: 변수 대입 선언
슈: 변수 inc
아: 변수 dec
.: 변수 **= 2

(공백): 스택 포인터 += 1
,: 스택 포인터 -= 1

시발럼아 : 스택 포인터가 가리키는 스택 데이터에 변수 대입
시발람아 : 변수에 스택 포인터가 가리키는 스택 데이터 대입

욱: 변수에서 스택 데이터 더하기
우욱: 변수에서 스택 데이터 빼기
우우욱: 변수에서 스택 데이터 곱하기
우우우욱: 변수에서 스택 데이터 나누기

슥: 변수를 str형으로 변환 후 스택 포인터 위치에서 역순으로 저장 (산술연산 결과 출력 시 사용)
-: 스택 포인터 변수에 대입 선언
_: 스택 포인터 변수에 대입 완료
시발롬아: 스택 데이터가 0이거나 스택포인터가 0이 될 때까지 -1 하며 1byte씩 출력
```

## Demo ( 3 * 4 )
```
// 슉슈슈슈시발럼아 슉슈슈슈슈,우우욱시발럼아 슥,,,시발람아아아시발럼아슉슈슈..   시발럼아슉슈슈..욱욱,,욱시발럼아  슉슈슈..욱욱,욱시발럼아 슉시발럼아시발롬아
$ python3 -m shook-lang.main --input=example/multiple3by4.shook --debug=False
12
```

## Demo ( helloworld )
```
// 슉슈슈슈.슈시발럼아 슉슈슈..시발럼아슉슈슈슈.우우욱우욱우욱우욱슈슈슈슈시발럼아시발람아시발럼아슉슈슈슈.아욱 시발럼아슉슈슈.욱슈슈 시발럼아시발람아 아아아시발럼아시발람아  시발럼아슉슈슈.욱슈슈슈슈,시발럼아,,,시발람아     시발럼아,,,,,시발람아      시발럼아시발람아아아아아  시발럼아시발람아,아아아시발럼아  시발롬아
$ python3 -m shook-lang.main --input=example/helloworld.shook --debug=False
helloworld
```
