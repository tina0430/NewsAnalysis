from konlpy.tag import Twitter as kTwitter
# pip install customized-KoNLPy==0.0.51
from ckonlpy.tag import Twitter as cTwitter
from konlpy.tag import Hannanum
from konlpy.tag import Kkma
from konlpy.tag import Komoran

#ctwitter._customized_tagger.add_a_template(('Noun', 'Noun', 'Josa'))
# 포인트 : 축약어, 명사 인식, 숫자, 년, ~금, 명/조사 구분, 특수문자
#txt = '식약처는 2018년의 확장에 세금 등과 범칙금 부여가 필요할 수도 있다는 것에 동의했다.'
#txt = '금시세가 급등한 것은 이것과 _저것_이 부과금과 관련이 있다.'
#txt = '중소벤처기업부의 정책이 중기부 장관에 의해서 실패했다.'
txt = '문화체육관광부와 과학기술정보통신부와 국토교통부와 산업통상자원부와 기획재정부와 국민권익위원회가 협력한다.'

ktwitter = kTwitter()
print('트위터: ', ktwitter.pos(txt))
hannanum = Hannanum()
print('한나눔: ', hannanum.pos(txt))
kkma = Kkma()
print('꼬꼬마: ', kkma.pos(txt))
komoran = Komoran()
print('코모란: ', komoran.pos(txt))

print('\n')
ctwitter = cTwitter()
print('추가 이전: ', ctwitter.pos(txt))
ctwitter.add_dictionary(['문화체육관광부', '과학기술정보통신부'], 'Noun')
print('추가 이후: ', ctwitter.pos(txt))