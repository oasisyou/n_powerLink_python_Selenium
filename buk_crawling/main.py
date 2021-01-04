#파워링크를 통해 시장 규모 예측 가능.

def main():
    # python 3에서는 print() 으로 사용합니다.

    select_device = input('검색할 환경을 입력하세요. (pc/m 대소문자 구분함) : ')

    if "m" in select_device:
        print("모바일")
        import buk_crawling.m_201114__powerLink_ranking
    else:
        print("PC")
        import buk_crawling.pc_201114_powerLink_ranking


if __name__ == "__main__":
	main()