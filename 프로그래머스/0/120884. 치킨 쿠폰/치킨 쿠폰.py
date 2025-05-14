def solution(chicken):
    coupons = chicken  # 처음 시켜먹은 치킨 수만큼 쿠폰을 받는다.
    service_chicken = 0  # 받은 서비스 치킨의 수
    
    while coupons >= 10:  # 쿠폰이 10개 이상일 때 서비스 치킨을 받을 수 있다.
        new_service = coupons // 10  # 받을 수 있는 서비스 치킨의 수
        service_chicken += new_service  # 서비스 치킨의 수에 더한다.
        coupons = coupons % 10 + new_service  # 남은 쿠폰은 나머지 쿠폰 + 서비스 치킨에서 받은 쿠폰으로 갱신

    return service_chicken